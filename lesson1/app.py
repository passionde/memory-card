from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QGroupBox, QPushButton, QHBoxLayout, QVBoxLayout

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Memory Card")

"""Линия 1"""
layout_h_1 = QHBoxLayout()
question = QLabel("В каком году была основана Москва?")
layout_h_1.addWidget(question, alignment=(Qt.AlignVCenter | Qt.AlignHCenter))

"""Линия 2"""
layout_h_2 = QHBoxLayout()

# Необходимые виджеты
answer_group = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton("1147")
rbtn_2 = QRadioButton("1242")
rbtn_3 = QRadioButton("1861")
rbtn_4 = QRadioButton("1943")

# Компоновка виджетов
layout_col_1 = QVBoxLayout()
layout_col_2 = QVBoxLayout()
layout_answers = QHBoxLayout()

layout_col_1.addWidget(rbtn_1)
layout_col_1.addWidget(rbtn_2)
layout_col_2.addWidget(rbtn_3)
layout_col_2.addWidget(rbtn_4)

layout_answers.addLayout(layout_col_1)
layout_answers.addLayout(layout_col_2)

answer_group.setLayout(layout_answers)
layout_h_2.addWidget(answer_group)

"""3 линия"""
layout_h_3 = QHBoxLayout()
btn_ok = QPushButton("Ответить")

layout_h_3.addStretch(1)
layout_h_3.addWidget(btn_ok, stretch=2)
layout_h_3.addStretch(1)

"""Компоновка линий в один макет"""
main_layout = QVBoxLayout()
main_layout.addLayout(layout_h_1, stretch=2)
main_layout.addStretch(1)
main_layout.addLayout(layout_h_2, stretch=8)
main_layout.addStretch(1)
main_layout.addLayout(layout_h_3, stretch=1)
main_layout.setSpacing(5)
main_layout.addStretch(1)

"""Установка основного макета"""
main_win.setLayout(main_layout)

main_win.show()
app.exec_()
