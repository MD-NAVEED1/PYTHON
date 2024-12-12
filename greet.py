import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title("GREETING APP")
app.geometry("300x200")

def greet():
    name = name_entry.get()
    if name:
        messagebox.showinfo("Greeting",f"hello{name}!")
    else:
        messagebox.showwarning("input error","please enter your name.")
        
        
name_label= tk.Label(app, text="enter your name:")
name_label.pack(pady=10)

name_entry = tk.Entry(app)
name_entry.pack(pady=10)

greet_button = tk.Button(app, text="Greet", command=greet)
greet_button.pack(pady=10)

app.mainloop()
