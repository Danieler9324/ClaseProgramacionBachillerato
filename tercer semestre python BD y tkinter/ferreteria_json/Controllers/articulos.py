from Clases.clase_articulo import *         #Se llama a el documento clase_articulo que se encuentra en la carpeta Clases
from Controllers.tipo_articulos import *    #Se llama a el documento tipo_articulos que se encuentra en la carpeta de Controllers
from Controllers.tipo_movimiento import *

#Define carga_articulo
def carga_articulo():
    global lista_articulo  #Retoma lista_articulo como global
    with open ("Data/articulo.json", "r") as file:  #Abre articulo que se encuentra en la carpeta de Data como un metodo de leer
        Data=json.load(file)    #La libreria json carga el archivo
        for art in Data:        #Crea un ciclo for para cada el elemento de Data
            print(art)          #Imprime el diccionario
            obj_articulo=articulo(art["identificado"],art["descripcio"],art["identificador_tipo_articul"],art["cost"],art["precio_mayore"],art["precio_menude"],art["cantidad_almace"],art["cantidad_tiend"])   #Crea el obj_articulo retomando la clase articulo
            lista_articulo.append(obj_articulo) #Ingresa los datos a la lista_articulo

#Define guarda_articulo
def guarda_articulo():
    global lista_articulo   #Retoma lista_articulo global
    Data=[]     #Crea la variable data como un vector
    for art in lista_articulo:  #Crea un ciclo for para recorrer toda la lista de articulo
        Data.append(art.__dict__)   #Convierte a los articulos en diccionario 
    with open("Data/articulo.json", "w")  as file:  #Abre el archivo articulo que se encuentra en la carpeta de Data con el metodo de escritura 
        json.dump(Data,file, indent= 4) #Guarda la lista en formato json con una identacion de 4

#Se define indi_articulo
def indi_articulo(busca):
    global lista_articulo      #Se retoma lista_articulo como global   
    for ind in range (0,len(lista_articulo),1):     #Recorre lo largo de la lista
        if (lista_articulo[ind].get_Identifica()==busca):   #busca mediante el identificador
            return ind      #Regresa el indice
    return -1   #Si no encuentra nada entonces regresara un -1

#Se define busca_articulo
def busca_articulo():
    global lista_articulo      #Se retoma lista_articulo como global
    busca=input("Dame el indice a buscar: ")    #Lee el indice introducido
    ind_encontrado=indi_articulo(busca)         #Retoma la funcion de buscar mediante el identificador
    if ind_encontrado!=-1:                      #Si indi_encontrado no es -1 entonces imprimir los datos del articulo buscado
        print("ID: ", lista_articulo[ind_encontrado].get_Identifica() ,"| Descripcion: ", lista_articulo[ind_encontrado].get_Descripci() ,"| Identificador de tipo articulo: ", lista_articulo[ind_encontrado].get_Identificador_Tipo_Articu() ,"| Costo: ", lista_articulo[ind_encontrado].get_Cos() ,"| Precio mayoreo: ", lista_articulo[ind_encontrado].get_Precio_Mayor() ,"| Precio menudeo", lista_articulo[ind_encontrado].get_Precio_Menud() ,"| Cantidad en el almacen: ", lista_articulo[ind_encontrado].get_Cantidad_Almac() ,"| Cantidad en la Tienda: ", lista_articulo[ind_encontrado].get_Cantidad_Tien())
    else:
        print ("El articulo no existe")

#Se define alta_articulo
def alta_articulo():
        global lista_articulo      #Se retoma lista_articulo como global  
        print ("Ingresa los datos del articulo")    #Solicita ingresar los datos    
        id=input("Identificador: ")                 #Lee el identificador introducido
        while indi_articulo (id)!=-1:          
            print("ID existente")
            id= input("ID: ")
        des=input("Descripcion: ")               #Lee la descripcion introducida
        lista_tip_articulo()                        #Se retoma la definicion de lista_tip_articulo
        ind_tipo=input("Dame el tipo articulo: ")  #Lee el identificador del tipo articulo
        while indi_tipo_articulo(ind_tipo)==-1:     #Inicia un ciclo para verificar el tipo articulo introducido
            ind_tipo=input("Dame el tipo articulo correcto: ")  #Si el tipo de articulo introducido no existe entonces volver a preguntar hasta que no se ingrese un tipo articulo existente
        co=input("Costo: ")                         #Lee el costo del articulo
        precio_ma=input("Precio de mayoreo: ")      #Lee el precio de mayoreo del articulo
        precio_me=input("Precio de menudeo: ")      #Lee el precio de menudeo del articulo
        can_al=input("Cantidad en el almacen: ")    #Lee la cantidad en el almacen que hay del articulo
        can_ti=input("Cantidad en la Tienda: ")     #Lee la cantidad en la tienda que hay del articulo
        
        #Funcion para intoducir datos a la clase articulo
        lista_articulo.append(articulo(id, des,ind_tipo, co, precio_ma, precio_me, can_al, can_ti))
        print (lista_articulo)  #Imprime los valor de la lista_articulo

#Se define listar_articulo
def listar_articulo():
    global lista_articulo      #Se retoma lista_articulo como global
    for art in lista_articulo: #Crea un ciclo for para recorrer la lista_articulo
        #Imprime los datos de los articulos
        print("ID: ", art.get_Identifica() ,"| Descripcion: ", art.get_Descripci() ,"| Identifcador de tipo articulo: ", art.get_Identificador_Tipo_Articu() ,"| Costo: ", art.get_Cos() ,"| Precio mayoreo: ", art.get_Precio_Mayor() ,"| Precio menudeo: ", art.get_Precio_Menud() ,"| Cantidad en el almacen: ", art.get_Cantidad_Almac() ,"| Cantidad en la Tienda: ", art.get_Cantidad_Tien())

#Se define modifica_articulo
def modifica_articulo():
    global lista_articulo      #Se retoma lista_articulo como global
    listar_articulo()          #Retoma la defincion de listar_articulo
    busca = input("Identificador del artículo: ")   #Lee el identificador del articulo
    indi_encontrado = indi_articulo(busca)  #Se retoma la funcion de buscar mediante el identificador del articulo
    if indi_encontrado != -1:       #Si indi_encontrado no es -1 entonces imprimir los datos del articulo a modificar
        articulo = lista_articulo[indi_encontrado]  #Variable para la lista_articulo
        print("ID: ", articulo.get_Identifica())                                                #Obtiene el valor del ID
        print("Descripcion: ", articulo.get_Descripci())                                        #Obtiene el valor de la descripcion                            
        print("Identificador de tipo articulo: ", articulo.get_Identificador_Tipo_Articu())     #Obtiene el valor de el identificador de tipo articulo
        print("Costo: ", articulo.get_Cos())                                                    #Obtiene el valor del costo
        print("Precio mayoreo: ", articulo.get_Precio_Mayor())                                  #Obtiene el precio de mayoreo   
        print("Precio menudeo: ", articulo.get_Precio_Menud())                                  #Obtiene el precio de menudeo
        print("Cantidad en el almacen: ", articulo.get_Cantidad_Almac())                        #Obtiene la cantidad en el almacen
        print("Cantidad en la tienda: ", articulo.get_Cantidad_Tien())  
        #Te da la opcion de establecer los cambios 
        corregir = input("¿Quieres establecer los nuevos cambios S/N?: ").upper()               
        if corregir == "S":     #Si corregir es igual a "S" entonces preguntar los nuevos datos del articulo
            descripcion_nue = input("Ingresa la nueva descripcion: ")       #Lee la descripcion nueva
            costo_nue = input("Ingresa el costo nuevo: ")                   #Lee el costo nuevo
            Precio_ma_nue = input("Ingresa el precio de mayoreo nuevo: ")   #Lee el precio de mayoreo nuevo
            precio_me_nue = input("Ingresa el precio de menudeo nuevo: ")   #Lee el precio de menudeo nuevo
            can_al_nue = input("Ingresa la nueva cantidad en el almacen: ") #Lee la nueva cantidad en el almacen
            can_tie_nue = input("Ingresa la nueva cantidad en la tienda: ") #Lee la nueva cantidad en la tienda
            
            lista_articulo[indi_encontrado].set_descripcio(descripcion_nue) #Establece la descripcion nueva
            lista_articulo[indi_encontrado].set_cos(costo_nue)              #Establece el costo nuevo
            lista_articulo[indi_encontrado].set_precio_mayor(Precio_ma_nue) #Establece el precio de mayoreo nuevo
            lista_articulo[indi_encontrado].set_precio_menud(precio_me_nue) #Establece el precio de menudeo nuevo
            lista_articulo[indi_encontrado].set_cantidad_almace(can_al_nue) #Establece la nueva cantidad en el almacen  
            lista_articulo[indi_encontrado].set_cantidad_tien(can_tie_nue)  #Establece la nueva canridad en la tienda
        else:
            print("El artículo no existe")

#Se define baja_articulo
def baja_articulo():
    global lista_articulo      #Se retoma lista_articulo como global
    listar_articulo()          #Se retoma la definicion de listar articulo
    busca = input("Identificador del artículo: ") #Lee el identificador del articulo   
    indi_encontrado = indi_articulo(busca)  #Se retoma la funcion de buscar mediante el identificador del articulo
    if indi_encontrado != -1:           #Si indino es -1 entonces imprimir los datos del articulo a dar de baja
        articulo = lista_articulo[indi_encontrado]  #Variable para la lista_articulo
        print("ID: ", articulo.get_Identifica())                                                #Obtiene el valor del identificador
        print("Descripcion: ", articulo.get_Descripci())                                        #Obtiene el valor de la descripcion
        print("Identificador de tipo articulo: ", articulo.get_Identificador_Tipo_Articu())     #Obtiene el valor del identificador de tipo articulo
        print("Costo: ", articulo.get_Cos())                                                    #Obtiene el valor del costo
        print("Precio mayoreo: ", articulo.get_Precio_Mayor())                                  #Obtiene el valor del precio de mayoreo
        print("Precio menudeo: ", articulo.get_Precio_Menud())                                  #Obtiene el valor del precio de menudeo
        print("Cantidad en el almacen: ", articulo.get_Cantidad_Almac())                        #Obtiene el valor de la cantidad en el almacen
        print("Cantidad en la tienda: ", articulo.get_Cantidad_Tien())                          #Obtiene el valor de la cantidad en la tienda
        #Te da la opcion si dar de baja al articulo
        baja = input("¿Quieres dar de baja al articulo S/N?: ").upper()
        if baja == "S": #Si baja es igual a "S" entonces eliminar al articulo con la funcion pop
            lista_articulo.pop(indi_encontrado)
        else:
            print("El artículo no existe")

#Se define ordena_id_articulo
def ordena_id_articulo():
    global lista_articulo      #Se retoma lista_articulo como global
    #Ordena lista_articulo mediante el identificador
    lista_articulo= sorted(lista_articulo, key=lambda lista_articulo:lista_articulo.identificado)
    
#Se define ordena_desc_articulo
def ordena_desc_articulo():
    global lista_articulo      #Se retoma lista_articulo como global
    #Ordena la lista_articulo mediante la descripcion 
    lista_articulo= sorted(lista_articulo, key=lambda lista_articulo:lista_articulo.descripcio)