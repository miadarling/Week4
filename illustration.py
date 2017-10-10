  import turtle 

painter = turtle.Turtle()

painter.pencolor("red")
for i in range(50):
    painter.forward(50)
    painter.left(123) # Let's go counterclockwise this time 
    
painter.pencolor("orange")
for i in range(50):
    painter.forward(100)
    painter.left(123)
    
painter.pencolor("yellow")
for i in range(50):
    painter.forward(150)
    painter.left(123)
    
painter.pencolor("green")
for i in range(50):
    painter.forward(200)
    painter.left(123)
    
painter.pencolor("blue")
for i in range(50):
    painter.forward(250)
    painter.left(123)
    
painter.pencolor("purple")
for i in range(50):
    painter.forward(200)
    painter.left(123)
    
turtle.done()
