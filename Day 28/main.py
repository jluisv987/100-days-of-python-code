
from tkinter import *
import math
#  ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    global reps
    reps = 0
    check_label.config(text=f"{reps} reps")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    check_label.config(text=f"{reps} reps")
    if reps == 5:
        timer_label.config(text="L Break", fg=RED)
        count_down(LONG_BREAK_MIN*60)
        reps = 0
    elif reps !=0 and reps % 2 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(SHORT_BREAK_MIN*60)      
        reps+=1
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN*60)
        reps+=1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_seg= count%60
    if count_min<10:
        count_min = "0"+str(count_min)
    if count_seg<10:
        count_seg = "0"+str(count_seg)
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_seg}")
    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_label =Label(text = "Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))
start_button = Button(text="Start",command = start_timer)
reset_button = Button(text="Reset",command = reset_timer)
check_label=Label(text = "0",fg=GREEN,bg=YELLOW,font=(FONT_NAME,15))
timer_text = canvas.create_text(100,112,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
#grid
timer_label.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)
check_label.grid(column=1, row=3)
window.mainloop()