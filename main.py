from tkinter import *
from tkinter import ttk
from calc import Calculator


if __name__=='__main__':
    root = Tk()
    root.title("Calculadora")
    calculator=Calculator(root)
    root.bind('<Return>', calculator.result)
    s=ttk.Style()
    print(s.theme_names())
    s.theme_use('clam')
    #root.geometry("250x200") definir el tamaño por defecto
    root.resizable(0,0)
    root.mainloop()