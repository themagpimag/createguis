# Imports ---------------

from guizero import App, Slider, Text
from time import ctime


# Functions -------------

def update_date():
    the_date.value = ctime(date_slider.value)


# App -------------------

app = App("Set the date with the slider")
the_date = Text(app)
date_slider = Slider(app, start=0, end=999999999, command=update_date)

app.display()
