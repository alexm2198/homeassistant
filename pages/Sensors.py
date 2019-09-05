from tkinter import *
from utils import system_handlers
import os
from graphs import get_sensor_value
from PIL import Image,ImageTk


live_plot_path = os.getcwd() + r"\graphs"


class Sensors(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        title_label = Label(self, text='Sensors').place(relx =0.5, rely=0.1, anchor=CENTER)

        # For textvariable is needed StringVar() type
        self.sensor_val = StringVar()
        self.sensor_val.set((get_sensor_value.current_sensor_value('data\data1_in.txt')))

        sensor_name = Label(self, text='Senzor General [U.M]: ')
        sensor_name.place(relx=0.39, rely=0.2, anchor=CENTER)
        sensor_value = Label(self, textvariable=self.sensor_val, width=7, bg='white')
        sensor_value.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.graph_button = Button(self, text='graph', width=10, bg='red', fg='white',
                                   command=lambda: system_handlers.call_script(rf'{live_plot_path}\live_plot.py'))
        self.graph_button.place(relx=0.6, rely=0.2, anchor=CENTER)

        temp_image = Image.open("resources/button_home.png")
        self.home_button_image = ImageTk.PhotoImage(temp_image)
        home_button = Button(self, image=self.home_button_image, border=0,
                             command=lambda: controller.show_frame("Start"))
        home_button.place(relx=0.5, rely=0.9, anchor=CENTER)

        self.update_sensor_data('data\data1_in.txt')

    def update_sensor_data(self, data_path):
        new_val = get_sensor_value.current_sensor_value(data_path)
        self.sensor_val.set(new_val)
        self.graph_button.config(bg='green')
        self.master.after(1000, lambda: self.update_sensor_data(data_path))
