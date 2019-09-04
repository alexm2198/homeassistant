from tkinter import *
import geoip2.database
import socket
import requests, json

class Weather(Frame):
    city = ""

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.get_location()
        title_label = Label(self, text=f'Weather in {self.city}:', font=('Bahnschrift', 32))
        title_label.place(relx =0.5, rely=0.1, anchor=CENTER)

        start_page = Button(self, text='Start Page', command=lambda: controller.show_frame("Start"))
        start_page.place(relx=0.9, rely=0.9)

        self.get_weather()

    def get_weather(self):
        '''Gets information about the weather from t he OpenWeather API'''
        api_key = '7bba42c4b4362ab23bf498ea7207a210'
        api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=' + api_key + '&q=' + str(self.city)
        response = requests.get(api_address)
        data = response.json()

        if data["cod"] != "404":
            current = data["main"]
            temp = round(current["temp"] - 273.15, 2)
            pressure = current["pressure"]
            humidity = current["humidity"]
            print(temp, pressure, humidity)
        else:
            print("Error while getting weather")

    def get_location(self):
        '''
        Temporarily opens a socket to ping a standard server and retrieve the IP of the device and set the city
        based on IP
        '''
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        reader = geoip2.database.Reader('resources/GeoLite2-City.mmdb')
        s.close()
        response = reader.city(ip)
        if response.city.name != None:
            self.city = response.city.name
        else:
            self.city = "Bucharest"