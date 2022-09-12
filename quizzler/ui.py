from linecache import checkcache
from textwrap import fill
import tkinter as tk 

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)

        self.score = tk.Label()
        self.score.config(padx=20, pady=20, bg=THEME_COLOR, fg="white", text="Score: 0")
        self.score.grid(row=0, column=1)

        self.canvas = tk.Canvas()    
        self.canvas.config(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20)

        check_image = tk.PhotoImage(file="images/true.png")
        self.check = tk.Button(image=check_image)
        self.check.grid(row=2, column=0)

        false_image = tk.PhotoImage(file="images/false.png")
        self.false = tk.Button(image=false_image)
        self.false.grid(row=2, column=1)




        self.window.mainloop()