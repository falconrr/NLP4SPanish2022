#import shutup;shutup.please() # ignora esto por favor. No es necesario en tu código

import nltk # importamos módulos
import sys
tokens = [] # creamos una lista vacia

with open(sys.argv[1], 'r') as f: # le pedimos a python que lea el archivo que especificamos en la terminal
    Lines = f.readlines() # lee línea por línea
    for line in Lines: # for loop: lee línea por línea y realiza una tarea repetitivamente
        nltk_tokens = nltk.word_tokenize(line) # la tarea es que tokenice el texto con el módulo NLTK
        tokens.append(nltk_tokens) # agrega los tokens a la lista vacía
        print(nltk_tokens) # imprime el resultado
