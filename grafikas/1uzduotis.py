import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import numpy as np

langas=Tk()
langas.title('Grafikas')
langas.geometry('450x300')
formule=Label(langas, text='y=x**2-5*x', relief=RIDGE)
zyma1=Label(langas, text='Iveskite skaiciu diapazona')
zyma2=Label(langas, text='Skaiciavimo rezultatai')
formule.place(relx=0.03, rely=0.05, relwidth=0.3, relheight=0.1)
zyma1.place(relx=0.5, rely=0.02, relwidth=0.5, relheight=0.1)
zyma2.place(relx=0.03, rely=0.2, relwidth=0.3, relheight=0.1)
e1=Entry(langas)
e2=Entry(langas)
e1.place(relx=0.5, rely=0.1, relwidth=0.1, relheight=0.1)

meniu=Menu(langas)
langas.config(menu=meniu)
is_m=Menu(meniu)
meniu.add_cascade(label='pasirinkti',menu=is_m)
is_m.add_command(label='Irasyti faila')
is_m.add_command(label='ketvir')
is_m.add_command(label='ketvirto trecias')


langas.mainloop()