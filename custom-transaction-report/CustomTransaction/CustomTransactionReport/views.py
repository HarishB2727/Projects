from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Transcations, Product, Cart
from django.contrib.auth import authenticate
import json

filter_data = []
additional_filter = []

def filter(request, name):
    # global Name, pincode , amount_lower, amount_upper\
    global additional_filter
    # filter_data = date_time_filter
    if request.method == 'POST':
        # name_filter = Transcations.objects
        if request.POST.get('customer_name') != "":
            Name = request.POST.get('customer_name')
            additional_filter = additional_filter.filter(customer_name = Name)
        if request.POST.get('pin_code') != "":
            pincode = request.POST.get('pin_code')
            additional_filter = additional_filter.filter(pin_Code = pincode)
        if request.POST.get('amount_upper') != "":
            amount_upper = request.POST.get('amount_upper')
            additional_filter = additional_filter.filter(total_Transaction__lt = amount_upper)
        if request.POST.get('amount_lower') != "":
            amount_lower = request.POST.get('amount_lower')
            additional_filter = additional_filter.filter(total_Transaction__gt = amount_lower)
        # filter_data = filter_data.all()
        
        # return HttpResponse(f"{filter_data}")
    # return render(request, 'CustomerTransactionReport/index.html')
        return redirect(f'Transaction:{name}')

def Home_page(request):
    # name = 'harish'
    global filter_data, additional_filter
    # request.session['date_from'] = None
    # request.session['date_to'] = None
    if request.session.get('Access'):
        filter_data = Transcations.objects
        if request.method == 'POST':
            report_type = request.POST.get('report_type')
            if request.POST.get('date_from') != "":
                # Name = request.POST.get('customer_name')
                date_from = request.POST.get('date_from')
                request.session['date_from'] = date_from
                filter_data = filter_data.filter(date_field__gt = date_from)
                # print(filter_data)
                # return HttpResponse(f"{filter_data}")
            if request.POST.get('date_to') != "":
                date_to = request.POST.get('date_to')
                request.session['date_to'] = date_to
                filter_data = filter_data.filter(date_field__lt = date_to)
                # print(filter_data)
                # return HttpResponse(f"{filter_data}")
            # print(filter_data.all())
            filter_data = filter_data.all()
            additional_filter = filter_data
            print(filter_data)
            # return HttpResponse(f"{filter_data}")
            # filter_data.all()
            # report_type = request.POST.get('report_type')
            # print(filter_data)
            # return(f"{filter_data}")
            return redirect(f'Transaction:{report_type}')
        
        return render(request, 'CustomerTransactionReport/index.html')
    return HttpResponse("""please login <a href ="http://127.0.0.1:8000/CustomTransaction/login">here</a> to access the page""")
        


def product_volume_report(request):
    name = 'product_volume'
    #filter
    global additional_filter, filter_data
    Product_volume_dict_ = {}
    list_ = []
    for filter in additional_filter:
        list_ += Cart.objects.filter(customer = filter)
    products = list_
    # products = Cart.objects.all()
    # --------------------------------------
    # pincode_filter = Transcations.objects.filter(pin_Code = 508211)
    # list_ = []
    # for filter in pincode_filter:
    #     list_ += Cart.objects.filter(customer = filter)
    # products = list_
    # -----------------------------------
    # name_filter = Transcations.objects.get(customer_name = "Harish")
    # products = Cart.objects.filter(customer = name_filter)
    for product_ in products:
        if product_.product.product_name in Product_volume_dict_:
            Product_volume_dict_[product_.product.product_name] += product_.quantity
        else:
            Product_volume_dict_[product_.product.product_name] = product_.quantity

    # Product_volume_dict_[product_name] = quantity
    additional_filter = filter_data
    json_data = json.dumps(Product_volume_dict_)
    # json_data = ""
    context = {'product_volume': Product_volume_dict_, 'name':name, 'date_from':request.session.get('date_from'), 'date_to':request.session.get('date_to'), 'json_data':json_data}
    return render(request,'CustomerTransactionReport/product_volume_report.html',context)

def product_value_report(request):
    name = 'product_value'
    #filter
    global additional_filter, filter_data
    Product_value_dict_ = {}
    list_ = []
    for filter in additional_filter:
        list_ += Cart.objects.filter(customer = filter)
    products = list_
    # Product_value_dict_ = {}
    # products = Cart.objects.all()
    for product_ in products:
        
        if product_.product.product_name in Product_value_dict_:
            Product_value_dict_[product_.product.product_name] += int(product_.subtotal())
        else:
            Product_value_dict_[product_.product.product_name] = int(product_.subtotal())
    # context = {'product_volume': product_volume_dict_}
    # return HttpResponse(f"<p>{Product_value_dict_}</p>")
    additional_filter = filter_data
    json_data = json.dumps(Product_value_dict_)
    context = {'product_value': Product_value_dict_, 'name':name, 'json_data':json_data}
    return render(request,'CustomerTransactionReport/product_value_report.html',context)

def customer_value_report(request):
    name = 'customer_value'
    #filter
    global additional_filter, filter_data
    # Product_value_dict_ = {}
    list_ = []
    for filter in additional_filter:
        list_ += Cart.objects.filter(customer = filter)
    products = list_
    customer_value_dict_ = {}
    # customers = Cart.objects.all()
    for customer_ in products:
        customer_value_dict_[customer_.customer.customer_name] = customer_.customer.total_Transaction

    # customer_volume_dict_[customer_name] = quantity
    # context = {'customer_volume': customer_volume_dict_}
    additional_filter = filter_data
    json_data = json.dumps(customer_value_dict_)
    context = {'customer_value': customer_value_dict_, 'name':name, 'json_data':json_data}
    return render(request,'CustomerTransactionReport/customer_value_report.html',context)
    # return HttpResponse(f"<p>{customer_value_dict_}</p>")

def customer_volume_report(request):
    name = 'customer_volume'
    #filter
    global additional_filter, filter_data
    # Product_value_dict_ = {}
    list_ = []
    for filter in additional_filter:
        list_ += Cart.objects.filter(customer = filter)
    products = list_
     # customer_value_dict_ = {}
    customer_volume_dict_ = {}
    # customers = Cart.objects.all()

    for customer_ in products:
        if customer_.customer.customer_name in customer_volume_dict_:
            customer_volume_dict_[customer_.customer.customer_name] += customer_.quantity
        else:
            customer_volume_dict_[customer_.customer.customer_name] = customer_.quantity

    # Product_volume_dict_[product_name] = quantity
    # context = {'product_volume': product_volume_dict_}
    # return HttpResponse(f"<p>{customer_volume_dict_}</p>")
    # customer_value_dict_[customer_name] = total_transaction
    # context = {'customer_volume': customer_value_dict_}
    # pass
    additional_filter = filter_data
    json_data = json.dumps(customer_volume_dict_)
    context = {'customer_volume': customer_volume_dict_,'name':name, 'json_data':json_data}
    return render(request,'CustomerTransactionReport/customer_volume_report.html',context)

def complete_report(request):
    name = 'complete_report'
    global additional_filter, filter_data
    Comlete_report_dict_ = {}
    list_ = []
    for filter in additional_filter:
        list_ += Cart.objects.filter(customer = filter)
    products = list_






def login(request):
    error_message = ''
    if request.method == 'POST':
        username_ = request.POST.get('username')
        password_ = request.POST.get('password')
        user = authenticate(username=username_, password=password_)
        if user is not None:
            request.session['logged_in_customer'] = user.username
            request.session['date_from'] = ""
            request.session['date_to'] = "Today"
            request.session['Access'] = True

            # owner = Owner.objects.get(user=user)
            context = {'error_message': error_message}
            return render(request, 'CustomerTransactionReport/index.html', context)
        else:
            error_message = 'Incorrect Password'
    context = {'error_message': error_message}
    return render(request, 'CustomerTransactionReport/login_page.html', context)

def logout(request):
    # del request.session['logged_in_student']
    del request.session['Access']
    return redirect('Transaction:login')

def registration(request):
    return render(request, 'CustomerTransactionReport/registration_page.html')
