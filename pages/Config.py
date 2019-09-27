#!/usr/bin/python3
from tkinter import *
from PIL import Image, ImageTk
from pages.Start import Start
from utils import globals

global name, city
user_data = open("config.txt", "r+").read()
name, city = user_data.split(",")

class Config(Start):
    def __init__(self, parent, controller, bg):
        Start.__init__(self, parent, controller, bg=bg)

        title_label = Label(self, text='Configurations', font=(globals.UNIVERSAL_FONT, 20), bg=bg)
        title_label.place(relx=0.6, rely=0.1, anchor=CENTER)

        # user_name and user_city
        self.user_name = StringVar()
        self.user_city = StringVar()

        # initializing usr_name and city with latest values from config if this exists
        global name, city
        self.user_name.set(name)
        self.user_city.set(city)

        user_name_label = Label(self, text='Your name: ', font=(globals.UNIVERSAL_FONT, 16), bg=bg)
        user_name_label.place(relx=0.6, rely=0.2, anchor=CENTER)
        user_name_entry = Entry(self, textvariable=self.user_name, font=(globals.UNIVERSAL_FONT, 16),
                                bg=bg)
        user_name_entry.place(relx=0.6, rely=0.27, anchor=CENTER)

        user_city_label = Label(self, text='Your location: ', font=(globals.UNIVERSAL_FONT, 16), bg=bg)
        user_city_label.place(relx=0.6, rely=0.4, anchor=CENTER)
        user_city_entry = Entry(self, textvariable=self.user_city, font=(globals.UNIVERSAL_FONT, 16),
                                bg=bg)
        user_city_entry.place(relx=0.6, rely=0.47, anchor=CENTER)

        # Save config button
        save_config = Button(self, text="Save configuration", command=self.register_user,
                             font=(globals.UNIVERSAL_FONT, 16), bg=bg)
        save_config.place(relx=0.6, rely=0.7, anchor=CENTER)

    def register_user(self):
        # Save the configs in a file
        file = open("config.txt", "w+")
        file.write(str(self.user_name.get()) + "," + str(self.user_city.get()))
        global name, city
        name = str(self.user_name.get())
        city = str(self.user_city.get())
        file.close()