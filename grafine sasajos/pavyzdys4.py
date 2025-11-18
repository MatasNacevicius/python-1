import tkinter as tk
from tkinter import *
from tkinter import filedialog

langas=Tk()
langas.title('Išsaugoti failą')
langas.geometry('400x200')

def saugoti():
    ff=filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    ff.write(tekstas.get(1.0,END))
    ff.close()

tekstas=Text(langas,font=20)
tekstas.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.7)

m=Button(langas,text='Išsaugoti',command=saugoti)
m.place(relx=0,rely=0.7,relwidth=1,relheight=0.3)

langas.mainloop()