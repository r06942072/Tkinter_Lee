#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *

if __name__ == '__main__': #���� 
    print("Start script")
    root = Tk()
    root.title("My calculator") #�]�w�o��GUI�����D
    
    e = Entry(root, width=35, borderwidth=5)
    #e.grid(row=0, column=0, columnspan=30, padx=10, pady=10)

    e.insert(0, "Enter your name: ")


    root.mainloop()
    print("Finish script")
