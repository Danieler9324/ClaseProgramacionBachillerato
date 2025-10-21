from Controllers.articulos import * #Se llama al archivo articulos que se encuentra en la carpeta de Controllers

#Define menu_articulos
def menu_articulos():
    while True:     #Inicia el ciclo del menu de Articulo
            print("(A) Alta Articulo")
            print("(L) Lista de Articulos")
            print("(U) Buscar articulo")
            print("(M) modifica articulo")
            print("(B) Dar de baja a articulo")
            print("(O) Ordenar por el identificador del articulo")
            print("(R) Ordenar por la descripcion del articulo")
            print("(V) Volver al catalogo de articulos")

            #Retoma opcion como upper
            opcion= input().upper()

            if opcion=="A":         #Si opcion es "A" entonces ejecutar alta_articulo
                alta_articulo()
            elif opcion=="L":       #Si opcion es "L" entonces ejecutar listar_articulo
                listar_articulo()
            elif opcion =="U":      #Si la opcion es "U" entonces ejecutar busca_articulo
                busca_articulo()
            elif opcion=="M":       #Si la opcion es "M" entonces ejecutar modifica_articulo
                modifica_articulo()
            elif opcion=="B":       #Si la opcion es "B" entonces ejecutar baja_articulo
                baja_articulo()
            elif opcion=="O":       #Si la opcion es "O" entonces ejecutar ordena_id_articulo
                ordena_id_articulo()
            elif opcion=="R":       #Si la opcion es "R" entonces ejecutar ordena_des_articulo
                ordena_desc_articulo()
            elif opcion=="V":       #Si la opcion es "V" entonces volver al menu principal
                guarda_articulo()
                return
            else:
                print("Opcion incorrecta")
            