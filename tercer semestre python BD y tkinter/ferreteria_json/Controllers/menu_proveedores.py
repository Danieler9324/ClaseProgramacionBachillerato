from Controllers.proveedores import *   #Se llama el archivo proveedores que se encuentra en la carpeta de Controllers 

#Se define menu_proveedor
def menu_proveedor():
    while True:     #Inicia el ciclo del menu de proveedor
            print("(A) Alta Provedor")
            print("(L) Lista de Provedor")
            print("(U) Busca Provedor")
            print("(M) Modifica Provedor")
            print("(B) Baja Provedor")
            print("(O) Ordenar por el identificador de Provedor")
            print("(R) Ordenar por la descripcion de Provedor")
            print("(V) Volver al catalogo de Proveedores")

            #Retoma opcion como upper
            opcion= input().upper()

            if opcion=="A":     #Si la opcion es "A" entonces ejecutar alta_proveedor
                alta_proveedor()
                
            elif opcion=="L":   #Si la opcion es "L" entonces ejecutar listar_proveedor
                listar_proveedor()
                
            elif opcion =="U":  #Si la opcion es "U" entonces ejecutar busca_proveedor
                busca_proveedor()
                
            elif opcion=="M":   #Si la opcion es "M" entonces ejecutar modifica_proveedor
                modifica_proveedor()
                
            elif opcion=="B":   #Si la opcion es "B" entonces ejecutar baja_proveedor
                baja_proveedor()
                
            elif opcion=="O":   #Si la opcion es "O" entonces ejecutar ordena_id_proveedor
                ordena_id_proveedor()
                
            elif opcion=="R":   #Si la opcion es "R" entonces ejecutar ordena_desc_proveedor
                ordena_desc_proveedor()
                
            elif opcion=="V":   #Si la opcion es "V" entonces volver al menu principal
                guarda_proveedor()
                return
            
            else:
                print("Opcion incorrecta")