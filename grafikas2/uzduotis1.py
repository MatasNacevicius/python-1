import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def uzduotis():
    langas=Tk()
    langas.geometry('300x500')

    def skaiciavimas():
        global x1
        global x2
        x1 = e1.get()
        if x1:
            x1=int(x1)

            x2 = e2.get()
            if x2:
                x2=int(x2)
                for i in range(x1, x2):
                    y=np.sin(i)
                    print(f'{i}\t{y: 1.2f}')
                    eilute=f'{i}\t{y: 1.2f}\n'
                    t1.insert(END, eilute)
                    m2.config(state=NORMAL)
            else:
                messagebox.showerror('Klaida ', 'Neivestas x2')
        else:
            messagebox.showerror('Klaida ', 'Neivestas x1')
        # x=np.arange(int(x1), int(x2), 1)

        # y = 5**x

        # print(f'x\ty\n-------------\n')

        # for i in range(x1, x2):
        #     y=np.sin(i)
        #     print(f'{i}\t{y: 1.2f}')
        #     eilute=f'{i}\t{y: 1.2f}\n'
        #     t1.insert(END, eilute)
        
    def grafikas():
        x=np.linspace(x1, x2, 100)
        y=np.sin(x)

        plt.plot(x,y, label='y=5**x')

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Funkcijos grafikas')
        plt.grid()
        plt.legend()
        plt.show()

    e1=Entry(langas, justify=CENTER)
    e2=Entry(langas, justify=CENTER)
    e1.place(relx=0.01,rely=0.01, relwidth=0.4, relheight=0.15)
    e2.place(relx=0.43,rely=0.01, relwidth=0.4, relheight=0.15)
    t1=Text(langas)
    t1.place(relx=0.01,rely=0.2, relwidth=0.98, relheight=0.4)

    m1=Button(langas, text='skaiciuoti', command=skaiciavimas)
    m1.place(relx=0.01,rely=0.69, relwidth=0.98, relheight=0.15)
    m2=Button(langas, text='grafikas', command=grafikas, state=DISABLED)
    m2.place(relx=0.01,rely=0.82, relwidth=0.98, relheight=0.15)

    # meniu=Menu(langas)
    # langas.config(menu=meniu)
    # meniu.add_command(label='grafikas', command=grafikas)



    # x=np.linspace(-10, 10, 100)
    # # y=5**x

    # print(f'x\ty\n-------------\n')

    # for i in range(-10, 10):
    #     y=5**i
    #     print(f'{i}\t{y}')

    # plt.plot(x,5**x, label='y=5**x')

    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.title('Funkcijos grafikas')
    # plt.grid()
    # plt.legend()
    # plt.show()

    langas.mainloop()