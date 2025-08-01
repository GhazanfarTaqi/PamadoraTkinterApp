from tkinter import *
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
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def resetTimer():
    window.after_cancel(timer)
    text_label.config(text="Timer",fg=GREEN)
    check_label.config(text="")
    canvas.itemconfig(timerText,text="00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def startTimer():
    global reps
    reps += 1
    workSec = WORK_MIN * 60
    shortBreakSec = SHORT_BREAK_MIN * 60
    longBreakSec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countDown(longBreakSec)
        text_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countDown(shortBreakSec)
        text_label.config(text="Break", fg=PINK)
    else:
        countDown(workSec)
        text_label.config(text="Work", fg=GREEN)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countDown(count):
    countMin = math.floor(count/60)
    countSec = math.floor(count%60)

    if countSec<10:
        countSec = f"0{countSec}"

    canvas.itemconfig(timerText,text=f"{countMin}:{countSec}")
    if count > 0:
        global timer
        timer = window.after(1000,countDown,count-1)
    else:
        startTimer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        check_label.config(text = marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)



canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timerText = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


text_label = Label(text="Timer",font=(FONT_NAME,40,"bold"),fg=GREEN,bg=YELLOW)
text_label.grid(column=1,row=0)

check_label = Label(font=(FONT_NAME,20,"bold"),fg=GREEN,bg=YELLOW)
check_label.grid(column=1,row=3)

start_button = Button(text="Start",command=startTimer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset", command=resetTimer)
reset_button.grid(column=2,row=2)

window.mainloop()
