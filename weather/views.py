import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm



def index(request):
	appid='6fa2cf01ef405b38aa17de1651d76437'
	url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

	

	cities = City.objects.all()

	all_cities=[]

	for city in cities:
	    res=requests.get(url.format(city.name)).json()
	    city_info= {
	      'city':city.name,
	      'temp':res["main"]["temp"],
	      'icon':res["weather"][0]["icon"]  
	    }
        
	    all_cities.append(city_info)

	context={'all_info':all_cities}

	return render(request, 'weather/index.html', context)

