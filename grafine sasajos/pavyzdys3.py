import tkinter as tk
from tkinter import *
from tkinter import filedialog

langas=Tk()
langas.title('Entry laukas')
langas.geometry('300x100')

def atidaryti():
    f=filedialog.askopenfilename(title='pasirinkite faila', filetypes=(('txt failai','*.txt'),('Visi failai','*.*')))

    failas=open(f,'r')
    skaityt=failas.readlines()
    langas1=Toplevel(langas)
    langas1.title('Failo turinys')
    langas1.geometry('400x200')
    tekstas=Text(langas1)
    tekstas.place(relx=0,rely=0,relwidth=1, relheight=1)
    tekstas.insert(1.0,skaityt)
    failas.close()

m1=Button(langas,text='atidaryti',command=atidaryti)
m1.place(relx=0,rely=0, relwidth=1, relheight=1)



langas.mainloop()