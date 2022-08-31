import email
import tkinter as tk
from turtle import width

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels

website_label = tk.Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

email_label = tk.Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)

pw_label = tk.Label(text="Password:", bg="white")
pw_label.grid(row=3, column=0)

# Entries

website_input = tk.Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky=tk.W)

email_input = tk.Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky=tk.W)

pw_input = tk.Entry()
pw_input.grid(row=3, column=1, sticky=tk.W)

# Buttons

generate_button = tk.Button(text="Generate Password", bg="white")
generate_button.grid(row=3, column=2, columnspan=2)

add_button = tk.Button(text="Add", width=35, bg="white")
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()