from django.shortcuts import render
import requests
# Create your views here.
from django.contrib import messages

def index(request):
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city='kathmandu'
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=bf22686cf11682e29d657b984d138978"
    data=requests.get(url,{'units':'metric'}).json()
    
    try:
        temp=data['main']['temp']
        desc=data['weather'][0]['description']
        speed=data['wind']['speed']
        water=data['main']['humidity']
        pressure=data['main']['pressure']
        visible=data['visibility']
        icon=data['weather'][0]['icon']
        return render(request,'index.html',{'temp':temp,'desc':desc,'city':city , 'speed':speed , 'humidity':water , 'pressure':pressure , 'visiable':visible , 'icon':icon})
    except:
        temp=0
        desc="no desc"
        messages.error(request,'city incorrect')
        return render(request,'index.html',{'temp':temp,'desc':desc,'city':city})

