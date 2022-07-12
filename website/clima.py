import json
import requests
from .tradutor import tradutor

KEY = '99d9aa4dfbae9657f164d9a0b4898203'

def clima(cidade='New York'):
    city = cidade
    link = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={KEY}'
    link = requests.get(link)
    link = link.content
    all = json.loads(link)
    def kelvtocel(kelv):return round(float(kelv) - 273.15,0)
    desc = str(all['weather'][0]['description'])
    desc = tradutor(desc)
    all = {'temperatura':kelvtocel(all['main']['temp']),'sensação':kelvtocel(all['main']['feels_like']),
    'temp_min':kelvtocel(all['main']['temp_min']),'temp_max':kelvtocel(all['main']['temp_max']),
    'desc':desc,'umidade':all['main']['humidity'],'vento':all['wind']['speed'],
    'pais':all['sys']['country'],'cidade':all['name']
    }
    return all