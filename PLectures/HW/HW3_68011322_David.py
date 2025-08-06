# # Q1

name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked in a week: "))
pay_rate = float(input("Enter hourly pay rate: "))
ftax = float(input("Enter federal tax withholding rate: "))
stax = float(input("Enter state tax withholding rate: "))

#calculate gross pay and deductions
gross_pay = hours * pay_rate
federal_withholding = gross_pay * ftax
state_withholding = gross_pay * stax
total_d = federal_withholding + state_withholding
net_pay = gross_pay - total_d

print("Employee Name:", name)
print("Hours Worked:", hours)
print("Pay Rate: $", pay_rate)
print("Gross Pay: $", (gross_pay))
print("Deductions:")
print(f"  Federal Withholding ({ftax * 100.0}%): $", (federal_withholding))
print(f"  State Withholding({stax * 100.0}%): $", (state_withholding))
print("  Total Deduction: $", (total_d))
print("Net Pay: $", net_pay)

# Q2 
n = input("Enter a number: ")
numbers = n[::-1] 
print("Reversed number:", numbers)

# Q3 
import turtle as t
t.speed(1)
length = int(input("Enter the length of the star: "))
for i in range(5):
    t.forward(length)
    t.right(144)
t.done()

# Q4
import turtle as t
t.speed(100)
radius = int(input("Enter the radius of the rings: "))
x = 1
dis = radius * 2.2

# Function to check color
def check_color(x):
    if x == 1:
        return "blue"
    elif x == 2:
        return "black"
    elif x == 3:
        return "red"
    elif x == 4:
        return "yellow"
    else:
        return "green"

# Function to move the turtle without drawing
def move(steps, left=0, right=0):
    t.penup()
    t.forward(steps)
    t.left(left)
    t.right(right)
    t.pendown() 

# First 3 circles
for i in range(3):
    color = check_color(x)
    t.color(color)
    t.circle(radius)
    move(dis)
    x += 1

# The other 2 circles
ys = -radius * 1.2
t.teleport(radius+5, ys)
for i in range(2):
    color = check_color(x)
    t.color(color)
    t.circle(radius)
    move(dis)  
    x += 1
t.done()    

# Q5
import turtle as t
t.speed(1)

