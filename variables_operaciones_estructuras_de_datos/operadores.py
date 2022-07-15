#Operadores basicos 

#Aritmetico: Permite realizar calculos matematicos. Retorna un valor numerico
#+, -, *, /, %, **, //. Suma, resta, multiplicacion, division, modulo, potencia, division entera.
from operator import xor


a = 5;
b = 3;
#Suma
print(a+b)
#Resta
print(a-b)
#Multiplicacion
print(a*b)
#Division
print(a/b)
#Modulo
print(a%b)
#Potencia
print(a**b)
#Division entera
print(a//b)

#Relacionales: Permiten comparar valores. Retornan un valor booleano
"==" # Devuelve True si ambos valores son iguales
"<"  # Devuelve True si el primer valor es menor que el segundo
">"  # Devuelve True si el primer valor es mayor que el segundo
"<="  # Devuelve True si el primer valor es menor o igual al segundo
">="  # Devuelve True si el primer valor es mayor o igual al segundo
"!="  # Devuelve True si ambos valores son distintos

#Ejemplos de operaciones relacionales
print(-2 < 3.5)
print(3.5 <= 3.5)
print(-2 > 3.5)
print(-2 >= 3.5)
print(4 != 4)
print(4 == 4)
print("-------o-------o-------o-------o-------o-------o-------o-------o-------o")
#Booleanos: Permiten operar con valores binarios. Retornan un valor booleano
"and o &" # Devuelve True si ambos valores son True
"or o |"  # Devuelve True si al menos uno de los los valores es True
"not"     # Invierte el valor. Devuelve True si el valor el False y viceversa
"^"       # xor devuelve True si los dos valores son distintos

#Ejemplos de operaciones booleanas
print(True and True)
print(True and False)
print(not True)
print(True or False)
print(False ^ True)

#Cadenas de Texto: Se emplea para manipular cadenas de texto (solo se mostraran algunos)
# Concatenacion: Permite unir cadenas de texto utilizando "+"
a = "Hola"
b = " Mundo"
print(a + b)
#Podemos conocer la longuitud de una cadena de texto empleando el operador "len"
print(len("Hola Mundo"))
#len cuenta espacios y signos especiales
#Podemos pasar una cadena de texto a mayuscula utilizando "upper"
a = "Hola Mundo"
print(a.upper())
# Podemos tambien convertir el texto a minusculas con "lower"
print(a.lower())