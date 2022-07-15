# Una estructra de datos o coleccion es un tipo de dato que permite almacenar multiples valores
# Los màs conocidos son:
#Listas []
#Diccionarios {}

#Listas[]: Secuencia ordenada de valores de cualquier tipo
#Para declarar una lista:
l = [] #Lista vacia
# Podemos tambien declarar una lista y agregarles valores desde el inicio
l = [1.54, "Hola", "Mundo", 3]
# Los valores se ingresan en la lista y se ordenan por un indece que comienza desde 0
# indice | valor
#   0       1.54
#   1      "Hola"
#   2      "Mundo"
#   3        3

#Podemos añadir un elemento al final de una lista empleando "append"
l.append("Adios")
print(l)
#Podemos tambien insertar un elemento en una posicion que eligamos con "insert"
l.insert(2,"Que tal")
# Lo que pasaria seria que en el indice 2 se agregaria la cadena "Que tal"
#Los elementos posteriores se desplazan tras la insercion. Se veria tal que asi:
# indice | valor
#   0       1.54
#   1      "Hola"
#   2      "Que tal"---> Elemento agregado con insert
#   3      "Mundo" ---> Desplazado
#   4       3      ---> Desplazado
#   5      "Adios" ---> Elemento agregado con apend

#Podemos eliminar un elemento de una lisya con "remove"
l.remove(1.54)
#Los elementos posteriores se desplazan tras el borrado ajustandose al indice
# *Si hubieran varios valores coincidentes, solo se borra el primero de ellos 
# indice | valor   
#   0      "Hola"
#   1      "Que tal"
#   2      "Mundo"
#   3       3      
#   4      "Adios"

#Podemos eliminar un elemento dada su posicion o index con "del"
del l[1]
#Los elementos se reajustan luego del borrado
# indice | valor   
#   0      "Hola"
#   1      "Mundo"
#   2       3      
#   3      "Adios"

#Podemos obtener el valor de un elemento mediante su posicion
print(l[0]) # "Hola"
print(l[3]) # "Adios"
#Podemos emplear indices negativos para empesar a contar desde el final de la lista
print(l[-1]) # "Adios"
print(l[-2]) # 3
#Si empleamos indices negativos el ultimo elemento es -1

#Sepuede obtener una sublista empleadno rangos.
#Para ello, se indica entre corchetes los expremos de la sublista, separados por ":"
print(l[1:3]) # ["Mundo", 3]. El valor que indica el final de la lista no va incluiodo
print(l[-2])  # 3
#Podemos no incluir alguno de los expremos
print(l[:3])  # ["Hola", "Mundo"], 3. Si no se indica uno de los 2 expremos, python lo incluira desde el inicio
# O desde el final si es que no se indica el cierre.
print(l[1:])  #["Mundo", 3, "Adios"]
#Trea todos los elementos de la lista
print(l[ : ]) #["Hola", "Mundo", 3, "Adios"]
#Extra
# Este mismo metodo de acceso se puede emplear con cadenas de texto
print("Hola Mundo"[1:-3]) # "ola Mu"

#Actualizacion de una sublista
#Creamos la lista "l" y la iniciamos con los valores: ["Hola", "Mundo", 3, "Adios"]
l = ["Hola", "Mundo", 3, "Adios"]
# Modificacion de sublista
l[2] = "Que tal?"
# Se remplaza el valor del indice 2, el cual tiene un valor int 3 y se reescribe con el valor str "Que tal?"
# indice | valor   
#   0      "Hola"
#   1      "Mundo"
#   2      "Que tal"      
#   3      "Adios"
# Podemos tambien modificar una sublista mediante rangos.
l[1:3] = ["Que tal?", "Mundo"]
# indice | valor   
#   0      "Hola"
#   1      "Que tal"
#   2      "Mundo"    
#   3      "Adios"
# El metodo de rangos se puede emplear ademas para insertar o borrar.
l[2:] = []          # Borra la lista desde el incice 2
l[1:1] = ["a"] # Inserta el elemento a en el indice 1

# Operaciones usando listas
# Podemos conecer la longuitud de una lista empleando "len"
l = ["Hola", "Mundo", 3, "Adios"]
print(len(l)) # 4
# Podemos concatenar listas empleando "+"
l1 = [1, "Mundo"]
l2 = ["Hola"]
print(l1 + l2) # [1, 'Mundo', 'Hola']
# Podemos emplear "in" para comprobar si un elemento pertenece a una lista
l = ["Hola", "Mundo", 3, "Adios"]
print("Mundo" in l)    # True
print("Que tal?" in l) # False
# Si tenemos una lista constituida solo por numeros, podemos sumar sus elementos empleando "sum"
a = [1, 2 ,3 ,4 ,5]
print(sum(a)) # 15
# Podemos invertir el orden de los elementos empleando "reversed". Devuelve un valor de tipo iterador
b = ["a", "b", "c", "d"]
reverso = list(reversed(b)) # Es necesario pasarlo de iterador a lista para poder visualizarlo
print(reverso) # ['d', 'c', 'b', 'a']

#Podemos ordenar los elementos de una lista empleando "sorted"
c = [4, 1, 3, 2, 5] 
print(sorted(c))

# Diccionario de datos
# Un diccionario es un tipo de coleccion no ordenada de valores asociados a una clave unica que no se repite
# En python declaramos un diccionario con llaves "{}"
d = {} # Crecion de diccionario vacio
# Podemos declarar un diccionario con datos desde el inicio. Para ello los elementos se separan con comas 
# y las claves se separan de los valores empreando ":"
d = {"c1":1, 3:"Hola", "b2":True, "a_":1.4}
print(d) # {'c1': 1, 3: 'Hola', 'b2': True, 'a': 1.4}
#Podemos insertar un nuevo elemento mediante asignacion 
d["d7"] = "Mundo"
print(d)
# * Recordemos que los elementos de un diccionario no estan ordenados, por lo que no existe un primer elemento
# ni ultimo
#Podemos eliminar un elemento con "del"
del d["c1"]
# De esta forma eliminamos un elemento dada su clave
# Podemos acceder a un elemento de un diccionario mediante su clave
print(d["a_"]) # 1.4
print(d[3])    # "Hola"
# *Al no estar ornenados los diccionarios, no podemos acceder a los elementos mediante rangos

# Actualizacion de un elemento
# El valor de un elemento se puede modificar mediante una asignacion. Si la clave ya existia en el diccionario
# su valor se remplaza por el nuevo
d["c1"] = "Adios"
print(d) # {3: 'Hola', 'b2': True, 'a_': 1.4, 'd7': ['Mundo'], 'c1': 'Adios'}
#Podemos emplear "len" para conocer la longuitud de un diccionario
print(len(d)) # 5
#Podemos emplear "in" para comprobar si existe ya una CLAVE. Este metodo no se puede emplear asi para
#comprobar la existencia de un valor dentro de un diccionario, solo se puede emplear para claves
print("b2" in d) # True
#Podemos usar "keys" y "valores" para recuperar las claves y los valores del diccionario
print(d.keys()) # Se muestra en pantalla solo las claves del diccionario
print(d.values()) # Se muestra en pantalla solo los valores del diccionario

#Tuplas: Una tupla es una coleccion similar a una sublista, con algunas diferencias
# Se crean empleando parentesis () y no corchetes []
# Las tuplas son inmutables
t = (1, 3, 2)
# Las tuplas son inmutables, por lo que no se puede añadir, borrar o modificar sus elementos
#t[1] = 0    ---> Error
#del t[2]    ---> Error
#t.append(4) ---> Error
# Tuplas: Empaquetado y desempaquetado
# Si asignamos varios valores a una variable, python construye automaticamente una tupla
# Esta operacion se llamada empaquetado
# t = 1, 3, 2 ---> t = (1, 3, 2)  Python construye una tupla
# En sentido contrario, si se asigna una tupla a tantas variables como elementos tenga la tupla,
# se "desempaqueta" la tupla
t = (1 ,3, 2)
a, b, c = t
print(a, b, c)    #1 3 2
a, b, c = 1, 2, 3 # Empaquetado y desempaquetado

#Conjuntos: Un conjunto es una colecion similar a una lista, con diferencia de: 
# No se pueden almacenar valores repetidos
# Los elementos no tienen orden 
# Los conjutos se crean empleando llaves
s = {1, 2, 3}
# A diferencia de los diccionarios los no tienen keys, solo valores
#Se pueden añadir elementos empleando "add"
s.add(4)
print(s)
#No se puede acceder a los elemntos usando el indice ya que no tienen orden 
 
