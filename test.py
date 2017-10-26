from pymongo import MongoClient
import datetime
import requests
import json
from geopy.geocoders import Nominatim

geolocation = Nominatim()
reverse = geolocation.reverse("51.51, -0.13")
real_location = reverse
print real_location.address

client = MongoClient('localhost', 27017)
db = client.weather

collection = db.weather_collection

post = {"City" : " ",
        "Weather Condition" : " ",
        "time" : ""}


print "****************Weather Forecast****************\n"

freegeoip = "http://freegeoip.net/json"
geo_r = requests.get(freegeoip)
geo_json = geo_r.json()

user_latitude = geo_json['latitude']
user_longitude = geo_json['longitude']


#5day forecast
#five_day_api = 'http://api.openweathermap.org/data/2.5/forecast?lat=35&lon=139&appid=6b35061c42fdbe1965095189659a796b'
#url_1 = five_day_api + user_country
"""
while True:
    location = raw_input("Location: ")

    if location == "q":
        break

    main_api = ('http://api.openweathermap.org/data/2.5/weather?appid=6b35061c42fdbe1965095189659a796b&q=')
    url = main_api + location
    json_object = requests.get(url).json()
    temp_kelvin = float( json_object['main']['temp'])
    current_conditions = json_object['weather'][0]['description']
    #cweather = json_object['weather']
    temp_celsius = temp_kelvin - 273.15 #change from degrees kelvin to celsius

    print "The current temperature in", location, "is", str(temp_celsius), "celsius and the current conditions are", current_conditions


    #inserting data into db
    now = datetime.datetime.now()
    time_of_call =  now.strftime("%H:%M")
    db.weather.insert_one({"City": location,
                           "Weather Condition": current_conditions,
                           "time": time_of_call
                          })
"""

