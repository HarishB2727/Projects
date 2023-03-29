from django.urls import path, include
from . import views
urlpatterns = [
    path('hardcode', views.show_hardcode_board, name='hardcode_board'),
    path('board', views.show_board, name='show_board')
]