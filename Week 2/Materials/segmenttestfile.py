#import shutup;shutup.please() # ignora esto por favor. No es necesario en tu código

import nltk # importamos módulos
import sys
sentences = [] # creamos una lista vacia

with open(sys.argv[1], 'r') as f: # le pedimos a python que lea el archivo que especificamos en la terminal
    text = f.readlines() # lee línea por línea
    for line in text: # for loop: lee línea por línea y realiza una tarea repetitivamente
        nltk_sents = nltk.sent_tokenize(line) # la tarea es que segmente las oraciones del texto con el módulo NLTK
        sentences.append(nltk_sents) # agrega los tokens a la lista vacía
        print(nltk_sents) # imprime el resultado
