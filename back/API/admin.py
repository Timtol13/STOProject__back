from django.contrib import admin
from .models import Orders, Services, SuccessedOrders, Detail

admin.site.register([Orders, Services, SuccessedOrders, Detail])