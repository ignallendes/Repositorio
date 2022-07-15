# Estructura "try-except"
# En python, podemos emplear la estructura "try-except" para capturar errores 
precio = "Caro"
try:
    num_precio = float(precio)
    # Bloque de codigo que se intenta ejecutar
except:
    print("No se puede convertit un valor string a float")
    # Codigo que se ejecutara si el bloque anterior presenta un error
# Al igual que en la estructura if - else podemos anidar try - except dentro de otro. Se debe tener precaucion con las tabulaciones

# Podemos emplear varios except para capturar distintos tipos de errores
try:
    b = float(s)
    c = a / b
    print(c)
except ValueError:
  print("El valor 's' no puede ser convertido a float")
except ZeroDivisionError:
    print("s vale 0, no se puede dividir")
except NameError:
    print("La variable 's' no esta definida")
except:
    print("Ha ocurrido un error desconocido")
#Python al no poder ejecutar el bloque de codigo de try pasa a leer el bloque del except que se adecue al error que surge

