#Ejercicio 1
print ("Ejercicio Bisiesto")
anio=int(input("Ingrese el año:"))
if (anio % 400 == 0) or (anio % 4 == 0) and (anio % 100 != 0):
    print ("El año es Bisiesto")
else:
    print ("El año no es Bisiesto")
