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
a_textbox.pack(pady=(5, 5))  # pady=(x, y), x=Horizontal, y=Vert


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

# Spinbox
def spinbox_used():
    print(spinbox.get())
spinbox = tk.Spinbox(from_=0, to_=10, width=5, command=spinbox_used)
spinbox.pack(pady=(0,5))

# Scale is a slider
def scale_use(value):
    print(value)
scale = tk.Scale(from_=0, to_=100, command=scale_use,
                 orient=tk.HORIZONTAL, length=150, width=30,
                 sliderlength=10, tickinterval=20)
scale.pack(pady=(0, 5))

# Checkbutton
def checkbotton_used():
    print(checked_state.get())
checked_state = tk.BooleanVar()
checkbutton = tk.Checkbutton(text='Is On?', variable=checked_state,
                             command=checkbotton_used)
checkbutton.pack(pady=(0, 5))

# Radio button
def radio_used():
    print(radio_state.get())
radio_state = tk.IntVar()
radiobutton1 = tk.Radiobutton(text='Option 1', value=1,
                              variable=radio_state, command=radio_used)
radiobutton2 = tk.Radiobutton(text='Option 2', value=2,
                              variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack(pady=(0, 5))
radiobutton1.select()

# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))
listbox = tk.Listbox(height=6)
fruits = ['apple', 'Mango', 'Orange', 'Pear', 'Banana', 'Kiwi']
# enumerates goes through the values and creates a tupal
for i, fruit in enumerate(fruits):
    listbox.insert(i, fruit)
listbox.bind(sequence='<<ListboxSelect>>', func=listbox_used)
listbox.pack(pady=(0, 5))

# Combobox
def combobox_used(event):
    print(n.get())
n = tk.StringVar()
combobox = ttk.Combobox(width=30, textvariable=n)
combobox.bind(sequence='<<ComboboxSelected>>', func=combobox_used)
combobox['values'] = (' January',
                      ' February',
                      ' March',
                      ' April',
                      ' May',
                      ' June',
                      ' July',
                      ' August',
                      ' September',
                      ' October',
                      ' November',
                      ' December')
combobox.pack(pady=(0, 5))

# must be at the end
window.mainloop()
