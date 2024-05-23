from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(441, 644)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ноти.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background: #565C5C;")
        MainWindow.setIconSize(QtCore.QSize(60, 60))
        MainWindow.setProperty("note", icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setGeometry(QtCore.QRect(310, 270, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.play.setFont(font)
        self.play.setStyleSheet("QPushButton{\n"
"background-color: white;\n"
"border: 3px solid #0A0303;\n"
"border-radius: 13;\n"
"}")
        self.play.setObjectName("play")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(220, 270, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.stop.setFont(font)
        self.stop.setStyleSheet("QPushButton{\n"
"background-color: white;\n"
"border: 3px solid #0A0303;\n"
"border-radius: 13;\n"
"}")
        self.stop.setObjectName("stop")
        self.turn_left = QtWidgets.QPushButton(self.centralwidget)
        self.turn_left.setGeometry(QtCore.QRect(290, 310, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.turn_left.setFont(font)
        self.turn_left.setStyleSheet("QPushButton{\n"
"background-color: white;\n"
"border: 3px solid #0A0303;\n"
"border-radius: 13;\n"
"}")
        self.turn_left.setObjectName("turn_left")
        self.turn_right = QtWidgets.QPushButton(self.centralwidget)
        self.turn_right.setGeometry(QtCore.QRect(370, 310, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.turn_right.setFont(font)
        self.turn_right.setStyleSheet("QPushButton{\n"
"background-color: white;\n"
"border: 3px solid #0A0303;\n"
"border-radius: 13;\n"
"}")
        self.turn_right.setObjectName("turn_right")
        self.soundSetting = QtWidgets.QSlider(self.centralwidget)
        self.soundSetting.setGeometry(QtCore.QRect(230, 20, 20, 211))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.soundSetting.setFont(font)
        self.soundSetting.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.soundSetting.setFocusPolicy(QtCore.Qt.TabFocus)
        self.soundSetting.setAcceptDrops(True)
        self.soundSetting.setAutoFillBackground(False)
        self.soundSetting.setStyleSheet("QSlider{\n"
"background-color: white;\n"
"border: 3px solid #0A0303;\n"
"border-radius: 13;\n"
"}")
        self.soundSetting.setInputMethodHints(QtCore.Qt.ImhNone)
        self.soundSetting.setTracking(False)
        self.soundSetting.setOrientation(QtCore.Qt.Vertical)
        self.soundSetting.setInvertedAppearance(False)
        self.soundSetting.setInvertedControls(False)
        self.soundSetting.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.soundSetting.setObjectName("soundSetting")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setEnabled(True)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 181, 611))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background-color:#22222e;\n"
"border: 3px solid #0A0303;\n"
"border-radius: 13;\n"
"")
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 350, 161, 31))
        font = QtGui.QFont()
        font.setFamily("ESSTIXTen")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setTabletTracking(False)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: white;\n"
"border: 3px solid #0A0303;\n"
"border-radius: 13;\n"
"}")
        self.pushButton.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 390, 161, 31))
        font = QtGui.QFont()
        font.setFamily("ESSTIXTen")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: white;\n"
"border: 3px solid #0A0303;\n"
"border-radius: 13;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-40, -60, 561, 711))
        self.label.setStyleSheet("background-color:#22222e;\n"
"border: 3px solid #1A2323;\n"
"border-radius: 13;\n"
"phone: 3px;\n"
"")
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setPixmap(QtGui.QPixmap("фонннн.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(200, 240, 231, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.labeephone = QtWidgets.QLabel(self.centralwidget)
        self.labeephone.setGeometry(QtCore.QRect(260, 10, 171, 221))
        font = QtGui.QFont()
        font.setPointSize(70)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.labeephone.setFont(font)
        self.labeephone.setAutoFillBackground(False)
        self.labeephone.setStyleSheet("\n"
"background-color:#FFFFFF;\n"
"border: 3px solid #0A0303;\n"
"border-radius: 13;\n"
"")
        self.labeephone.setInputMethodHints(QtCore.Qt.ImhNone)
        self.labeephone.setScaledContents(True)
        self.labeephone.setAlignment(QtCore.Qt.AlignCenter)
        self.labeephone.setWordWrap(False)
        self.labeephone.setOpenExternalLinks(False)
        self.labeephone.setObjectName("labeephone")
        self.mute = QtWidgets.QPushButton(self.centralwidget)
        self.mute.setGeometry(QtCore.QRect(330, 310, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mute.setFont(font)
        self.mute.setStyleSheet("QPushButton{\n"
"background-color: white;\n"
"border: 3px solid #0A0303;\n"
"border-radius: 13;\n"
"}")
        self.mute.setObjectName("mute")
        self.turn_right_2 = QtWidgets.QPushButton(self.centralwidget)
        self.turn_right_2.setGeometry(QtCore.QRect(390, 270, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.turn_right_2.setFont(font)
        self.turn_right_2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.turn_right_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.turn_right_2.setAutoFillBackground(False)
        self.turn_right_2.setStyleSheet("QPushButton{\n"
"background-color: white;\n"
"border: 3px solid #0A0303;\n"
"border-radius: 13;\n"
"}")
        self.turn_right_2.setObjectName("turn_right_2")
        self.turn_left_2 = QtWidgets.QPushButton(self.centralwidget)
        self.turn_left_2.setGeometry(QtCore.QRect(260, 270, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.turn_left_2.setFont(font)
        self.turn_left_2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.turn_left_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.turn_left_2.setAutoFillBackground(False)
        self.turn_left_2.setStyleSheet("QPushButton{\n"
"background-color: white;\n"
"border: 3px solid #0A0303;\n"
"border-radius: 13;\n"
"}")
        self.turn_left_2.setObjectName("turn_left_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 440, 171, 151))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.label_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_2.setAcceptDrops(False)
        self.label_2.setStyleSheet("background-color:#FFFFFF;\n"
"border: 3px solid #0A0303;\n"
"border-radius: 13;\n"
"")
        self.label_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.play.raise_()
        self.stop.raise_()
        self.turn_left.raise_()
        self.turn_right.raise_()
        self.soundSetting.raise_()
        self.listWidget.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.horizontalSlider.raise_()
        self.labeephone.raise_()
        self.mute.raise_()
        self.turn_right_2.raise_()
        self.turn_left_2.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.setupButtonAnimations()

    def setupButtonAnimations(self):
        current_styles = {
            "turn_left_2": self.turn_left_2.styleSheet(),
            "turn_right_2": self.turn_right_2.styleSheet(),
            "pushButton": self.pushButton.styleSheet(),
            "pushButton_2": self.pushButton_2.styleSheet(),
            "turn_right": self.turn_right.styleSheet(),
            "turn_left": self.turn_left.styleSheet(),
            "play": self.play.styleSheet(),
            "mute": self.mute.styleSheet(),
            "stop": self.stop.styleSheet(),
            "horizontalSlider": self.horizontalSlider.styleSheet(),
        }
        hover_style = """
                    QPushButton:hover {
                        background-color: #C0C0C0;
                        border-color: #800F20;
                    }
                """
        pressed_style = """
                    QPushButton:pressed {
                        background-color: #A9A9A9;
                        border-color: #800F20;
                    }
                """
        slider_style = """
                    QSlider {
                        background-color: #E0E0E0;
                        border: 1px solid #C0C0C0;
                        border-radius: 5px;
                    }
                    QSlider::groove:horizontal {
                        background: #E0E0E0;
                        height: 8px;
                        border-radius: 5px;
                    }
                    QSlider::handle:horizontal {
                        background: #C0C0C0;
                        border: 1px solid #808080;
                        width: 15px;
                        margin: -4px 0px; /* отступы, чтобы ползунок был посередине */
                        border-radius: 7px;
                    }
                """
        groove_style = """
                    QSlider::groove:horizontal {
                        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                            stop:0 #FF0000, stop: 1 #FF0000);
                        height: 8px;
                        border-radius: 5px;
                    }
                """
        for widget_name, current_style in current_styles.items():
            new_style = current_style + hover_style + pressed_style
            if widget_name == "horizontalSlider":
                new_style += slider_style + groove_style
            getattr(self, widget_name).setStyleSheet(new_style)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.play.setText(_translate("MainWindow", "▶"))
        self.stop.setText(_translate("MainWindow", "||"))
        self.turn_left.setText(_translate("MainWindow", "<<"))
        self.turn_right.setText(_translate("MainWindow", ">>"))
        self.pushButton.setText(_translate("MainWindow", "CREATE PLAYLIST"))
        self.pushButton_2.setText(_translate("MainWindow", "playlists"))
        self.labeephone.setText(_translate("MainWindow", "♫"))
        self.mute.setText(_translate("MainWindow", "✘"))
        self.turn_right_2.setText(_translate("MainWindow", "▶"))
        self.turn_left_2.setText(_translate("MainWindow", "◀"))
        self.label_2.setText(_translate("MainWindow", "Цей мультиплеєр був створений "
                                                      "студентов 201 групи - Сідей Владислав "))
