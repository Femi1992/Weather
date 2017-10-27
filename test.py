from pymongo import MongoClient
import datetime
import requests
import json
from geopy.geocoders import Nominatim

class weather():

        freegeoip = "http://freegeoip.net/json"

        weather_url = 'http://api.openweathermap.org/data/2.5/weather?'
        api_id = '6b35061c42fdbe1965095189659a796b'
        q = ""
        request_url = weather_url + 'appid=' + api_id + "&q="
        json_object = ""

        def __init__(self):
            print "Weather APP"
            client = MongoClient('localhost', 27017)
            db = client.weather
            collection = db.weather_collection

        def get_user_automatic(self):
            with open('C:\\Users\\HP-PC\\Downloads\\city.list.json') as data_file:
                data = json.load(data_file)

                print data

        def get_user_location(self):
            print "Enter the current city you are in"
            self.q = raw_input("Location: ")
            self.request_url = self.request_url + self.q



        def call_api(self):
            self.json_object = requests.get(self.request_url).json()


        def process_json(self):
            temp_kelvin = float(self.json_object['main']['temp'])
            current_conditions = self.json_object['weather'][0]['description']
            temp_celsius = temp_kelvin - 273.15

            print "The current temperature in", self.q, "is", str(temp_celsius), "celsius and the current conditions are", current_conditions



if __name__ == "__main__":
        w = weather()
        w.get_user_automatic()
        #w.get_user_location()
        w.call_api()
        w.process_json()
