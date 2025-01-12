from mongoengine import *
from model import *
from mechanics import elem



class Ligne (document) :
        ratio = FloatField
        qty = IntField
        effect = StringField(required=True) 
        stat = StringField
        elem = ReferenceField(elem.Elem)
    