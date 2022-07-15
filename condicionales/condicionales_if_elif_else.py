#Condicionales
# Una accion condicionales aquella que se raliza SI se presenta una condicion
#En programacion disponemos de la expresion "if" para ejecutar codigo de forma condicional
#Sintaxis
# 1      2    3
# if condicion:
# 1 La palabra reservada "if" indica el comienzo de una expresion condicional
# 2 La condicion debe retornar un valor booleano
# 3 los dos puntos indican que comienza el bloque condicional

# La condicionse cumple cuando el valor retornado es True
# Ejemplos de condicionales
# if True:               ---> Siempre se cumple
# if False:              ---> Nunca se cumple   
# if a < b:              ---> Si el valor de a es menor a el de b
# if a == 1 and b == c:  ---> Si ambas condiciones se cumplen
# if a == 1 or b == c:  ---> Si alguna de las 2 condiciones se cumple

# Otro ejemplo puede ser comprobar si hay un valor en una lista empreando "in"
l = ["Hola", "Adios"]
if "Hola" in l: 
    print("'Hola' pertenece a la lista l")
print("------o------o------o------o------o------o------o------o------o------o------o------o")
# Al cumplirse la condicion se ingresa al bloque de codigo dentro de la sentencia condicional if
# Los bloques de codigos deben ser tabulados para ser ejecutados correctamentes por python

# Podemos emplear la estructura "if-else" para ejecutar codigo si no se cumple la condicion
a = 1
if a < 15:
    print("Se muestra si la condicion se cumple")
else:
    print("Se muestra si la condicion no se cumple")
print("Siempre se muestra al estar fuera de los bloques de if o else")
# Estas estrucututas condicionales solo permiten ejecutar una solo bloque, en ningun caso ambos
print("------o------o------o------o------o------o------o------o------o------o------o------o")
# De forma similar podemos emplear la estructura "if-elif-else" para gestionar varias condiciones
nota = 8
if nota < 5:
    print("Suspendido")        # No se cumple
elif nota > 7:
    print("Aprobado")          # No se cumple
elif nota > 9:
    print("Notable")           # Se cumple y se ejecuta
elif nota >= 10:
    print("Sobresaliente")     # Se cumple pero no no se ejecuta ya que el anterior ya se cumplio
else:
    print("Matricula de honor")

# Anidacion de condiciones
# Los bloques condicionales se pueden anidar unos dentros de otros
# Se debe tener precaucion con las tabulaciones
a = 5
b = 3
if a < 3:
    print("Caso 1")
else:
    if b < 5:
        print("Caso 2")
    else:
        print("Caso 3")
