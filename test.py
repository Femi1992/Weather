from pymongo import MongoClient
import datetime
import requests
import json


class weather():

        freegeoip = "http://freegeoip.net/json"

        weather_url = 'http://api.openweathermap.org/data/2.5/weather?'
        api_id = '6b35061c42fdbe1965095189659a796b'
        q = ""
        request_url = weather_url + 'appid=' + api_id + "&q="
        json_object = ""


        def __init__(self):
            print "Weather APP\n"
            client = MongoClient('localhost', 27017)
            db = client.weather
            collection = db.weather_collection


        def get_user_automatic(self):
            with open('C:\\Users\\HP-PC\\Downloads\\city.list.json') as data_file:
                data = json.load(data_file)

            r = requests.get(self.freegeoip)
            j = json.loads(r.text)
            current_country = j['time_zone']
            current_city = current_country.split("/")[1]

            print "You are currently in the city of", current_city,"\n"


        def get_user_location(self):
            print "Enter the name of the city which you want to display the current weather forecast"
            self.q = raw_input("City Name: ")
            self.request_url = self.request_url + self.q


        def call_api(self):
            self.json_object = requests.get(self.request_url).json()


        def process_json(self):
            temp_kelvin = float(self.json_object['main']['temp'])
            current_conditions = self.json_object['weather'][0]['description']
            temp_celsius = temp_kelvin - 273.15

            print "The current temperature in", self.q, "is", str(temp_celsius), "celsius and the current conditions are", current_conditions,"\n"

        def update_database(self):
            """
            now = datetime.datetime.now()
            time_of_call = now.strftime("%H:%M")
            self.db.weather.insert_one({"City": self.q,
                                   "Weather Condition": self.current_conditions,
                                   "time": time_of_call
                                   })"""

if __name__ == "__main__":
        w = weather()
        w.get_user_automatic()
        w.get_user_location()
        w.call_api()
        w.process_json()
        #w.update_database()