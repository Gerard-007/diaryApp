from peewee import *
from collections import OrderedDict


db = SqliteDatabase("challenges.db")

class Challenge(Model):
    name = CharField(max_length=100)
    language = CharField(max_length=100)
    
    class Meta:
        database = db
        
def initialize():
    db.connect()
    db.create_table([Challenge], safe=True)

#from models import Challenge
def get_all_challenges():
    all_challenges = Challenge.select()
    for challenge in all_challenges:
        print(challenge.name, ' --> ', challenge.language)

def add_new_challenge():
    Challenge.create(language="Ruby", name="Booleans")

def sort_all_challenge():
    sorted_challenges = Challenge.select().order_by(Challenge.steps.asc())

def create_challenge(name, language, steps=1):
    Challenge.create(name=name,
                     language=language,
                     steps=steps)


def search_challenges(name, language):
    return Challenge.select().where(
        Challenge.name.contains(name),
        Challenge.language==language
    )

def delete_challenge(Challenge):
    Challenge.delete_instance()

menu = OrderedDict([
    ('n', new challenge),
    ('s', new step),
    ('d', delete a challenge),
    ('e', edit a challenge),
])
		
if __name__ == '__main__':
    initialize()
    add_new_challenge()
    get_all_challenges()