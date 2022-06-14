#Variable : Nombre que se le asigna a un valor, para utilizarlo posteriormente
a = 3
#Declaramos una variable "a" y la asignamos con el valor 3
print(a + 5)
#Accedemos y utilizamos la variable a dentro de una operacion aritmetica
#Las variables permiten guardar datos en memoria y emplearlos durante la ejecucion del programa.
# Cuando hacemos "a = 3" sucede 
# 1.Python busca un espacio de memoria libre y almacena el valor 3
# 2.Python crea un identificador "a" que referencia a dicha direccion

int = a; #Declaracion del tipo de dato y nombre de la variable
a = 3; #Asignacion de dato que almacenara la variable

# Los nombre de variable no pueden comenzar con un numero o por signos
# Solo debem contener letras,numeros o guiones bajos 
variable = 3 #Nombre adecuado
#1variable = 3 #Nombre inadecuado

#Tipos de datos que puede almacenar una variable y ejemplos
#int: numeros enteros sin decimales ---> 3, 5, 7
#float: numeros con decimales       ---> 3.1415, 5.2, 7.98
#string(str): cadenas de texto      ---> "Hola Mundo", "Què tal"
#bool: Valores binarios             ---> True, False

#Importante: Cuando declaramos una variable de tipo float, para marcar el decimal debemos emplear "."
# y no ","
a = 3.1415 #Correcto
a = 3,1415 #Incorrecto
#Por què la segunda es incorrecta?
#Porque en python podemos hacer varias asignaciones en la misma linea de codigo. De esta manera:
a , b, c = 1, 5, 7
#Entonces al emplear una coma para marcar el decimal python falla ya ue se esta esta tratando de asignar
#un valor a una variable no declarada
a = 3,1415
#Se asigna el valor 3 a la variable a y 1415 no se asigna a ninguna variable ya que no hay una creada.

#Algunos datos pueden convertirse de un tipo a otro
#Para cambiar el tipo de dato se debe anteponer a què se quiere convertir y se debe ingresar el valor
#a cambiar dentro de parentesis. De la siguiente manera:
int (7.5)    # Convertimos el dato de tipo float a int. Resultado  ---> 7
str(12.1)   #Convertimos el dato de tipo float a string. Resultado ---> "12.1"
int(True)   #Convertimos el dato de tipo bool a int. Resultado     ---> 1
float("7.5")#Convertimos el dato de tipo str a float. Resultado    ---> 7.5

#Para conocer el tipo de dato de una variable podemos emplear "type":
type("7.5") #---> str
type(10)    #---> int
type(7.5)   #--->float
type(False) #--->bool