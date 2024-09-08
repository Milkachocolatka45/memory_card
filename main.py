from PyQt5.QtWidgets import QApplication
from random import choice, shuffle

app = QApplication([]) #створення додатку

from main_window import * # імпортує файл з вікна
from menu_window import *

main_window.show()# показує вікно 


class Question: #створення клас для  створення запитань
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question
        self.answer = answer
        self.wrong_ans1 = wrong_ans1
        self.wrong_ans2 = wrong_ans2
        self.wrong_ans3 = wrong_ans3
#створення запитань
q1 = Question("Чупакабра", "chupacabra", "chipa", "Chupakabra", "chupic" ) #запитання які будуть тут
q2 = Question("Маркер", "marker", "maker", "ma", "Marker")
q3 = Question("Шарик", "ballon", "ball", "chapuk", "balls")
q4 = Question("Женя", "викладач", "лапочка", "вчитель", "безсердечний")
q5 = Question("Школа", "кладбище", "Херня", "ААДДД", "дом душей мертвих дітей")
q6 = Question("Математичка", "Демон во плоти", "Демон", "Вампир","смерть")

questions = [q1, q2, q3, q4]#список з запитаннями
radio_btns = [r_btn1, r_btn2, r_btn3, r_btn4]#список з кнопками
#змінні для статистики
count_right = 0
count_wrong = 0
count_all = 0

def new_question(): #додавання питання в вікно з карткою
    global cur_quest
    cur_quest = choice(questions)# вибираємо рандомне питання
    lbl_question.setText(cur_quest.question)#відобраємо питання
    lbl_right.setText(cur_quest.answer)#відображаємо правильну відповідь

    shuffle(radio_btns)# перемішуємо список з кнопками
    #додаємо варіанти відповідей в кнопки
    radio_btns[0].setText(cur_quest.answer)
    radio_btns[1].setText(cur_quest.wrong_ans1)
    radio_btns[2].setText(cur_quest.wrong_ans2)
    radio_btns[3].setText(cur_quest.wrong_ans3)

new_question()

def check_ans(): #перевірка правильності відповідей
    global count_all, count_right, count_wrong
    radio_buttons_group.setExclusive(False) #дозволяє змінювати кнопки
    for btn in radio_btns:#перебераємо список з кнопками
        if btn.isChecked():#знайодимо вибрану кнопку
            if btn.text() == cur_quest.answer:#перевірка правильності відповіді
                count_right += 1
                count_all += 1
                lbl_correct.setText("Правильно!")
                btn.setChecked(False)#прибираємо виділення з кнопки
                break
    else:
        lbl_correct.setText("Не правилно!")
        btn.setChecked(False)#блокуємо змінню кнопок
        count_wrong += 1
        count_all += 1
    radio_buttons_group.setExclusive(True)
              
def next_question():
    if btn_answer.text() == "Відповісти":
        check_ans()
        answer_group_box.hide()
        result_group_box.show()
        btn_answer.setText("Наступне запитання")
    elif btn_answer.text() == "Наступне запитання":
        new_question()
        result_group_box.hide()
        answer_group_box.show()
        btn_answer.setText("Відповісти")

def clear():
    question_input.clear()
    right_ans_input.clear()
    wrong_ans1_input.clear()
    wrong_ans2_input.clear()
    wrong_ans3_input.clear()

def add_question():
    question =Question(question_input.text(), right_ans_input.text(), wrong_ans1_input.text(), wrong_ans2_input.text(), wrong_ans3_input.text())
    questions.append(question)
    clear()

def to_menu():#показує вікно з меню 
    main_window.hide()
    menu_window.show()

def to_main():# показує головне вікно
    menu_window.hide()
    main_window.show()
#підключення кнопок до фунція
btn_menu.clicked.connect(to_menu)
btn_back.clicked.connect(to_main)
btn_answer.clicked.connect(next_question)
btn_add.clicked.connect(add_question)
btn_clear.clicked.connect(clear)

app.exec_()# щоб вікно не зачинялося коли захоче