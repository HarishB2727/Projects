from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import random
from .models import clients, clients_data, food_table, diet_table 

def test(request):
    # return HttpResponse("harish")
    return HttpResponse('ok')

def Home(request):

    return render(request, 'Home.html')

def Clients(request):
    clients_ = clients.objects.all()
    # return HttpResponse(f'ok..Hi clients{clients_}')
    context = {'clientss': clients_}
    return render(request, 'clients.html', context)

def Food_data(request):
    return HttpResponse('ok..Hi food_data')

def Clients_diet(request, name):
    client_object = clients.objects.get(name = name)

    client = clients_data.objects.get(clients_name = client_object)
    # return HttpResponse(f'ok..Hi clients_data{client}')
    food_data = food_table.objects.all()
    diet_table_ = diet_table.objects.filter(clients = client_object)
    total_calories_ = sum([c.food_table.calories * c.quantity/100 for c in diet_table.objects.filter(clients = client_object)])
    total_protein_ = sum([c.food_table.protein * c.quantity/100 for c in diet_table.objects.filter(clients = client_object)])
    total_fat_ = sum([c.food_table.fat * c.quantity/100 for c in diet_table.objects.filter(clients = client_object)])
    total_carbs_ = sum([c.food_table.carbs * c.quantity/100 for c in diet_table.objects.filter(clients = client_object)])
    total_quantity_ = sum([c.quantity for c in diet_table.objects.filter(clients = client_object)])
    context = {'name':client_object, 'client_datas':client, 'food':food_data, 'diet':diet_table_, 'total_calories':total_calories_, 'total_protein': total_protein_, 'total_fat':total_fat_, 'total_carbs':total_carbs_, 'total_quantity':total_quantity_}
    return render(request,'client_data.html',context)
     
    # print(name)

def add_diet(request,name,item):
    # if request.method == "POST":
        # form = DietForm(request.POST)
    name_  = name
    client_object = clients.objects.get(name = name)
    food_object = food_table.objects.get(item_name = item)
    quantity_ = request.POST.get('quantity')

    diets_ = diet_table(clients = client_object,food_table = food_object,quantity = quantity_)
    diets_.save()
    # url = reverse('Clients_diet', args=[name_])
    # url = f'fitness/Clients_diet/?param={param_value}'
    return redirect(f'http://127.0.0.1:8000/fitness/Clients_diet/{name_}/')

def delete_diet_column(request,name,item):
    name_ = name
    client_object = clients.objects.get(name = name)
    food_object = food_table.objects.get(item_name = item)
    diets_ = diet_table.objects.filter(clients=client_object,food_table = food_object).delete()
    return redirect(f'http://127.0.0.1:8000/fitness/Clients_diet/{name_}/')




