from django.urls import path
from . import views

app_name='fitness'

urlpatterns = [
    path('test', views.test, name='test'),
    path('home', views.Home, name='Home'),
    path('clients', views.Clients, name = "Clients"),
    path('food_data', views.Food_data, name = "Food_data"),
    path('Clients_diet/<str:name>/', views.Clients_diet, name = "Clients_diet"),
    path('add_diet/<str:name>/<str:item>', views.add_diet, name = "add_diet"),
    path('delete_diet_colomn/<str:name>/<str:item>', views.delete_diet_column, name = "delete_diet_colomn")
]

