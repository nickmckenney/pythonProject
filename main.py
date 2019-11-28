from peewee import *
from datetime import date
from tkinter import *
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


root = tk.Tk()
app = Application(master=root)
app.mainloop()


# db = PostgresqlDatabase('flashcards', user='postgres', password='',
#                         host='localhost', port=5432)
# db.connect()


# class BaseModel(Model):

#     class Meta:
#         database = db


# class Card(BaseModel):
#     question = CharField()
#     answer = CharField()


# def menu():
#     a = input("C:Create\nV: View\n G: Game\n")
#     if(a == 'V'):
#         viewAllCards()
#     if a == 'G':
#         game()
#     if a == 'C':

#         question = input("NEW QUESTION for your card \n")
#         answer = input("NEW answer for your card \n")
#         card = Card(question=question, answer=answer)
#         card.save()
#         print(f"{card.question} and {card.answer}")
#         question = input("Do you want to add more:y/n ")
#         if question == 'y':
#             menu()


# def viewAllCards():
#     for card in Card.select():
#         print("QUESTION "+card.question+" ANSWER "+card.answer)


# def game():
#     correct = 0
#     incorrect = 0
#     for card in Card.select():
#         if input(f"{card.question}\n") == card.answer:
#             correct += 1
#             print(f"Amount of correct: {correct}")

#         else:
#             incorrect += 1
#             print(f"Amount of incorrect: {incorrect}")
#             if input("do you want to see the back y/n") == 'y':
#                 print(f"answer is {card.answer}")


# db.create_tables([Card])
# menu()
