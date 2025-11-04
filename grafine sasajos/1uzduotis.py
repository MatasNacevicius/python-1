
import tkinter as tk
from tkinter import*

langas=Tk()
langas.title('registracijos forma')
langas.geometry('300x150')
langas.resizable(True, True)

vardas=Label(langas, text='Vardas').place(relx=0, rely=0)
pavarde=Label(langas, text='Pavardė').place(relx=0, rely=0.3)
psw=Label(langas, text='Slaptažodis').place(relx=0, rely=0.6)
Evardas=Entry(langas, justify=CENTER).place(relx=0.3, rely=0)
Epavarde=Entry(langas, justify=CENTER).place(relx=0.3, rely=0.3)
Epsw=Entry(langas, justify=CENTER, show='*').place(relx=0.3, rely=0.6)
lab=Label(langas,bitmap='hourglass').place(relx=0.8,rely=0.2)
mygtukas=Button(langas, text='Registracija').place(relx=0.01, rely=0.8, relwidth=0.98)
langas.mainloop()
