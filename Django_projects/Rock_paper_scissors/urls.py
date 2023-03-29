from django.urls import path,include
from . import views
#RPS/
urlpatterns = [
    path('game',views.game_function,name = "RPS"),
]