nombre_conocido = ["Gillian", "Jorge", "Marina"] # puse nombres de usuarios conocidos
nombre = input("¿Cómo te llamas? ") # crea una variable donde hay un input del usuario

if nombre in nombre_conocido: # condicional para imprimir mensaje de bienvenida
    print("Bienvenido " + nombre)
    print("Es un placer que estés de vuelta!")
else: # si no encuentra el usuario queremos que lo agregue a la lista = append()
    nombre_conocido.append(nombre)
    print("Se te ha agregado a la lista.")
