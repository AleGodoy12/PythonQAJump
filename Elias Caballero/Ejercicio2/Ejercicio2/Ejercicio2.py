#!/usr/bin/python
# -*- coding: latin-1 -*-

#1
print("Ejercicio 1:")
materias = ["Matem�ticas", "F�sica", "Qu�mica", "Historia", "Lengua"]
print(materias)

print()
#-------------------------------------------------------------------------------------------

#2
print("Ejercicio 2:")
artOficina = ["Biromes", "Libreta", "L�mpara"]
artHomeoffice = ["Cafetera", "Taza"]

articulos = artOficina + artHomeoffice
print(articulos)

print()
#-------------------------------------------------------------------------------------------

#3
print("Ejrcicio 3:")
bruh = ["B", "R", "U", "H"]
tuple(bruh)
print(bruh)

print()
#-------------------------------------------------------------------------------------------

#4
print("Ejercicio 4:")
letras = ["A", "B", "C"]
print(letras)

print("Se quita un elemento")
letras.pop(0) #pop "A"
print(letras)

print("Se agrega un elemento")
letras.append("D") #push "D"
print(letras)

print("El largo de la lista es ", len(letras)) 

numeros = ["1", "2", "3"]
print("Se concatena con una lista de n�meros:")
letYNum = letras + numeros
print(letYNum)

print()
