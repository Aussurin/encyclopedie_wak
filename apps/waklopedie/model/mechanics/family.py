from mongoengine import *


class Family (document) :
        nom : StringField
        lvl_cap : int
        icon : ImageField