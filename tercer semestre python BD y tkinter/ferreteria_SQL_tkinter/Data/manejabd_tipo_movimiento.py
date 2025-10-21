from Controllers.tipo_movimiento_controller import *

def list_tipo_movimiento():
    conexion= connect()     #Conecta la base de datos retomando la funcion de connect
    lista_tipo_movimiento=[]  #Creala lista_tipo_movimiento
    with conexion:          #Con la funcion connect se crea un cursor
        with conexion.cursor() as cursor:
            sql= "SELECT * FROM tipo_movimiento"  #Se crea un quer para mostrar los registros
            cursor.execute(sql)         #Ejecuta el quer
            resultado=cursor.fetchall() #Muestra los registros
            for row in resultado:       #Crea un ciclo para recorrer todos los registros
                lista_tipo_movimiento.append(row) #Ingresa la lista a cada uno de los datos de la lista tipo movimiento
    return lista_tipo_movimiento      #Regresa los datos de la lista_tipo_movimiento
                
def insert_tipo_movimiento(descripcion,entrada_salida,almacen_piso):
    conexion=connect()           #Hace la conexion con la base de datos
    with conexion:               #Con conexion crea un cursor
        with conexion.cursor() as cursor:
            sql="INSERT INTO tipo_movimiento (descripcion,entrada_salida,almacen_piso) VALUES (%s,%s,%s)"   #Crea un query para agrega el tipo movimiento a la tabla
            cursor.execute(sql,(descripcion,entrada_salida,almacen_piso))   #Ejecuta el query 
            conexion.commit()   #Guarda los cambios
            print("Registro ingresado") #Imprime "Registro ingresado"
            
def update_tipo_movimiento(id_tipo_movimiento,nueva_descripcion,nueva_entrada_salida,nueva_almacen_piso):
    conexion=connect()      #Hace la conexion con la base de datos
    try:        #Se toma el metodo try para verificar si el tipo movimiento existe para poder modificarlo
        with conexion:  #Con conexion crea un cursor
            with conexion.cursor() as cursor:   
                sql = "UPDATE tipo_movimiento SET descripcion=%s,entrada_salida=%s,almacen_piso=%s WHERE id_tipo_movimiento=%s" #Crea un query para actualizar el tipo movimiento
                cursor.execute(sql, (nueva_descripcion, nueva_entrada_salida, nueva_almacen_piso, id_tipo_movimiento)) #Ejecuta el query
                conexion.commit()   #Guarda los cambios
                print("Registro actualizado")   #Imprime "Registro actualizado"
    except ValueError as error:     #Toma el metodo ValueError y lo imprime
        print(error)


def delete_tipo_movimiento(id_tipo_movimiento):
    conexion=connect()  #Conecta el servidor
    try:        #Se utiliza el metodo try 
        with conexion:      #Con conexion crea un cursor
            with conexion.cursor() as cursor:       
                sql = "DELETE FROM tipo_movimiento WHERE id_tipo_movimiento=%s" #Se crea un query para eliminar al tipo movimiento
                cursor.execute(sql, (id_tipo_movimiento,))  #Se ejecuta el query
                conexion.commit()       #Guarda los cambios
                print("Registro eliminado") #Imprime "Registro eliminados"
    except ValueError as error:     #Toma el metodo ValueError y lo imprime
        print(error)