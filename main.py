from peewee import *
from datetime import date

db = PostgresqlDatabase('flashcards', user='postgres', password='',
                        host='localhost', port=5432)
db.connect()


class BaseModel(Model):

    class Meta:
        database = db


class Card(BaseModel):
    question = CharField()
    answer = CharField()


class Menu:
    def __init__(self):
        a = input("C:Create\nP: Play\n")
        if(a == 'P'):
            game()
        if a == 'C':
            question = question = input("NEW QUESTION for your card \n")
            answer = answer = input("NEW answer for your card \n")
            card = Card(question=question, answer=answer)
            card.save()
            print(f"{card.question} and {card.answer}")
            question = input("Do you want to add more:y/n ")
            if question == 'y':
                # menu()
                print("x")


def game():
    print("Welcome to the game")


db.create_tables([Card])
# menu()
