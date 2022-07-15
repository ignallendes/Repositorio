# Expresion "pass"
# Si queremos capturar un error si ejecutar ningun codigo utilizamos 'pass'
# Esto permite continuar con la ejecucion del codigo 
try:
    precio = "Caro"
    precio_num = float(precio)
except:
    pass
    print("Pass permite que el codigo no se caiga")

# En Python no puede haber bloques de codigo vacios. Por ello, la instruccion 'pass' realmente no hace nada, pero sirve para rellenar el bloque