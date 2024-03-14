import turtle
tw= turtle.Turtle()
tw.screen.bgcolor("black")
tw.pensize(2)
tw.color("green")
tw.left(90)
tw.speed(600000)
tw.shape("turtle")

def tree(i):
    if i<10:
        return
    else:
        tw.forward(i)
        tw.color("orange")
        tw.circle(2)
        tw.color("brown")
        tw.left(30)
        tree(3*i/4)
        tw.right(60)
        tree(3*i/4)
        tw.left(30)
        tw.backward(1)

tree(10)
turtle.done
