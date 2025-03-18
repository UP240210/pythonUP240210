# 1.- Get user input.
age = int(input(f'Enter your age: '))
if age >= 19:
    print(f'You are old enough to drive')
else:
    print(f'You need {18-age} years to drive')
#----------------------------------------------------------------
# 2.- Complete values.
yourAge = int(input("Enter your age: "))
myAge = 19

if myAge > yourAge:
    print(f"I'm {myAge-yourAge} older than you")
elif myAge < yourAge:
    print(f"You're {yourAge-myAge} older than me")
else:
    print(f'We are of the same age ')
#----------------------------------------------------------------
# 3.- Get two numbers from the user.
n1 = int(input(f"Enter number 1: "))
n2 = int(input(f"Enter number 2: "))

if n1 > n2:
    print(f"{n1} is greater than {n2}")
elif n1 < n2:
    print(f"{n2} is greater than {n1}")
else:
    print(f'The numbers are equal')
