import pyautogui
from tkinter import *


def take_ss():
    add_data = entry.get()
    path = add_data + "\\test_12.png"
    print(path)
    ss = pyautogui.screenshot()
    ss.save(path)

win = Tk() 
win.title("Screen Shot app")
win.geometry("700x500")
win.config(bg="yellow")
win.resizable(False,False)

entry = Entry(win,font=('Time New Roman',30))
entry.place(x=20,height=100,width=660,y=50)

button = Button(win,text="Done",font=('Time New Roman',50),command=take_ss)
button.place(x=250,y=160,height=100,width=200)

win.mainloop()