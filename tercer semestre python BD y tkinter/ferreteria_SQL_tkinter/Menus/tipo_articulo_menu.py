from Controllers.tipo_articulo_controller import *      #De la carpeta de Controllers importa el archivo llamado tipo_articulo_controllers

#Funcion para el menu del tipo articulo
def menu_tipo_articulo():
    #Crea un ciclo while para la ejecucion del menu
    while True:
        #Imprime las opciones del menu
        print("(L) Listar registros tipo articulo") 
        print("(A) Agregar tipo articulo")
        print("(M) Modifica tipo articulo")
        print("(B) Baja tipo articulo")
        print("(S) Salir")
        #Crea la variable opcion como .upper
        opcion=input().upper()
            
        if opcion=="L": #Si opcion es "L" entonces ejecutar mostrar_registros 
            mostrar_registros_tipo_articulo()
        if opcion=="A": #Si opcion es "A" entonces ejecutar agregar_tipo_articulo
            agregar_tipo_articulo()
        if opcion=="M": #Si opcion es "M" entonces ejecutar modificar_tipo_articulo
            modificar_tipo_articulo()
        if opcion=="B": #Si opcion es "B" entonces ejecutar eliminar_tipo_articulo
            eliminar_tipo_articulo()    
        if opcion=="S": #Si opcion es "S" entonces romper el ciclo
            break