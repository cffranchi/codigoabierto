import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
import pyfolio as pf



def sele():
    if activo.get() == "":
        messagebox.showinfo(message="Ingresa el ticker del activo", title="Grafica activo")
        return

    if per.get() == "" or cbo.get() == "":
        messagebox.showinfo(message="Ingresa el periodo", title="Grafica activo")
        return
    
    if ch1.get() == 0 and ch2.get() == 0 and ch3.get() == 0 and ch4.get() == 0:
        messagebox.showinfo(message="Selecciona una opcion a graficar", title="Grafica activo")
        return
            
    if ch1.get() == 1:
        graph()
    if ch2.get() == 1:
        graph2()
    if ch3.get() == 1:
        graph3()
    if ch4.get() == 1:
        graph4()
    

def graph():
    ticker = activo.get()
    periodo = per.get() + cbo.get()
    data = yf.download(ticker, period = periodo)
    plt.style.use('dark_background')
    plt.rcParams['figure.figsize'] = [9.0, 5]
    plt.yscale('log')
    data['Adj Close'].plot(kind='line',title= ticker + " " + periodo)
    plt.show()

def graph2():
    ticker = activo.get()
    periodo = per.get() + cbo.get()
    data = yf.download(ticker, period = periodo)
    plt.style.use('dark_background')
    variaciones =  data['Adj Close'].pct_change()*100
    agrupados = variaciones.groupby(data.index.year).sum()
    agrupados.plot(kind='bar',title= ticker + ' - Suma de Rendimientos/año')
    plt .show()

def graph3():
    ticker = activo.get()
    periodo = per.get() + cbo.get()
    data = yf.download(ticker, period = periodo)
    plt.style.use('dark_background')
    variaciones =  data['Adj Close'].pct_change()*100
    agrupados = variaciones.groupby(data.index.dayofweek).mean()
    agrupados.plot(kind='bar',title= ticker + ' - Rendimientos/Dia Semana')
    plt .show()


def graph4():
    ticker = activo.get()
    periodo = per.get() + cbo.get()
    data = yf.download(ticker, period = periodo)
    plt.style.use('dark_background')
    data['Adj Close'].resample('W').last() 
    variaciones =  data['Adj Close'].pct_change()*100
    agrupados = variaciones.groupby(data.index.week).mean()
    agrupados.plot(kind='bar',title= tikcer + '- Rendimientos/Semana del Año')
    plt .show()

def fin ():
    root.destroy()

root = tk.Tk()
root.title ('Grafica activos')
root.geometry("400x200")

ch1 = tk.IntVar()
ch2 = tk.IntVar()
ch3 = tk.IntVar()
ch4 = tk.IntVar()

lbl = ttk.Label(root,text="Codigo activo")
lbl.pack()
lbl.place(x=10, y=10)

activo = ttk.Entry(root)
activo.place(x=10, y=40)

lbl1 = ttk.Label(root,text="Periodo")
lbl1.pack()
lbl1.place(x=150, y=10)

per = ttk.Entry(root)
per.place(x=150, y=40, width = '40')

cbo = ttk.Combobox(root, values=["Y", "M",  "D"], width = '5')
cbo.place(x=200, y=40)

chk1 = ttk.Checkbutton(root, text="Evolucion", variable = ch1, onvalue = 1, offvalue = 0)
chk1.place(x=5, y=60)

chk2 = ttk.Checkbutton(root, text="Suma de Rendimientos/año", variable = ch2, onvalue = 1, offvalue = 0)
chk2.place(x=5, y=80)

chk3 = ttk.Checkbutton(root, text="Rendimientos/Dia Semana", variable = ch3, onvalue = 1, offvalue = 0)
chk3.place(x=5, y=100)

chk4 = ttk.Checkbutton(root, text="Rendimientos/Semana del Año", variable = ch4, onvalue = 1, offvalue = 0)
chk4.place(x=5, y=120)

my_button = ttk.Button(root, text = "Grafica", command = sele)
my_button.pack()
my_button.place(x=5, y=150)

button2 = ttk.Button(root, text = "Salir", command = fin)
button2.pack()
button2.place(x=80, y=150)


root.mainloop()
