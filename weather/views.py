import requests
from django.shortcuts import render
from weather.models import City
from weather.forms import CityForm



def index(request):
    appid = '1327e58b44062a45b570ed26a0356900'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=|{}&units=metric&lang=ru' + appid
    if(request.method == 'POST'):
       form = CityForm(request.POST)
       form.save()

    form = CityForm()
   
    cities = City.objects.all()
    
    all_cities = []

    for city in cities:
        response = requests.get(url.format(city.name)).json()

        city_info = {
            'city': city.name,
            'temp': response['main']['temp'],
            'icon': response['weather'][0]['icon'],
        }

        all_cities.append(city_info)

    context = {
        'all_info': all_cities,
        'form': form
    }
            
    return render(request, 'index.html', context)

