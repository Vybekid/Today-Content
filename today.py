import turtle

screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.left(90)  
t.penup()
t.backward(250) 
t.pendown()

def draw_fractal_tree(branch_length, pen):
    if branch_length > 5:
        if branch_length < 20:
            pen.pencolor("green") 
        elif branch_length < 50:
            pen.pencolor("#966F33")
        else:
            pen.pencolor("#654321") 

        pen.pensize(branch_length / 10)
        pen.forward(branch_length)
        
        pen.right(25)
        draw_fractal_tree(branch_length - 15, pen)
        
        pen.left(50)
        draw_fractal_tree(branch_length - 15, pen)
        
        pen.right(25)
        pen.penup()
        pen.backward(branch_length)
        pen.pendown()

draw_fractal_tree(100, t)
screen.done()