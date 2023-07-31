from graphics_mine import *
from math import sqrt

def initial():
    win = GraphWin("Line Segment Information", 400,400)
    win.setCoords(-10.0, -10.0, 10.0, 10.0)
    win.setBackground("white")
    #Draw the horizontal line
    Line(Point(-10,0), Point(10,0)).draw(win)
    for i in range(-9,10,1):
        if i == 0:
            continue
        else:
            Text(Point(i, -0.50), f"{i}").draw(win)

    Line(Point(0,-10), Point(0, 10)).draw(win)
    for i in range(-9,10,1):
        if i == 0:
            continue
        else:
            Text(Point(0.50, i), f"{i}").draw(win)

    return win

def clicks(win):
    a = win.getMouse()
    b = win.getMouse()
    a_1 = a.getX()
    a_2 = a.getY()
    b_1 = b.getX()
    b_2 = b.getY()
    line = Line(Point(a_1,a_2), Point(b_1, b_2))
    line.setWidth(2)
    line.draw(win)
    #Draw the midpoint
    x = (a_1 + b_1)/2
    y = (a_2 + b_2)/2
    c = Circle(Point(x,y), 0.15)
    c.setFill("cyan")
    c.draw(win)
    #Inf about the slope and the lenght of line
    dx = b_1 - a_1
    dy = b_2 - a_2
    slope = dy/dx
    lenght = sqrt(dx**2 + dy**2)
    Text(Point(-5,-5), f"The slope is {round(slope,3)}").draw(win)
    Text(Point(-5,-8), f"The lengh is {round(lenght,3)}").draw(win)




def main(win):
    clicks(win)
    win.getMouse()
    win.close()


main(initial())