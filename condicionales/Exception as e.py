# Una exception es un objeto que hace referencia a que se ha producido una situacion excepcional en el codigo
# Al capturar un error, podemos objeter la excepcion y trabajar con ella
try:
    #a = 1
    #b = 0
    c = a / b
    print("c")
except Exception as e:
    print(e)

# El codigo anterior captura el error y lo almacena en la variable "e", la cual es luego leida en consola para mostrar el tipo de error