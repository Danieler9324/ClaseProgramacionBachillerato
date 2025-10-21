from Clases.clase_proveedor import *        #Importa el archivo clase_proveedor que esta en la carpeta de Clases  
from Controllers.tipo_proveedor import *    #Importa el archivo tipo_proveedor que esta en la carpte de Controllers

#Define carga_proveedor
def carga_proveedor():
    global lista_proveedor  #Retoma la lista_proveedor como global
    with open("Data/proveedor.json", "r") as file:  #Abre el archivo de proveedor que se encuentra en la carpeta de proveedor con el metodo de leer 
        Data=json.load(file)     #La libreria json carga el archivo
        for prov in Data:        #Crea un ciclo for para cada elemento de Data
            print (prov)         #Imprime el diccionario
            obj_proveedor=proveedor(prov["identificador_proveedor"],prov["razon_social"],prov["identificador_tipo_proveedor"],prov["rfc"],prov["direccion"],prov["telefono"],prov["correo_electronico"],prov["contacto"])  #Crea el obj_proveedor retomando la clase proveedor
            lista_proveedor.append(obj_proveedor) #ingresa los datos a la lista_proveedor

#Define guarda_proveedor
def guarda_proveedor():
    global lista_proveedor  #Retoma lista_proveedor como global
    Data=[]     #Crea la variable data como un vector
    for prov in lista_proveedor:    #Crea un ciclo for para recorrer toda la lista de proveedores
        Data.append(prov.__dict__)  #Convierte a los proveedores en diccionarios
    with open("Data/proveedor.json", "w") as file:  #Abre el archivo proveedor que se encuentra en la carpeta de Data con el metodo de escritura
        json.dump(Data,file, indent= 4) #Guarda la lista en formato json con una identificacion de 4


#Se define indi_proveedor
def indi_proveedor(busca):
    global lista_proveedor   #Se retoma lista_proveedor como global
    for pro in range (len(lista_proveedor)):    #Recorre el largo de la lista_proveedor
        if (lista_proveedor[pro].get_identificador_proveedor()==busca):  #Si el indice encontro al ID introducido entonces regresar al indice
            return pro
    return -1   #Si no se encontro el ID entonces regresar un -1

#Se define busca_proveedor
def busca_proveedor():
    global lista_proveedor   #Se retoma lista_proveedor como global
    busca=input("Dame el indice a buscar: ")    #Lee el indice a buscar
    indi_encontrado=indi_proveedor(busca)       #Retoma indi_proveedor para buscar mediante el ID
    if indi_encontrado !=-1:    #Si indi_encontrado no es -1 entonces imprimir los datos del proveedor buscado
         print("ID", lista_proveedor[indi_encontrado].get_identificador_proveedor(), "| Razon Social: ", lista_proveedor[indi_encontrado].get_razon_social(), "| Identificador tipo de articulo: ", lista_proveedor[indi_encontrado].get_identificador_tipo_proveedor(), "| RFC: ", lista_proveedor[indi_encontrado].get_rfc(),"| Direccion: ", lista_proveedor[indi_encontrado].get_direccion(), "| telefono: ", lista_proveedor[indi_encontrado].get_telefono(), "| correo electronico: ", lista_proveedor[indi_encontrado].get_correo_electronico(), "| Contacto: ", lista_proveedor[indi_encontrado].get_contacto())
    else:
        print("El proveedor no existe")

#Se define alta_proveedor
def alta_proveedor():
        global lista_proveedor   #Se retoma lista_proveedor como global
        ide=input("Identificador del proveedor: ")               #Lee el identicador
        while indi_proveedor(ide)!=-1:      #Incia un ciclo para comprobar si el ID existe
            print("ID existente")           #Imprime "ID existente" si el ID introducido ya existe
            ide= input("ID: ")              #Pide ingresar de nuevo el ID
        rz=input("Razon Social: ")                              #Lee la razon social
        listar_tipo_proveedor()                                 #Retoma la definicion de listar_tipo_proveedor
        indi_tipo_pro=input("Identificador del tipo de proveedor: ")    #Lee el identificador de tipo proveedor
        while indi_tipo_proveedor(indi_tipo_pro) ==-1:       #Inicia un ciclo para verificar el tipo proveedor introducido
            indi_tipo_pro=input("Dame el tipo proveedor correcto: ")     #Si el tipo de proveedor introducido no existe entonces volver a preguntar hasta que no se ingrese un tipo proveedor existente
        rf=input("RFC: ")                    #Lee el RFC
        di=input("Direccion: ")             #Lee la direccion
        te=input("Telefono: ")              #Lee el telefono
        ce=input("Correo electronico: ")    #Lee el correo electronico
        co=input("Contacto: ")              #Lee el contacto
        #Ingresa los datos a la clase proveedor
        lista_proveedor.append(proveedor(ide,rz,indi_tipo_pro,rf,di,te,ce,co))
        print(lista_proveedor)  #Imrpime los datos de la lista_proveedor


#Se define listar_proveedor
def listar_proveedor():
    global lista_proveedor   #Se retoma lista_proveedor como global
    for pro in lista_proveedor: #Crea un ciclo for que recorre toda la lista_proveedor
        #Imprime los datos de los proveedores
        print ("ID: ", pro.get_identificador_proveedor(),"Razon Social: ", pro.get_razon_social(),"ID tipo proveedor: ", pro.get_identificador_tipo_proveedor(), "RFC: ",pro.get_rfc(), "Direccion: ", pro.get_direccion(), "Telefono: ", pro.get_telefono(), "Correo electronico: ", pro.get_correo_electronico(), "Contacto: ", pro.get_contacto())
        
#Se define modifica_proveedor
def modifica_proveedor():
    global lista_proveedor   #Se retoma lista_proveedor como global
    listar_proveedor()       #Retoma la defincion listar_proveedor
    busca = input("Identificador del proveedor: ") #Lee el identificador del tipo proveedor
    indi_encontrado = indi_proveedor(busca)        #Retoma indi_tipo_proveedor para buscar mediante el ID
    if indi_encontrado != -1:       #Si indi_encontrado no es igual a -1 entonces imprimir los datos del proveedor a modificar
        proveedor = lista_proveedor[indi_encontrado]    #Variable para la lista_proveedor
        print("ID: ", proveedor.get_identificador_proveedor())                                   #Obtiene el valor de identificador_tipo_proveedor
        print("Razon Social: ", proveedor.get_razon_social())                                    #Obtiene el valor de la razon social
        print("Identificador del tipo articulo", proveedor.get_identificador_tipo_proveedor())   #Obtiene el valor del identficador
        print("RFC: ", proveedor.get_rfc())                                                      #Obtiene el valor del RFC
        print ("Direccion: ", proveedor.get_direccion())                                         #Obtiene el valor de la direccion
        print ("Telefono: ", proveedor.get_telefono())                                           #Obtiene el valor del telefono
        print ("Correo Electronico: ", proveedor.get_correo_electronico())                       #Obtiene el valor del correo electronico
        print("Contacto: ", proveedor.get_contacto())                                            #Obtiene el valor del contacto
        #Te da la opcion de establecer los cambios
        corregir = input("¿Quieres establecer los nuevos cambios S/N?: ").upper()           
        if corregir == "S": #Si la opicon es "S" entonces leer los nuevos cambios
            razon_social_nue = input("Ingresa la nueva razon social: ")     #Lee la razon social nueva
            rfc_nue= input("RFC nueva: ")                                   #Lee la RFC nueva
            direccion_nue= input("Direccion nueva: ")                       #Lee la direccion nueva
            telefono_nue=input("Telefono nuevo: ")                          #Lee le telefono nuevo
            correo_electronico_nue=input("Correo electronico nuevo:")       #Lee el correo electronico nuevo
            contacto_nue=input("Contacto nuevo: ")                          #Lee el contacto nuevo
            lista_proveedor[indi_encontrado].set_razon_social(razon_social_nue)                 #Establece el valor de la razon social
            lista_proveedor[indi_encontrado].set_rfc(rfc_nue)                                   #Establece el valor del rfc
            lista_proveedor[indi_encontrado].set_direccion(direccion_nue)                       #Establece el valor de la direccion
            lista_proveedor[indi_encontrado].set_telefono(telefono_nue)                         #Establece el valor del telefono
            lista_proveedor[indi_encontrado].set_correo_electronico(correo_electronico_nue)     #Establece el valor del correo electronico
            lista_proveedor[indi_encontrado].set_contacto(contacto_nue)                         #Establece el valor del contacto
        else:
            print("El tipo de proveedor no existe")

#Se define baja_proveedor
def baja_proveedor():
    global lista_proveedor   #Se retoma lista_proveedor como global
    listar_proveedor()       #Se retoma listar_proveedor
    busca = input("Identificador del proveedor: ") #Lee el identificador del proveedor
    indi_encontrado = indi_proveedor(busca)     #Retoma indi_proveedor para buscar mediante el ID
    if indi_encontrado != -1:   #Si indi_encontrado no es -1 entonces imprimir los datos del proveedor a eliminar
        proveedor = lista_proveedor[indi_encontrado]        #Variable para lista_proveedor
        print("ID: ", proveedor.get_identificador_proveedor())                                   #Obtiene el valor del identificador
        print("Razon Social: ", proveedor.get_razon_social())                                    #Obtiene el valor de la descripcion
        print("Identificador del tipo articulo", proveedor.get_identificador_tipo_proveedor())   #Obtiene el valor del identificador_tipo_proveedor
        print("RFC: ", proveedor.get_rfc())                                                      #Obtiene el valor del rfc
        print ("Direccion: ", proveedor.get_direccion())                                         #Obtiene el valor de la direccion
        print ("Telefono: ", proveedor.get_telefono())                                           #Obtiene el valor del telefono
        print ("Correo Electronico: ", proveedor.get_correo_electronico())                       #Obtiene el valor del correo electronico
        print("Contacto: ", proveedor.get_contacto())                                            #Obtiene el valor del contacto
        #Da la opcion si dar de baja o no al proveedor seleccionado
        corregir = input("¿Quieres darlo de baja S/N?: ").upper()
        if corregir == "S": #Si la opcion es igual a "S" entonces eliminar al proveedor de la lista_proveedor
            lista_proveedor.pop(indi_encontrado)
        else:
            print("El proveedor no existe")

#Se define ordena_id_proveedor
def ordena_id_proveedor():
    global lista_proveedor   #Se retoma lista_proveedor como global
    #Ordena lista_proveedor mediante el identificador
    lista_proveedor= sorted(lista_proveedor, key=lambda lista_proveedor:lista_proveedor.identificador_proveedor)
   
#Se define ordena_desc_proveedor
def ordena_desc_proveedor():
    global lista_proveedor   #Se retoma lista_proveedor como global
    #Ordena lista_proveedor mediante la razon social
    lista_proveedor= sorted(lista_proveedor, key=lambda lista_proveedor:lista_proveedor.razon_social)