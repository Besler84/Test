import tkinter as tk
from tkinter import ttk

def say_hello():
    print("Ich habe dich gewarnt...")

def print_entry():
    ttk.Label(root, text=entry1.get()).pack()

def delete_entry():
    entry1.delete(0, tk.END)

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

button1 = ttk.Button(root, text="Bloß nicht drauf klicken !", command=say_hello)
button1.pack()

button2 = ttk.Button(root, text="Programm beenden", command=root.destroy)
button2.pack()

entry1 = ttk.Entry(root, width=60, foreground="red", justify="center")
entry1.pack()

entry1.insert(0, "Bitte hier deinen Namen eintragen")
entry1.insert(2, "TEST")

button3 = ttk.Button(root, text="Eingabe ausgeben", command=print_entry)
button3.pack()

button4 = ttk.Button(root, text="Eingabe löschen", command=delete_entry)
button4.pack()

text_variable.set("Aktualisierter Text")

text_variable2.set("20")

text_variable3.set("223.55")

text_variable4.set(False)

root.mainloop()