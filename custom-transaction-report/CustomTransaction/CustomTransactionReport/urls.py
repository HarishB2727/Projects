from django.urls import path
from . import views

app_name='Transaction'

urlpatterns = [
    path('test', views.filter, name='test'),
    path('Home', views.Home_page, name = 'Home'),
    path('Product_volume_report', views.product_volume_report, name = 'product_volume'),
    path('Product_value_report', views.product_value_report, name = 'product_value'),
    path('Customer_volume_report', views.customer_volume_report, name = 'customer_volume'),
    path('customer_value_report', views.customer_value_report, name = 'customer_value'),
    path('filter/<str:name>', views.filter, name = 'filter'),
    path('login', views.login, name = 'login'),
    path('registration', views.registration, name = 'registration'),
    path('logout', views.logout, name = 'logout')
]