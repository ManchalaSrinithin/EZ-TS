Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
s=turtle.Turtle()
s.forward(100)
s.clear()
s.reset()
for i in range(4):
    s.forward(100)
    s.right(90)

turtle.bgcolor("black")
s.color("white")
s.circle(100)

s.reset()
s.clear()
for i in range(100):
    s.circle(100)
    s.circle(105)
    s.circle(115)
    s.circle(120)
    s.right(45)

