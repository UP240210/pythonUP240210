# longitud 
print ("Longitud de palabras ")
# Utilización de len( )
a = input ("Nombre completo:  ")
print(len(a))
# Comparación de nombre y apellido usando len ( )
b = input ("Nombres: ")
c = input ("Apellidos: ")


if b > c:
    print ("Tus nombres son mas largos ")
else:
    print ("Tus apellidos son mas largos ")

# Declaración de numeros
num_uno = 5
num_dos = 4
# Sumatoria de numeros

n = num_uno + num_dos
p = num_uno - num_dos
ñ = num_uno * num_dos
x = num_uno / num_dos
remainder = num_uno ** num_dos
cociente = num_uno // num_dos

print ("La suma de los valores es:")
print (n)
# Resta de numeros
print ("La resta de los valores es:")
print (p)
# Multiplicación de numeros
print ("La multiplicación de los valores es:")
print (ñ)
# Divisón de numeros
print ("La divisón de los valores es:")
print (x)
# Porcentaje de numeros
print ("El porcentaje de los valores es:")
print (remainder)
# Porcentaje de numeros
print ("La potencia de los valores es:")
print (cociente)

# Calcular el área del círculo
# Llamo a la libreria de matematicas
import math

radio = 30
# Operaciónes para sacar el area y circunferencia del circulo
area_del_circulo= math.pi  * radio ** 2
print (area_del_circulo)
circunferencia_del_circulo= 2 * radio * math.pi
print (circunferencia_del_circulo)
# Entrada del usuario y calculación del área
radio = float(input("Ingrese el radio del círculo: "))
area_del_circulo = math.pi * radio**2
print("El área del círculo es:", area_del_circulo)