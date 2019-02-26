import tkinter as tk
import turtle
t = turtle.Pen()
t.speed(100)

            
def draw_a_square():
    for x in range (200):
                t.forward(x)
                t.left(91)
def make_it_blue():
    t.pencolor("blue")

def make_it_red():
    t.pencolor("red")


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

###color buttons
blue_button = tk.Button(frame, 
                   text="Blue", 
                   fg="blue",
                   command=make_it_blue)
blue_button.pack(side=tk.LEFT)
red_button = tk.Button(frame, 
                   text="Red", 
                   fg="red",
                   command=make_it_red)
red_button.pack(side=tk.LEFT)

###shape buttons
square_button = tk.Button(frame, 
                   text="Square", 
                   fg="green",
                   command=draw_a_square)
square_button.pack(side=tk.LEFT)


quit_button = tk.Button(frame,
                   text="Quit",
                   command=quit)
quit_button.pack(side=tk.LEFT)

root.mainloop()
