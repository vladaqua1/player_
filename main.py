import os
import sys
import shutil
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QListWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer, Qt
from interface import Ui_MainWindow
import pygame
import mutagen
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        pygame.init()
        self.playlist = []
        self.original_playlist = []
        self.muted = False
        self.current_track = None
        self.current_position = 0
        self.track_length = 0
        self.paused_position = 0
        self.playlist_folder = "saved_playlist"
        if not os.path.exists(self.playlist_folder):
            os.makedirs(self.playlist_folder)
        self.loadPlaylist()
        self.ui.pushButton.clicked.connect(self.openFolder)
        self.ui.pushButton_2.clicked.connect(self.viewPlaylist)
        self.ui.turn_left_2.clicked.connect(self.playPrevious)
        self.ui.turn_right_2.clicked.connect(self.playNext)
        self.ui.stop.clicked.connect(self.stopMusic)
        self.ui.turn_left.clicked.connect(self.rewindBackward)
        self.ui.turn_right.clicked.connect(self.rewindForward)
        self.ui.mute.clicked.connect(self.toggleMute)
        self.ui.play.clicked.connect(self.playMusic)
        self.ui.soundSetting.valueChanged.connect(self.changeVolume)
        self.ui.horizontalSlider.sliderMoved.connect(self.setMusicPosition)
        self.ui.listWidget.itemDoubleClicked.connect(self.playSelectedTrack)
        self.setWindowIcon(QIcon("ноти.png"))
        self.ui.soundSetting.setValue(30)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updatePosition)
        self.timer.start(1000)
        pygame.mixer.music.set_endevent(pygame.USEREVENT)
        self.playlist_end_handler()
    def openFolder(self):
        options = QFileDialog.Options()
        files, _ = QFileDialog.getOpenFileNames(self, "Вибрать музыкальные файлы", "",
                                                "Музыкальные файлы (*.mp3 *.wav *.ogg)", options=options)
        if files:
            self.ui.listWidget.clear()
            self.playlist.clear()
            self.original_playlist.clear()
            for file in files:
                file_name = os.path.basename(file)
                self.ui.listWidget.addItem(file_name)
                self.playlist.append(file)
                self.original_playlist.append(file)
                shutil.copy(file, os.path.join(self.playlist_folder, file_name))
            self.savePlaylist()
    def savePlaylist(self):
        with open(os.path.join(self.playlist_folder, "playlist.json"), 'w') as f:
            json.dump(self.original_playlist, f)
    def loadPlaylist(self):
        playlist_file = os.path.join(self.playlist_folder, "playlist.json")
        if os.path.exists(playlist_file):
            with open(playlist_file, 'r') as f:
                self.original_playlist = json.load(f)
                self.playlist = self.original_playlist.copy()
                for file in self.playlist:
                    file_name = os.path.basename(file)
                    self.ui.listWidget.addItem(file_name)
    def viewPlaylist(self):
        self.ui.listWidget.clear()
        if os.path.exists(self.playlist_folder):
            for file_name in os.listdir(self.playlist_folder):
                if file_name.endswith(('.mp3', '.wav', '.ogg')):
                    self.ui.listWidget.addItem(file_name)
        else:
            QMessageBox.information(self, "Плейлист", "Плейлист не найден.")
    def playPrevious(self):
        if self.playlist:
            self.current_track = self.playlist.pop(0)
            self.track_length = self.getTrackLength(self.current_track)
            self.ui.horizontalSlider.setMaximum(self.track_length)
            pygame.mixer.music.load(self.current_track)
            pygame.mixer.music.play()
            self.current_position = 0
            self.highlightCurrentTrack()
    def playNext(self):
        if self.playlist:
            self.current_track = self.playlist.pop(0)
            self.track_length = self.getTrackLength(self.current_track)
            self.ui.horizontalSlider.setMaximum(self.track_length)
            pygame.mixer.music.load(self.current_track)
            pygame.mixer.music.play()
            self.current_position = 0
            self.highlightCurrentTrack()
    def stopMusic(self):
        self.paused_position = pygame.mixer.music.get_pos() / 1000
        pygame.mixer.music.pause()
    def playMusic(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.unpause()
            pygame.mixer.music.play(start=self.paused_position)
        elif self.playlist:
            self.current_track = self.playlist[0]
            self.track_length = self.getTrackLength(self.current_track)
            self.ui.horizontalSlider.setMaximum(self.track_length)
            pygame.mixer.music.load(self.current_track)
            pygame.mixer.music.play(start=self.paused_position)
            self.highlightCurrentTrack()
    def rewindBackward(self):
        if self.current_track:
            self.current_position = max(0, self.current_position - 10)
            pygame.mixer.music.load(self.current_track)
            pygame.mixer.music.play(start=self.current_position)
    def rewindForward(self):
        if self.current_track:
            self.current_position += 10
            pygame.mixer.music.load(self.current_track)
            pygame.mixer.music.play(start=self.current_position)
    def toggleMute(self):
        if self.muted:
            pygame.mixer.music.set_volume(self.previous_volume)
            self.ui.soundSetting.setValue(int(self.previous_volume * 100))
            self.muted = False
        else:
            self.previous_volume = pygame.mixer.music.get_volume()
            pygame.mixer.music.set_volume(0)
            self.ui.soundSetting.setValue(0)
            self.muted = True

    def changeVolume(self, value):
        if not self.muted:
            volume = value / 100.0
            pygame.mixer.music.set_volume(volume)
        else:
            self.previous_volume = value / 100.0

    def updatePosition(self):
        if pygame.mixer.music.get_busy():
            self.current_position += 1
            self.ui.horizontalSlider.setValue(self.current_position)
    def setMusicPosition(self, position):
        self.current_position = position
        pygame.mixer.music.play(start=self.current_position)

    def getTrackLength(self, track):
        audio = mutagen.File(track)
        return int(audio.info.length)

    def playSelectedTrack(self, item):
        track_name = item.text()
        track_path = os.path.join(self.playlist_folder, track_name)
        if os.path.exists(track_path):
            self.current_track = track_path
            self.track_length = self.getTrackLength(self.current_track)
            self.ui.horizontalSlider.setMaximum(self.track_length)
            pygame.mixer.music.load(self.current_track)
            pygame.mixer.music.play()
            self.current_position = 0
            self.highlightCurrentTrack()
    def highlightCurrentTrack(self):
        for index in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.item(index)
            if item.text() == os.path.basename(self.current_track):
                item.setForeground(Qt.red)
                self.ui.listWidget.setCurrentItem(item)
            else:
                item.setForeground(Qt.black)
    def playlist_end_handler(self):
        self.timer.timeout.connect(self.check_end_of_track)
    def check_end_of_track(self):
        if not pygame.mixer.music.get_busy() and self.current_track:
            self.playNext()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())