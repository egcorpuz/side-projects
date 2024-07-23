from tkinter import *
import math

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


def reset_timer():
    # stop the timer
    window.after_cancel(timer)
    
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    global reps 
    reps = 0
    
    
def start_timer():
    global reps
    reps += 1
    work_sec = 25
    short_break_sec = 5
    long_break_sec = 20
    if reps % 8 == 0:
        timer_label.config(text="long\nbreak", fg=RED)
        count_down(long_break_sec * 60)
    elif reps % 2 == 0:
        timer_label.config(text="break", fg=PINK)
        count_down(short_break_sec * 60)
    else:
        timer_label.config(text="work", fg=GREEN)
        count_down(work_sec * 60)


def count_down(count):
    global timer
    # format in 00:00
    # 245 / 60 = 4 minutes rounded down
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{str(count_min)}"
    # 245 % 60 = seconds remainder
    count_sec = count % 60
    if count_sec == 0 or count_sec < 10:  # see dynamic typing for python
        count_sec = f"0{str(count_sec)}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)  # 1000ms
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            if len(marks) == 4:
                marks = ""
            marks += "✅"
        check_label.config(text=marks)
        

# create new window and give a background
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# use fg for coloring texts ie fg=GREEN

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # this has the same size as the image
# highlightthickness adjusts the borders of the canvas creates
tomato_img = PhotoImage(file="tomato.png")  # way to read through a file and to get hold of a particular 
# image at given location # provide relative or abosulute path
canvas.create_image(100, 112, image=tomato_img)  # positioning by half of width and height of the image
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))  # by trial and error, these figures place the counter right in the middle of the tomato
canvas.grid(row=1, column=1)

# Timer Label
timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

# Check Label
check_label = Label(font=(FONT_NAME, 18, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)

# Start button
start_button = Button(text="Start", bg=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

# Reset button
reset_button = Button(text="Reset", bg=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()

# TODO: DID Reset when 4 marks are achieved!
# TODO: Fix bug when start button is clicked again while timer is running
# TODO: When clicking start, it should turn the text to pause, and vice versa
# TODO: implement pause and unpause mechanism for the start button
# TODO: daily standup timer
