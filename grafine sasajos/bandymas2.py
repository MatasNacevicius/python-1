import tkinter as tk
from tkinter import *

langas=Tk()
langas.geometry('400x300')
langas.title('Grafinė sąsaja')

mano=Menu(langas)
langas.config(menu=mano)
mano.add_command(label='pirmas')
mano.add_command(label='antras')
mano.add_command(label='trecias')
is_m=Menu(mano)
mano.add_cascade(label='keturi', menu=is_m)
is_m.add_command(label='ketvirto pirmas')
is_m.add_command(label='ketvirto antras')
is_m.add_command(label='ketvirto trecias')
langas.mainloop()
