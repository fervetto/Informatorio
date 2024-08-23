from tkinter import *
from tkinter import ttk
root = Tk()


frm = ttk.Frame(root, padding=50)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=5, row=8)
ttk.Button(frm, text="Sallir", command=root.destroy).grid(column=5, row=10)
root.mainloop()