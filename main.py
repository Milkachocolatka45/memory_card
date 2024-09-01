from PyQt5.QtWidgets import QApplication
from random import choice, shuffle

app = QApplication([]) #створення додатку

from main_window import * # імпортує файл з вікна
from menu_window import *

main_window.show()# показує вікно 


class Question:
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question
        self.answer = answer
        self.wrong_ans1 = wrong_ans1
        self.wrong_ans2 = wrong_ans2
        self.wrong_ans3 = wrong_ans3

q1 = Question("Чупакабра", "chupacabra", "chipa", "Chupakabra", "chupic" )
q2 = Question("Маркер", "marker", "maker", "ma", "Marker")
q3 = Question("Шарик", "ballon", "ball", "chapuk", "balls")
q4 = Question("Женя", "викладач", "лапочка", "вчитель", "безсердечний")
q5 = Question("Школа", "кладбище", "Херня", "ААДДД", "дом душей мертвих дітей")
q6 = Question("Математичка", "Демон во плоти", "Демон", "Вампир","смерть")

questions = [q1, q2, q3, q4]
radio_btns = [r_btn1, r_btn2, r_btn3, r_btn4]

count_right = 0
count_wrong = 0
count_all = 0

def new_question():
    global cur_quest
    cur_quest = choice(questions)
    lbl_question.setText(cur_quest.question)
    lbl_right.setText(cur_quest.answer)

    shuffle(radio_btns)
    radio_btns[0].setText(cur_quest.answer)
    radio_btns[1].setText(cur_quest.wrong_ans1)
    radio_btns[2].setText(cur_quest.wrong_ans2)
    radio_btns[3].setText(cur_quest.wrong_ans3)

new_question()

def check_ans():
    global count_all, count_right, count_wrong
    radio_buttons_group.setExclusive(False)
    for btn in radio_btns:
        if btn.isChecked():
            if btn.text() == cur_quest.answer:
                count_right += 1
                count_all += 1
                lbl_correct.setText("Правильно!")
                btn.setCheckable(False)
                break
    else:
        lbl_correct.setText("Не правилно!")
        btn.setCheckable(True)
        count_wrong += 1
        count_all += 1
                

def to_menu():#показує вікно з меню 
    main_window.hide()
    menu_window.show()

def to_main():# показує головне вікно
    menu_window.hide()
    main_window.show()
#підключення кнопок до фунція
btn_menu.clicked.connect(to_menu)
btn_back.clicked.connect(to_main)
app.exec_()# щоб вікно не зачинялося коли захоче