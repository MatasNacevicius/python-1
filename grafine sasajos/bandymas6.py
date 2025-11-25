from cProfile import label
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
import numpy as np

langas=Tk()

x=np.linspace(-10,10, 100)
y=x**2*x
y1=x**3
plt.plot(x,y, label='y=x**2*x')
plt.title('Funkcija')
plt.xlabel('x reiksme')
plt.ylabel('y reiksme')
plt.grid(axis='both')
plt.legend()
plt.show()

langas.mainloop()