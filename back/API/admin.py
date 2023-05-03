from django.contrib import admin
from .models import Orders, Services

admin.site.register([Orders, Services])