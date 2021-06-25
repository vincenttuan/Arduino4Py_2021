import requests

city = 'taoyuan'
country = 'tw'
apikey = '3b657e4dc92918d9d95fff4633377535'
url = 'api.openweathermap.org/data/2.5/weather?q={},{}&appid={}'\
      .format(city, country, apikey)

print(url)
