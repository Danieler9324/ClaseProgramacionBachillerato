from Controllers.articulo_controller import *       #De la carpeta Controllers importa el archivo articulo_controller

def menu_articulo():
    #Crea un ciclo while para el menu
    while True:
        print("(L) Listar articulos")
        print("(A) Agregar articulo")
        print("(M) Modificar articulos")
        print("(B) Baja articulos")
        print("(S) Salir")
        
        #Crea la variable opcion como upper
        opcion=input().upper()
        
        if opcion=="L":     #Si opcion es "L" entonces mostrar los articulos
            mostrar_articulo()
        
        elif opcion=="A":   #Si opcion es "A" entonces agregar el articulo
            agregar_articulo()
            
        elif opcion=="M":   #Si opcion es "M" entonces modificar el articulo
            modificar_articulo()

        elif opcion=="B":   #Si opcion es "B" entonces eliminar el articulo
            eliminar_articulo()

        elif opcion=="S":   #Si opcion es "S" entonces romper el ciclo
            break