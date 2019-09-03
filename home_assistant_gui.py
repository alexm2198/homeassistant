from tkinter import *
from PIL import Image, ImageTk

class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # MainMenu
        MainMenu(self)

        # Setting the resolution fixed
        self.geometry("800x500")
        self.resizable(0, 0)

        # Setting the favicon
        self.iconbitmap('favicon.ico')

        # Setting the title
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
        frame = self.frames[frame_name]  # If we approach the second way in which we build only a general Page class this line needs to be commented
        frame.tkraise()  # Shows the frame

class StartPage(Frame):
    # Parent is the container and controller is the app
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="StartPage")
        label.pack()

        # Navigation through pages
        page_one = Button(self, text='Page One', command=lambda: controller.show_frame(PageOne))
        page_one.place(x=725, y=465)
        page_two = Button(self, text='Page Two', command=lambda: controller.show_frame(PageTwo))
        page_two.place(x=10, y=465)

        img = Image.open('button.png')
        self.photo = ImageTk.PhotoImage(img)
        img_button1 = Button(self, image=self.photo, border=0)
        img_button1.place(x=90, y=80)
        img_button2 = Button(self, image=self.photo, border=0)
        img_button2.place(x=520, y=80)
        img_button3 = Button(self, image=self.photo, border=0)
        img_button3.place(x=90, y=280)
        img_button4 = Button(self, image=self.photo, border=0)
        img_button4.place(x=520, y=280)



class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="PageOne")
        label.pack()
        start_page = Button(self, text='Start Page', command=lambda: controller.show_frame(StartPage))
        start_page.place(x=10, y=465)
        page_two = Button(self, text='Page Two', command=lambda: controller.show_frame(PageTwo))
        page_two.place(x=725, y=465)

class PageTwo(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="PageTwo")
        label.pack()
        start_page = Button(self, text='Start Page', command=lambda: controller.show_frame(StartPage))
        start_page.place(x=725, y=465)
        page_one = Button(self, text='Page One', command=lambda: controller.show_frame(PageOne))
        page_one.place(x=10, y=465)

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


# TO DO: //

# class Page(Frame):
#     # Parent is the container and controller is the app
#     def __init__(self, parent, controller):
#         Frame.__init__(self, parent)
#         self.grid(row=0, column=0, sticky='nsew')
#
#     def create_label(self, label_name):
#         label = Label(self, text=label_name)
#         return label

# //
app = App()
app.mainloop()