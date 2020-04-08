import turtle
import random

# Available Sprites
dinosaurs = {
    "triceratops": "trippy.gif",
    "stegosaurus": "steggy.gif",
}

# Screen Settings
screen = turtle.Screen()
screen.title("Dinosaur Zoo")
screen.setup(1000, 624)
screen.bgpic("grass.gif")
screen.addshape(dinosaurs['triceratops'])
screen.addshape(dinosaurs['stegosaurus'])

# Dinosaur Functions
def create_dino(dino_type):
    dino = turtle.Turtle(shape=dinosaurs[dino_type], visible=False)
    dino.penup()
    x = random.randint(-500,500)
    y = random.randint(-312,312)
    dino.setposition(x,y)
    dino.showturtle()
    return dino

def move_dino(dino):
    dino.penup()
    dino.speed("slowest")
    while True:
        dino.fd(100)
        dino.lt(90)
        dino.fd(100)
        dino.lt(180)
        dino.fd(200)

# Testing execution
def main():
    dino_1 = create_dino('triceratops')
    screen.delay(750)
    #dino_2 = create_dino('stegosaurus')
    move_dino(dino_1)

if __name__ == "__main__":
    main()