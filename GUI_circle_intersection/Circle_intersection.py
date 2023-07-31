from graphics_mine import *
from math import sqrt
def initial():
    win = GraphWin("Circle intersection",500,500)
    win.setCoords(-10, -10, 10, 10)
    win.setBackground("white")
    #initial window
    a = Text(Point(-5,7),"Radius").draw(win)
    b = Text(Point(-5,5), "Y-intercept").draw(win)
    a_i = Entry(Point(-2, 7), 3).draw(win)
    b_i = Entry(Point(-2, 5), 3).draw(win)
    c_i = Rectangle(Point(-2.5,-2.5), Point(2.5,2.5))
    c_i.setFill("yellow")
    c_i.draw(win)
    c = Text(Point(0,0), "Draw").draw(win)
    while True:
        user = win.getMouse()
        if -2.5 < user.getX() < 2.5 and -2.5 < user.getY() < 2.5:
            radius = eval(a_i.getText())
            y_int = eval(b_i.getText())
            #Cleaning the scene
            a.undraw()
            b.undraw()
            a_i.undraw()
            b_i.undraw()
            c.undraw()
            c_i.undraw()
            
            return radius, y_int, win

def circle():
    radius,y_int, win = initial()
    circle = Circle(Point(0,0), radius)
    circle.setFill("yellow")
    circle.draw(win)
    #Drawing the line with the given y
    line = Line(Point(-radius, y_int), Point(radius, y_int)).draw(win)
    x1 = sqrt(radius**2 - y_int**2)
    m = Circle(Point(x1,y_int), 0.10)
    m.setFill("red")
    m.draw(win)
    n = Circle(Point(-x1, y_int), 0.10)
    n.setFill("red")
    n.draw(win)
    Text(Point(-3,-9.5),f"{-x1} and {x1}").draw(win)

    return win

def graph(win):
    win = win
    #vertical line
    Line(Point(-10,0), Point(10, 0)).draw(win)
    for i in range(-9,10,2):
        Text(Point(0.5,i), f"{i}").draw(win)
    #horizontal line
    Line(Point(0, -10), Point(0, 10)).draw(win)
    for i in range(-9,10,2):
        Text(Point(i, -0.5), f"{i}").draw(win)

def main():
    win = circle()
    graph(win)
    #Closing the program 
    win.getMouse()
    win.close()
main()