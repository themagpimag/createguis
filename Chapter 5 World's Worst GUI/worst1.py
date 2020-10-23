# Imports ---------------

from guizero import App, Text


# App -------------------

app = App("its all gone wrong", bg="dark green")

title = Text(app, text="Hard to read", size="14", font="Comic Sans", color="green")

app.display()
