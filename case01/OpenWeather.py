import requests
import json

def openweather():
    city = 'taoyuan'
    country = 'tw'
    apikey = '3b657e4dc92918d9d95fff4633377535'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}'\
          .format(city, country, apikey)

    resp = requests.get(url)
    if(resp.status_code == 200):
        jo = json.loads(resp.text)
        print(jo)
    else:
        print('Error', resp.status_code)

if __name__ == '__main__':
    openweather()