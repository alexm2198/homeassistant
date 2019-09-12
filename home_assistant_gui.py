#!/usr/bin/python3
from tkinter import *
from pages.Start import Start
from pages.Weather import Weather
from pages.Sensors import Sensors
from pages.CameraView import CameraView
from utils import system_handlers, globals
import os
import signal


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # MainMenu
        MainMenu(self)
        # Setting the resolution fixed\
        self.geometry("1280x720")
        self.resizable(0, 0)
        # Setting the title
        self.title("Home Assistant")
        # Setup Frame
        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Start, Weather, Sensors, CameraView):
            page_name = F.__name__
            frame = F(parent=container, controller=self, bg=globals.UNIVERSAL_BG)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Start")
        self.tcp_server = system_handlers.call_script(r"utils/data_collector.py")

    # Shows different frames inside the app
    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        if frame_name == "Weather":
            frame.get_location()
            frame.get_weather()
            frame.set_image()
            frame.set_labels()
        frame.tkraise()  # Shows the frame

    def close_server(self):
        try:
            os.system(f"taskkill /f /im Python.exe")
        except:
            for line in os.popen("ps ax | grep -i " + "*python*" + " | grep -v grep"):
                fields = line.split()
                pid = fields[0]
                os.kill(int(pid), signal.SIGKILL)
        self.destroy()

class MainMenu:
    def __init__(self, master):
        root_menu = Menu(master, tearoff=0)
        master.config(menu=root_menu)

        file_menu = Menu(root_menu, tearoff=False)  # this line creates a file sub_menu in the root_menu
        root_menu.add_cascade(label='File', menu=file_menu)  # it creates the name of the sub_menu
        file_menu.add_command(label='New File')
        file_menu.add_command(label='Open File')
        file_menu.add_command(label='Save File')
        file_menu.add_separator()
        file_menu.add_command(label='Quit!', command=master.quit)

        login_menu = Menu(file_menu, tearoff=False)
        root_menu.add_cascade(label='Log IN', menu=login_menu)
        login_menu.add_command(label='Sign UP')


if __name__ == "__main__":
    app = App()
    app.protocol('WM_DELETE_WINDOW', lambda: app.close_server())
    app.mainloop()
