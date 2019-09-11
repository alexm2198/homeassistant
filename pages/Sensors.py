#!/usr/bin/python3
from tkinter import *
from utils import system_handlers, globals
import os
from graphs import get_sensor_value
from PIL import Image, ImageTk

live_plot_path = os.getcwd() + r"/graphs"


class Sensors(Frame):
    def __init__(self, parent, controller, bg):
        Frame.__init__(self, parent, bg=bg)
        title_label = Label(self, text='Home Sensors', font=(globals.UNIVERSAL_FONT, 32), bg=bg)
        title_label.place(relx=0.5, rely=0.1, anchor=CENTER)

        # Sensor part
        # For textvariable is needed StringVar() type
        # Temperature Sensor
        self.temp_sensor_val = StringVar()
        self.temp_sensor_val.set((get_sensor_value.current_sensor_value(globals.TEMP_SENSOR)))

        temp_name = Label(self, text='Temperatura [°C]: ')
        temp_name.place(relx=0.39, rely=0.2, anchor=CENTER)
        temp_value = Label(self, textvariable=self.temp_sensor_val, width=7, bg='white')
        temp_value.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.temp_button = Button(self, text='graph', width=10, bg='red', fg='white',
                                  command=lambda: system_handlers.call_script(r"graphs/live_temp_plot.py"))
        self.temp_button.place(relx=0.6, rely=0.2, anchor=CENTER)

        # Humidity Sensor
        self.hum_sensor_val = StringVar()
        self.hum_sensor_val.set((get_sensor_value.current_sensor_value(globals.HUM_SENSOR)))

        hum_name = Label(self, text='Umiditate aer [%]: ')
        hum_name.place(relx=0.39, rely=0.3, anchor=CENTER)
        hum_value = Label(self, textvariable=self.hum_sensor_val, width=7, bg='white')
        hum_value.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.hum_button = Button(self, text='graph', width=10, bg='red', fg='white',
                                 command=lambda: system_handlers.call_script(r"graphs/live_hum_plot.py"))
        self.hum_button.place(relx=0.6, rely=0.3, anchor=CENTER)

        # Home Button
        temp_image = Image.open("resources/button_home.png")
        self.home_button_image = ImageTk.PhotoImage(temp_image)
        home_button = Button(self, image=self.home_button_image, border=0, bg=bg, activebackground=bg,
                             command=lambda: controller.show_frame("Start"))
        home_button.place(relx=0.5, rely=0.9, anchor=CENTER)

        self.update_sensor_data(globals.TEMP_SENSOR, self.temp_sensor_val, self.temp_button)
        self.update_sensor_data(globals.HUM_SENSOR, self.hum_sensor_val, self.hum_button)

    def update_sensor_data(self, data_path, sensor_update, blink_status):
        counter = 0
        new_val = get_sensor_value.current_sensor_value(data_path)
        sensor_update.set(new_val)
        if get_sensor_value.sensor_status(data_path):
            blink_status.config(bg='green')
            print('green ' + data_path)
            counter += 1
        else:
            blink_status.config(bg='red')
            print('red ' + data_path)
        self.master.after(3000, lambda: self.update_sensor_data(data_path, sensor_update, blink_status))
