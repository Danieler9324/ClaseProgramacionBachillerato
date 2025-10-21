import json     #Importa la libreria de json
from Clases.clase_tipo_articulo import * #Se llama a el archivo clase_tipo_articulo que esta en la carpeta de Clases

#Define carga_tipo_articulo
def carga_tipo_articulo():
    global lista_tipo_articulo    #Retoma lista_tipo_articulo como global
    with open("Data/tipo_articulos.json", "r") as file: #Abre el archivo de tipo_articulos que se encuentra en la carpeta de Data con el metodo de leer
        Data=json.load(file)    #La libreria json carga el archivo
        for tipo in Data:       #Crea un ciclo for para cada elemento de Data
            print(tipo)         #Imprime el diccionario
            obj_tipo_articulo = tipo_articulo(tipo["identificador_tipo"], tipo["descripcion_tipo"]) #Crea obj_tipo_articulo retomando la clase tipo articulo
            lista_tipo_articulo.append(obj_tipo_articulo)   #Ingresa los datos a la lista_tipo_articulo

#Define guarda_tipo_articulo
def guarda_tipo_articulo():
    global lista_tipo_articulo  #Retoma lista_tipo_articulo como global
    data=[]     #Crea la variable data como vector
    for tipo in lista_tipo_articulo:    #Crea un ciclo for para recorrer toda la lista de tipo_articulo
        data.append(tipo.__dict__)      #Convierte a los tipo_articulo en diccionarios
    with open("Data/tipo_articulos.json", "w") as file:     #Abre el archivo tipo_articulo que se encuentra en la carpeta Data con el metodo de escritura
        json.dump(data,file, indent=4)  #Guarda la lista en formato json con una identacion de 4

#Define indi_tipo_articulo 
def indi_tipo_articulo(busca):
    global lista_tipo_articulo  #Retoma lista_tipo_articulo
    for ind in range (len(lista_tipo_articulo)):    #Crea un ciclo for que hace que recorra toda la lista
        if (lista_tipo_articulo[ind].get_id_tipo_a()== busca):  #Si el indice encontro a el id solicitado entonces regresa al indice
            return ind
    return -1   #Si no encontro el id solicitado regresar un -1

#Define busca_tipo_articulo 
def busca_tipo_articulo ():
    global lista_tipo_articulo  #Retoma lista_tipo_articulo como global
    busca= input ("Dame el indice a buscar: ")  #Lee el indice introducido
    indi_encontrado = indi_tipo_articulo(busca) #Retoma la definicion indi_tipo_articulo para buscar mediante el ID
    if indi_encontrado !=-1:    #Si indi_encontrado no sea -1 entonces imprimir los datos del tipo articulo
        print ("ID: ", lista_tipo_articulo[indi_encontrado].get_id_tipo_a(), "Descripcion: ", lista_tipo_articulo[indi_encontrado].get_descripcion_tipo_a())
    else:
        print("El tipo articulo no existe")


#define modifica_tipo_articulo
def modifica_tipo_articulo ():
    global lista_tipo_articulo  #Retoma lista_tipo_articulo como global
    lista_tip_articulo()        #Retoma la variable lista_tip_articulo para mostrar los tipos de datos ingresados
    busca= input ("Identificador: ")    #Lee el identificador ingresado
    indi_encontrado = indi_tipo_articulo(busca) #Retoma la definicion de indi_tipo_articulo para comenzar a buscar el tipo de articulo mediante el ID ingresado
    if indi_encontrado != -1:   #Si indi_encontrado no sea igual a -1 entonces imprimir los datos del tipo articulo a modificar
        print ("ID: ", lista_tipo_articulo[indi_encontrado].get_id_tipo_a(), "Descripcion: ", lista_tipo_articulo[indi_encontrado].get_descripcion_tipo_a())
        corregir= input("Quieres establecer los nuevos cambios S/N?: ").upper() #Da la opcion si modificarlo o no
        if corregir =="S":
            descripcion_nue=input("Ingresa la descripcion nueva: ")     #Lee la descripcion nueva
            lista_tipo_articulo[indi_encontrado].set_descripcion_tipo(descripcion_nue)  #Establece la descripcion nueva
    else:
        print("El tipo de articulo no existe")

#Define baja_tipo_articulo
def baja_tipo_articulo ():
    global lista_tipo_articulo  #Retoma lista_tipo_articulo
    lista_tip_articulo()    #Retoma la defincion de lista_tip_articulo para mostrar los tipos de articulos ya registrados
    busca= input ("Identificador del tipo articulo a dar de baja: ")   #Lee el ID del tipo de articulo a dar de baja
    indi_encontrado = indi_tipo_articulo(busca) #Retoma la definicion de indi_tipo_articulo para comenzar a buscar el tipo de articulo mediante el ID
    if indi_encontrado != -1:   #Si indi_encontrado no sea igual a -1 entonces imprimir los datos del tipo articulo a dar de baja
        print ("ID: ", lista_tipo_articulo[indi_encontrado].get_id_tipo_a(), "Descripcion: ", lista_tipo_articulo[indi_encontrado].get_descripcion_tipo_a())
        borrar= input("Quieres eliminar a el tipo articulo S/N?: ").upper() #Da la opcion si dar de baja o no el tipo articulo
        if borrar =="S":        #Si se selecciona S entonces eliminar el tipo articulo
            lista_tipo_articulo.pop(indi_encontrado)    #Funcion para eliminar al tipo articulo
    else:
        print("El tipo de articulo no existe")

#Se define alta_tipo_articulo
def alta_tipo_articulo():
    global lista_tipo_articulo  #Se retoma lista_tipo_articulo como global
    #Pide ingresar los datos
    print ("Ingresa los datos del tipo de articulo")
    id_ti=input("Identificador: ")  #Lee el Identificador ingresado
    while indi_tipo_articulo(id_ti)!=-1:    #Inicia un ciclo para comprobar si el ID existe
        print("ID existente")               #Si el ID ya existe imprime "ID existente" 
        id_ti=input("ID: ")                 #Pide que ingreses un ID que no existe
    des_ti=input("Descripcion: ")   #Lee la Descripcion ingresada
    #Retoma la clase tipo_articulo y te permite agregar datos a la clase
    lista_tipo_articulo.append(tipo_articulo(id_ti, des_ti))
    print(lista_tipo_articulo)

#Se define lista_tip_articulo
def lista_tip_articulo():
    global lista_tipo_articulo  #Se retoma lista_tipo_articulo como global
    for tipo in lista_tipo_articulo:    #Se crea un ciclo for para que busque en la lista
        #Imprime los tipos de articulos
        print ("ID: ", tipo.get_id_tipo_a(), "Descripcion: ", tipo.get_descripcion_tipo_a())

#Se define ordena_id_tipo_articulo
def ordena_id_tipo_articulo():
    global lista_tipo_articulo  #Se retoma lista_tipo_articulo como global
    #Ordena la lista mediante el identificador
    lista_tipo_articulo= sorted(lista_tipo_articulo, key=lambda lista_tipo_articulo:lista_tipo_articulo.identificador_tipo)
    
#Se define ordena_desc_tipo_articulo
def ordena_desc_tipo_articulo():
    global lista_tipo_articulo  #Se retoma lista_tipo_articulo como global
    #Ordena la lista mediante la descripcion
    lista_tipo_articulo= sorted(lista_tipo_articulo, key=lambda lista_tipo_articulo:lista_tipo_articulo.descripcion_tipo)