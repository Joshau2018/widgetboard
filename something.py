# Python
import tkinter as tk
from tkinter import ttk

# window is an object of the tk class
window = tk.Tk()
window.title("Widget Board")
window.minsize(width=500, height=300)

# Label a location to DISPLAY text
a_label = tk.Label(text="Howdy", font=("Monospace", 24, "normal"))
a_label.pack()

# Entry (textbox)
a_textbox = tk.Entry(width=40, font=("Times New Roman", 18, "normal"))
a_textbox.focus()
a_textbox.insert(index=tk.END, string='Some text to take up space')
a_textbox.pack(pady=(5, 5))  # pady(x, y), x=Horizontal, y=Vert


# Button
def button_clicked():
    a_label["text"] = f'{a_textbox.get()}'


button = tk.Button(text="DO NOT CLICK", command=button_clicked)
button.pack(pady=(0, 5))


# Text (Multi-line textbox)
text = tk.Text(width=30, height=5)
# Add some text to begin with
text.insert(index=tk.END, chars="Ex of multi line entry :)")
text.pack(pady=(0, 5))


# must be at the end
window.mainloop()
