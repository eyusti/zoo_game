import turtle
import random

# Available Sprites
dinosaurs = {
    "triceratops": "trippy.gif",
    "stegosaurus": "steggy.gif",
}

# Main Screen Settings
width = 1000
height = 624
main_screen = turtle.Screen()
main_screen.title("Dinosaur Zoo")
main_screen.setup(width, height)
main_screen.bgpic("grass.gif")

main_screen.addshape(dinosaurs['triceratops'])
main_screen.addshape('trippy_heart.gif')
main_screen.addshape(dinosaurs['stegosaurus'])
main_screen.addshape('steggy_heart.gif')
main_screen.addshape('egg.gif')
main_screen.addshape('egg_crack.gif')

clicks = 0

# Game Functions
def get_dino_clicked(x,y):
    global clicks 
    clicks += 1
    print("click registered")
    lowest_diff = 10000000000
    current_dino = None
    for dino in all_dinos.keys():
        diff = 0
        diff += abs(x-dino.xcor())
        diff += abs(y-dino.ycor())
        if diff < lowest_diff:
            current_dino = dino
            lowest_diff = diff
    return current_dino

def generate_random_dinosaur():
    random_dinosaur = random.choice(list(dinosaurs.keys()))
    return random_dinosaur

def move_handler(x,y):
    dino = get_dino_clicked(x,y)
    move_dino(dino)

def heart_handler(x,y):
    dino = get_dino_clicked(x,y)
    main_screen.delay(500)
    if all_dinos[dino] == 'stegosaurus':
        dino.shape("steggy_heart.gif")
        dino.shape("steggy.gif")
    if all_dinos[dino] == 'triceratops':
        dino.shape("trippy_heart.gif")
        dino.shape("trippy.gif")
    main_screen.delay(0)

def egg_handler():
    global clicks

    if clicks > 5:
        egg_appears()
        clicks = 0

    main_screen.ontimer(egg_handler, 100)

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
    movement = random.randint(0,4)
    distance = random.randint(200,400)
    #dino.speed("slowest")
    main_screen.delay(500)
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

    main_screen.delay(0)

# Egg Functions
def egg_appears():
    egg = turtle.Turtle(shape="egg.gif", visible=False)
    egg.penup()
    x = random.randint(-width/2,width/2)
    y = random.randint(-height/2,height/2)
    egg.setposition(x,y)
    egg.showturtle()
    pass

# Testing execution
all_dinos = {}
random_dinosaur = generate_random_dinosaur()
all_dinos[create_dino(random_dinosaur)] = random_dinosaur

for dino in all_dinos.keys():
    dino.onclick(move_handler,1)
    dino.onclick(heart_handler,2)

main_screen.ontimer(egg_handler,100)

turtle.listen()
turtle.mainloop()
