from tkinter import *
from PIL import Image, ImageTk

min_w = 0  # Minimum width of the frame
max_w = 280  # Maximum width of the frame
cur_width = min_w  # Increasing width of the frame
expanded = False  # Check if it is completely expanded

def expand():
    global cur_width, expanded
    cur_width += 10  # Increase the width by 10
    rep = root.after(5, expand)  # Repeat this func every 5 ms
    menu_drawer.config(width=cur_width)  # Change the width to new increase width
    if cur_width >= max_w:  # If width is greater than maximum width
        expanded = True  # Frame is expanded
        root.after_cancel(rep)  # Stop repeating the func
     

def contract():
    global cur_width, expanded
    cur_width -= 10  # Reduce the width by 10
    rep = root.after(5, contract)  # Call this func every 5 ms
    menu_drawer.config(width=cur_width)  # Change the width to new reduced width
    if cur_width <= min_w:  # If it is back to normal width
        expanded = False  # Frame is not expanded
        root.after_cancel(rep)  # Stop repeating the func
        

def on_enter(e):
    e.widget['background'] = 'green'

def on_leave(e):
    e.widget['background'] = 'SystemButtonFace'

root = Tk()
root.geometry("600x950+50+50")

menu_bar = Frame(root, width=700, height=80, bg='#34ebba')
menu_bar.place(x=0, y=0)

title = Label(menu_bar, text='ABOUT US', font=('Helvetica', 20, 'bold' ), bg='#34ebba')
title.place(x=240,y=25)

about_frame = Frame(root, height=650, width=500, bg='#203243')
about_frame.place(x=50, y=180)

about_text = 'At Eye Weather, we understand the importance of staying informed about the weather conditions in your area. Our app is designed to provide you with accurate and up-to-date weather forecasts, so you can plan your day accordingly. Whether you are heading out for work, planning a weekend getaway, or simply want to stay informed, our app has you covered.'

about_content = Label(about_frame, text=about_text, font=('Helvetica', 15), bg='#203243',fg='white', wraplength=400, justify='center')
about_content.place(x=50, y=25)

root.update()  # For the width to get updated

menuopen = ImageTk.PhotoImage(Image.open('C:/Users/kx063/OneDrive/桌面/91906/assest/menuopen.png').resize((50, 50), Image.ANTIALIAS))
menuclose = ImageTk.PhotoImage(Image.open('C:/Users/kx063/OneDrive/桌面/91906/assest/menuclose.png').resize((50, 50), Image.ANTIALIAS))
logo = ImageTk.PhotoImage(Image.open('C:/Users/kx063/OneDrive/桌面/91906/assest/logo.png').resize((200, 100), Image.ANTIALIAS))

menu_drawer = Frame(root, bg='white', width=0, height=root.winfo_height())
menu_drawer.place(x=0, y=0)

openmenu_button = Button(menu_bar, image=menuopen, bg='#34ebba', activebackground = '#34ebba',relief='flat',command=expand)
openmenu_button.place(x=20, y=13)

closemenu_button = Button(menu_drawer, image=menuclose, bg='white', relief='flat',command=contract)
closemenu_button.place(x=210, y=30)

logolabel = Label(menu_drawer, image=logo, bg='white')
logolabel.place(x=5, y=10)

Home_button = Button(menu_drawer, text='Home',bg = 'white', relief = 'flat', width = 39, height = 3)
Home_button.place(x=0,y=170)

Travel_button = Button(menu_drawer, text='Travel',bg = 'white', relief = 'flat', width = 39, height = 3)
Travel_button.place(x=0,y=230)

Quiz_button = Button(menu_drawer, text='Quiz',bg = 'white', relief = 'flat', width = 39, height = 3)
Quiz_button.place(x=0,y=290)

About_button = Button(menu_drawer, text='About',bg = 'white', relief = 'flat', width = 39, height = 3)
About_button.place(x=0,y=350)

Logout_button = Button(menu_drawer, text='Logout',bg = 'white', relief = 'flat', width = 39, height = 3)
Logout_button.place(x=0,y=410)

# Bind to the frame, if entered or left
menu_drawer.bind('<Enter>')
menu_drawer.bind('<Leave>')

Home_button.bind("<Enter>", on_enter)
Home_button.bind("<Leave>", on_leave)

Travel_button.bind("<Enter>", on_enter)
Travel_button.bind("<Leave>", on_leave)

Quiz_button.bind("<Enter>", on_enter)
Quiz_button.bind("<Leave>", on_leave)

About_button.bind("<Enter>", on_enter)
About_button.bind("<Leave>", on_leave)

Logout_button.bind("<Enter>", on_enter)
Logout_button.bind("<Leave>", on_leave)

# So that it does not depend on the widgets inside the frame
menu_drawer.grid_propagate(False)

root.mainloop()