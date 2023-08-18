import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Simple GUI Application")

# Create a label widget
label = tk.Label(root, text="Hello, GUI World!")
label.pack()

# Create a function for button click
def show_message():
    messagebox.showinfo("Message", "Button Clicked!")

# Create a button widget
button = tk.Button(root, text="Click Me", command=show_message)
button.pack()

# Run the main event loop
root.mainloop()
