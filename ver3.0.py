
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QMessageBox, QRadioButton
from ni99 import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x,win_y)
    def initUI(self):
        self.hello = QLabel(txt_hello)
        self.description = QLabel(txt_desc)
        self.button = QPushButton(txt_button)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello)
        self.layout.addWidget(self.description)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)



    def connects(self):
        self.button.clicked.connect(self.next_click)


    def next_click(self):
        self.hide()
        self.tw = TestWin()

app=QApplication([])
main_menu=MainWin()
app.exec()






























from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import (QApplication, QWidget,QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QMessageBox, QRadioButton)
from ni99 import *

    

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle('Тест Диксона Руфье')
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.label_name = QLabel("Введите ФИО")
        self.line_lf_name = QLineEdit('Ф.И.О')

        self.label_age = QLabel('Полных лет')
        self.line_age = QLineEdit('0')

        self.label_inst_1 = QLabel(intstr_1)
        self.btn_test_1 = QPushButton('Начать первый тест')

        self.text_timer=QLabel('00:00:60')

        self.line_bpm_1 = QLineEdit('Введите количество ударов в минуту')

        self.check_res = QPushButton('Узнать результат')

        self.layout_vert_left = QVBoxLayout()
        self.layout_vert_right = QVBoxLayout()
        self.total_layout = QHBoxLayout()
        self.layout_vert_left.addWidget(self.label_name)
        self.layout_vert_left.addWidget(self.line_lf_name)
        self.layout_vert_left.addWidget(self.label_age)
        self.layout_vert_left.addWidget(self.line_age)
        self.layout_vert_left.addWidget(self.label_inst_1)
        self.layout_vert_left.addWidget(self.btn_test_1)

        self.layout_vert_right.addWidget(self.text_timer)

        self.layout_vert_left.addWidget(self.line_bpm_1)
        self.layout_vert_left.addWidget(self.check_res, alignment=Qt.AlignRight)

        self.total_layout.addLayout(self.layout_vert_left)
        self.total_layout.addLayout(self.layout_vert_right)

        self.setLayout(self.total_layout)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm.:ss'))
        if time.toString('hh:mm:ss')=='00:00:00':
            self.timer.stop()

    def timer_test(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def connects(self):
        self.btn_test_1.clicked.connect(self.timer_test)

    def next_click(self):
        pass

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    txt_title = ' test rufie'
win_width = 750
win_height = 500
win_x = 400
win_y = 10
txt_hello = 'dobro pozhalovat v prilozhenie dlya prohoda testa rufie'
txt_desc = 'glavnaya cel testa rufie zaklyuchaetsya v tom chto by pomoch svoim klientam uznat podrobnee detali svoego zdorovya'
txt_button = 'nachat'
intstr_1 = ''
