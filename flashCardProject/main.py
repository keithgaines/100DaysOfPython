BACKGROUND_COLOR = "#B1DDC6"

from dataclasses import field
from email.mime import image
import tkinter as tk
from turtle import width

window = tk.Tk()
window.config(bg=BACKGROUND_COLOR)
window.title("Flashy")

canvas = tk.Canvas(height=526, width=800, highlightthickness=0)
card_front = tk.PhotoImage(file="./images/card_front.png")
canvas.create_image(526, 800, image=card_front)
title = canvas.create_text(400, 150, text="Title", font=("arial", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("arial", 60, "bold"))

canvas.grid(padx=50, pady=50, column=0, columnspan=2)

x_image = tk.PhotoImage(file="./images/wrong.png")
x_button = tk.Button(image=x_image, highlightthickness=0)
x_button.grid(column=0, row=1)

check_image = tk.PhotoImage(file="./images/right.png")
check_button = tk.Button(image=check_image, highlightthickness=0)
check_button.grid(column=1, row=1)

window.mainloop()