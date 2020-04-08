import turtle
import random

# Available Sprites
dinosaurs = {
    "triceratops": "trippy.gif",
    "stegosaurus": "steggy.gif",
}

# Screen Settings
width = 1000
height = 624
screen = turtle.Screen()
screen.title("Dinosaur Zoo")
screen.setup(width, height)
screen.bgpic("grass.gif")
screen.addshape(dinosaurs['triceratops'])
screen.addshape(dinosaurs['stegosaurus'])

# Dinosaur Functions
def create_dino(dino_type):
    dino = turtle.Turtle(shape=dinosaurs[dino_type], visible=False)
    dino.penup()
    x = random.randint(-width/2,width/2)
    y = random.randint(-height/2,height/2)
    dino.setposition(x,y)
    dino.showturtle()
    return dino

def move_dino(dino):
    dino.penup()
    dino.speed("slowest")
    movement = random.randint(0,4)
    distance = random.randint(200,400)
    if movement == 0:
        if dino.xcor() + distance < width/2:
            dino.forward(distance)
        else:
            dino.forward(distance + (width/2 -(dino.xcor() + distance)))
    elif movement == 1:
        if dino.xcor() - distance > -width/2:
            dino.backward(distance)
        else:
            dino.backward(distance + (width/2 + (dino.xcor() - distance)))
    elif movement == 2:
        if dino.ycor() - distance > -height/2:
            dino.sety(-distance)
        else:
            dino.sety(-distance - ((dino.ycor() - distance)+ height/2))
    elif movement == 3:
        if dino.ycor() + distance < height/2:
            dino.sety(distance)
        else:
            dino.sety(distance - ((dino.ycor() + distance) - height/2))
    else:
        x = random.randint(-width/2,width/2)
        y = random.randint(-height/2,height/2)
        dino.goto(x,y)

# Testing execution
def main():
    dino_1 = create_dino('triceratops')
    dino_2 = create_dino('stegosaurus')
    #screen.delay(750)
    while True:
        move_dino(dino_1)
        move_dino(dino_2)

if __name__ == "__main__":
    main()