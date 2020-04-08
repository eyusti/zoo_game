import turtle

dinosaurs = {
    "triceratops": "trippy.gif",
    "stegosaurus": "steggy.gif",
    # "trex": "rex.gif",
}

#Background
turtle.title("Dinosaur Zoo")
screen = turtle.getscreen()
screen.setup(1000, 625)
screen.bgpic("grass.gif")
screen.delay(750)
screen.addshape(dinosaurs['triceratops'])
screen.addshape(dinosaurs['stegosaurus'])

#Make A dinosaur
def create_dino(dino_type):
    dino = turtle.Turtle()
    dino.shape(dinosaurs[dino_type])

dino_1 = create_dino('triceratops')
dino_2 = create_dino('stegosaurus')

#Dinosaur Movement
"""
def move_dino(dino):
    # dino.penup()
    dino.speed("slowest")
    while True:
        dino.backward(100)
        dino.left(90)
        dino.backward(100)
        dino.left(180)
        dino.backward(200)

move_dino(dino_1)
"""
input()