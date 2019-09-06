from tkinter import *
from PIL import Image,ImageTk


class Start(Frame):
    # Parent is the container and controller is the app
    def __init__(self, parent, controller, bg):
        Frame.__init__(self, parent, bg=bg)

        self.button_images = {}
        for image_name in ("weather", "sensors", "camera", "calendar"):
            temp_image = Image.open(f"resources/button_{image_name}.png")
            self.button_images[image_name] = ImageTk.PhotoImage(temp_image)

        weather_button = Button(self, image=self.button_images["weather"], border=0, bg=bg, activebackground=bg,
                                command=lambda: controller.show_frame("Weather"))
        weather_button.place(relx=0.25, rely=0.25, anchor=CENTER)
        sensor_button = Button(self, image=self.button_images["sensors"], border=0, bg=bg, activebackground=bg,
                               command=lambda: controller.show_frame("Sensors"))
        sensor_button.place(relx=0.75, rely=0.25, anchor=CENTER)
        camera_button = Button(self, image=self.button_images["camera"], border=0, bg=bg, activebackground=bg,
                             command=lambda: controller.show_frame("CameraView"))
        camera_button.place(relx=0.25, rely=0.75, anchor=CENTER)
        calendar_button = Button(self, image=self.button_images["calendar"], border=0, bg=bg, activebackground=bg,)
        calendar_button.place(relx=0.75, rely=0.75, anchor=CENTER)