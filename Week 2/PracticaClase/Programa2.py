import re # importamos el módulo de expresiones regulares = re

mi_oracion = input("Escribe una oración: ") # recolecta la oración del usuario
lista = [] # creamos lista vacía. Ésta nos va a permitir agregar datos

if (re.search('[ !?;\.]', mi_oracion)): # creamos la expresión regular para que nos reconozca la oración
    print("Esto parece una oración") # imprimimos mensaje de éxito
    lista.append(mi_oracion) # agregamos la oración a la lista vacía
    nueva_oración = re.sub('[A-Z]', 'X', mi_oracion) # substituimos mayúsculas por una 'X'
    print(nueva_oración) # imprime la oración cambiando las mayusculas por 'X'
    minusculas = mi_oracion.lower() # cambiamos el texto a minusculas
    print(minusculas) # imprimimos el texto en minusculas
else:
    print("Esto no parece una oración")
