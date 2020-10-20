import turtle
import urllib.request
import time
turtle.speed(6)

#istiklal marşı ilk başlık ve ilk iki kıtası intenetten alınıyor
baglanti="https://raw.githubusercontent.com/ibrahim-kasalak/codeweek2020/main/istiklal_marsi.txt"
dosya = urllib.request.urlopen(baglanti)
mars=dosya.readlines()

#bayrak için uygun konuma gidiliyor
turtle.Screen().setup(800,600)
turtle.shape("turtle")
turtle.penup()
turtle.goto(-300,100)
turtle.pendown()
turtle.color("red")
#dikdörtgen
turtle.begin_fill()
for i in range(2):
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()
turtle.penup()
turtle.goto(-240,120)
turtle.color("white")
#hilal
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()
turtle.goto(-230,125)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()
turtle.penup()
turtle.goto(-220,145)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
#yıldız
for i in range(5):
    turtle.forward(30)
    turtle.left(144)
turtle.end_fill()

turtle.penup()
turtle.color("red")
turtle.goto(100,200)
#istiklal marşı yazılıyor
x,y=turtle.position()
for misra in mars:
    turtle.write(misra.decode("utf-8"), align="center", font=("Times New Roman",14,"italic"))
    time.sleep(1)
    y-=30
    turtle.goto(x,y)

turtle.hideturtle()
turtle.done()
turtle.mainloop()
