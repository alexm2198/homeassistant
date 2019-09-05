from tkinter import *
from PIL import Image,ImageTk


class Start(Frame):
    # Parent is the container and controller is the app
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        img = Image.open('button.png')
        self.photo = ImageTk.PhotoImage(img)
        weather_button = Button(self, image=self.photo, border=0, command=lambda: controller.show_frame("Weather"))
        weather_button.place(relx=0.25, rely=0.2, anchor=CENTER)
        sensor_button = Button(self, image=self.photo, border=0, command=lambda: controller.show_frame("Sensors"))
        sensor_button.place(relx=0.75, rely=0.2, anchor=CENTER)
        img_button3 = Button(self, image=self.photo, border=0, command=lambda: controller.show_frame("CameraView"))
        img_button3.place(relx=0.25, rely=0.6, anchor=CENTER)
        img_button4 = Button(self, image=self.photo, border=0)
        img_button4.place(relx=0.75, rely=0.6, anchor=CENTER)