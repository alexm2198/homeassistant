#!/usr/bin/python3
import socket
from tkinter import *

import geoip2.database
import requests
from PIL import Image, ImageTk

from utils import globals
from pages.Start import Start

class Weather(Start):
    city = "Bucharest"
    temp = 0
    pressure = 0
    humidity = 0
    description = ""
    id = 0

    def __init__(self, parent, controller, bg):
        Start.__init__(self, parent, controller, bg=bg)

        self.get_location()
        title_label = Label(self, text=f'Weather in {self.city}:', font=(globals.UNIVERSAL_FONT, 20), bg=bg)
        title_label.place(relx=0.6, rely=0.1, anchor=CENTER)

        tmp_image = Image.open("resources/button_home.png")
        self.weatherimage = ImageTk.PhotoImage(tmp_image)

        self.temp_label = Label(self, font=(globals.UNIVERSAL_FONT, 16), bg=globals.UNIVERSAL_BG)
        self.temp_label.place(relx=0.6, rely=0.7, anchor=CENTER)
        self.pressure_label = Label(self, font=(globals.UNIVERSAL_FONT, 16), bg=globals.UNIVERSAL_BG)
        self.pressure_label.place(relx=0.6, rely=0.8, anchor=CENTER)
        self.humidity_label = Label(self, font=(globals.UNIVERSAL_FONT, 16), bg=globals.UNIVERSAL_BG)
        self.humidity_label.place(relx=0.6, rely=0.9, anchor=CENTER)

    def get_weather(self):
        """Gets information about the weather from the OpenWeather API"""
        api_key = globals.OPENWEATHER_API_KEY
        api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=' + api_key + '&q=' + str(self.city)
        response = requests.get(api_address)
        data = response.json()

        if data["cod"] != "404":
            current = data["main"]
            self.temp = round(current["temp"] - 273.15, 2)
            self.pressure = round(current["pressure"] * 0.75006, 2)
            self.humidity = current["humidity"]
            self.description = data["weather"][0]["description"]
            self.id = data["weather"][0]["id"]
            print(self.temp, self.pressure, self.humidity, self.description, self.id)
        else:
            print("Error while getting weather")

    def get_location(self):
        """
        Temporarily opens a socket to ping a standard server and retrieve the IP of the device and set the city
        based on IP
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        print(ip)
        reader = geoip2.database.Reader('resources/GeoLite2-City.mmdb')
        s.close()

        try:
            response = reader.city(ip)
            if response.city.name != None:
                self.city = response.city.name
        except:
            pass

    def set_image(self):
        """Based on the current weather desciption, sets the image accordingly"""
        filename = ""

        if self.id < 300:
            filename = "thunderstorm"
        elif self.id < 500:
            filename = "drizzle"
        elif self.id < 502:
            filename = "light_rain"
        elif self.id < 600:
            filename = "heavy_rain"
        elif self.id < 700:
            filename = "snow"
        elif self.id == 800:
            filename = "clear"
        elif self.id < 803:
            filename = "cloudy"
        elif self.id >= 803:
            filename = "overcast"

        pil_weather_image = Image.open(f"resources/{filename}.png")
        self.weather_image = ImageTk.PhotoImage(pil_weather_image.resize((400, 220)))
        image_label = Label(self, image=self.weather_image, bg=globals.UNIVERSAL_BG)
        image_label.place(relx=0.6, rely=0.4, anchor=CENTER)

    def set_labels(self):
        """Update the text in the labels to match current weather variables"""
        self.temp_label.config(text=f"Temperature: {self.temp}°C")
        self.pressure_label.config(text=f"Pressure: {self.pressure} mmHg")
        self.humidity_label.config(text=f"Humidity: {self.humidity}%")
