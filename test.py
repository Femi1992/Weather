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
        currentCity = "You are currently in the city"


        def __init__(self):
            print "Weather APP\n"
            client = MongoClient('localhost', 27017)
            db = client.weather
            collection = db.weather_collection


        def get_user_automatic(self):
            r = requests.get(self.freegeoip)
            j = json.loads(r.text)
            current_country = j['time_zone']
            current_city = current_country.split("/")[1]

            print current_city, current_city, "\n"


            """
            while True:

                r = requests.get(self.freegeoip)
                jsonResult = json.loads(r.text)

                if jsonResult["country_code"] == "US":
                    if jsonResult["zip_code"] != "":
                        self.sort_stuff(jsonResult["zip_code"], True)
                        break

                if jsonResult["city"] != "":
                    self.sort_stuff(jsonResult["city"], True)
                    break

                if jsonResult["time_zone"] != "":
                    #call function
                    break

                raise Exception()
                """

        def sort_stuff(self, val, boolean):

            if boolean == True:
                pass

            else:
                loc = val.split('/')[1]
                with open('C:\\Users\\HP-PC\\Downloads\\city.list.json') as data_file:
                    data = json.load(data_file)

                    data[loc]["id"]

            print ""

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


        def five_day_forecast(self):
            five_day_url = 'http://api.openweathermap.org/data/2.5/forecast?q='+self.q+'&appid=6b35061c42fdbe1965095189659a796b'
            json_object_five = requests.get(five_day_url).json()
            forecast = json_object_five['list']

            print "FIVE DAY FORECAST\n"
            for items in forecast:
                description = items['weather'][0]['description']
                date = items['dt_txt']
                day_temp = items['main']['temp']
                day_temp_celsius = day_temp - 273.15
                print "Date: ", date,"\n", "Description: ", description,"\n", "Temperature: ",day_temp_celsius,"\n"


        def update_database(self):
            """
            now = datetime.datetime.now()
            time_of_call = now.strftime("%H:%M")
            self.db.weather.insert_one({"City": self.q,
                                   "Weather Condition": self.current_conditions,
                                   "time": time_of_call
                                   })"""

if __name__ == "__main__":
        weather = weather()
        weather.get_user_automatic()
        weather.get_user_location()
        weather.call_api()
        weather.process_json()
        weather.five_day_forecast()
