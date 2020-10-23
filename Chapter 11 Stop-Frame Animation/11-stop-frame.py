# Imports ---------------

from guizero import App, Picture, PushButton, Text, Slider, Box
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
            append_images=frames[1:],
            duration=duration.value)
        viewer.image = "animation.gif"
    else:
        viewer.hide()

def delete_frame():
    if len(frames) > 0:
        frames.pop()
        total_frames.value = len(frames)

    save_animation()


# Variables -------------

frames = []

camera = PiCamera(resolution="400x400")


# App -------------------

app = App(title="Stop frame animation")

controls = Box(app, align="top")
total_frames = Text(controls, text="0", align="left")
take_next_picture = PushButton(controls, align="left", text="Take picture", command=capture_image)
delete_last_picture = PushButton(controls, align="left", text="Delete last", command=delete_frame)
Text(controls, align="left", text="Duration")
duration = Slider(controls, align="left", start=100, end=1000, command=save_animation)

viewer = Picture(app)

app.display()
