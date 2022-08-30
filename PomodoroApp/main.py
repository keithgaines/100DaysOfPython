import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Image and timer 
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

# Label 
label = tk.Label()
label.config(text="Timer", font=("Times New Roman", 25, "bold"), bg=YELLOW, fg=GREEN)
label.grid(row=1, column=2)


# Buttons
start = tk.Button(text="Start", bg="white", borderwidth=0)
start.grid(row=3, column=1)

reset = tk.Button(text="Reset", bg="white", borderwidth=0)
reset.grid(row=3, column=3)

# checkmarks
checkmark = tk.Label()
checkmark.config(text="✔", bg=YELLOW, fg=GREEN, font=("Times New Roman", 25, "bold"))
checkmark.config(pady=20)
checkmark.grid(row=4, column=2)

window.mainloop()