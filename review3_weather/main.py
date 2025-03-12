from weather import Weather
import requests
import sys

def getWeather(city='Athlone'):
    key='48f2d5e18b0d2bc50519b58cce6409f1'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={key}'
    try:
        resp = requests.get(url)
        resp_dict = resp.json()
        return resp_dict
    except Exception as err:
        print(err)

def buildWeatherInstance(city='Athlone'):
    weather_dict = getWeather(city)
    desc = weather_dict['weather'][0]['description']
    temp = weather_dict['main']['temp']
    weather_report = Weather(city, desc, temp)
    print(weather_report)
    # also write the instances to a text file
    fout = open('weather.txt', 'at') # append text
    print(weather_report, file=fout)
    fout.close()

if __name__ == '__main__':
    buildWeatherInstance()

