from Controllers.tipo_proveedor import *    #Se llama el archivo tipo_proveedor que se encuentra en la carpeta Controllers

#Define menu_tipo_proveedor
def menu_tipo_proveedor():
    while True:     #Inicia el ciclo del menu de tipo proveedor
            print("(A) alta de tipo proveedor")  
            print("(L) lista de tipo proveedor")
            print("(U) Buscar indice de tipo proveedor")
            print("(M) Modficar tipo de proveedor")
            print("(B) Dar de baja tipo proveedor")
            print("(D) Ordena por el identificador del tipo de proveedor")
            print("(R) Ordena por la descripcion del tipo proveedor")
            print("(O) Volver al catalogo de Proveedores")
            
            # Retoma opcio para seleccionar las funciones del catalogo de tipo proveedor
            opcio = input().upper()

            if opcio=="A":      #Si la opcion es "A" entonces ejecutar alta_tipo_proveedor
                alta_tipo_proveedor()
            
            elif opcio=="L":    #Si la opcion es "L" entonces ejecutar listar_tipo_proveedor
                listar_tipo_proveedor()
            
            elif opcio=="U":    #Si la opcion es "U" entonces ejecutar busca_tipo_proveedor
                busca_tipo_proveedor()
            
            elif opcio=="M":    #Si la opcion es "M" entonces ejecutar modifica_tipo_proveedor
                modifica_tipo_proveedor()
            
            elif opcio=="B":    #Si la opcion es "B" entonces ejecutar baja_tipo_proveedor
                baja_tipo_proveedor()
                
            elif opcio=="D":    #Si la opcion es "D" entonces ejecutar ordena_id_tipo_proveedor
                ordena_id_tipo_proveedor()
                
            elif opcio=="R":    #Si la opcion es "R" entonces ejecutar ordena_desc_tipo_proveedor
               ordena_desc_tipo_proveedor()
            
            elif opcio=="O":  #Si la opcion es "O" entonces volver al menu principal
                guarda_tipo_proveedor()
                return  
            else:
                print("Opcion incorrecta")