from django.db import models
from django.db.models import CharField, TextField, IntegerField, FileField, Model
from django.contrib.auth.models import User

class Orders(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username', blank=True, null=True)
    orderType = CharField("Order Type", max_length=255, blank=True)
    title = CharField('Title', max_length=255, blank=True)
    adress = CharField('Adress', max_length=255, blank=True)
    price = IntegerField("Price", blank=True)
    time = CharField('Date', max_length=255, blank=True)
    status = CharField('Status', max_length=255, blank=True)

    def __str__(self):
        return str(self.user)

class Services(Model):
    image = FileField('Icon', upload_to='images', max_length=100)
    title = CharField('Title', max_length=255, blank=True)
    description = TextField('Description', blank=True)
    openDescription = TextField('Description on open', blank=True)
    price = CharField('Price', max_length=200, blank=True)