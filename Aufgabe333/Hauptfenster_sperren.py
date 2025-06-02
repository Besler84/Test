import tkinter as tk

root = tk.Tk()
root.title("Hauptfenser")
root.geometry("720x480")
root.minsize(width=320, height=240)
root.maxsize(width=1280, height=720)
root.resizable(width=False, height=True)

label1 = tk.Label(root, text="Hauptmenü")
label1.pack()

root.mainloop()