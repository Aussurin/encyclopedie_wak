from mongoengine import *


class Elem (document) :
        nom : StringField
        icon_m : ImageField
        icon_r : ImageField