# Descripción de la actividad. 

# Escribir un programa que indique la generación 
# correspondiente para un año de nacimiento indicado. 
# Importante: Para los años que no pertenezcan a ninguna
# generación, se deberá colocar: “No existe generación asociada”

# Generazion z = 2000 - 2010
# Generacion x = 1980 - 1999
#Generacion y = 1960 - 1979

# año = int(input("Ingresa el año de nacimiento: "))
# if año >= 1960 and año <= 1979:
#     print("Soy abuelo")
# elif año  >= 1980 and año <= 1999:
#     print("Soy generacion x")
# elif año >= 2000 and año <= 2010:
#     print("Generacion z")
# else:
#     print("No existe generacion asociada")

# Mayor de 18, ademas tener un ingreso superior a los 2500usd, y antiguedad de 3 años.
# Mayor de 18, ingreso de 4000usd y antiguedad mayor a 2años.

edad = int(input("ingrese su edad: "))
ingreso = int(input("Cuando gana por mes: "))
antiguedad = int(input("Cual es su antiguedad laboral? "))

if edad > 18 and ingreso > 2500 and antiguedad > 3:
    print("Se puede otorgar")
elif edad > 18 and ingreso > 4000 and antiguedad > 2:
    print("Tambien se puede otorgar")
else:
    print("No se aprueba el credito")
    

