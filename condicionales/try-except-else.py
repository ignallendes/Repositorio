# En Python, podemos emplear la estructura try-except-else para ejecutar codigo sino se produce ningun error
try: 
    #Codigo que se intentara ejecutar
    a = "hOla QUE tAL"
    a = a.capitalize()
except:
    #Codigo que se ejecuta si ha surguido un error
    print("La cadena de texto no ha sido modificada")
else:
    #Codigo que se ejecuta si no se ha producido un error
    print("Se ha modificado correctamente la cadena: "+a)