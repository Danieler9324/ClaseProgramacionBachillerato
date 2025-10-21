from Controllers.tipo_movimiento_controller import *    #De la carpeta Controllers importar el archivo de tipo_movimiento_controller

#Funcion para el menu del tipo movimiento
def menu_tipo_movimiento():
    #Crea un ciclo while para el menu
    while True:
        print("(L) Listar tipo movimiento")
        print("(A) Agrega tipo movimiento")
        print("(M) Modifica tipo movimiento")
        print("(B) Baja tipo movimiento")
        print("(S) Salir")

        #Crea la variable opcion como upper

        opcion=input().upper()

        if opcion=="L":     #Si la opcion es "L" entonces mostrar el tipo movimiento
            mostrar_tipo_movimiento()
        elif opcion=="A":   #Si la opcion es "A" entonces agregar el tipo movimiento
            agregar_tipo_movimiento()
        elif opcion=="M":   #Si la opcion es "M" entonces modificar el tipo movimiento
            modifica_tipo_movimiento()
        elif opcion=="B":   #Si la opcion es "B" entonces eliminar el tipo movimiento
            elimina_tipo_movimiento()
        elif opcion=="S":   #Si la opcion es "S" entonces romper el ciclo 
            break