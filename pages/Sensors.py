from tkinter import *
from utils import system_handlers, globals
import os
from graphs import get_sensor_value
from PIL import Image, ImageTk

live_plot_path = os.getcwd() + r"\graphs"


class Sensors(Frame):
    def __init__(self, parent, controller, bg):
        Frame.__init__(self, parent, bg=bg)
        title_label = Label(self, text='Home Sensors', font=(globals.UNIVERSAL_FONT, 32), bg=bg)
        title_label.place(relx=0.5, rely=0.1, anchor=CENTER)

        # Sensor part
        # For textvariable is needed StringVar() type
        self.sensor_val = StringVar()
        self.sensor_val.set((get_sensor_value.current_sensor_value(globals.UNIVERSAL_SENSOR)))

        sensor_name = Label(self, text='Senzor General [U.M]: ')
        sensor_name.place(relx=0.39, rely=0.2, anchor=CENTER)
        sensor_value = Label(self, textvariable=self.sensor_val, width=7, bg='white')
        sensor_value.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.graph_button = Button(self, text='graph', width=10, bg='red', fg='white',
                                   command=lambda: system_handlers.call_script(rf'{live_plot_path}\live_plot.py'))
        self.graph_button.place(relx=0.6, rely=0.2, anchor=CENTER)

        # Home Button
        temp_image = Image.open("resources/button_home.png")
        self.home_button_image = ImageTk.PhotoImage(temp_image)
        home_button = Button(self, image=self.home_button_image, border=0, bg=bg, activebackground=bg,
                             command=lambda: controller.show_frame("Start"))
        home_button.place(relx=0.5, rely=0.9, anchor=CENTER)

        self.update_sensor_data(globals.UNIVERSAL_SENSOR)

    def update_sensor_data(self, data_path):
        counter = 0
        new_val = get_sensor_value.current_sensor_value(data_path)
        self.sensor_val.set(new_val)
        if get_sensor_value.sensor_status(data_path):
            self.graph_button.config(bg='green')
            counter += 1
        else:
            self.graph_button.config(bg='red')
        self.master.after(1000, lambda: self.update_sensor_data(data_path))
