import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from uzduotis1 import *

langas=Tk()
langas.geometry('300x500')

def registracija():
    vardas=input("iveskite varda: ")
    if vardas == 'matas':
        uzduotis()

e1=Entry(langas, justify=CENTER)
e2=Entry(langas, justify=CENTER)
e1.place(relx=0.01,rely=0.01, relwidth=0.4, relheight=0.15)
e2.place(relx=0.43,rely=0.01, relwidth=0.4, relheight=0.15)

m1=Button(langas, text='skaiciuoti', command=registracija)
m1.place(relx=0.01,rely=0.69, relwidth=0.98, relheight=0.15)

langas.mainloop()