from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QGroupBox, QPushButton, QHBoxLayout, \
    QVBoxLayout, QButtonGroup

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Memory Card")

"""Вопрос карточки"""
layout_h_1 = QHBoxLayout()
question = QLabel("В каком году была основана Москва?")
layout_h_1.addWidget(question, alignment=(Qt.AlignVCenter | Qt.AlignHCenter))

"""Макет для панели вопроса/ответа"""
layout_h_2 = QHBoxLayout()

# Необходимые виджеты
answer_group = QGroupBox("Варианты ответов")  # <-- панель вопросов
button_group = QButtonGroup()

rbtn_1 = QRadioButton("1147")
rbtn_2 = QRadioButton("1242")
rbtn_3 = QRadioButton("1861")
rbtn_4 = QRadioButton("1943")

button_group.addButton(rbtn_1)
button_group.addButton(rbtn_2)
button_group.addButton(rbtn_3)
button_group.addButton(rbtn_4)

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

# Панель результатов
result_group = QGroupBox("Результат тест")
lb_result = QLabel("Правильно / неправильно")
lb_correct = QLabel("Правильный ответ")

result_layout = QVBoxLayout()
result_layout.addWidget(lb_result, alignment=(Qt.AlignTop | Qt.AlignLeft))
result_layout.addWidget(lb_correct, alignment=Qt.AlignCenter, stretch=2)

result_group.setLayout(result_layout)
layout_h_2.addWidget(result_group)
result_group.hide()

"""Кнопка отправки ответа"""
layout_h_3 = QHBoxLayout()
btn_ok = QPushButton("Ответить")

layout_h_3.addStretch(1)
layout_h_3.addWidget(btn_ok, stretch=2)
layout_h_3.addStretch(1)

"""Сборка всех элементов в один макет"""
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


def show_result():
    answer_group.hide()
    result_group.show()
    btn_ok.setText("Следующий вопрос")


def show_question():
    button_group.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    button_group.setExclusive(True)

    answer_group.show()
    result_group.hide()
    btn_ok.setText("Ответить")


def start_test():
    if btn_ok.text() == "Ответить":
        show_result()
    elif btn_ok.text() == "Следующий вопрос":
        show_question()


btn_ok.clicked.connect(start_test)

main_win.show()
app.exec_()
