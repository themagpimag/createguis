# Imports ---------------

from guizero import App, Text


# Functions -------------

def flash_text():
    if title.visible:
        title.hide()
    else:
        title.show()


# App -------------------

app = App("its all gone wrong", bg="dark green")

title = Text(app, text="Hard to read", size="14", font="Comic Sans", color="green")

app.repeat(1000, flash_text)

app.display()
