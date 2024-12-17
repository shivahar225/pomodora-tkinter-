from tkinter import *
import math

COLOUR_1 = "#e730d2"
COLOUR_2 = "#a599e2"
COLOUR_3 = "#30e7aa"
COLOUR_4 = "#7e130"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

def reset_time():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marker.config(text="")
    global reps
    reps = 0


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_term_sec = SHORT_BREAK_MIN * 60
    long_term_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_term_sec)
        title_label.config(text="break", fg=COLOUR_2)
    elif reps % 2 == 0:
        count_down(short_term_sec)
        title_label.config(text="break", fg=COLOUR_3)
    else:
        count_down(work_sec)
        title_label.config(text="work", fg=COLOUR_4)
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer =window.after(1000,count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

window = Tk()
window.title("pomodoro")
window.config(padx=100,pady=100, bg=COLOUR_1)



title_label = Label(text="TIMER",fg=COLOUR_2,font=(FONT_NAME,50,"bold"), bg=COLOUR_1)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200,height=300,bg=COLOUR_1,highlightthickness=0)
#shiva_img = PhotoImage(file="tomoto1.jpg")
#canvas.create_image(100,125 ,image=shiva_img)
timer_text = canvas.create_text(100,125, text="00:00", fill="white", font=(FONT_NAME,40,"bold"))
canvas.grid(column=1 ,row=1)

star_button = Button(text="start", highlightthickness=0, command=start_timer)
star_button.grid(column=0, row=2)

reset_button = Button(text="reset",highlightthickness=0, command=reset_time)
reset_button.grid(column=2, row=2)

check_marker = Label(fg=COLOUR_2, bg=COLOUR_1, font=(FONT_NAME,25,"bold"))
check_marker.grid(column=1, row=3)

window.mainloop()

