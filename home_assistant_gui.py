from tkinter import *


class App(Tk):
    def __init__(self, *args, **kwwargs):
        Tk.__init__(self, *args, **kwwargs)
        # Setting the resolution fixed
        self.geometry("800x500")
        self.resizable(0, 0)

        # # Setting the title
        self.title("Home Assistant")

        # Setup Frame
        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # This part constructs each frame that we want to add to our App
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)  # Constructor for each frame
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        # Here we are setting the start_page
        self.show_frame(StartPage)

    # Shows different frames inside the app
    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()  # Shows the frame

class StartPage(Frame):
    # Parent is the container and controller is the app
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="StartPage")
        label.pack()

        # Navigation through pages
        page_one = Button(self, text='Page One', command=lambda: controller.show_frame(PageOne))
        page_one.pack()
        page_two = Button(self, text='Page Two', command=lambda: controller.show_frame(PageTwo))
        page_two.pack()

class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="PageOne")
        label.pack()
        start_page = Button(self, text='Start Page', command=lambda: controller.show_frame(StartPage))
        start_page.pack()
        page_two = Button(self, text='Page Two', command=lambda: controller.show_frame(PageTwo))
        page_two.pack()

class PageTwo(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="PageTwo")
        label.pack()
        start_page = Button(self,text='Start Page', command=lambda: controller.show_frame(StartPage))
        start_page.pack()
        page_one = Button(self, text='Page One', command=lambda: controller.show_frame(PageOne))
        page_one.pack()

app = App()
app.mainloop()