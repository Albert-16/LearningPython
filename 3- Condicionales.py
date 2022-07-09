#   Capitulo 3: Booleanos, condicionales y entrada de usuario

#   Entrada de datos del usuario. Identificación de tipos de datos
"""
edad = input("Escribe tu edad por favor: ") #Pedirle datos al usuario

tipo_de_dato = type(edad) #sabemos el tipo de dato de una variable.

print(edad)
print(tipo_de_dato)


#   Booleanos, if
verdadero = True
falso = False

'''El = asigna,  el == compara valores '''
if(verdadero == True):
    print("Soy verdadero!")

if(falso == True):
    print("Son iguales")

if(falso == False):
    print("Si soy falso")
    
"""


"""
# Operadores de comparacion elif, else
edad = int(input("Dime tu edad por favor: "))
if (edad >= 18):
    print("Tienes permitido pasar")
elif(edad< 0):
    print("Olle esto es imposible")
else:
    print("Eres menor de edad no puedes pasar")
"""


# Operadores logicos and or not

edad = input("Dime tu edad por favor: ")

if (edad.isnumeric()):
    edad = int(edad)
    if (edad > 120 or edad < 0):
        print("Esto no es posible")
    elif (edad > 18 and edad < 40):
        print("Puedes entrar en mi club")
    elif (edad < 18 and edad > 15):
        print("Eres un chaval, pasa")
    else:
        print("No se cumple ninguna de las condiciones")
else:
    print("Oye que la edad debe ser un numero entero.")

'''
numero = input("Ingrese un numero: ")
if(not(numero.isnumeric())):
    print("Eso no es un numero")
elif(int(numero)%2 == 0):
    print("Es un numero par.")
'''