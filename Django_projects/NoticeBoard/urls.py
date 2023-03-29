from django.urls import path, include
from . import views
app_name = 'Notice'
urlpatterns = [
    path('show_board', views.show_board, name= 'show_'),
    path('data', views.Notice_board, name='notice_board'),
]