import json       #Importa la libreria json  
from Clases.clase_tipo_movimiento import *  #Llama al archivo clase_tipo_movimiento que se encuentra en la carpeta de Clases

#Se defone carga_tipo_movimiento
def carga_tipo_movimineto():
    global lista_tipo_movimiento    #Retoma lista_tipo_movimiento como global
    with open("Data/tipo_movimiento.json", "r") as file:    #Abre el archivo tipo_movimiento en modo lectura
        data=json.load(file)    #Carga el archivo en la Data
        for tipo in data:       #Recorre la lista de Data
            print(tipo)         #Imprime el tipo
            #Ingresa los datos a la lista de data
            obj_tipo_movimiento=tipo_movimiento(tipo["id_tipo_movimiento"], tipo["descripcion_tipo_movimiento"], tipo["entrada_salida"], tipo["almacen_piso"])
            lista_tipo_movimiento.append(obj_tipo_movimiento)
#Se define guarda_tipo_movimiento
def guarda_tipo_movimiento():
    global lista_tipo_movimiento    #Se retoma lista_tipo_movimiento como global
    data=[]     #Se crea la variable data como una lista
    for tipo in lista_tipo_movimiento:  #Crea un ciclo for para recorrer toda la lista_tipo_movimiento
        data.append(tipo.__dict__)      #Convierte los tipo_movimiento en diccionarios
    with open ("Data/tipo_movimiento.json", "w") as file:   #Abre el archivo tipo_movimiento en modo escritura
        json.dump(data,file, indent= 4) #Guarda la lista en formato json con una identacion de 4

#Se define indi_tipo_movimiento
def indi_tipo_movimiento(busca):
    global lista_tipo_movimiento    #Se retoma lista_tipo_movimiento como global
    for ind in range (len(lista_tipo_movimiento)):  #Crea un ciclo for que hace que recorra toda la lista_tipo_movimiento
        if (lista_tipo_movimiento[ind].get_id_tipo_movimiento()==busca):    #Si el indice encontro al id solicitado entonces regresar el indice
            return ind
    return -1   #Si no encontro el id solicitado regresa un -1

#Se define busca_tipo_movimiento
def busca_tipo_movimiento():
    global lista_tipo_movimiento    #Se retoma lista_tipo_movimiento como global
    busca=int(input("Ingresa el ID del tipo movimiento: "))     #Lee el identificador introducido
    indi_encontrado=indi_tipo_movimiento(busca) #Retoma indi_tipo_movimiento para buscar mediante el ID
    if indi_encontrado!=-1: #Si indi_encontrado no es -1 entonces imprimir los datos del tipo movimiento
        print ("ID: ", lista_tipo_movimiento[indi_encontrado].get_id_tipo_movimiento(),"Descripcion: ", lista_tipo_movimiento[indi_encontrado].get_descripcion_tipo_movimiento(), "Entrada o Salida 1/-1: ", lista_tipo_movimiento[indi_encontrado].get_entrada_salida(), "Alamcen o Piso: ", lista_tipo_movimiento[indi_encontrado].get_almacen_piso())
    else:
        print("EL tipo de movimiento no existe")

#Se define alta_tipo_movimiento
def alta_tipo_movimiento():
    global lista_tipo_movimiento    #Se retoma lista_tipo_movimiento como global
    id_tipo_movimiento=int(input("Identificador del tipo movimiento: "))    #Lee el identificador del tipo movimiento ingresado
    while indi_tipo_movimiento(id_tipo_movimiento)!=-1: #Inicia un ciclo while para comprobar si el ID existe, si existe entonces vuelve a pedir un identificador que no exista
        print("Id tipo movimiento existente")
        id_tipo_movimiento=int(input("ID: "))
    descripcion_tipo_movimiento= input("descripcion del tipo movimiento: ") #Lee la descripcion ingresada
    entrada_salida=int(input("Es una entrada o salida -1/1?: "))    #Lee la entrada_salida del tipo movimiento ingresado
    while entrada_salida!=-1:       #Inicia un ciclo while para comprobar que entrada_salida sea -1 o 1 si es -1 o 1 entonces romper el ciclo y si no es -1 o 1 entonces volver a preguntar la entrada y salida
        if entrada_salida==1:       
            break
        print("Opcion incorrecta escoje -1/1")
        entrada_salida=int(input("entrada o salida -1/1:"))
    tipo_de_movimiento= input("Elige el tipo de movimiento Almacen/Piso (A/P): ").upper()   #Lee el tipo de movimiento ingresado
    while tipo_de_movimiento!="A":  #Inicia un ciclo while para comprobar el tipo de movimiento sea A o P si no es A o P entonces volver a preguntar Almacen/Piso
        if tipo_de_movimiento=="P":
            break
        print ("Opcion incorrecta")
        tipo_de_movimiento=input("Almacen/Piso (A/P): ").upper()
    #La lista_tipo_movimiento ingresa los datos a la clase de tipo_movimiento
    lista_tipo_movimiento.append(tipo_movimiento(id_tipo_movimiento,descripcion_tipo_movimiento,entrada_salida,tipo_de_movimiento))
    print (lista_tipo_movimiento)   #Imprime la lista_tipo_movimiento

#Se define listar_tipo_movimiento
def listar_tipo_movimiento():
    global lista_tipo_movimiento    #Se retoma lista_tipo_movimiento como global
    for tipo in lista_tipo_movimiento:  #Recorre la lista_tipo_movimiento
        #Imprime los datos de tipo movimiento
        print("ID: ", tipo.get_id_tipo_movimiento(), "| Descripcion: ", tipo.get_descripcion_tipo_movimiento(), "| Entrada/salida 1/-1: ", tipo.get_entrada_salida(), "| Almacen o Piso A/P: ", tipo.get_almacen_piso())

#Se define modifica_tipo_movimiento
def modifica_tipo_movimiento():
    global lista_tipo_movimiento    #Se retoma lista_tipo_movimiento como global
    listar_tipo_movimiento()        #Retoma la funcion de listar_tipo_movimiento para mostrar los datos
    busca=int(input("Identificador del tipo movimiento: "))     #Lee el identificador del tipo movimiento
    indi_encontrado=indi_tipo_movimiento(busca)     #Retoma la funcion indi_tipo_movimiento
    if indi_encontrado!=-1:     #Si indi_encontrado no es -1 
        #Variable para la lista_tipo_movimiento
        movimiento=lista_tipo_movimiento[indi_encontrado]
        print("ID: ", movimiento.get_id_tipo_movimiento())                      #Imprime el identificador del tipo movimiento
        print("Descripcion: ", movimiento.get_descripcion_tipo_movimiento())    #Imprime la descripcion del tipo movimiento
        print("Entrada o Salida 1/-1: ", movimiento.get_entrada_salida())       #Imprime la entrada_salida del tipo movimiento
        print("Almacen o Piso: ", movimiento.get_almacen_piso())                #Imprime el almacen_piso del tipo movimiento
        corregir=input("Quieres corregir los cambios S/N?: ").upper()   #Crea la variable para dar la opcion si modificar o no al tipo movimiento
        if corregir=="S":       #Si corregir es "S" entonces preguntar los nuevos datos
            de_nue=input("Descripcion nueva: ")           #Lee la descripcion nueva      
            es_nue=int(input("Entrada o Salida nueva 1/-1: "))  #Lee la entrada o salida nueva
            while es_nue!=-1:   #Comprueba que es_nue sea igual a -1
                if es_nue==1:   #Comprueba que es_nue sea igual a 1
                    break       #Si es_nue es igual a -1 o 1 entonces romper el ciclo   
                es_nue=int(input(" opcion incorrecta escoje 1/-1: "))   #Si es_nue no es igual a -1 o 1 entonces volver a preguntar
            alpi_nue=input("Almacen o Piso nuevo A/P: ").upper()    #Lee el almacen o piso nueva
            while alpi_nue!="A":    #Comprueba que alpi_nue sea igual a "A"
                if alpi_nue=="P":   #Comprueba que alpi_nue sea igual a "P"
                    break           #Si alpi_nue es igual a "A" o "P" entonces romper el ciclo
                alpi_nue=input("opcion incorrecta escoje A/P: ").upper()    #Si alpi_nue no es igual a "A" ni a "P" entonces volver a preguntar
            lista_tipo_movimiento[indi_encontrado].set_descripcion_tipo_movimiento(de_nue)  #Se retoma el metodo set para establecer el nuevo valor de la descripcion
            lista_tipo_movimiento[indi_encontrado].set_entrada_salida(es_nue)               #Se retoma el metodo set para establecer el nuevo valor de la entrada y salida
            lista_tipo_movimiento[indi_encontrado].set_almacen_piso(alpi_nue)               #Se retoma el metodo set para establecer el nuevo valor de el almacen o piso 

#Se define baja_tipo_movimiento      
def baja_tipo_movimiento():
    global lista_tipo_movimiento    #Se retoma lista_tipo_movimiento como global
    listar_tipo_movimiento()        #Retoma la funcion de listar_tipo_movimiento para mostrar los datos
    busca=int(input("Identificador del tipo movimiento: "))     #Lee el identificador del tipo movimiento
    indi_encontrado=indi_tipo_movimiento(busca)     #Retoma indi_tipo_movimiento
    if indi_encontrado!=-1:     #Si indi_encontrado no es -1 
        #Crea una variable para la lista_tipo_movimiento
        movimiento=lista_tipo_movimiento[indi_encontrado]
        print("ID: ", movimiento.get_id_tipo_movimiento())                      #Imprime el identificador del tipo movimiento
        print("Descripcion: ", movimiento.get_descripcion_tipo_movimiento())    #Imprime la descripcion del tipo movimiento
        print("Entrada o Salida 1/-1: ", movimiento.get_entrada_salida())       #Imprime la entrada o salida del tipo movimiento
        print("Almacen o Piso: ", movimiento.get_almacen_piso())                #Imprime el almacen o piso del tipo movimiento
        eliminar=input("Quieres dar de baja al tipo movimiento S/N?: ").upper()    #Crea la variable para dar la opcion si dar de baja o no al tipo movimiento
        if eliminar=="S":       #Si elimina es igual a "S" entonces eliminar el tipo movimiento
            lista_tipo_movimiento.pop(indi_encontrado)  #Metodo para eliminar el tipo movimiento
           
#Se define ordena_id_tipo_movimiento 
def ordena_id_tipo_movimiento():
    global lista_tipo_movimiento    #Se retoma lista_tipo_movimiento como global
    #Ordena la lista de tipo movimiento mediante el identificador
    lista_tipo_movimiento=sorted(lista_tipo_movimiento, key=lambda lista_tipo_movimiento:lista_tipo_movimiento.id_tipo_movimiento)
    
#Se define ordena_desc_tipo_movimiento
def ordena_desc_tipo_movimiento():
    global lista_tipo_movimiento    #Se retoma lista_tipo_movimiento como global
    #Ordena la lista de tipo movimiento mediante la descripcion
    lista_tipo_movimiento=sorted(lista_tipo_movimiento, key=lambda lista_tipo_movimiento:lista_tipo_movimiento.descripcion_tipo_movimiento)