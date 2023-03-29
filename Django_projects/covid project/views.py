from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members
from django.shortcuts import render
import requests

def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))
  
def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  member = Members(firstname=x, lastname=y)
  member.save()
  return HttpResponseRedirect(reverse('index'))

def cowin(request):
      centers=requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=581&date=16-09-2022').json()
      
      slotData = []
      def data(center1, session1):
        for i in range(2):
          slotData1 = {}
          slotData1['name'] = center1['name']
          slotData1['address'] = center1['address']
          slotData1['state_name'] = center1['state_name']
          slotData1['district_name'] = center1['district_name']
          slotData1['fee_type'] = center1['fee_type']
          slotData1['vaccine'] = session1['vaccine']
          slotData1['age'] = session1['min_age_limit']
          if i == 0:
            slotData1['dose'] = '#1'
            slotData1['doseCapacity'] = session1['available_capacity_dose1']
          if i == 1:
            slotData1['dose'] = '#2'
            slotData1['doseCapacity'] = session1['available_capacity_dose2']
          slotData.append(slotData1)
          # slotData.append(slotData1)
        


      for center in centers['centers']:
        for session in center['sessions']:
          # if session['available_capacity_dose1'] > 0:
          data(center, session)
            # slotData['name'] = center['name'] 
      #   slotData['address'] = center.address
      return render(request,'myfirst.html',{'slotData':slotData})

# def search(request):
#       return districtId

# def show(request):
#       age = 
#       dose = 
#       cost = 
#       vaccine = 
