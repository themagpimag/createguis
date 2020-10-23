# drawing lines by tracking when the mouse is clicked

# ------------------------------
# Imports
# ------------------------------

from guizero import App, Drawing


# ------------------------------
# Functions
# ------------------------------

def start(event):
    painting.last_event = event

def draw(event):
    painting.line(
        painting.last_event.x, painting.last_event.y,
        event.x, event.y,
        color="black",
        width=3
    )

    painting.last_event = event


# ------------------------------
# App
# ------------------------------

app = App("Paint")

painting = Drawing(app, width="fill", height="fill")

painting.when_left_button_pressed = start
painting.when_mouse_dragged = draw

app.display()
