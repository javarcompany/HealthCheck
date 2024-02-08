from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)

from final import *
from inst import *

class TestEnv(QWidget):
    def __init__(self):
        super().__init__()

    
    def initUI(self):
        # Buttons
        self.btn_sendresult = QPushButton(txt_sendresults, self)
        self.btn_test1 =  QPushButton(txt_starttest1, self)
        self.btn_test2 =  QPushButton(txt_starttest2, self)
        self.btn_test3 =  QPushButton(txt_starttest3, self)

        #Labels
        self.txt_name = QLabel(txt_name)
        self.txt_age = QLabel(txt_age)
        self.txt_test1 = QLabel(txt_test1)
        self.txt_test2 = QLabel(txt_test2)
        self.txt_test3 = QLabel(txt_test3)
        self.txt_timer = QLabel(txt_timer)

        #Textboxes
        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QLineEdit(txt_hintage)
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)

        #Layouts
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()

        #placing the elements on the layouts
        self.l_line.addWidget(self.txt_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment = Qt.AlignLeft)

        self.l_line.addWidget(self.txt_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment = Qt.AlignLeft)

        self.l_line.addWidget(self.txt_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1, alignment = Qt.AlignLeft)

        self.l_line.addWidget(self.txt_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test2, alignment = Qt.AlignLeft)

        self.l_line.addWidget(self.txt_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3, alignment = Qt.AlignLeft)

        self.l_line.addWidget(self.btn_sendresult, alignment = Qt.AlignCenter)

        self.r_line.addWidget(self.txt_timer, alignment = Qt.AlignCenter)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)

        self.setLayout(self.h_line)

        