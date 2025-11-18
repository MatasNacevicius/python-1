from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
langas=Tk()
langas.geometry('300x180')
def irasyti():
    a=tekstas.get(1.0,END)
    if a:
        f = open('Naujas.txt', 'w')
        f.write(a)
        f.close()

  
tekstas=Text(langas, wrap=WORD)
tekstas.place(relx=0,rely=0,relwidth=1,relheight=0.7)
m1=Button(langas,text='Įrašyti į failą', command=irasyti)
m1.place(relx=0, rely=0.7, relwidth=1, relheight=0.3)
langas.mainloop()