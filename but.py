import builtins
import pyautogui as cl
from tkinter import messagebox

def clicked(s1,s2):
    if float(s2.get()) >= 0.001:
        cl.click(clicks=int(s1.get()),interval=float(s2.get()),button="left")
    else:
        messagebox.showerror('Ошибка', 'Вы ввели недопустимое значение')  