import tkinter as tk

app = tk.Tk()
app.title("counter")
app.geometry("300x200")

counter = 0

def update_label():
    count_label.config(text=f"count:{counter}")
    
    
def incriment():
    global counter
    counter += 1
    update_label()
    
    
def decrimnet():
    global counter
    counter -= 1
    update_label()
    
count_label = tk.Label(app, text=f"count:{counter}", font=("Helvetica",16))
count_label.pack(pady=20) 

button_frame = tk.Frame(app)
button_frame.pack(pady=10)

incriment_button = tk.Button(button_frame,text="incriment",command=incriment,width=10)
incriment_button.pack(side=tk.LEFT,padx=5)

decrimnet_button = tk.Button(button_frame, text="decriment", command=decrimnet, width=10)
decrimnet_button.pack(side=tk.LEFT,padx=5)

app.mainloop()

       