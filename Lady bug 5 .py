import turtle as trtl


ladybug = trtl.Turtle()
ladybug.speed(0)

ladybug.pensize(40)
ladybug.color("black")
ladybug.circle(5)

ladybug.penup()
ladybug.goto(0, -55)
ladybug.pendown()
ladybug.color("red")
ladybug.pensize(40)
ladybug.circle(20)

ladybug.penup()
ladybug.goto(0, 5)
ladybug.setheading(270)
ladybug.pendown()
ladybug.color("black")
ladybug.pensize(2)
ladybug.forward(75)

ladybug.penup()
ladybug.pensize(10)
ladybug.color("black")


ladybug.goto(-20, -40)
ladybug.pendown()
ladybug.circle(3)


ladybug.penup()
ladybug.goto(20, -40)
ladybug.pendown()
ladybug.circle(3)

ladybug.hideturtle()


wn = trtl.Screen()
wn.mainloop()
