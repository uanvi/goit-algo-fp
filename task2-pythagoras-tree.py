import turtle
import math

depth = 5

def draw_pythagoras_tree(t, length, angle, curr_depth):
    if curr_depth == 0:
        return

    if ((curr_depth/depth)*100 < 30):
        t.pencolor("green")
    
    t.forward(length)
    t.left(angle)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, 45, curr_depth - 1)
    t.right(2 * angle)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, 45, curr_depth - 1)
    t.left(angle)
    t.backward(length)

    t.pencolor("black")
    
def main():

    global depth 
    depth = int(input("Enter the depth of recursion (Example: 10): "))
    
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.left(90)
    t.pensize(2)

    draw_pythagoras_tree(t, 200, 45, depth)
    

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
