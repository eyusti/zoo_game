import turtle
import random
import tkinter as tk
from PIL import ImageTk,Image

# Globals
clicks = 0 # get_dino_clicked
all_dinos = {} # egg_hatches
all_eggs = [] # egg_appears

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

# Game Functions

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

def hatch_handler():
    if all_eggs:
        egg_hatches()
    main_screen.ontimer(hatch_handler,60000)

def refresh_onclick_settings():
    for dino in all_dinos.keys():
        dino.onclick(move_handler,1)
        dino.onclick(heart_handler,2)

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

def get_dino_clicked(x,y):
    global clicks 
    clicks += 1
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

# Egg Functions
def egg_appears():
    global all_eggs

    egg = turtle.Turtle(shape="egg.gif", visible=False)
    all_eggs.append(egg)
    egg.penup()
    x = random.randint(-width/2,width/2)
    y = random.randint(-height/2,height/2)
    egg.setposition(x,y)
    egg.showturtle()

def egg_hatches():
    global all_dinos

    main_screen.delay(500)
    hatching_egg = all_eggs.pop()
    hatching_egg.shape("egg_crack.gif")
    random_dinosaur = generate_random_dinosaur()
    hatching_egg.shape(dinosaurs[random_dinosaur])
    all_dinos[hatching_egg] = random_dinosaur
    refresh_onclick_settings()

# Game Execution
starter_dinosaur = generate_random_dinosaur()
all_dinos[create_dino(starter_dinosaur)] = starter_dinosaur
refresh_onclick_settings()
main_screen.ontimer(egg_handler,100)
main_screen.ontimer(hatch_handler,60000)

# Needs to get moved into method
lastx, lasty = 0, 0
color = "black"

def setColor(newcolor):
    global color
    color = newcolor

def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def addLine(event):
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y), fill=color)
    lastx, lasty = event.x, event.y

window = tk.Tk()
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

canvas = tk.Canvas(master = window, width = 500, height = 500)
canvas.grid(column=0, row=0, sticky=("n", "w", "e", "s"))
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)

background_image = tk.PhotoImage(master = window, file = "crack.gif", name = "egg_test")
background_dino = tk.Label(master = window, image = background_image)
background_dino.place(relx=0.5, rely=0.5, anchor="center")
background_dino.image = background_image

id = canvas.create_rectangle((10, 10, 30, 30), fill="red")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("red"))
id = canvas.create_rectangle((10, 35, 30, 55), fill="yellow")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("yellow"))
id = canvas.create_rectangle((10, 60, 30, 80), fill="green")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("green"))
id = canvas.create_rectangle((10, 85, 30, 105), fill="blue")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("blue"))
id = canvas.create_rectangle((10, 110, 30, 130), fill="magenta")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("magenta"))
id = canvas.create_rectangle((10, 135, 30, 155), fill="white")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("white"))
id = canvas.create_rectangle((10, 160, 30, 180), fill="black")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("black"))	

'''
TURTLE VERSION PROBABLY DELETE
cursor = turtle.RawTurtle(canvas)
cursor.speed(-1)
canvas.pack()

def drag(x,y):
    cursor.ondrag(None)
    cursor.setheading(cursor.towards(x,y))
    cursor.goto(x,y)
    cursor.ondrag(drag)

cursor.ondrag(drag)
'''
# END MOVE TO METHOD

turtle.listen()
turtle.mainloop()
