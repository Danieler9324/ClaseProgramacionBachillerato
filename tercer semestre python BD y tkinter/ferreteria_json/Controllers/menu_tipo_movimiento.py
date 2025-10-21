from Controllers.tipo_movimiento import *   #Se llama el archivo tipo_movimiento que se encuentra en la carpeta de Controllers
#Define menu_tipo_movimiento
def menu_tipo_movimiento():
    while True:     #Se crea un ciclo while para el menu de tipo movimiento
        print("(A) Alta tipo movimiento")
        print("(L) Lista tipo movimiento")
        print("(U) Buscar tipo movimiento")
        print("(M) Modifica tipo movimiento")
        print("(B) Baja tipo movimiento")
        print("(O) Ordena por identificador del tipo movimiento")
        print("(D) Ordena por la descripcion del tipo movimiento")
        print("(V) Volver al menu principal")
        
        #Se crea la variable opcion como .upper
        opcion=input().upper()
        
        
        if opcion=="A":     #Si opcion es "A" entonces ejecutar alta_tipo_movimiento
            alta_tipo_movimiento()
        elif opcion=="L":   #Si opcion es "L" entonces ejecutar listar_tipo_movimiento
            listar_tipo_movimiento()
        elif opcion=="U":   #Si opcion es "U" entonces ejecutar busca_tipo_movimiento
            busca_tipo_movimiento()
        elif opcion=="M":   #Si opcion es "M" entonces ejecutar modifica_tipo_movimiento
            modifica_tipo_movimiento()
        elif opcion=="B":   #Si opcion es "B" entonces ejecutar baja_tipo_movimiento
            baja_tipo_movimiento()
        elif opcion=="O":   #Si opcion es "O" entonces ejecutar ordena_id_tipo_movimiento
            ordena_id_tipo_movimiento()
        elif opcion=="D":   #Si opcion es "D" entonces ejecutar ordena_desc_tipo_movimiento
            ordena_desc_tipo_movimiento()
        elif opcion=="V":   #Si opcion es "V" entonces guardar los datos y cerrar el menu
            guarda_tipo_movimiento()
            return