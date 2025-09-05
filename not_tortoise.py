import turtle as tt
from random import randint, choice
tt.speed(999999999999999999999999999999999999999999)
colours = []
colour_in = 0

def rect(width, height):
    for i in range(2):
        tt.forward(width)
        tt.right(90)
        tt.forward(height)
        tt.right(90)

def polygon(sides, sidelength):
    angle = ((sides - 2) * 180) / sides
    tt.begin_fill()
    for i in range(sides):
        tt.forward(sidelength)
        tt.right(180 - angle)
    tt.end_fill()

def star(diameter, points):
    tt.begin_fill()
    for i in range(int(points / 2)):
        tt.forward(diameter)
        tt.right(((points - 2) * 180) / points)
        tt.end_fill()

print("enter background colour (hex code, example #000000) (certain colour names are also valid)")
while True:
    try:
        bgc = input("> ")
        tt.bgcolor(bgc)
        break
    except Exception:
        print("try again.")

print("\n\n")

print("enter number of colours to use for shapes (integer)")
while True:
    try:
        col_num = int(input("> "))
        break
    except Exception:
        print("try again.")

print("\n\n")

for i in range(col_num):
    print(f"enter colour number {i + 1} (hex code, example #000000) (certain colour names are also valid)")
    while True:
        try:
            colour = input("> ")
            tt.bgcolor(colour)
            print("don't worry, that's just testing that the colour's valid. the background will be set back to the colour you picked before.")
            colours.append(colour)
            break
        except Exception:
            print("try again.")

print("\n\n")

print("enter number of shapes (integer) (larger numbers will take longer to generate)")
while True:
    try:
        num_shapes = int(input("> "))
        break
    except Exception:
        print("try again.")

tt.bgcolor(bgc)
for i in range(1, num_shapes + 1):
    tt.color(colours[colour_in])
    tt.fillcolor(colours[colour_in])
    try:
        polygon(num_shapes - i, 100)
    except ZeroDivisionError:
        break
    tt.home()
    tt.left(180)
    polygon(num_shapes - i, 100)
    tt.home()
    colour_in += 1
    if colour_in >= len(colours):
        colour_in = 0
tt.penup()
tt.forward(9999)

print("would you like to save this image? y/n")
while True:
    save = input("> ")
    if save.upper() in ["Y", "YES"]:
        print("name the file.")
        name = input("> ")
        tt.getcanvas().postscript(file = f"{name}.png")
        break
    elif save.upper() in ["N", "NO"]:
        print("ok.")
        break
    else:
        print("what?")