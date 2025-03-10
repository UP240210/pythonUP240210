# 1.- Age+.
age = input("How old are you? ")
print("My age is:", age)
#----------------------------------------------------------------
# 2.- Height.
height = input("Which is yout height? ")
print("My height is:", height)
#----------------------------------------------------------------
# 3.- Real number and complex numbers
real_number = float(input("Enter a real number: "))
complex_number4 = complex(input("Enter a complex number: "))

complex_number = real_number + complex_number4 
print (complex_number)
#----------------------------------------------------------------
# 4.-Triangle.
base = float(input("Enter base: "))
height = float(input("Enter height: "))

area = 0.5 * base * height
print("The area of the triangle is", int(area))
#----------------------------------------------------------------
# 5.- Rectangle.
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))

perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is", perimeter)
#----------------------------------------------------------------
# 6.- length and width from the user.
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width

perimeter = 2 * (length + width)

print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)
#----------------------------------------------------------------
# 7.- length and width from the user.
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)
#----------------------------------------------------------------
# 7.- Circule.
import math
radio = 30

area_del_circulo= math.pi  * radio ** 2
print (area_del_circulo)
circunferencia_del_circulo= 2 * radio * math.pi
print (circunferencia_del_circulo)

radio = float(input("Ingrese el radio del círculo: "))
area_del_circulo = math.pi * radio**2
print("El área del círculo es:", area_del_circulo)
#----------------------------------------------------------------
# 8.- Slope line (Equation: y = 2x - 2).
slope = 2
print(f"Slope: {slope}")

interceptY = -2  
print(f"Y-intercept: (0, {interceptY})")

x_intercept = 1
print(f"X-intercept: ({x_intercept}, 0)")
print(f"Intersección con el eje Y: (0, {interceptY})")
#----------------------------------------------------------------
# 9.- Equation: y = 2x - 2.
x1, y1 = 2,2
x2, y2 = 6,10
Num = (y2-y1)/(x2-x1)
print(f"The slope is {slope}")
#----------------------------------------------------------------
# 10.- Compare the slopes in tasks 8 and 9.
if slope > Num:
    print(f"La pendiente {slope} es mayor que la pendiente {Num}.")
elif slope < Num:
    print(f"La pendiente {slope} es menor que la pendiente {Num}.")
else:
    print(f"Las pendientes {slope} y {Num} son iguales.")
#----------------------------------------------------------------
# 11.- Calculate the value of y (y = x^2 + 6x + 9).
''' Me aparece que hay un error en la linea 105 por la y,
    pero no sé como solucionarlo.'''

def calculate_y(x):
    y = (x**2 + 6*x + 9)
    return y

n = [-5, -4, -3, -2, -1, 0, 1, 2]
for x in n: 
    y = calculate_y(x)
    print(f"When x = {x}, y = {y}")

    x_zero = -3
    print(f"\nY is 0 when x = {x_zero}")
#----------------------------------------------------------------
# 12.- Find the length between 'pytho' and 'Dragon'
length_python = len("python")  
length_dragon = len("dragon")  

print(length_python > length_dragon)
#----------------------------------------------------------------
# 13.- Use and operator to check if 'on' is found in both 'python' and 'dragon'
b = 'python'
a = 'dragon'

if 'on' in b and 'on' in a:
    print("'on' is found in both 'python' and 'dragon'")
else:
    print("'on' is not found in both words")
#----------------------------------------------------------------
# 14.- Check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon."
word = "jargon"

if word in sentence:
  print(f"The word '{word}' is in the sentence.")
else:
  print(f"The word '{word}' is not in the sentence.")
#----------------------------------------------------------------
# 15.- There is no 'on' in both dragon and python
jargon_w = "I hope this course is not full of jargon."
python = "Python"

word2 = "on"
if word2 in jargon_w:
  print(f"The word '{word2}' is in both sentences.")
else:
  print(f"The word '{word2}' is not in both sentences.")
#----------------------------------------------------------------
# 16.- Len "python"
text = "python"

length = len(text)
length_float = float(length)
length_string = str(length_float)

print("Length of the text:", length)
print("Length as a float:", length_float)
print("Length as a string:", length_string)
#----------------------------------------------------------------
# 17.- Check if a number is even or not using python.
num = int(input("Ingresa un numero entero: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("the number is not even")
#----------------------------------------------------------------
# 18.- Check if the floor the divisions are equal.
print("7//3 == int(2.7)")
if 7//3 == int(2.7):
    print("They are equal")
else:
    print("They aren't equal")
#----------------------------------------------------------------
# 19.- Check if type of '10' is equal to type of 10.
print(type('10') == type(10))
if type('10') == type(10):
    print("They are equal")
else:
    print("They aren't equal")
#----------------------------------------------------------------
# 20.- Check if int('9.8') is equal to 10.
print("int(9.8) == 10")
if int(9.8) == 10:
    print("They are equal")
else:
    print("They aren't equal")
#----------------------------------------------------------------
# 21.- Ask the user to enter hours and rate per hour.
hour = float(input("Enter hours "))
hourRate = float(input("Enter rate per hours "))
print(f"Your weekly earning is {hour*hourRate}")
#----------------------------------------------------------------
# 22.- Ask the user to enter number of years.
year = int(input("Enter number of years you have lived: "))
days = 365 * year
hour = days * 24
second = hour * 3600
print(f"You have lived {second} seconds")
#----------------------------------------------------------------
# 23.- Write a Python script that displays the following table
"""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)