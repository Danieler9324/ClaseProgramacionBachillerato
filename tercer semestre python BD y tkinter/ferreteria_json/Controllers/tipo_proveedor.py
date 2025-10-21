import json     #Importa la libreria de json
from Clases.clase_tipo_proveedor import * #Se llama al archivo tipo_proveedor que se encuentra en la carpeta Clases

#Define carga_tipo_proveedor
def carga_tipo_proveedor():
    global lista_tipo_proveedor #Retoma lista_tipo_proveedor como global
    with open ("Data/tipo_proveedores.json", "r") as file:  #Abre el archivo tipo_proveedores que se encuentra en la carpeta de Data, con el metodo de leer
        Data=json.load(file)    #La libreria json carga el archivo
        for tipo in Data:       #Crea un ciclo for para cada elemento en Data
            print(tipo)         #Imprime el diccionario
            obj_tipo_proveedor=tipo_proveedor(tipo["identificador_tipo_proveedor"], tipo["descripcion_tipo_proveedor"]) #Crea obj_tipo_proveedor retomando la clase tipo proveedor
            lista_tipo_proveedor.append(obj_tipo_proveedor) #Ingresa los datos a la lista_tipo_proveedor

#Define guarda_tipo_proveedor
def guarda_tipo_proveedor():
    global lista_tipo_proveedor #Retoma la lista_tipo_proveedor como global
    data=[]     #Crea la variable data como un vector
    for tipo in lista_tipo_proveedor:   #Crea un ciclo for para recorrer toda la lista de tipo_proveedor
        data.append(tipo.__dict__)      #Convierte a los tipo_proveedores en diccionarios
    with open ("Data/tipo_proveedores.json", "w")as file:   #Abre el archivo de tipo_proveedores que se encuentra en la carpeta Data con el metodo de escritura
        json.dump(data,file, indent=4)  #Guarda la lista en formato json con una identacion de 4


#Se define indi_tipo_proveedor
def indi_tipo_proveedor(busca):
    global lista_tipo_proveedor   #Se retoma lista_tipo_proveedor como global
    for tipo in range (len(lista_tipo_proveedor)):  #Recorre lo latog de lista_tipo_proveedor
        if (lista_tipo_proveedor[tipo].get_identificador_tipo_proveedor()==busca):  #Si el indice encontro el id solicitado entonces regresa el indice
            return tipo
    return -1   #Si no encontro el id solicitado regresar un-1

#Se define busca_tipo_proveedor
def busca_tipo_proveedor():
    global lista_tipo_proveedor   #Se retoma lista_tipo_proveedor como global
    busca=input("Dame el indice a buscar: ")        #Lee el indice a buscar
    indi_encontrado=indi_tipo_proveedor(busca)      #Retoma la definicion indi_tipo_proveedor para buscar mediante el ID
    if indi_encontrado !=-1:    #Si indi_encontrado no es igual a -1 entonces imprimir los datos del tipo proveedor ingresado
        print("ID:", lista_tipo_proveedor[indi_encontrado].get_identificador_tipo_proveedor(), "Descripcion: ", lista_tipo_proveedor[indi_encontrado].get_descripcion_tipo_proveedor())
    else:
        print("El tipo de proveedor no existe")

#Se define alta_tipo_proveedor
def alta_tipo_proveedor():
    global lista_tipo_proveedor   #Se retoma lista_tipo_proveedor como global
    id=input("Identificador del tipo de proveedor: ")   #Lee el identificador
    while indi_tipo_proveedor(id)!=-1:
        print("ID existente")
        id=input("ID: ")
    de=input("Descripcion del tipo de proveedor: ")     #Lee la descripcion
    lista_tipo_proveedor.append(tipo_proveedor(id,de))  #Ingresa datos a la clase tipo_proveedor
    print(lista_tipo_proveedor) #Imprime los datos que da la lista_tipo_proveedor

#Se define listar_tipo_proveedor
def listar_tipo_proveedor():
    global lista_tipo_proveedor   #Se retoma lista_tipo_proveedor como global
    for tipo in lista_tipo_proveedor:   #Crea un ciclo for para recorrer toda la lista
        #Imprime los datos de los tipos de articulos ingresados
        print("ID", tipo.get_identificador_tipo_proveedor(), "Descripcion: ", tipo.get_descripcion_tipo_proveedor())
        
#Se define modifica_tipo_proveedor
def modifica_tipo_proveedor():
    global lista_tipo_proveedor   #Se retoma lista_tipo_proveedor como global
    listar_tipo_proveedor()       #Retoma la defincion listar_tipo_proveedor
    busca = input("Identificador del tipo proveedor: ") #Lee el identificador del tipo proveedor
    indi_encontrado = indi_tipo_proveedor(busca)    #Retoma la defincion de indi_tipo_proveedor para buscar mediante el ID
    if indi_encontrado != -1:       #Si indi_encontrado no es igual a -1 entonces imprimir los datos del tipo proveedor a modificar
        proveedor = lista_tipo_proveedor[indi_encontrado]   #Variable para la lista_tipo_proveedor
        print("ID: ", proveedor.get_identificador_tipo_proveedor())         #Obtiene el valor del identificador del tipo articulo
        print("Descripcion: ", proveedor.get_descripcion_tipo_proveedor())  #Obtiene el valor de la descripcion del tipo articulo
        #Da la opcion si establecer los cambios
        corregir = input("¿Quieres establecer los nuevos cambios S/N?: ").upper()
        if corregir == "S":     #Si corregir es "S" entonces
            descripcion_nue = input("Ingresa la nueva descripcion: ")       #Lee la descripcion nueva
            lista_tipo_proveedor[indi_encontrado].set_descripcion_tipo_proveedor(descripcion_nue)   #Establece la descripcion nueva
        else:
            print("El tipo de proveedor no existe")

#Se define baja_tipo_proveedor
def baja_tipo_proveedor():
    global lista_tipo_proveedor   #Se retoma lista_tipo_proveedor como global
    listar_tipo_proveedor()       #Retoma la defincion listar_tipo_proveedor
    busca = input("Identificador del tipo de proveedor: ")  #Lee el identificador del tipo articulo
    indi_encontrado = indi_tipo_proveedor(busca)            #Retoma la definicion de indi_tipo_proveedor para  buscar mediante el ID
    if indi_encontrado != -1:         #Si indi_encontrado no es igual a -1 entonces imprimir los datos del tipo_proveedor a eliminar
        proveedor = lista_tipo_proveedor[indi_encontrado]    #Variable para lista_tipo_proveedor    
        print("ID: ", proveedor.get_identificador_tipo_proveedor())         #Obtiene el valor del identificador_tipo_proveedor
        print("Descripcion: ", proveedor.get_descripcion_tipo_proveedor())  #Obtiene el valor de la descripcion_tipo_proveedor
        #Da la opcion si dar de baja a el tipo proveedor
        baja = input("¿Quieres dar de baja a el tipo de proveedor S/N?: ").upper()
        if baja == "S": #Si baja es igual a "S" entonces eliminar al tipo proveedor de la lista
            lista_tipo_proveedor.pop(indi_encontrado)
        else:
            print("El tipo de proveedor no existe")

#Se define ordena_id_tipo_proveedor
def ordena_id_tipo_proveedor():
    global lista_tipo_proveedor   #Se retoma lista_tipo_proveedor como global
    #Ordena la lista_tipo_proveedor mediante el identificador
    lista_tipo_proveedor= sorted(lista_tipo_proveedor, key=lambda lista_tipo_proveedor:lista_tipo_proveedor.identificador_tipo_proveedor)

#Se define ordena_desc_tipo_proveedor
def ordena_desc_tipo_proveedor():
    global lista_tipo_proveedor   #Se retoma lista_tipo_proveedor como global
    #Ordena lista_tipo_proveedor mediante la descripcion
    lista_tipo_proveedor= sorted(lista_tipo_proveedor, key=lambda lista_tipo_proveedor:lista_tipo_proveedor.descripcion_tipo_proveedor)