from tkinter import *
from PIL import Image,ImageTk

class CameraView(Frame):
    def __init__(self, parent, controller, bg):
        Frame.__init__(self, parent, bg=bg)
        title_label = Label(self, text='camera view')
        title_label.place(relx =0.5, rely=0.1, anchor=CENTER)

        temp_image = Image.open("resources/button_home.png")
        self.home_button_image = ImageTk.PhotoImage(temp_image)
        home_button = Button(self, image=self.home_button_image, border=0,
                             command=lambda: controller.show_frame("Start"))
        home_button.place(relx=0.5, rely=0.9, anchor=CENTER)