# Imports ---------------

from guizero import App, Picture, PushButton, Text
from picamera import PiCamera
from PIL import Image


# Functions -------------

def capture_image():
    camera.capture("frame.jpg")
    viewer.image = "frame.jpg"

    frame = Image.open("frame.jpg")
    frames.append(frame)
    total_frames.value = len(frames)

    save_animation()

def save_animation():
    if len(frames) > 0:
        viewer.show()
        frames[0].save(
            "animation.gif",
            save_all=True,
            append_images=frames[1:])
        viewer.image = "animation.gif"
    else:
        viewer.hide()


# Variables -------------

frames = []

camera = PiCamera(resolution="400x400")


# App -------------------

app = App(title="Stop frame animation")

total_frames = Text(app, text="0")
take_next_picture = PushButton(app, text="Take picture", command=capture_image)

viewer = Picture(app)

app.display()
