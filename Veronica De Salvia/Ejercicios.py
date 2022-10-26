#Ejercicio 1.NumerosyString
#1
from itertools import count
nombre = input("Por favor ingrese su nombre: ")
print("Ahora estas en la matrix " + nombre)

#2
nrodecimale = float(input("Por favor ingrese un número con decimales: "))
nroentero = int(input("Por favor ingrese un número entero: "))
Suma = nrodecimale + nroentero
print("El resultado de la suma es " + Suma)

#3
nro1 = float(input("Por favor ingresa un número: "))
nro2 = float(input("Por favor ingresa otro número: "))
suma = nro1 + nro2
print("El resultado de la suma es" + suma)
nro3 = float(input("Por favor ingrese un tercer número: "))
multi = suma * nro3
print("El resultado de la multiplicación es: " + multi)

#4
palabra1 = input("Por favor ingrese una palabra")
palabra2 = input("Por favor ingrese otra palabra")
concatenacion = palabra1 + " " + palabra2
print(concatenacion)

#5
print("Hola mundo")

#Ejercicio 2.ListasyTuplas

#1
Materias = ["Literatura", "Quimica", "Ingles"]
print(Materias + " ")

#2
ArtOficina = ["Engrapadora", "Lapicera", "Portapapeles"]
ArtHomeOffice = ["Mate", "Post-it", "Tostadas"] #perdón, me daba gracia
Lista3 = ArtOficina + ArtHomeOffice
print(Lista3)

#3
Lista = ["Esto", "es", "una", "lista"]
tuple(Lista)

#4
Lista = ["Pera", "Tulipan", "Corcho", "Lata", "Jarron"]
Lista.append("Carta")
print(Lista)

len(Lista)

Lista.pop(2) #Por default te borra el ultimo dato

Lista.count("Lata")

#Ejercicios 3.Expresiones