import turtle
import time
a = turtle.getscreen()
a.title("TrafficLight ")
a.bgcolor("black")
	
write= turtle.Turtle()
write.color("White")
write.width(3)
write.hideturtle()
write.penup()
write.goto(-30, 60)
write.pendown()
write.fd(60)
write.rt(90)
write.fd(120)
write.rt(90)
write.fd(60)
write.rt(90)
write.fd(120)
	

red_light =turtle.Turtle()
red_light.shape("circle")
red_light.color("Black")
red_light.penup()
red_light.goto(0, 40)
	
yellow_light =turtle.Turtle()
yellow_light.shape("circle")
yellow_light.color("Black")
yellow_light.penup()
yellow_light.goto(0, 0)
	
green_light =turtle.Turtle()
green_light.shape("circle")
green_light.color("Black")
green_light.penup()
green_light.goto(0,-40)
	


while (1):
            green_light.color("Black")
            yellow_light.color("Black")
            red_light.color("red")
            print("Stop -  Stop behind zebra cross..")
            print("Blink!!")
            time.sleep(2)
            print("Blink!!")


            red_light.color("Black")
            yellow_light.color("yellow")
            print("Move - You can go..")
            print("Blink!!")
            time.sleep(3)
            print("Blink!!")


            yellow_light.color("Black")
            green_light.color("green")
            print("Wait for Signal -  Ready to go..")
            print("Blink!!")
            time.sleep(1)
            print("Blink!!")
	

a.mainloop()
