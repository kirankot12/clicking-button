import tkinter as tk
i = 0
def button_clicked():
    global i
    i+= 1
    label.config(text="Button pressed {} times!".format (i))

window = tk.Tk()

window.title("button clicker")

label=tk.Label(window, text = "Welcome to the button!")
label.pack(pady = 10)


button= tk.Button(window, text="Click me", command=button_clicked)
button.pack()

window.mainloop()