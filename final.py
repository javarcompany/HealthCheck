from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit, QImage)

from inst import *

class FinalWin(QWidget):
    def __init__(self, exp_data):
        super().__init__()

        self.exp = exp_data

        self.initUI()

        self.set_appear()

        self.show() 


    def results(self):
        if self.exp.age < 7:
            self.index = 0
            return "There is No Data for this Age"
    	
        self.index = (4 * (int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3)) - 200 ) / 10
        if self.exp.age >= 15:
            if self.index >= 15:
                return level1
            elif self.index >= 11:
                return level2
            elif self.index >= 6:
                return level3
            elif self.index >= 0.5:
                return level4
            else:
                return level5

        elif self.exp.age >= 13:
            if self.index >= 15:
                return level1
            elif self.index >= 11:
                return level2
            elif self.index >= 6:
                return level3
            elif self.index >= 0.5:
                return level4
            else:
                return level5

        elif self.exp.age >= 11:
            if self.index >= 15:
                return level1
            elif self.index >= 11:
                return level2
            elif self.index >= 6:
                return level3
            elif self.index >= 0.5:
                return level4
            else:
                return level5
        
        elif self.exp.age >= 9:
            if self.index >= 15:
                return level1
            elif self.index >= 11:
                return level2
            elif self.index >= 6:
                return level3
            elif self.index >= 0.5:
                return level4
            else:
                return level5

        elif self.exp.age >= 7:
            if self.index >= 15:
                return level1
            elif self.index >= 11:
                return level2
            elif self.index >= 6:
                return level3
            elif self.index >= 0.5:
                return level4
            else:
                return level5

    def initUI(self):
        self.workheart_text = QLabel(txt_workheart + self.results())
        self.index_text = QLabel(txt_index + str(self.index))

        self.logo = QPixmap('\images\logo.png')
        self.displayLogo = QLabel()
        self.displayLogo.setPixmap(self.logo)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.workheart_text, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)