from mongoengine import *


class Category (document) :
        nom : StringField
        icon : ImageField