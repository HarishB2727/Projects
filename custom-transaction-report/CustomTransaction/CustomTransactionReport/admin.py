from django.contrib import admin
from .models import Transcations, Product, Cart
# Register your models here.

admin.site.register([Transcations, Product, Cart])