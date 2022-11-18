# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 00:16:49 2022

@author: nguye
"""

from os import listdir, rename
from os.path import splitext
from tkinter import Tk,Frame,Menu,Label,Text,Button



window = Tk()
window.title("Options")

width = 200
height = 270

screen_width = window.winfo_screenwidth()  # Width of the screen
screen_height = window.winfo_screenheight() # Height of the screen
 
# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
 
window.geometry('%dx%d+%d+%d' % (width, height, x, y))

frame = Frame(window, bg="#e8f1fa").place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.30)
frame2 = Frame(window, bg="#c7ddf2").place(relx=0.0, rely=0.30, relwidth=1.0, relheight=0.30)
frame3 = Frame(window, bg="#8ebae5").place(relx=0.0, rely=0.60, relwidth=1.0, relheight=0.30)
menu = Menu(window)
window.config(menu=menu)

label = Label(frame ,text='Replace:', bd='3', fg='black',bg="#e8f1fa", font='Times 9')
label.place(relx=0.0,rely = 0.0, relwidth = 1.0, relheight = 0.10)
entry_field = Text(frame, bd='3',bg="#ecf6ff")
entry_field.place(relx=0.05,rely = 0.10, relwidth = 0.9, relheight = 0.15)

label2 = Label(frame2 ,text='By:', bd='3', fg='black',bg="#c7ddf2", font='Times 9')
label2.place(relx=0.0,rely = 0.30, relwidth = 1, relheight = 0.10)
entry_field2 = Text(frame2, bd='3',bg="#ecf6ff")
entry_field2.place(relx=0.05,rely = 0.40, relwidth = 0.9, relheight = 0.15)


label3 = Label(frame3 ,text='File .extension:', bd='3', fg='black',bg="#8ebae5", font='Times 9')
label3.place(relx=0.0,rely = 0.60, relwidth = 1.0, relheight = 0.10)
entry_field3 = Text(frame3, bd='3',bg="#ecf6ff")
entry_field3.place(relx=0.05,rely = 0.70, relwidth = 0.9, relheight = 0.15)

def get_value():
    Rename = entry_field.get(1.0, "end-1c")
    Bythat = entry_field2.get(1.0, "end-1c")
    Extension = entry_field3.get(1.0, "end-1c")


    for count, f in enumerate(listdir()):
        if Extension in f and Rename in f:
            f_name, f_ext = splitext(f)
            a,b = f_name.split(Rename)
            new_name = a + Bythat +b  + f_ext
            rename(f, new_name)

button= Button(window, text="Apply", command= get_value)
button.place(relx=0.0,rely = 0.9, relwidth = 1.0, relheight = 0.1)

window.mainloop()

