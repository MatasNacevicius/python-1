import tkinter as tk
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt

langas=Tk()
langas.geometry('400x300')
langas.title('Grafinė sąsaja')
mano=Menu(langas)

def informacinis():
    messagebox.showinfo('informacinis','pranesimas')

def klaida():
    messagebox.showerror('Klaida','klaida')

def ispejamasis():
    messagebox.showwarning('Įspėjimas','ispejimas')

def pasirinkimas():
    klausimas=messagebox.askokcancel('Pasirinkimas','Ar tikrai norite uzbaikti darba?')
    if klausimas:
        langas.destroy()
    else:
        messagebox.showinfo('dirbam','dirbam toliau')


langas.config(menu=mano)
mano.add_command(label='informacinis', command=informacinis)
mano.add_command(label='klaida', command=klaida)
mano.add_command(label='trecias')
is_m=Menu(mano)
mano.add_cascade(label='keturi', menu=is_m)
is_m.add_command(label='ketvirto pirmas')
is_m.add_command(label='ketvirto antras')
is_m.add_command(label='ketvirto trecias')

def pop_up(e):
    kont.tk_popup(e.x_root, e.y_root)

fr=Frame(langas, bg='red')
fr.place(relx=0.2, rely=0.2, relwidth=0.3, relheight=0.3)
# kont=Menu(langas)
kont=Menu(fr)
kont.add_command(label='ispejamas', command=ispejamasis)
kont.add_command(label='viso gero', command=pasirinkimas)



fr.bind("<Button-3>",pop_up)
langas.mainloop()
