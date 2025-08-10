# # Q1
# import turtle as t

# x0, y0, x1, y1, x2, y2 = map(int, input("Enter x & y for the three points (p0, p1, p2): ").split(";"))

# p0 = (x0, y0)
# p1 = (x1, y1)
# p2 = (x2, y2)

# # multiplies the inputed points as vectors
# crossProduct = (x1 - x0) * (y2 - y0) - (y1 - y0) * (x2 - x0)

# if crossProduct > 0:
#     print("P2 is to the left the line")
# elif crossProduct < 0:
#     print("P2 is to the right of the line")
# else:
#     print("P2 is on the line")

# t.penup()
# t.goto(p0)
# t.write("P0", align="center")
# t.pendown()
# t.goto(p1)
# t.write("P1", align="center")
# t.penup()
# t.goto(p2)
# t.write("P2", align="center")
# t.pendown()
# t.hideturtle()
# t.done()

# Q2
import turtle as t

x1, y1, x2, y2 = map(int, input("Enter the center coordinates of the rectangles (x1;y1;x2;y2): ").split(";"))
w1, h1, w2, h2 = map(int, input("Enter width & height for the 2 rectangles (w1;h1;w2;h2): ").split(";"))

rightX1 = x1 + w1 / 2
leftX1 = x1 - w1 / 2
rightX2 = x2 + w2 / 2
leftX2 = x2 - w2 / 2

topX1 = y1 + h1 / 2
bottomX1 = y1 - h1 / 2
topX2 = y2 + h2 / 2
bottomX2 = y2 - h2 / 2

if rightX1 <= leftX2 or rightX2 <= leftX1 or \
    topX1 <= bottomX2 or topX2 <= bottomX1:
    print("The rectangles do not overlap")
elif rightX1 <= rightX2 and leftX1 >= leftX2 and \
     topX1 <= topX2 and bottomX1 >= bottomX2:
    print("Rectangle 1 is inside Rectangle 2")
elif rightX2 <= rightX1 and leftX2 >= leftX1 and \
     topX2 <= topX1 and bottomX2 >= bottomX1:
    print("Rectangle 2 is inside Rectangle 1")
else:
    print("The rectangles overlap")

def rectangle(x, y, w, h):
    t.penup()
    t.goto(x, y)
    t.write(f"({x}, {y})", align="center")
    t.forward(w/2)
    t.left(90)
    t.forward(h/2)
    t.left(90)
    t.pendown()
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    
rectangle(x1, y1, w1, h1)
rectangle(x2, y2, w2, h2)
t.hideturtle()
t.done()


