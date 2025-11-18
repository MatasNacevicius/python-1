import tkinter as tk
from tkinter import *

langas=Tk()
langas.title('Entry laukas')
langas.geometry('300x100')

def rasyt():
    a=Ent1.get()
    if a:
        a=a+'\n'
        tekstas.insert(END,a)
        Ent1.delete(0,END)


Ent1=Entry(langas,font=20, justify=CENTER)
Ent1.place(relx=0,rely=0, relwidth=1, relheight=0.5)

m1=Button(langas,text='Irašyti',command=rasyt)
m1.place(relx=0,rely=0.5, relwidth=1, relheight=0.5)

langas1=Toplevel(langas)
langas1.title('Textbox')
tekstas=Text(langas1,wrap=WORD)
tekstas.place(relx=0,rely=0, relwidth=1, relheight=1)

langas.mainloop()