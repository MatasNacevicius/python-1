
import tkinter as tk
from tkinter import *
from tkinter import messagebox



langas=Tk()
langas.geometry('400x300')
langas.title('Grafinė sąsaja')


messagebox.showinfo('Uzduotis', 'Iveskite skaiciu paspauskite mygtuka')

def laipsnis():

    sk=ent.get()
    
    if sk:
        sk=int(sk)
        print(f'{sk} kvadratas: {sk**2}')
        ent.delete(0, END)
        kvad=sk**2
        zyma['text']=kvad 

        atv=zyma['text']
        print(atv-100)

    else:
        messagebox.showerror('Klaida', 'Klaida nieko nebuvo ivesta')


ent=Entry(langas, justify=CENTER)
ent.place(relx=0.01,rely=0.01, relwidth=0.98, relheight=0.1)

mygt=Button(langas, text='skaiciuoti', command=laipsnis)
mygt.place(relx=0.01,rely=0.3, relwidth=0.98, relheight=0.2)

zyma=Label(langas)
zyma.place(relx=0.1,rely=0.55, relwidth=0.98, relheight=0.44)


langas.mainloop()