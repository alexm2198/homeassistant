#!/usr/bin/python3
from tkinter import *
from PIL import Image, ImageTk
from pages.Start import Start


class CameraView(Start):
    def __init__(self, parent, controller, bg):
        Start.__init__(self, parent,controller, bg=bg)
        title_label = Label(self, text='camera view')
        title_label.place(relx=0.6, rely=0.1, anchor=CENTER)
