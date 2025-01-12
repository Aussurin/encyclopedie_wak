from mongoengine import *


class Slot (document) :
        nom : StringField
        icon : ImageField