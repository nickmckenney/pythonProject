from peewee import *
from datetime import date

db = PostgresqlDatabase('flashcards', user='postgres', password='',
                        host='localhost', port=5432)


class BaseModel(Model):

    class Meta:
        database = db


class Frontcard(BaseModel):
    question = CharField()


class Backcard(BaseModel):

    answer = CharField()


class Menu(BaseModel):
    a = input("C:Create\nR:Read\n")
    if a == 'C':
        question = Frontcard(question=input("NEW QUESTION for your card \n"))
        question.save()
        print(f"{question.question}")

    else:
        print(f"{question.question}")


db.connect()

db.drop_tables([Frontcard])
db.create_tables([Frontcard])
db.drop_tables([Backcard])
db.create_tables([Backcard])
db.drop_tables([Menu])
db.create_tables([Menu])
