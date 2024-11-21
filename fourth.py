# import requests
#
# r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2022-2-27&to=2022-2-28&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')
# content = r.json()
# print(content)
# #print(content['message'])

import requests

def get_weather(city, units='metric', api_key='26631f0f41b95fb9f5ac0df9a8f43c92'):
  url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
  r = requests.get(url)
  content = r.json()
  with open('data.txt', 'a') as file:
    for dicty in content['list']:
      file.write(f"{dicty['dt_txt']}, {dicty['main']['temp']}, {dicty['weather'][0]['description']}\n")

print(get_weather(city='Washington'))