from peewee import *
from datetime import date

db = PostgresqlDatabase('flashcards', user='postgres', password='',
                        host='localhost', port=5432)


class BaseModel(Model):

    class Meta:
        database = db


class Card(BaseModel):
    question = CharField()
    answer = CharField()


def Menu():
    a = input("C:Create\nR:Read\n")
    if a == 'C':
        question = Card(question=input("NEW QUESTION for your card \n"))
        question.save()
        print(f"{question.question}")

    else:
        print(f"{question.question}")


db.connect()

db.create_tables([Card])
db.drop_tables([Card])
