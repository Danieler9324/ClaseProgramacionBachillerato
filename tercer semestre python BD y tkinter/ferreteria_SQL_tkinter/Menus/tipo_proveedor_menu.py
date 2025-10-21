from Controllers.tipo_proveedor_controller import *     #De la carpeta Controllers importa el archivo tipo_proveedor_controller

#Funcion para el menu del tipo proveedor
def menu_tipo_proveedor():
    #Crea un ciclo while para el menu
    while True:
        print("(L) Listar tipo proveedor")
        print("(A) Agregar tipo proveedor")
        print("(M) Modifica tipo proveedor")
        print("(B) Baja tipo proveedor")
        print("(S) Salir")

        #Crea la variable opcion como upper
        opcion=input().upper()

        if opcion=="L":     #Si la opcion es "L" entonces mostrar el tipo proveedor
            mostrar_tipo_proveedor()
        elif opcion=="A":   #Si la opcion es "A" entonces agrega el tipo proveedor
            agregar_tipo_proveedor()
        elif opcion=="M":   #Si la opcion es "M" entonces modificar el tipo proveedor
            modifica_tipo_proveedor()
        elif opcion=="B":   #Si la opcion es "B" entonces eliminar el tipo proveedor
            eliminar_tipo_proveedor()
        elif opcion=="S":   #Si la opcion es "S" entonces romper el ciclo
            break