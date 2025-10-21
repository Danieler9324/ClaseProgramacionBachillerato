from Controllers.tipo_articulo_controller import *      #De la carpeta de controllers importa el archivo tipo_articulo
from Data.conectaBD import *                            #De la carpeta Data importa el archivo conectaBD


def list_tipo_articulo():
    conexion= connect()     #Conecta la base de datos retomando la funcion de connect
    lista_tipo_articulo=[]  #Creala lista_tipo_articulo
    with conexion:          #Con la funcion connect se crea un cursor
        with conexion.cursor() as cursor:
            sql= "SELECT * FROM tipo_articulo"  #Se crea un quer para mostrar los registros
            cursor.execute(sql)         #Ejecuta el quer
            resultado=cursor.fetchall() #Muestra los registros
            for row in resultado:       #Crea un ciclo para recorrer todos los registros
                lista_tipo_articulo.append(row) #Ingresa la lista a cada uno de los datos de la lista tipo articulo
    return lista_tipo_articulo      #Regresa los datos de la lista_tipo_articulo
                
def insert_tipo_articulo(descripcion):
    conexion=connect()      #Conecta la base de datos retomando la funcion de connect
    with conexion:          #Con la funcion connect se crea un cursor
        with conexion.cursor() as cursor:
            sql="INSERT INTO tipo_articulo (descripcion) VALUES (%s)"   #Se crea un quer para insertar los registros
            cursor.execute(sql, (descripcion,))     #Ejecuta el quer
            conexion.commit()                       #Guarda los datos insertados
            print("Registro ingresado")             #Imprime "Registro Ingresado" si se a agregado exitosamente
            
def update_tipo_articulo(id_tipo_articulo,nueva_descripcion):
    conexion= connect()     #Conecta la base de datos retomando la funcion de connect
    #Se usa el metodo try para comprobar si el tipo articulo existe
    try:
        with conexion:      #Con la funcion connect se crea un cursor
            with conexion.cursor() as cursor:
                sql = "UPDATE tipo_articulo SET descripcion=%s WHERE id_tipo_articulo=%s"   #Se crea un quer para actualizar el valor de la descripcion
                cursor.execute(sql, (nueva_descripcion, id_tipo_articulo))  #Ejecuta el quer
                conexion.commit()       #Guarda los datos insertados
                print("Registro actualizado")   #Imprime "Registro actualizado" en caso de que se haya actualizado correctamente
    except ValueError as error:     #Toma el metodo ValueError y lo imprime
        print(error)
        
def delete_tipo_articulo(id_tipo_articulo):
    conexion= connect()     #Conecta la base de datos retomando la funcion de connect
    #Se usa el metodo try para comprobar si el tipo articulo existe
    try:
        with conexion:    #Con la funcion connect se crea un cursor  
            with conexion.cursor() as cursor:   
                sql="DELETE FROM tipo_articulo WHERE id_tipo_articulo=%s"   #Se crea un quer para borrar el tipo de articulo seleccionado
                cursor.execute(sql, (id_tipo_articulo,))    #Ejecuta el quer
                conexion.commit()   #Guarda los datos insertados
                print("Registro eliminado") #Imprime "Registro eliminado" en caso de que se haya eliminado correctamente
    except ValueError as e:     #Toma el metodo ValueError y lo imprime
        print(e)