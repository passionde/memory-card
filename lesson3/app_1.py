from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QGroupBox, QPushButton, QHBoxLayout, \
    QVBoxLayout, QButtonGroup

from random import shuffle

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
rbtn_1 = QRadioButton("1147")
rbtn_2 = QRadioButton("1242")
rbtn_3 = QRadioButton("1861")
rbtn_4 = QRadioButton("1943")

btn_group = QButtonGroup()  # <-- логическая группа кнопок
btn_group.addButton(rbtn_1)
btn_group.addButton(rbtn_2)
btn_group.addButton(rbtn_3)
btn_group.addButton(rbtn_4)

result_group = QGroupBox("Результат теста")  # <-- панель результатов
lb_result = QLabel("Прав ты или нет?")
lb_correct = QLabel("Ответ будет тут")

layout_result = QVBoxLayout()
layout_result.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_result.addWidget(lb_correct, alignment=Qt.AlignCenter, stretch=2)

result_group.setLayout(layout_result)


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
layout_h_2.addWidget(result_group)
result_group.hide()  # Скрыть панель

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
main_layout.addStretch(1)

main_layout.setSpacing(5)

"""Установка основного макета"""
main_win.setLayout(main_layout)


def show_result():
    answer_group.hide()
    result_group.show()
    btn_ok.setText("Следующий вопрос")


def show_question():
    answer_group.show()
    result_group.hide()
    btn_ok.setText("Ответить")

    btn_group.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    btn_group.setExclusive(True)


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(question_txt, right_answer, wrong_1, wrong_2, wrong_3):
    shuffle(answers)

    answers[0].setText(right_answer)
    answers[1].setText(wrong_1)
    answers[2].setText(wrong_2)
    answers[3].setText(wrong_3)

    question.setText(question_txt)
    lb_correct.setText(right_answer)
    show_question()


def show_correct(res):
    lb_result.setText(res)
    show_result()


def check_answer():
    if answers[0].isChecked():
        show_correct("Правильно!")
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct("Неверно!")


ask("2 + 2 = ?", "4", "6", "1", "-4")
btn_ok.clicked.connect(check_answer)


main_win.resize(400, 300)
main_win.show()
app.exec_()
