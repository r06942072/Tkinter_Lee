#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *

if __name__ == '__main__': #中文 
    print("Start script")
    root = Tk()
    root.title("My calculator") #設定這個GUI的標題
    
    e = Entry(root, width=35, borderwidth=5)
    #e.grid(row=0, column=0, columnspan=30, padx=10, pady=10)

    e.insert(0, "Enter your name: ")


    root.mainloop()
    print("Finish script")
