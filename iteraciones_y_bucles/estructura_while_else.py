# Si un bucle "while" va precedido de un "else", el contenido de 'else' solo se ejecutara si el bucle se ha interrumpido porque la condiciòn 
# se ha dejado de cumplir
i = 0
while i < 10:
    print(i)
    i = i + 1
else:
    print("Fin del bucle")
# En el còdigo anterior se mostraran los nùmeros del 0 al 9, yaque al i incrementarse a 10 el condicional dejara de cumplirse y se ejecutara
# la cadena "Fin del bucle" del bloque 'else'