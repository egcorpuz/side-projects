from tkinter import *
from tkinter import messagebox
import pandas as pd
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
random_word = {}

ceb_df = pd.read_csv("./data/ceb_words.csv")
ceb_list = ceb_df.to_dict(orient="records")  # creates a list of dictionary


def reset_play():
    global ceb_list
    os.remove('./data/words_to_learn.csv')
    ceb_list = ceb_df.to_dict(orient="records")
    next_card()


def check_save():
    global ceb_list
    ceb_list.remove(random_word)
    if len(ceb_list) == 0:
        is_ok = messagebox.askokcancel(title="Yay!", message="Congratulations!\n"
                                                             "You have completed the challenge.\n"
                                                             "Click ok to close.\n"
                                                             "Click cancel to restart game.")
        if is_ok:
            window.destroy()
        else:
            os.remove('./data/words_to_learn.csv')
            ceb_list = ceb_df.to_dict(orient="records")
    else:
        df = pd.DataFrame(ceb_list)
        df.to_csv('./data/words_to_learn.csv', index=False)  # does not add index numbers 
        next_card()


def flip_card():
    canvas.itemconfig(flash_card, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=random_word["English"], fill="white")


def next_card():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    try:
        with open('./data/words_to_learn.csv'):
            pass
    except FileNotFoundError:
        random_word = random.choice(ceb_list)
    else:
        to_learn_df = pd.read_csv("./data/words_to_learn.csv")
        to_learn_list = to_learn_df.to_dict(orient="records")
        random_word = random.choice(to_learn_list)
    finally:
        canvas.itemconfig(flash_card, image=card_front_img)
        canvas.itemconfig(title_text, text="Cebuano", fill="black")
        canvas.itemconfig(word_text, text=random_word["Cebuano"], fill="black")
        flip_timer = window.after(3000, func=flip_card)


# -------------------- UI/UX SETUP --------------------- #
window = Tk()
window.title("Cebuano Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
flash_card = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=3)

# buttons
x_img = PhotoImage(file="./images/wrong.png")
x_button = Button(image=x_img, highlightthickness=0, command=next_card)
x_button.grid(row=1, column=0)

check_img = PhotoImage(file="./images/right.png")
check_button = Button(image=check_img, highlightthickness=0, command=check_save)
check_button.grid(row=1, column=2)

reload_img = PhotoImage(file="./images/reload.png")
reset_button = Button(image=reload_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=reset_play)
reset_button.grid(row=1, column=1)


next_card()

window.mainloop()
