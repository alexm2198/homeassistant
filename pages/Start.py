#!/usr/bin/python3
from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime
from utils import globals

class Start(Frame):
    # Parent is the container and controller is the app
    def __init__(self, parent, controller, bg):
        Frame.__init__(self, parent, bg=bg)
        self.button_images = {}
        for image_name in ("weather", "sensors", "camera", "calendar","exit"):
            temp_image = Image.open(f"resources/button_{image_name}.png")
            self.button_images[image_name] = ImageTk.PhotoImage(temp_image)

        weather_button = Button(self, image=self.button_images["weather"], border=0, bg=bg, activebackground=bg,
                                command=lambda: controller.show_frame("Weather"))
        weather_button.place(relx=0.12, rely=0.1, anchor=CENTER)
        sensor_button = Button(self, image=self.button_images["sensors"], border=0, bg=bg, activebackground=bg,
                               command=lambda: controller.show_frame("Sensors"))
        sensor_button.place(relx=0.12, rely=0.3, anchor=CENTER)
        camera_button = Button(self, image=self.button_images["camera"], border=0, bg=bg, activebackground=bg,
                               command=lambda: controller.show_frame("CameraView"))
        camera_button.place(relx=0.12, rely=0.5, anchor=CENTER)
        calendar_button = Button(self, image=self.button_images["calendar"], border=0, bg=bg, activebackground=bg, )
        calendar_button.place(relx=0.12, rely=0.7, anchor=CENTER)
        exit_button = Button(self, image=self.button_images["exit"], border=0, bg=bg, activebackground=bg,
                             command=parent.quit)
        exit_button.place(relx=0.12, rely=0.9, anchor=CENTER)

        self.clock_time = StringVar()
        self.clock_time.set(datetime.now().strftime("%H:%M:%S"))
        time_label = Label(self, textvariable=self.clock_time, bg=bg, font=(globals.UNIVERSAL_FONT, 20))
        time_label.place(relx=1, rely=0, anchor=NE)
        self.update_clock_time()

    def update_clock_time(self):
        self.clock_time.set(datetime.now().strftime("%H:%M:%S"))
        self.master.after(1000, self.update_clock_time)

