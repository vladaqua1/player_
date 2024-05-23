from PyQt5.QtWidgets import QPushButton

class CustomButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)  # Разрешаем отслеживание движения мыши

        # Стили для обычного состояния кнопки
        self.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 3px solid #0A0303;
                border-radius: 13;
            }
        """)

        # Стили для состояния при наведении
        self.hover_style = """
            QPushButton:hover {
                background-color: #EDEDED;
                border: 3px solid #FFD700;
            }
        """

        # Стили для состояния при нажатии
        self.pressed_style = """
            QPushButton:pressed {
                background-color: #D3D3D3;
                border: 3px solid #FFA500;
            }
        """

        self.setStyleSheet(self.styleSheet() + self.hover_style)  # Устанавливаем стиль при создании

    def enterEvent(self, event):
        # При наведении меняем стиль на hover_style
        self.setStyleSheet(self.styleSheet() + self.hover_style)

    def leaveEvent(self, event):
        # При выходе мыши возвращаем обычный стиль
        self.setStyleSheet(self.styleSheet().replace(self.hover_style, ""))

    def mousePressEvent(self, event):
        # При нажатии кнопки мыши меняем стиль на pressed_style
        self.setStyleSheet(self.styleSheet() + self.pressed_style)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        # При отпускании кнопки мыши возвращаем обычный стиль или стиль при наведении
        if self.underMouse():
            self.setStyleSheet(self.styleSheet() + self.hover_style)
        else:
            self.setStyleSheet(self.styleSheet().replace(self.pressed_style, ""))
        super().mouseReleaseEvent(event)
