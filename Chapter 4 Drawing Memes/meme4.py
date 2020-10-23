# Imports ---------------

from guizero import App, TextBox, Drawing, Combo, Slider


# Functions -------------

def draw_meme():
    meme.clear()
    meme.image(0, 0, "woodpecker.png")
    meme.text(
        20, 20, top_text.value, 
        color=color.value,
        size=40, 
        font="courier")
    meme.text(
        20, 320, bottom_text.value,
        color=color.value,
        size=28,
        font="times new roman",
        )


# App -------------------

app = App("meme")

top_text = TextBox(app, "top text", command=draw_meme)
bottom_text = TextBox(app, "bottom text", command=draw_meme)

color = Combo(app,
              options=["black", "white", "red", "green", "blue", "orange"],
              command=draw_meme, selected="blue")

meme = Drawing(app, width="fill", height="fill")

draw_meme()

app.display()
