"""
This is a program which displays Analog Clock.
Name: Muluken Hakim
ID: UGR/1110/12
Section:1
"""
import turtle
import time
Mule=turtle.Turtle()
Mule.hideturtle()

background=turtle.Turtle()
background=turtle.Screen()
background.bgcolor("gold")
background.tracer(0)

Mule.hideturtle()
# x and y are the coordinates of x and y axis
def draw_circle(x,y,size,radius,color1,color2):
	
	Mule.up()
	Mule.pensize(size)
	Mule.up()
	Mule.goto(x,y)
	Mule.begin_fill()
	Mule.fillcolor(color1)
	Mule.pencolor(color2)
	Mule.down()
	Mule.circle(radius)
	Mule.end_fill()
	Mule.up()
	Mule.goto(0,0)
	
def draw_clock(hour,minute,second, Mule):
	
	angle=0
	for i in range(60):
		angle +=6
		if angle%30==0:
			Mule.setheading(angle)
			Mule.up()
			Mule.forward(260)
			Mule.down()
			Mule.pencolor("black")
			Mule.pensize(10)
			Mule.backward(40)
			Mule.up()
			Mule.goto(0,0)
		else:
			Mule.setheading(angle)
			Mule.forward(260)
			Mule.down()
			Mule.pencolor("black")
			Mule.pensize(2)
			Mule.backward(20)
			Mule.up()
			Mule.goto(0,0)
	
	Mule.up()
	Mule.goto(0,0)		
	angle = hour * 30
	Mule.setheading(90)
	Mule.pensize(15)
	Mule.pencolor("black")
	Mule.right(angle)
	Mule.down()
	Mule.forward(110)
	
	Mule.up()
	Mule.goto(0,0)
	angle=minute * 6
	Mule.setheading(90)
	Mule.pensize(5)
	Mule.pencolor("blue")
	Mule.right(angle)
	Mule.down()
	Mule.forward(160)
	
	Mule.up()
	Mule.goto(0,0)
	angle=second * 6
	Mule.setheading(90)
	Mule.pensize(1)
	Mule.pencolor("red")
	Mule.right(angle)
	Mule.down()
	Mule.forward(200)
	Mule.up()
	Mule.goto(0,0)
	
	Mule.up()
	Mule.goto(-200,500)
	Mule.down()
	Mule.pensize(25)
	Mule.pencolor("black")
	Mule.write(" Drawn by:   Muluken Hakim  ")
	Mule.up()
	Mule.home()
Mule.hideturtle()
while True:
	hour=int(time.strftime("%I"))
	minute=int(time.strftime("%M"))
	second=int(time.strftime("%S"))
	
	draw_circle(0,-300,50,300,"white","orange")
	draw_clock(hour,minute,second, Mule)
	background.update()
	time.sleep(0)
	Mule.clear()

Mule.hideturtle()
turtle.done()