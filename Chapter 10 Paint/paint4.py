# adding different drawing shapes

# ------------------------------
# Imports
# ------------------------------

from guizero import App, Drawing, Combo, Slider


# ------------------------------
# Functions
# ------------------------------

def start(event):
    painting.last_event = event
    painting.first_event = event
    painting.last_shape = None
    
def draw(event):
    if shape.value == "line":
        painting.line(
            painting.last_event.x, painting.last_event.y,
            event.x, event.y,
            color=color.value,
            width=width.value
        )
    
    if shape.value == "rectangle":
        
        if painting.last_shape is not None:
            painting.delete(painting.last_shape)
        
        rectangle = painting.rectangle(
            painting.first_event.x, painting.first_event.y, 
            event.x, event.y, 
            color=color.value
        )

        painting.last_shape = rectangle

    painting.last_event = event


# ------------------------------
# App
# ------------------------------

app = App("Paint")

color = Combo(app, options=["black", "white", "red", "green", "blue"])
width = Slider(app, start=1, end=10)
shape = Combo(app, options=["line", "rectangle"])

painting = Drawing(app, width="fill", height="fill")

painting.when_left_button_pressed = start
painting.when_mouse_dragged = draw

app.display()
