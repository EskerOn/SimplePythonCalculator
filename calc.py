from tkinter import *
from tkinter import ttk

class Calculator(ttk.Frame):
    """docstring for Calculator"""
    def __init__(self, parent):
        super().__init__(parent)
        self.setUp()

    def setUp(self):
        an=7
        self.grid(column=0, row=0)
        self.entrystr = StringVar()
        #self.entrystr=""
        self.res = StringVar()
        self.entry=ttk.Entry(self, width=an*4, textvariable=self.entrystr)
        self.entry.grid(row=1, columnspan=4, sticky=W)
        #ttk.Entry(self,width=an*4, textvariable="").grid(row=1, columnspan=4, sticky=W)
        ttk.Button(self,width=an, text="7", command=lambda:self.write("7")).grid(column=1, row=2, sticky=W)
        ttk.Button(self,width=an, text="8", command=lambda:self.write("8")).grid(column=2, row=2, sticky=W)
        ttk.Button(self,width=an, text="9", command=lambda:self.write("9")).grid(column=3, row=2, sticky=W)
        ttk.Button(self,width=an, text="4", command=lambda:self.write("4")).grid(column=1, row=3, sticky=W)
        ttk.Button(self,width=an, text="5", command=lambda:self.write("5")).grid(column=2, row=3, sticky=W)
        ttk.Button(self,width=an, text="6", command=lambda:self.write("6")).grid(column=3, row=3, sticky=W)
        ttk.Button(self,width=an, text="1", command=lambda:self.write("1")).grid(column=1, row=4, sticky=W)
        ttk.Button(self,width=an, text="2", command=lambda:self.write("2")).grid(column=2, row=4, sticky=W)
        ttk.Button(self,width=an, text="3", command=lambda:self.write("3")).grid(column=3, row=4, sticky=W)
        ttk.Button(self,width=an, text="0", command=lambda:self.write("0")).grid(column=1, row=5, sticky=W)
        ttk.Button(self,width=an, text=".", command=lambda:self.write(".")).grid(column=2, row=5, sticky=W)
        ttk.Button(self,width=an, text="=", command=self.result).grid(column=3, row=5, sticky=W)
        ttk.Button(self,width=an, text="+", command=lambda:self.write("+")).grid(column=4, row=5, sticky=(E, S))
        ttk.Button(self,width=an, text="-", command=lambda:self.write("-")).grid(column=4, row=4, sticky=E)
        ttk.Button(self,width=an, text="/", command=lambda:self.write("/")).grid(column=4, row=3, sticky=E)
        ttk.Button(self,width=an, text="*", command=lambda:self.write("*")).grid(column=4, row=2, sticky=E)
        ttk.Button(self,width=an, text="←", command=self.dele).grid(column=4, row=1, sticky=W)
        for child in self.winfo_children(): child.grid_configure(padx=5, pady=5)

        self.entry.focus()

    def result(self):
        print("resultado")
        try:
            self.entrystr.set(eval(self.entrystr.get()))
        except SyntaxError as e:
            self.entrystr.set("Syntax error")
        except ZeroDivisionError as e:
            self.entrystr.set("Math Error")
        except Exception as e:
            self.entrystr.set("Syntax error")

    def write(self, symbol):
        print("presionado")
        if self.entrystr.get()=="Syntax error" or self.entrystr.get()=="Math Error":
            self.entrystr.set(symbol)
        else:
            self.entrystr.set(self.entrystr.get()+ symbol)

    def dele(self):
        print("del")
        if self.entrystr.get()=="Syntax error" or self.entrystr.get()=="Math Error":
            self.entrystr.set("")
        else:
            self.entrystr.set(self.entrystr.get()[0:len(self.entrystr.get())-1])