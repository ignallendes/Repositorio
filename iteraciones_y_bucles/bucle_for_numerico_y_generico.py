# Bucle 'for NUMERICO' --------> En español 'Para'
# Bucle que nos permite recorrer el codigo en iteraciones utilizando "range"
n = 3
for i in range(n):
    print(i)

#   i  : Nombre de la variable donde se almacena el valor numerico
# range: Indica que rango de numeros se desea recorrer dado un rango
#   n  : El valor màximo del rango (No incluido en la secuencia. Osea n - 1)
print("----------o----------------o------------------o")
# Existen varias alternativas para crear rangos numèricos:
# - Solo con el valor màximo, el rango comienza en 0.
for i in range(10):     #---> 0,1,2,3,4,5,6,7,8,9
    print(i)
print("----------o----------------o------------------o")
# - Determinando el valor min y max.
for i in range(3,10):    #---> 3,4,5,6,7,8,9
    print(i)
print("----------o----------------o------------------o")
# - Determinando el valor min y max y un 'paso'.
for i in range(3,10,2):  #---> 3,5,7,9
    print(i)
# En el codigo anterior, el paso '2' indica en cuanto se imcrementa el valor en cada iteraciòn
print("----------o----------------o------------------o")
# Un rango no es màs que una colecciòn:
l = list(range(3,10,2))
print(l)
print("----------o----------------o------------------o")
# Al emplear la palabra clave 'list' envolviendo a range, se nos desplegara como lista

# Bucle 'for GENERICO':
# Podemos recorrer facilmente los contenidos de una colecciòn
# for elemento in coleccion:
    # Hace algo con elemento
# Elemento: Variable empleada para almacenar cada elemento de la coleccion. Se puede renombrar a gusto
# El sieguiente còdigo imprime los elementos de una lista
l = ["Hola", 3, 7.3]
for el in l:
    print(el)
print("----------o----------------o------------------o")
# Bucle for generico con diccionarios:
# Recordemos que los diccionarios cuentan con keys y values.
# Podemos recorrer las claves del diccionario de la siguiente manera:
d = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e"}
for k in d.keys():
    print(k)
print("----------o----------------o------------------o")
# Podemos recorrer los valores del diccionario de la siguiente manera:
for v in d.values():
    print(v)
print("----------o----------------o------------------o")
# Podemos recorrer las keys y valores del diccionario a la vez de la siguiente manera:
for k,v in d.items():
    print(k,v)
print("----------o----------------o------------------o")
# Podemos deterne el bucle empleadno la instruccion 'break'
# Si se ejecuta esta instruccion la ejecucuon del bucle se interrumpe
l = [1, 10, 772, 4, "stop", 3, 11]
for i in l:
    if i == "stop":
        break
    print(i)
print("----------o----------------o------------------o")
# Podemos detener la iteraciòn actual empleadno la instrucciòn "continue".
# Al ejecutarse esta instruccion, el bucle interrumpe la iteraciòn actual y continua desde la siguiente iteraciòn.
for i in range(10):
    if i == 5:
        continue
    print(i)
# En el còdigo anterior se imprime los nùmeros del 0 al 9, con excepciòn del 5