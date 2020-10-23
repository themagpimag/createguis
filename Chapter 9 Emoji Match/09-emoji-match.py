# ------------------------------
# Imports
# ------------------------------

import os
from random import shuffle, randint
from guizero import App, Box, Picture,  PushButton, Text


# ------------------------------
# Variables
# ------------------------------

# set the path to the emoji folder on your computer
emojis_dir = "emojis"
emojis = [os.path.join(emojis_dir, f) for f in os.listdir(emojis_dir)]
shuffle(emojis)


# ------------------------------
# Functions
# ------------------------------

def setup_round():
    for picture in pictures:
        picture.image = emojis.pop()

    for button in buttons:
        button.image = emojis.pop()
        button.update_command(match_emoji, args=[False])

    matched_emoji = emojis.pop()
    
    random_picture = randint(0,8)
    pictures[random_picture].image = matched_emoji
    
    random_button = randint(0,8)
    buttons[random_button].image = matched_emoji

    buttons[random_button].update_command(match_emoji, [True])

def match_emoji(matched):
    if matched:
        result.value = "correct"
        score.value = int(score.value) + 1
    else:
        result.value = "incorrect"
        score.value = int(score.value) - 1

    setup_round()

def reduce_time():
    timer.value = int(timer.value) - 1
    # is it game over?
    if int(timer.value) < 0:
        result.value = "Game over! Score = " + score.value
        # hide the game
        game_box.hide()


# ------------------------------
# App
# ------------------------------

app = App("emoji match")

game_box = Box(app, align="top")

top_box = Box(game_box, align="top", width="fill")
Text(top_box, align="left", text="Score ")
score = Text(top_box, text="4", align="left")
timer = Text(top_box, text="30", align="right")
Text(top_box, text="Time", align="right")

pictures_box = Box(game_box, layout="grid")
buttons_box = Box(game_box, layout="grid")

pictures = []
buttons = []

for x in range(0,3):
    for y in range(0,3):
        picture = Picture(pictures_box, grid=[x,y])
        pictures.append(picture)

        button = PushButton(buttons_box, grid=[x,y])
        buttons.append(button)

result = Text(app)

setup_round()

app.repeat(1000, reduce_time)

app.display()
