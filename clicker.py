#Библиотеки
import pyautogui as cl
from tkinter import *
from but import clicked

window = Tk()
window.title("Автокликер")
window.geometry('210x120')

lbl = Label(window, text="Количество нажатий")  
lbl.pack(side="top")  
spin1 = Spinbox(window, from_=0, to=100, width=10)  
spin1.pack(side="top") 
float(spin1.get())
lbl = Label(window, text="Интервал")  
lbl.pack(side="top")
spin2 = Spinbox(window, from_=0, to=100, width=10)  
spin2.pack(side="top")
float(spin2.get())
s1 = float(spin1.get())
s2 = float(spin2.get())
btn = Button(window, text="Начать", command=lambda:clicked(spin1,spin2))
btn.pack(side="bottom") 


window.mainloop()