import requests

city = input("Введите название города: ")
api_key = 'bd5e378503939ddaee76f12ad7a97608'

params = {
    'q': city,
    'appid': api_key,
    'units': 'metric',
    'lang': 'ru'
}

response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    print(f"Текущая температура в городе {city}: {temp}°C")
    print(f"Описание погоды: {description}")
else:
    print(f"Ошибка {response.status_code}")
    
