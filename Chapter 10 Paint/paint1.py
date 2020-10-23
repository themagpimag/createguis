# simple paint app, just draw dots 

# ------------------------------
# Imports
# ------------------------------

from guizero import App, Drawing



# ------------------------------
# Functions
# ------------------------------

def draw(event):
    painting.oval(
        event.x - 1, event.y - 1,
        event.x + 1, event.y + 1,
        color="black")


# ------------------------------
# App
# ------------------------------

app = App("Paint")

painting = Drawing(app, width="fill", height="fill")

painting.when_mouse_dragged = draw

app.display()
