# Imports ---------------

from guizero import App, Text, Waffle


# Variables -------------


# Functions -------------


# App -------------------

app = App("Destroy the dots")

instructions = Text(app, text="Click the dots to destroy them")
board = Waffle(app, width=5, height=5)

app.display()
