# Imports ---------------

from guizero import App, Picture, PushButton
from picamera import PiCamera


# Functions -------------

def capture_image():
    camera.capture("frame.jpg")
    viewer.image = "frame.jpg"


# App -------------------

app = App(title="Stop frame animation")

camera = PiCamera(resolution="400x400")
take_next_picture = PushButton(app, text="Take picture", command=capture_image)
viewer = Picture(app)

app.display()
