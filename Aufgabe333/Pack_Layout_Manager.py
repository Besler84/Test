import tkinter as tk

root = tk.Tk()
root.title("Hauptfenser")
root.geometry("720x480")
root.minsize(width=320, height=240)
root.maxsize(width=1280, height=720)

label1 = tk.Label(root, text="Hauptmenü", bg="green")
label1.pack(side="top", expand=True, fill="y")

label2 = tk.Label(root, text="Anwendung verlassen", bg="red")
label2.pack(side="top", expand=True, fill="both")

root.mainloop()