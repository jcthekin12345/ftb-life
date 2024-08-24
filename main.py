import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Football Life")

        NEW_GAME_BUTTON = QPushButton("New Game")

        NEW_GAME_BUTTON.setCheckable(True)
        NEW_GAME_BUTTON.clicked.connect


        self.setMinimumSize(QSize(400, 300))
        self.setMaximumSize(QSize(1600, 800))

        self.setCentralWidget(NEW_GAME_BUTTON)

    def new_game(self):
       """The new game menu"""
       print("1.start new game")
       print("2.")


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
