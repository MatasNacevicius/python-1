from math import remainder
import tkinter as tk

langas=tk.Tk()
langas.geometry('300x400')
langas.title('Grafinė sąsaja')

# langas1=tk.Toplevel(langas)


def skaiciuoti():
    print(11*112)

rem=tk.Frame(langas) 
rem.place(relx=0.01, rely=0.01, relwidth=0.5, relheight=0.98)

mygtukas=tk.Button(rem, text='vienas', command=skaiciuoti)
mygtukas.place(relx=0.1, rely=0.2, relwidth=0.5, relheight=0.3)

mygtukas1=tk.Button(rem, text='du', command=skaiciuoti)
mygtukas1.place(relx=0.01, rely=0.3, relwidth=0.5, relheight=0.3)

mygtukas3=tk.Button(rem, text='trys', command=skaiciuoti)
mygtukas3.place(relx=0.01, rely=0.3, relwidth=0.5, relheight=0.3)

langas.mainloop()