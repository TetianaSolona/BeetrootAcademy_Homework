import requests

api_key = 'cde2bc99beea574abdb51a1c0c072cbe'
city_name = input('Enter city name : ')
url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

response = requests.get(url)
weather_response = response.json()

if weather_response['cod'] != '404':
    temperature = weather_response['main']['temp']
    pressure = weather_response['main']['pressure']
    humidity = weather_response['main']['humidity']
    weather_description = weather_response['weather'][0]['description']

    print(f'Temperature (in kelvin unit):{temperature} \n atmospheric pressure (in hPa unit): {pressure} '
          f'\n humidity (in percentage):{humidity}\n description:{weather_description}')
else:
    print(" City Not Found ")
