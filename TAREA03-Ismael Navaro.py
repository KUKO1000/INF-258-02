
#Ismael navarro
#Matricula: 21-1689

""" Primero definimos las variables kWh para el consumo 
y la instalacion para definir el tipo si va a ser residencial,
comercial o industrial.
"""


kWh = float(input("Cantidad de kWh consumida: "))
instalacion = input("tipo de instalacion: ")

#Ahora empezamos a definir cada una para decir si se cumple o no

if instalacion == "R":
    if kWh <= 500:
        input("precio = RD$550.00")
    else:
        input("precio = RD$850.00")

#Definimos el precio del Residencial segun el consumo y damos sus respectivos precios 

elif instalacion == "C":
    if kWh < 1000:
        input("precio = RD$1300.00")
    else:
        input("precio = RD$2500.00 ")
#Definimos el precio del Comercial segun el consumo y damos sus respectivos precios 

elif instalacion == "I":
    if kWh < 5000:
        input("precio = RD$3800.00")
    else:
        input("precio = RD$4200.00")

#Definimos el precio del Industrial segun el consumo y damos sus respectivos precios 
else:
    print("Lo escribiste mal revisalo debes poner R,C,I")
    precio = 0

