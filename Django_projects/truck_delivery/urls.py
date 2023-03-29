from django.urls import path, include
from . import views

app_name='truck_delivery'

urlpatterns = [
    path('check', views.checking_, name='check'),
    path('data', views.truck_data, name='data'),
    path('login',views.login, name='login'),
    path('assign/<int:number>', views.assign_truck, name='assign_data'),
    path('unassign/<int:number>', views.unassign_truck, name='unassign_data'),
    path('logout',views.logout, name='logout'),

]