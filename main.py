#!/usr/bin/python
from tkinter import *

def button_add():
    return

def button_click(number):
    return

def button_clear():
    return

if __name__ == '__main__': 
    print("Start script")
    root = Tk()
    root.title("My calculator")
    
    e = Entry(root, width=50)  #An input box

    # Define Buttons
    # The size of the buttons are 20*20
    button_1 = Button(root, text="1", padx=20, pady=20, command=button_add)
    button_2 = Button(root, text="2", padx=20, pady=20, command=button_add)
    
    # Put the buttons on the screen
    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=2)

    root.mainloop()
    print("Finish script")
