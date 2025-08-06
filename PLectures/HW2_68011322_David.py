# HW1
numbers = []

for i in range(5):
    n = float(input(f"Please input a number: "))
    numbers.append(n)

sum  = sum(numbers)
average = sum/5

print(f"The summation of the all the numbers is {sum}")
print(f"The average of the numbers is {average}")

# HW2
import turtle as t 

# function for disabling drawing and going forward
def move(steps, left=0, right=0):
    t.penup()
    t.forward(steps)
    t.left(left)
    t.right(right)
    t.pendown()

# For drawing windows
def window(size):
    t.fillcolor("gray")
    t.begin_fill()
    t.circle(size)
    t.end_fill()
    t.left(90)
    move(size/2)
    t.fillcolor("light blue")
    t.begin_fill()
    t.right(90)
    t.circle(size/2)
    t.end_fill

t.speed(100)

#Screen size
t.Screen().setup(750, 750)
t.Screen().bgcolor('skyblue')
t.teleport(0, 0)

# Ears first layer
t.fillcolor("blue")
move(100, 90)
move(100)
t.begin_fill()
for i in range(2): #rectangle
    t.forward(100)
    t.left(90)
    t.forward(125)
    t.left(90)
t.end_fill()


# House structure (trapezoid)
t.teleport(0, 0)
t.right(90)
t.fillcolor("blue")
t.begin_fill()
print(t.pos())
t.forward(100)
t.left(95)
t.forward(300)
t.left(85)
t.forward(70)
t.left(85)
t.forward(300)
t.left(95)
t.forward(30)
t.end_fill()

# Door && lines on door && knob
move(10)
print(t.pos())
t.fillcolor("brown")
t.begin_fill()
t.left(90)
t.forward(50)
t.circle(-20, 180)
t.forward(50)
t.end_fill()
n = 0 
nn = 0
for i in range(3): # Lines on door
    t.teleport(0, 0)
    t.left(90)
    move(25 + n, 90)
    t.forward(65 + (5 * nn)) # Add 5 to height if the line is even
    t.right(180)
    n += 12
    nn += 1
    if nn == 2: nn = 0 # for every odd line, reset n to 0 to decrease the height
t.teleport(0, 0)
t.left(90)
move(50, 90)
move(30)
t.fillcolor("yellow")
t.begin_fill()
t.circle(3)
t.end_fill()


# Eyebrows
t.teleport(0, 0)
t.right(90)
move(100, 90)
move(220)
t.fillcolor("blue")
t.begin_fill()
for i in range(2): # rectangle
    t.forward(20)
    t.left(90)
    t.forward(125)
    t.left(90)
t.end_fill()

# Nose (also trapezoid)
t.teleport(18)
print(t.pos())
t.right(180)
move(100, 90)
move(5)
t.forward(40)
t.left(95)
t.forward(100)
t.left(85)
t.forward(28)
t.left(85)
t.forward(100)
t.left(95)
t.forward(12)

# Windows
t.teleport(10, 190)
window(18)
t.teleport(70, 190)
window(18)
t.teleport(0, 0)

t.hideturtle()
t.done()

