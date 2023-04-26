import requests
from pprint import pprint

API_key = '58a8d0ba35d934c2bbd2bf08046cd420'

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)