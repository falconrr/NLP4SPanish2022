import re # importamos el módulo

mi_oracion = input("Escribe una oración: ") # recolectamos la información del usuario
lista = [] # creamos una lista vacia. Ésta nos va a servir para agregar datos.

if (re.search('[ !\.;?]', mi_oracion)): # utilizamos la función re.search para buscar una expresión regular
    print("Esto parece una oración")
    lista.append(mi_oracion) # Si reconoce la oración, entonces la adjuntamos a la lista
    nueva_oracion = re.sub('[A-Z]', '[X]', mi_oracion) # Creamos una variable con la función de substitución de expresiones regulares
    print("He agregado la siguiente oración a la lista: ", lista) # imprimimos mensaje y la lista de oraciones que se agregan
    print(nueva_oracion)
    minuscula = mi_oracion.lower() # nueva función para cambiar a minúsculas el texto. Se encapsula en una nueva variable
    print("", minuscula) # imprimimos la variable
else:
    print("Esto no parece una oración y no será agregada a la lista") # imprimimos mensaje alternativo.
