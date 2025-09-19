from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import requests
import datetime

# Create your views here.
def home(request):
    context = {'true':False}
    if request.method == "POST":
        city = request.POST.get('city')
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        res = requests.get(url).json()
        if 'weather' in res:
            descr = res['weather'][0]['description']
            temp = res['main']['temp']
            temp = temp - 273.15
            icon = res['weather'][0]['icon']
            time = datetime.datetime.now()
            context = {'true':True, 'city':city,'des':descr,'temp':temp,'icon':icon, 'time':time}
            return render(request, "home.html",context)
        else:
            context = {'error':True, 'city':city}
            return render(request, "home.html",context)
    return render(request, "home.html")