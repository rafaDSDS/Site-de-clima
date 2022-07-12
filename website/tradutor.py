import requests
from json import loads

def tradutor(text):
    url = "https://just-translated.p.rapidapi.com/"

    querystring = {"lang":"pt","text":str(text)}

    headers = {
        "X-RapidAPI-Key": "96d9e8b76dmsh1b2e1fea5baa1bfp11606cjsn138f262251d0",
        "X-RapidAPI-Host": "just-translated.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    response = loads(response.content)

    response = response['text'][0]

    return response
    
