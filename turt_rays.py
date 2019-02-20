import turtle
t = turtle.Pen()
t.speed(100)
def left_spiral():
        for x in range (200):
                t.pencolor("green")
                t.forward(x)
                t.left(91)

def right_spiral():
        for x in range (200):
                t.pencolor("red")
                t.forward(x)
                t.right(91)

def left_triangle():
        for x in range (200):
                t.pencolor("blue")
                t.forward(x)
                t.right(119)
def right_triangle():
        for x in range (200):
                t.pencolor("purple")
                t.forward(x)
                t.right(121)
while True:
        drawing = input("""Pick a number between
        1 and 4""")
        if drawing == "1":
                left_spiral()
        if drawing == "2":
                right_spiral()
        if drawing == "3":
                left_triangle()
        if drawing == "4":
                right_triangle()
