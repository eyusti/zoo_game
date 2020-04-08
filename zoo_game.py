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
    print(x)
    print(y)
    dino.setposition(x,y)
    dino.showturtle()
    return dino

def move_dino(dino):
    dino.penup()
    dino.speed("slowest")
    movement = random.randint(0,4)
    distance = random.randint(200,300)
    print(movement)
    print(distance)
    if movement == 0:
        dino.forward(distance)
    elif movement == 1:
        dino.backward(distance)
    elif movement == 2:
        dino.setx(distance)
    elif movement == 3:
        dino.sety(distance)
    else:
        x = random.randint(-500,500)
        y = random.randint(-312,312)
        dino.goto(x,y)

# Testing execution
def main():
    dino_1 = create_dino('triceratops')
    dino_2 = create_dino('stegosaurus')
    screen.delay(750)
    while True:
        move_dino(dino_1)
        move_dino(dino_2)

if __name__ == "__main__":
    main()