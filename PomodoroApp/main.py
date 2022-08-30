import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        title.config(text="Break", fg=RED)
        count_down(long_break_sec)
    if reps % 2 == 0:
        title.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else: 
        title.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60) 
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer 
        timer = window.after(1000, count_down, count -1)
    else: 
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2) 
        for _ in range(work_sessions):
            marks += "✔"
        checkmark.config(text=marks)



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

reset = tk.Button(text="Reset", bg="white", highlightthickness=0, command=reset_timer)
reset.grid(row=2, column=2)

# checkmarks
checkmark = tk.Label()
checkmark.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, "bold"))
checkmark.config(pady=20)
checkmark.grid(row=3, column=1)

window.mainloop()