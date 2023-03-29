from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Owner,Trucks
from django.contrib.auth import authenticate

def checking_(request):
    return HttpResponse("ok")

# Create your views here.

def login(request):
    error_message = ''
    if request.method == 'POST':
        username_ = request.POST.get('username')
        password_ = request.POST.get('password')
        user = authenticate(username=username_, password=password_)
        if user is not None:
            request.session['logged_in_student'] = user.username
            # owner = Owner.objects.get(user=user)
            return redirect('truck_delivery:data')
        else:
            error_message = 'Wrong password'
    context = {'error_message': error_message}
    return render(request, 'truck_delivery/login.html', context)
    



def truck_data(request):
    assign_trucks = []
    unassign_trucks = []
    owner_ = Owner.objects.get(pk=1)
    trucks_ = Trucks.objects.filter(owner=owner_)

    is_authenticated = request.session.get('logged_in_student') == owner_.user.username


    for truck in trucks_:
        if truck.assign == 'assign':
            assign_trucks.append(truck.number)
        else:
            unassign_trucks.append(truck.number)

    context = {'assign_trucks': assign_trucks, 'unassign_trucks': unassign_trucks}
    
    if is_authenticated:
        context['authenticated_student_id'] = True

    return render(request,'truck_delivery/data.html',context)
    # return HttpResponse(f"{assign_trucks}")




def assign_truck(request, number):
    # truck_number_ = request.GET.get('number')
    truck_number_ = number

    owner_ = Owner.objects.get(pk=1)
    trucks_ = Trucks.objects.filter(owner=owner_)
    # k = ""
    for truck in trucks_:
        if truck.number == truck_number_:
            # k = truck.assign
            truck.assign = "unassign"
            truck.save()
        truck.save()
        
    # trucks_.save()

    return redirect('truck_delivery:data')




    




def unassign_truck(request,number):
    truck_number_ = number

    owner_ = Owner.objects.get(pk=1)
    trucks_ = Trucks.objects.filter(owner=owner_)
    # k = ""
    for truck in trucks_:
        if truck.number == truck_number_:
            # k = truck.assign
            truck.assign = "assign"
            truck.save()
        truck.save()
        
    # trucks_.save()

    return redirect('truck_delivery:data')

def logout(request):
    del request.session['logged_in_student']
    return redirect('truck_delivery:login')
