from PyQt6.QtWidgets import QApplication,QMainWindow
from PyQt6.QtGui import QMovie
from menu import Ui_MainWindow as menuUI


class menuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = menuUI()
        self.ui.setupUi(self)
        self.movie=QMovie("music/new.gif")
        self.ui.label.setMovie(self.movie)
        self.movie.start()
        self.ui.pushgame.clicked.connect(self.open_game)

    def open_game(self):
        if self.ui.radioButton.isChecked():
            from main import gameWindow
            self.game=gameWindow()
            self.game.show()
            self.hide()
        if self.ui.radioButton_2.isChecked():
            from twologic import twoplayWindow
            self.game=twoplayWindow()
            self.game.show()
            self.hide()
