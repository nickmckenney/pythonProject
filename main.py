from peewee import *
from datetime import date
# from tkinter import *
# import tkinter as tk
# import PySimpleGUI as sg

# sg.change_look_and_feel('DarkAmber')  # Add a touch of color
# # All the stuff inside your window.
# layout = [[sg.Text('Some text on Row 1')],
#           [sg.Text('Enter something on Row 2'), sg.InputText()],
#           [sg.Button('Ok'), sg.Button('Cancel')]]

# # Create the Window
# window = sg.Window('Window Title', layout)
# # Event Loop to process "events" and get the "values" of the inputs
# while True:
#     event, values = window.read()
#     if event in (None, 'Cancel'):  # if user closes window or clicks cancel
#         break
#     print('You entered ', values[0])

# window.close()


db = PostgresqlDatabase('flashcards', user='postgres', password='',
                        host='localhost', port=5432)
db.connect()


class BaseModel(Model):

    class Meta:
        database = db


class Card(BaseModel):
    question = CharField()
    answer = CharField()


def menu():
    a = input("C:Create\nV: View\n G: Game\n")
    if(a == 'V'):
        viewAllCards()
    if a == 'G':
        game()
    if a == 'C':

        question = input("NEW QUESTION for your card \n")
        answer = input("NEW answer for your card \n")
        card = Card(question=question, answer=answer)
        card.save()
        print(f"{card.question} and {card.answer}")
        question = input("Do you want to add more:y/n ")
        if question == 'y':
            menu()


def viewAllCards():
    for card in Card.select():
        print("QUESTION "+card.question+" ANSWER "+card.answer)


def game():
    correct = 0
    incorrect = 0
    for card in Card.select():
        if input(f"{card.question}\n") == card.answer:
            correct += 1
            print(f"Amount of correct: {correct}")

        else:
            incorrect += 1
            print(f"Amount of incorrect: {incorrect}")
            if input("do you want to see the back y/n") == 'y':
                print(f"answer is {card.answer}")


db.create_tables([Card])
menu()
