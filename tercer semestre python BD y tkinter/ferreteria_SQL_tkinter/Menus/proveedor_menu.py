from Controllers.proveedor_controller import *      #De la carpeta

#Funcion para el menu de proveedor
def menu_proveedor():
    #Crea un ciclo while para el menu
    while True:
        print("(L) Listar proveedores")
        print("(A) Agregar proveedores")
        print("(M) Modificar proveedores")
        print("(B) Baja proveedores")
        print("(S) Salir")
        
        #Crea la variable opcion como upper
        opcion=input().upper()
        
        if opcion=="L":     #Si opcion es "L" entonces mostrar proveedores
            mostrar_proveedor()
        
        elif opcion=="A":   #Si opcion es "A" entonces agregar proveedor
            agregar_proveedor()
            
        elif opcion=="M":   #Si opcion es "M" entonces modificar proveedor
            modificar_proveedor()
        
        elif opcion=="B":   #Si opcion es "B" entonces eliminar proveedor
            eliminar_proveedor()
        
        elif opcion=="S":   #Si opcion es "S" entonces romper el ciclo
            break