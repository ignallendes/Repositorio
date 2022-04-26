#El operador "*" se puede emplear para repetir una cadena de texto miltiplicandola
print("abc"*3)
#Los string pueden verse como listas de caracteres
a = "Hola Mundo"
print(a[0])
print(a[0:5])
print(a[-6:-1])
print("Mundo" in a)
print("Adios" in a)
#Operadores comunes para alterar cadenas(Empleando variable "a")
#a.lower() Toda la cadena pasa a minusculas
#a.upper() Toda la cadena pasa a mayusculas
#a.capitalize() Primera letra de la cadena en mayusculas
#a.title() Primera letra de cada palanra de la cadena en mayus
#a.swapcase() Los mayus y minus de la cadena se invierten
#len(a) Permite contar los caracteres de la cadena de texto

#Operadores que permiten limpiar una cadena
b = "  Hola Mundo Adios "
print(b)
print(b.strip())# Elimina espacios al principio y al final
print(b.rjust(22))# Alinia a la derecha hasta alcancar la longuitud ingresada(en ese caso 22)
print(b.ljust(22))# Alinia a la izq hasta alcancar la longuitud ingresada //
print(b.center(22))#Centra la cadena hasta alcanzar la longuitid ingresada

#Podemos partir una cadena empleando "split"
c = "Hola_mundo_adios"
print(c.split("_"))
#Podemos unir los elementos de una lista en una cadena, empleando una subcadena de "espaciado"
d = ["Hola","Mundo","Que tal?"]
print("_".join(d))
print(" ".join(d))

#Podemos emplear "find" para buscar en un cadena
#Si hay conincidencias, se devuelve el indice de la primera concordancia, sino, devuelve -1
print(a.find("Hola"))
print(a.find("Que tal?"))
#Podemos acotar la busqueda de la cadena:
print(a.find("o",2))#Busca desde a[2]
print(a.find("o",2,7))#No hay "o" entre a[2] y a[7]