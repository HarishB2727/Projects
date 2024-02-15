from django.contrib import admin
from .models import clients,clients_data, food_table, diet_table
# Register your models here.
admin.site.register([clients,clients_data, food_table, diet_table])