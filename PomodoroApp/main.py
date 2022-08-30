import tkinter as tk
import math

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
def start_timer():
    count_down(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60) 
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count -1)

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Image and timer 
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


# Label 
title = tk.Label()
title.config(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
title.grid(row=0, column=1)


# Buttons
start = tk.Button(text="Start", bg="white", highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

reset = tk.Button(text="Reset", bg="white", highlightthickness=0)
reset.grid(row=2, column=2)

# checkmarks
checkmark = tk.Label()
checkmark.config(text="✔", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, "bold"))
checkmark.config(pady=20)
checkmark.grid(row=3, column=1)

window.mainloop()