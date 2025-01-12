from mongoengine import *
from model import spell

class Class(Document):
    name = StringField(required=True)
    img = ImageField
    spellbook = ListField(ReferenceField(spell.Spell))