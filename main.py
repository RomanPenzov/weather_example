import requests
import json
#url = 'https://www.postindexapi.ru/json/308/308017.json'
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=Denver&cnt=3'
response = requests.get(url)
data = json.loads(response.text)
print(data)

