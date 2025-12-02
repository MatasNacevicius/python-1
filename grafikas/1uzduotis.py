import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import numpy as np

x_values = None
y_values = None

def skaiciuoti():
    global x_values, y_values

    x1 = float(e1.get())
    x2 = float(e2.get())

    # Imame kiekvieną sveiką skaičių
    x_values = np.arange(int(x1), int(x2) + 1, 1)

    y_values = x_values**2 - 5*x_values

    rezultatai.delete(0, END)
    for x, y in zip(x_values, y_values):
        rezultatai.insert(END, f"x={x}   y={y}")


def braizyti():
    plt.figure(figsize=(6,4))
    plt.plot(x_values, y_values, marker='o', label="y = x² - 5x")

    plt.title("Funkcijos atvaizdavimas")
    plt.xlabel("X asis")
    plt.ylabel("Y asis")
    plt.grid(True)
    plt.legend()
    plt.show()


def irasyti_faila():
    failas = filedialog.asksaveasfilename(defaultextension=".txt",
                                          filetypes=[("Text files", "*.txt")])

    with open(failas, "w") as f:
        for x, y in zip(x_values, y_values):
            f.write(f"{x}; {y}\n")


langas = Tk()
langas.title("Grafikas")
langas.geometry('500x380')

formule = Label(langas, text='y = x**2 - 5*x', relief=RIDGE, font=("Arial", 12))
zyma1 = Label(langas, text='Įveskite x diapazoną:')
zyma2 = Label(langas, text='Skaičiavimo rezultatai:')

formule.place(relx=0.03, rely=0.05, relwidth=0.4, relheight=0.08)
zyma1.place(relx=0.45, rely=0.02, relwidth=0.5, relheight=0.1)
zyma2.place(relx=0.03, rely=0.22, relwidth=0.5, relheight=0.1)

e1 = Entry(langas, justify=CENTER)
e2 = Entry(langas, justify=CENTER)
e1.place(relx=0.5, rely=0.1, relwidth=0.15, relheight=0.08)
e2.place(relx=0.7, rely=0.1, relwidth=0.15, relheight=0.08)

rezultatai = Listbox(langas)
rezultatai.place(relx=0.03, rely=0.33, relwidth=0.45, relheight=0.55)

btn_skaiciuoti = Button(langas, text="Skaičiuoti", command=skaiciuoti)
btn_skaiciuoti.place(relx=0.55, rely=0.33, relwidth=0.35, relheight=0.1)

meniu = Menu(langas)
langas.config(menu=meniu)
is_m = Menu(meniu, tearoff=0)
meniu.add_cascade(label='pasirinkti', menu=is_m)

is_m.add_command(label='Irasyti faila', command=irasyti_faila)
is_m.add_command(label='grafikas', command=braizyti)
is_m.add_command(label='baigti', command=langas.destroy)

langas.mainloop()
