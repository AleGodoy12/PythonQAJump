# Primera clase 17/10/2022

#Horas = float(input("Por favor ingrese la cantidad de horas trabajadas: "))
#Coste = 20
#Paga = Horas * Coste
#print(Paga)

# Segunda clase 19/10/2022

#Frutas = ["banana", "manzana", "pera"] #Lista
#print(Frutas) 

#Frutas.append("sandia") #Agrega a lista
#print(Frutas) 

#Frutas.pop(1) #Borra de lista
#print(Frutas)

#print(Frutas.count("pera")) #Cuantas veces se encuentra el elemento en la lista

#tuple(Frutas)
#print(Frutas)

#Clase 4
#Flujo: forma de entender la sucesión de las intruscciones de un programa. Estas instrucciones se ejecutan una despues de otras de forma ordenada y suelent tener el objetivo final de manipular información
#Necesitamos que de alguna forma nuestro programa pueda elegir, que sepa como actuar en funcion de determinadas situaciones o incluso repetir una tarea si es necesario

#Sentencia de control:
#Condicional: para elegir distintas posibilidades
#Iterativas: para repetir un bloque de instrucciones

#Diagrama de flujo: expresan lo que hace el algoritmo

#Generación Z = 2000 - 2010
#Generación X = 1980 - 1999
#Generación Y = 1960 - 1979

año = int(input("Ingresa el año de nacimiento: "))
if año >= 1960 and año <= 1979:
    print("Es de la generación Z")
elif año >= 1980 and año <= 1999:
    print("Es generación X")
elif año >= 1960 and año <= 1979:
    print("Es generación Y")
else:
    print("No se que generación sos :(")

# Mayor de 18, adenas tener un ingreso superior a los 2500 usd

edad = int(input("Ingrese su edad: "))
ingreso = int(input("Cuanto gana por mes: "))
antiguedad = int(input("Cual es tu antiguedad laboral? "))
if edad >= 18 and ingreso >= 2500 and antiguedad > 3: 
    print("Se puede otorgar")
elif edad >= 18 and ingreso >= 4000 and antiguedad > 2:
    print("Tambien se puede otorgar")
else: 
    print("No se aprueba el credito")