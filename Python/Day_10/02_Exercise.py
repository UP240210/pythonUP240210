# 1.- Use for loop to iterate from 0 to 100.
suma = 0
for i in range(101):
    suma = suma + i
print(f"The sum of all numbers from 1 to 100 is {suma}")
#--------------------------------------------------------------------
# 2.- Use for loop to iterate from 0 to 100.
sumOdd = 0
sumEven = 0

for i in range(101):
    if i % 2 == 0:
        sumEven += i

    elif i % 2 != 0:
        sumOdd += i

print(f"The sum of all evens is {sumEven}. And the sum of all odds is {sumOdd}.")