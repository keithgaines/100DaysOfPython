from tkinter import *


def convert():
    km = float(miles_input.get()) * 1.609
    km_input.config(text=km)

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

# Labels

Miles_label = Label(text="Miles")
Miles_label.grid(column=3, row=1)

isEqualTo = Label(text="is equal to")
isEqualTo.grid(column=1, row=2)


Km_label= Label(text="Km")
Km_label.grid(column=3, row=2)

# Entry

miles_input = Entry(width=7)
miles_input.grid(column=2, row=1)

km_input = Label(text="0")
km_input.grid(column=2, row=2)

# Button
button = Button(text="calculate" ,command=convert)
button.grid(column=2, row=3)

window.mainloop()