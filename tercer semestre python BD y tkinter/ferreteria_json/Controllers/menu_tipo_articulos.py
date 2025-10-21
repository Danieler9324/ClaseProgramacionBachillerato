from Controllers.tipo_articulos import *    #Se llama al archivo tipo_articulos que se encuentra en la carpeta Controllers

#Define menu_tipo_articulo
def menu_tipo_articulo(): 
    #Se crea la variable para el ciclo
    opcio=""
    while opcio!="V":   #Se crea el ciclo del menu de tipo articulo
            print("(A) alta de tipo articulo")  
            print("(L) lista de tipo articulo")
            print("(U) Buscar indice de tipo artculo")
            print("(M) Modficar tipo de articulo")
            print("(B) Dar de baja tipo articulo")
            print("(O) Ordena por el identificador del tipo de articulo")
            print("(R) Ordena por la descripcion del tipo articulo")
            print("(V) Volver al Catalogo de articulos")
            
            # Retoma opcio para seleccionar las funciones del catalogo de tipo articulo
            opcio = input().upper()

            if opcio=="A":      #Si la opcion es "A" entonces ejecutar alta_tipo_articulo
                alta_tipo_articulo()
            
            elif opcio=="L":    #Si la opcion es "L" entonces ejecutar lista_tip_articulo
                lista_tip_articulo()
            
            elif opcio=="U":    #Si la opcion es "U" entonces ejecutar busca_tipo_articulo
                busca_tipo_articulo()
            
            elif opcio=="M":    #Si la opcion es "M" entonces ejecutar modifica_tipo_articulo
                modifica_tipo_articulo()

            elif opcio=="B":    #Si la opcion es "B" entonces ejecutar baja_tipo_articulo
                baja_tipo_articulo()
                
            elif opcio=="O":    #Si la opcion es "O" entonces ejecutar ordena_id_tipo_articulo
                ordena_id_tipo_articulo()
                
            elif opcio=="R":    #Si la opcion es "R" entonces ejecutar ordena_desc_tipo_articulo
                ordena_desc_tipo_articulo()
            
            elif opcio=="V":    #Si la opcion es "V" entonces volver al menu
                guarda_tipo_articulo()
                return  
            else:
                print("Opcion incorrecta")
