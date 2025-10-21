from Controllers.menu_tipo_articulos import *       #Se llama al archivo menu_tipo_articulos que se encuentra en la carpeta de Controllers
from Controllers.menu_articulos import *            #Se llama al archivo menu_articulos que se encuentra en la carpeta de Controllers
from Controllers.menu_tipo_proveedores import *     #Se llama al archivo menu_tipo_proveedores se encuentra en la carpeta de Controllers
from Controllers.menu_proveedores import *          #Se llama al archvio menu_proveedores se encuentra en la carpeta de Controllers
from Controllers.menu_tipo_movimiento import *      #Se llama al archivo menu_tipo_movimiento se encuentra en la carpeta de Controllers


#Define menu_articulo
def menu_articulo():
    while True:  # Crea un ciclo para comenzar con la ejecucion del catalogo
        print("(1) Catalogo tipo Articulo") 
        print("(2) Catalogo Articulo")
        print("(V) Volver al menu principal")
        #Crea la variable opcio para seleccionar los menu de el catalogo de articulos 
        opcio=input().upper()

        if opcio=="1":      #Si opcio es "1" entonces ejecutar menu_tipo_articulo
            menu_tipo_articulo()
        elif opcio=="2":    #Si opcio es "2" entonces ejecutar menu_articulos
            menu_articulos()
        elif opcio=="V":    #Si opcio es "V" entonces regresar al menu principal
            return

#Define menu_proveedores
def menu_proveedores():
    opcio = ""  # Define la funcion para elegir
    while opcio != "O":  # Crea un ciclo para comenzar con la ejecucion del catalogo
        print("(1) Catalogo Tipo proveedor") 
        print("(2) Catalogo Proveedor")
        print("(O) Volver al menu principal")
        
        #Retoma opcio como upper
        opcio= input().upper()
        
        if opcio=="1":  #Si opcio es "1" entonces ejecutar menu_tipo_proveedor
            menu_tipo_proveedor()
            
        if opcio=="2":  #Si opcio es "2" entonces ejecutar menu_proveedor
            menu_proveedor()
       
#Se llaman a las funciones para cargar los datos que esten almacenados en la base de datos json
carga_tipo_articulo()
print("")
carga_tipo_proveedor()
print("")
carga_tipo_movimineto()
print("")
carga_articulo()
print("")
carga_proveedor()
#Define menu
def menu():
    while True:     #Crea un ciclo para comenzar la ejecucion del menu principal
        print("(1) Catalogo de Articulo")
        print("(2) Catalogo de Proveedor")
        print("(3) Catalogo tipo movimientos")
        print("(S) Salir")
        #Retoma opcio como upper
        opcio = input().upper()
        
        if opcio=="1":      #Si opcio es "1" entonces ejecutar menu_tipo_articulo
            menu_articulo()
            
        elif opcio=="2":   #Si opcio es "2" entonces ejecutar menu_proveedores
            menu_proveedores()
        
        elif opcio=="3":    #Si opcio es "3" entonces ejecutar menu_tipo_movimiento
            menu_tipo_movimiento()

        elif opcio=="S":    #Si opcio es "S" entonces romper el ciclo
            break
        
        else:
            print("Opcion incorrecta")

# Ejecutar el menu
menu()