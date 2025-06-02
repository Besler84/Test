import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x400")

text_variable = tk.StringVar()
text_variable.set("Das ist der neue Text")

text_variable2 = tk.IntVar()
text_variable.set(10)

text_variable3 = tk.DoubleVar()
text_variable.set(112.67)

text_variable4 = tk.BooleanVar()
text_variable.set(True)

label1 = ttk.Label(root, textvariable=text_variable)
label1.pack()

label2 = ttk.Label(root, textvariable=text_variable2)
label2.pack()

label3 = ttk.Label(root, textvariable=text_variable3)
label3.pack()

label4 = ttk.Label(root, textvariable=text_variable4)
label4.pack()

text_variable.set("Aktualisierter Text")

text_variable2.set("20")

text_variable3.set("223.55")

text_variable4.set(False)

root.mainloop()