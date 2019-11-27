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
    # gameQuestion = []
    # gameAnswer = []
    # for card in Card.select():
    #     gameQuestion.append(card.question)
    #     gameAnswer.append(card.answer)
    # print(f"{gameQuestion}  and  {gameAnswer}")
    correct = 0
    incorrect = 0
    for card in Card.select():
        if input(f"{card.question}\n") == card.answer:
            print("YOU are NOT DUMB")
            correct += 1
        else:
            print("YOUR DUMB")
            incorrect += 1


db.create_tables([Card])
menu()
