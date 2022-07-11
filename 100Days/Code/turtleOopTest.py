from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

print(timmy_the_turtle)

myscreen = Screen()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("pink")
timmy_the_turtle.forward(100.0)
timmy_the_turtle.position()
print(myscreen.bgcolor)

myscreen.exitonclick()