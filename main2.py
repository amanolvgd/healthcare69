from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QWidget,
QPushButton,QVBoxLayout,QHBoxLayout, QLineEdit, QLabel, QMessageBox, QRadioButton)
from intr import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle('ВТОРОЕ ОКНО')
        self.resize(win_width, win_height)
        self.move(win_x,win_y)

    def initUI(self):
        self.label_name=QLabel("vvedite fio")
        self.line_if_name=QLineEdit('f.i.o')

        self.label_age=QLabel("polnyh let")
        self.line_age=QLineEdit('0')

        self.label_instr_1=QLabel(intstr_1)
        self.btn_test_1=QPushButton('nachat perviy test')

        self.line_beatsm_1=QLineEdit('vvedite kol bitov v minutu')

        self.check_res=QPushButton('uznat result')


        self.layout_vert_left=QVBoxLayout()
        self.layout_vert_right=QVBoxLayout()
        self.total_layout=QHBoxLayout()
        self.layout_vert_left.addWidget(self.label_name)
        self.layout_vert_left.addWidget(self.line_if_name)
        self.layout_vert_left.addWidget(self.label_age)
        self.layout_vert_left.addWidget(self.line_age)
        self.layout_vert_left.addWidget(self.label_instr_1)
        self.layout_vert_left.addWidget(self.btn_test_1)
        self.layout_vert_left.addWidget(self.line_beatsm_1)
        self.layout_vert_left.addWidget(self.check_res,alignment=Qt.AlignRight)
        self.setLayout(self.layout_vert_left)

    def timer1Event(self):
        pass


    def timer_test(self):
        time=QTime(0,1,0)
        self.timer=QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def connects(self):
        self.btn_test_1.clicked.connect(self.timer_test)

    def next_click(self):
        pass
