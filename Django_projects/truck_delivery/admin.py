from django.contrib import admin
from .models import Owner, Trucks
# Register your models here.
admin.site.register([Owner, Trucks])