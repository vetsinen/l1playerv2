import requests, json

api_key = "bfd293f0cf59a0a437215bda8aeff734"
# https://home.openweathermap.org/api_keys

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"


def get_weather():
    # complete_url variable to store
    # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + 'Kyiv, Ukraine'

    # get method of requests module
    # return response object
    response = res = requests.get("http://api.openweathermap.org/data/2.5/find",
                                  params={'q': 'Kyiv, UA', 'type': 'like', 'units': 'metric', 'APPID': api_key})
    x = response.json()

def cityid(appid):
    city_id = 0
    appid = "буквенно-цифровой APPID"
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': 'Kyiv, UA', 'type': 'like', 'units': 'metric', 'APPID': appid})
        data = res.json()
        print(data)
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
                  for d in data['list']]
        print("city:", cities)
        city_id = data['list'][0]['id']
        print('city_id=', city_id)
    except Exception as e:
        print("Exception (find):", e)
        pass

cityid(api_key)