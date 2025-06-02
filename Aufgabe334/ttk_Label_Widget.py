import tkinter as tk
from tkinter import  ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Hauptfenser")
root.geometry("820x580")
root.minsize(width=820, height=580)
root.maxsize(width=820, height=580)

# style = ttk.Style()
# style.theme_use("calm")

image = Image.open("chair.jpg").resize((720, 480))
photo = ImageTk.PhotoImage(image)

label1 = ttk.Label(root, text="The Emperors Chair", image=photo)
label1.pack()

label1.configure(font=("Courier", 30), compound="center", background="black", foreground="red", padding=50)

for item in label1.keys():
    print(item, ": ", label1[item])

root.mainloop()