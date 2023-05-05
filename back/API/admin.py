from django.contrib import admin
from .models import Orders, Services, SuccessedOrders

admin.site.register([Orders, Services, SuccessedOrders])