# -*- coding: utf-8 -*-
"""Laboratorio2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t9LDLNXyliUtYHEM73ZFpoLwCEltTDLe
"""

#Laboratorio 2
#1 Seleccionar TOWN
#2 TOWN: CRIM para aquellos casos superiores a 0.50
#3 Sacar el promedio de la edad, usar la funcion promedio de matematica
#4 Imprimir un indice y una edad, retorna los puntos correspondientes
#5 Ordenamiento por el CRIM, sort para el ordenamiento


#Apertura de archivo
import pandas as pd
df=pd.read_csv('/content/casasboston.csv')
data=pd.DataFrame(df)
print(data)
print(data.AGE)

dataResultado=data.loc[(data['AGE']==65.2)]
print(dataResultado)

#Pueblo y CRIM

#1
dataPueblo=data.loc[(data['TOWN']=="Marblehead")]
print("Pueblo seleccionado: ",dataPueblo)
#2
dataResultado=data.loc[(data['TOWN']=="Marblehead") & (data['CRIM']>=0.50)]
print("Datos Punto #2: ",dataResultado)


#3
promedio=dataPueblo['AGE'].mean()
print("El promedio de las edades es: ",promedio)

#4
dataCuatro=dataPueblo.loc[(data['AGE']>50) & (data['INDUS']>=2)]
print("Datos Punto #4:" ,dataCuatro)

#5
dataCinco=sorted(dataPueblo['CRIM'])
print("Datos ordenados por CRIM ",dataCinco)

