from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pd.read_csv("words_to_learn.csv)")
except:
    data = pd.read_csv("data/ger_to_eng.csv", names=["sn", "word", "german", "plural"])
    del data["sn"]
finally:
    df_dic = data.to_dict("records")

rand_word = {}

def current_card():
    global rand_word,flip_timer
    window.after_cancel(flip_timer)
    rand_word = random.choice(df_dic)
    english_word = rand_word["word"]
    canvas.itemconfig(can_title, text="English", fill="black")
    canvas.itemconfig(can_text, text=english_word, fill="black")
    canvas.itemconfig(canvas_image, image=fg_image)
    flip_timer = window.after(3000, func=back_card)

def back_card():
    german_word = rand_word["german"]
    german_plural = rand_word["plural"]
    translation = f"{german_word}\n{german_plural}(Plural)"
    canvas.itemconfig(canvas_image, image=bg_image)
    canvas.itemconfig(can_title, text="German", fill="white", font=("Bell MT", 30, "italic"))
    canvas.itemconfig(can_text, text=translation, fill="white", font=("Cambria", 39, "bold"))

def remove_card():
    df_dic.remove(rand_word)
    current_card()
    data = pd.DataFrame(df_dic)
    data.to_csv("words_to_learn.csv", index=False)

window = Tk()
window.title("Flash App")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
window.grid()

flip_timer = window.after(3000, func=back_card)

canvas = Canvas(width=800, height=526)
fg_image = PhotoImage(file="images/card_front.png")
bg_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=fg_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
can_title = canvas.create_text(400, 150, text="", font=("Bell MT", 40, "italic"))
can_text = canvas.create_text(400, 263, text="", font=("Arial", 65, "bold"))
canvas.grid(row=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=current_card)
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=remove_card)
wrong_button.grid(row=1, column=0)



current_card()





window.mainloop()