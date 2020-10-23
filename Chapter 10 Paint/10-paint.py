# styled up

# ------------------------------
# Imports
# ------------------------------

from guizero import App, Drawing, Combo, Slider, Box, Text


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

    else: 
        if painting.last_shape is not None:
                painting.delete(painting.last_shape)

        if shape.value == "rectangle":
            
            painting.last_shape = painting.rectangle(
                painting.first_event.x, painting.first_event.y, 
                event.x, event.y, 
                color=color.value
            )

        if shape.value == "oval":
            
            painting.last_shape = painting.oval(
                painting.first_event.x, painting.first_event.y, 
                event.x, event.y, 
                color=color.value
            )

    painting.last_event = event


# ------------------------------
# App
# ------------------------------

app = App("Paint")
app.font = "impact"

tools = Box(app, align="top", width="fill", border=True)

Text(tools, text="Tool", align="left")
shape = Combo(tools, options=["line", "rectangle", "oval"], align="left")

Text(tools, text="Colour", align="left")
color = Combo(tools, options=["black", "white", "red", "green", "blue"], align="left")

Text(tools, text="Width", align="left")
width = Slider(tools, start=1, end=10, align="left")

painting = Drawing(app, width="fill", height="fill")

painting.when_left_button_pressed = start
painting.when_mouse_dragged = draw

app.display()
