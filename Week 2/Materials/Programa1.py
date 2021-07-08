usuarios_conocidos = [ 'Gillian', 'Cari', 'Su Ar', 'Jorge', 'Falcon'] # creo una variables con los nombres de usuarios conocidos
nombre = input("Cómo te llamas? ") # creo una variable que tome el input del usuario

if nombre in usuarios_conocidos: # pongo el condicional aquí para que detecte si hay un usuario conocido
    print("Bienvenido" + nombre) # imprimo mensajes de bienvenida
    print("Es un placer que estés de vuelta.")
else: # si el programa detecta un usuario que no reconoce, entonces lo agrega a la lista
    usuarios_conocidos.append(nombre)
    print("Se te ha agregado a la lista") # imprime mensaje
