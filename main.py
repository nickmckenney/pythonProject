from peewee import *
from datetime import date
# import tkinter
# tk = tkinter.Tk()
# canvas = tkinter.Canvas(tk, width=500, height=500)
# canvas.pack()

# # Enter into eventloop <- this will keep
# # running your application, until you exit
# tk.mainloop()

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
    a = input("C:Create\nV: View\nG: Game\nD: Delete\n")
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
        question = input("Do you want to go to menu :y/n ")
        if question == 'y':
            menu()
    if a == 'D':
        card = Card.get(Card.id == input(
            "what question do you want to delete? Must use ID number "))
        card.delete_instance()
        card.save()
        question = input("Do you want to go to menu :y/n ")
        if question == 'y':
            menu()


def viewAllCards():
    for card in Card.select():
        print("QUESTION "+card.question+" ANSWER "+card.answer)


def game():
    correct = 0
    incorrect = 0
    a = int(input("How Many Cards Do You want from your deck? "))

    for card in Card.select():
        if a > 0:
            a -= 1
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
