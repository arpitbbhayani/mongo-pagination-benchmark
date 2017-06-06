import faker
import random

from dbutil import db

fak = faker.Faker()


def insert_one(student):
    student_id = db['students'].insert(student)


def populate(count):
    for i in range(count):
        student = {
            'name': fak.name(),
            'marks': random.randint(1, 100)
        }
        insert_one(student)
