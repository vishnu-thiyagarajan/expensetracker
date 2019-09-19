from django.contrib import admin
from .models import Client, Expense
# Register your models here.

admin.site.register(Client)
admin.site.register(Expense)
