from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit

menu_window = QWidget()
menu_window.resize(400, 300)# створюємо розміри 
menu_window.setWindowTitle("Memory card")
menu_window.move(700, 300)

question_lbl = QLabel("Введіть запитання:")# створюємо запитання 
right_ans_lbl = QLabel("Введіть правильну відповідь:")#створюємо правильну відповідь
wrong_ans1_lbl = QLabel("Введіть неправильну відповідь:")#створюємо неправильні відповіді
wrong_ans2_lbl = QLabel("Введіть неправильну відповідь:")
wrong_ans3_lbl = QLabel("Введіть неправильну відповідь:")

question_input = QLineEdit()
right_ans_input = QLineEdit()
wrong_ans1_input = QLineEdit()
wrong_ans2_input = QLineEdit()
wrong_ans3_input = QLineEdit()

btn_add = QPushButton("ДОдати запитання")# додаєм кнопкузапитання
btn_clear = QPushButton("Очистити")

lbl_start = QLabel("СТАТИСТИКА")#робим статистику жирной і великой щоб виділялася
lbl_start.setStyleSheet("font-size: 20px;font-weight: bold;")

statistics = QLabel()

btn_back = QPushButton("Назад")#робимо книпку назад щоб повертатися на другу сторінку

col1 = QVBoxLayout()#створення вертикальних ліній і кладання на них книпок
col2 = QVBoxLayout()

col1.addWidget(question_lbl)
col1.addWidget(right_ans_lbl)
col1.addWidget(wrong_ans1_lbl)
col1.addWidget(wrong_ans2_lbl)
col1.addWidget(wrong_ans3_lbl)

col2.addWidget(question_input)
col2.addWidget(right_ans_input)
col2.addWidget(wrong_ans1_input)
col2.addWidget(wrong_ans2_input)
col2.addWidget(wrong_ans3_input)

line2 = QHBoxLayout()
line2.addWidget(btn_add)
line2.addWidget(btn_clear)

line1 = QHBoxLayout()
line1.addLayout(col1)
line1.addLayout(col2)

main_line = QVBoxLayout()
main_line.addLayout(line1)
main_line.addLayout(line2)
main_line.addWidget(lbl_start)
main_line.addWidget(statistics)
main_line.addWidget(btn_back)

menu_window.setLayout(main_line)


