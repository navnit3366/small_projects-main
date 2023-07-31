from graphics_mine import *
class Door:
    def __init__(self,win,point1,point2,colour,number):
        self.win = win
        self.point1 = point1
        self.point2 = point2
        self.colour = colour
        x1 = self.point2.getX() - 0.5
        x = x1 - 0.5
        y1 = self.point2.getY() - 2
        y = y1 - 0.5
        self.p1 = Point(x, y)
        self.p2 = Point(x1, y1)
        self.num = number
    
    def text(self):
        self.x = (self.point1.getX() + self.point2.getX())/2 
        self.y = 9.25
        num = Text(Point(self.x,self.y),f"Door {self.num}")
        return num

    def get_pos(self):
        return self.point1, self.point2

    def get_door(self):
        return self.num
        
    def clicked(self,p):
        return (self.point1.getX() <= p.getX() <= self.point2.getX() and self.point1.getY() <= p.getY() <= self.point2.getY())
        
    def draw(self):
        door = Rectangle(self.point1, self.point2)
        door.setFill(self.colour)
        square = Rectangle(self.p1, self.p2)
        square.setFill("yellow")
        n = self.text()
        door.draw(self.win)
        square.draw(self.win)
        n.draw(self.win)
        return door



        

