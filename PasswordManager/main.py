import tkinter as tk


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    email = email_input.get()
    pw = pw_input.get()

    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {pw}\n")
        website_input.delete(0, tk.END)
        pw_input.delete(0, tk.END)


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
website_input.focus()

email_input = tk.Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky=tk.W)
email_input.insert(0, "<youremail@example.com>")

pw_input = tk.Entry()
pw_input.grid(row=3, column=1, sticky=tk.W)

# Buttons

generate_button = tk.Button(text="Generate Password", bg="white")
generate_button.grid(row=3, column=2, columnspan=2)

add_button = tk.Button(text="Add", width=35, bg="white", command=save())
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()