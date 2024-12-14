#0,0 to 199,199

#Simple testing window
from graphics import *
win = GraphWin("Graphic Window")
p1 = Point(50, 60)
p1.draw(win)
p2 = Point(150, 160)
p2.draw(win)

win.getMouse()
win.close()


#Red Circle, Line, oval, square
from graphics import *
win = GraphWin("Shapes")

cir = Circle(Point(100, 100), 30)
cir.setFill("red")
cir.draw(win)

label = Text(Point(100, 100), "Red Circle")
label.draw(win)

rectangle = Rectangle(Point(30,30), Point(90,90))
rectangle.draw(win)

line = Line(Point(0,0), Point(199,199))
line.draw(win)

oval = Oval(Point(20, 150), Point(180, 190))
oval.draw(win)

win.getMouse()
win.close()



#draw eye, note mouse coordinate
from graphics import *
win = GraphWin("eyes")

leftEye = Circle(Point(80,50), 5)
leftEye.setFill('white')
leftEye.setOutline('black')
leftEye.draw(win)

rightEye = leftEye.clone()# using clone method
rightEye.move(20,0)
rightEye.draw(win)

points = win.getMouse()
print(points.getX(), points.getY())
win.close()



#get points from user's mouseclicks and draw traingle
from graphics import *
win = GraphWin("Draw Triangle using points", 300, 300)

message = Text(Point(80, 250), "Click on three points")
message.draw(win)

p1 = win.getMouse()
p2 = win.getMouse()
p3 = win.getMouse()
p1.draw(win)
p2.draw(win)
p3.draw(win)

triangle = Polygon(p1, p2, p3)
triangle.setFill("brown")
triangle.setOutline("blue")
triangle.draw(win)

message.setText("Click anywhere to quit.")
win.getMouse()
win.close()




#Q
#Program to convert Celsius to Fahrenheit using a simple graphical interface.
from graphics import *
win = GraphWin("Celsius to Fahreneheit", 300, 300)

Text(Point(100, 100), "Celsius: ").draw(win)
Text(Point(100, 200), "Fahrenheit: ").draw(win)

input = Entry(Point(180, 100), 5)
input.setText("0.0")
input.draw(win)

output = Text(Point(180,200), "")
output.draw(win)

button = Text(Point(150, 150), "Convert It")
button.draw(win)

Rectangle(Point(100, 125), Point(200, 175)).draw(win)

win.getMouse()

celsius = int(input.getText())
fahrenheit = 9.0/5.0 * celsius + 32

output.setText(fahrenheit)
button.setText("Quit")

win.getMouse()
win.close()