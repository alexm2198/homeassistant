from tkinter import *

class CameraView(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        title_label = Label(self, text='camera view').place(relx =0.5, rely=0.1, anchor=CENTER)

        start_page = Button(self, text='Start Page', command=lambda: controller.show_frame("Start"))
        start_page.place(x=725, y=465)