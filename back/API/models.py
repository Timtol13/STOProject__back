from django.db import models
from django.db.models import CharField, TextField, IntegerField, FileField, Model, BooleanField
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
    
class Detail(Model):
    mark = CharField("Mark", max_length=255, blank=True)
    type = CharField("Type", max_length=255, blank=True)
    count = IntegerField("Count on store", blank=True)
    isAvaliable = BooleanField("Is avaliable", blank=True)
    price = IntegerField("Price", blank=True)

    def __str__(self):
        return '{self.mark} {self.type}'

class Services(Model):
    title = CharField('Title', max_length=255, blank=True)
    description = TextField('Description', blank=True)
    openDescription = TextField('Description on open', blank=True)
    price = CharField('Price', max_length=200, blank=True)

    def __str__(self):
        return str(self.title)
    
class SuccessedOrders(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username', blank=True, null=True)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, to_field='id', blank=True, null=True)
    stars = IntegerField("Stars", blank=True)
    feedback = CharField("Feedback", max_length=144, blank=True, null=True)

    def __str__(self):
        return str(self.feedback)