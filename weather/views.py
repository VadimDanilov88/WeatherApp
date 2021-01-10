import requests
from django.shortcuts import render



def index(request):
	appid='6fa2cf01ef405b38aa17de1651d76437'
	url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=' + appid
	city='London'
	res=requests.get(url.format(city))
	print(res.text)
	return render(request, 'weather/index.html')

