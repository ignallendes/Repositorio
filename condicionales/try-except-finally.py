# Utilizamos esta estructura para ejecutar codigo tanto si se ha producido un error, como si no 
from ctypes.wintypes import FLOAT


try:
    #Codigo que se tratara de ejecutar
    precio = "Diez miel"
    precio_num = int(precio)
except ValueError:
    #Codigo que se ejecutara si se produce un error
    print("No se puede convertir una cadena a float")
finally:
    #Codigo ue se ejecutara siempre
    print("Fin de la ejecucion")