import turtle
import random

print('WELCOME TO THE TURTLE RACE')
print('CHOOSE YOUR COLOUR TURTLE')
print('PRESS SPACEBAR TO START THE RACE')

#screen_graphics
s=turtle.Screen()
s.bgcolor('LightSalmon')
turtle.penup()
turtle.setpos(-140,240)
turtle.color('turquoise')
turtle.write('TURTLE RACE',font=('Arial',30,'bold'))
turtle.setpos(-200,-250)
turtle.color('olive')
turtle.write('CHOOSE YOUR COLOR AND',font=('Arial',20,'bold'))
turtle.setpos(-200,-280)
turtle.write('PRESS SPACEBAR TO START',font=('Arial',20,'bold'))
turtle.hideturtle()
x=-250
for I in range(6):
    turtle.setpos(x,-210)
    turtle.pendown()
    turtle.pensize(10)
    turtle.color('white')
    turtle.setheading(90)
    turtle.speed(0)
    turtle.forward(400)
    turtle.penup()
    x=x+100

#finish_line
turtle.color('black')
turtle.shape('square')
turtle.shapesize(15/20)
turtle.penup()

x=-240
for I in range(17):
    turtle.setpos(x,200)
    turtle.stamp()
    x=x+30

turtle.color('white')
x=-225
for I in range(16):
    turtle.setpos(x,215)
    turtle.stamp()
    x=x+30

#player1
a=turtle.Turtle()
a.shape('turtle')
a.penup()
a.setpos(-200,-200)
a.pendown()
a.color('red')
a.setheading(90)

#player2
b=turtle.Turtle()
b.shape('turtle')
b.penup()
b.setpos(-100,-200)
b.pendown()
b.color('yellow')
b.setheading(90)

#player3
e=turtle.Turtle()
e.shape('turtle')
e.penup()
e.setpos(0,-200)
e.pendown()
e.color('green')
e.setheading(90)

#player4
c=turtle.Turtle()
c.shape('turtle')
c.penup()
c.setpos(100,-200)
c.pendown()
c.color('magenta')
c.setheading(90)

#player5
d=turtle.Turtle()
d.shape('turtle')
d.penup()
d.setpos(200,-200)
d.pendown()
d.color('blue')
d.setheading(90)

#moving_the_turtles
def up():
    a_dist,b_dist,e_dist,c_dist,d_dist=0,0,0,0,0
    for I in range(120):
        x=(random.randint(1,5))
        a_dist+=x
        y=(random.randint(1,5))
        b_dist+=y
        z=(random.randint(1,5))
        e_dist+=z
        w=(random.randint(1,5))
        c_dist+=w
        q=(random.randint(1,5))
        d_dist+=q
        a.forward(x)
        b.forward(y)
        e.forward(z)
        c.forward(w)
        d.forward(q)
    #winner_of_the_race
    print('AND THE WINNERS ARE :-')
    Distance=[a_dist,b_dist,e_dist,c_dist,d_dist]
    for I in range(1,6):
        L=Distance.index(max(Distance))
        if L==0:
            print(I,'POSITION- RED TURTLE')
        elif L==1:
            print(I,'POSITION- YELLOW TURTLE')
        elif L==2:
            print(I,'POSITION- GREEN TURTLE')
        elif L==3:
            print(I,'POSITION- MAGENTA TURTLE')
        elif L==4:
            print(I,'POSITION- BLUE TURTLE')
        Distance[L]=0
turtle.listen()
turtle.onkey(up,"space")
turtle.hideturtle()

    
      




    
