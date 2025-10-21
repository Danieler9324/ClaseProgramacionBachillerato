from Controllers.articulo_controller import *
from Data.conectaBD import *

def list_articulo():
    conexion=connect()      #Crea la conexion con la base de datos
    lista_articulo=[]
    with conexion:          #Con conexion crea un cursor
        with conexion.cursor() as cursor:
            sql="SELECT * FROM articulo"        #Crea un query para mostrar los registros de la tabla articulo
            cursor.execute(sql)     #Ejecuta el query
            resultado=cursor.fetchall()     #Muestra la tabla
            for row in resultado:           #Crea un ciclo for para recorrer toda la tabla de articulo
                lista_articulo.append(row)
    return lista_articulo

def insert_articulo(descripcion,id_tipo_articulo,costo,precio_mayoreo,precio_menudeo,cantidad_almacen,cantidad_tienda):
    connexion=connect()
    try:        #Se usa el metodo try para verificar el tipo_articulo
        with connexion:          #Con conexion crea un cursor
            with connexion.cursor() as cursor:
                #Crea un query para introducir el articulo a la tabla
                sql="INSERT INTO articulo (descripcion,costo,precio_mayoreo,precio_menudeo,cantidad_almacen,cantidad_tienda,id_tipo_articulo) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                #Ejecuta el query
                cursor.execute(sql,(descripcion,costo,precio_mayoreo,precio_menudeo,cantidad_almacen,cantidad_tienda,id_tipo_articulo))
                connexion.commit()       #Guarda los datos
                print("Registro ingresado") #Imprime "Registro ingresado"
    except ValueError as error:     #Toma el metodo ValueError y lo imprime
        print(error)
        
def update_articulo(id_articulo,nueva_descripcion,nuevo_costo,nuevo_precio_mayoreo,nuevo_precio_menudeo,nueva_cantidad_almacen,nueva_cantidad_tienda):
    conexion=connect()      #Crea la conexion con la base de datos
    try:        #Se usa el metodo try para verificar el articulo
        with conexion:          #Con conexion crea un cursor
            with conexion.cursor() as cursor:
                #Crea un query para actualizar el registro de articulo seleccionado
                sql = "UPDATE articulo SET descripcion=%s, costo=%s, precio_mayoreo=%s, precio_menudeo=%s, cantidad_almacen=%s, cantidad_tienda=%s WHERE id_articulo=%s"
                #Ejecuta el query
                cursor.execute(sql, (nueva_descripcion, nuevo_costo, nuevo_precio_mayoreo, nuevo_precio_menudeo, nueva_cantidad_almacen, nueva_cantidad_tienda, id_articulo))
                conexion.commit()   #Guarda los datos
                print("Registro actualizado")   #Imprime "Registro actualizado"
    except ValueError as error:     #Toma el metodo ValueError y lo imprime 
        print(error)
        
def delete_articulo(id_articulo):
    conexion=connect()      #Crea la conexion con la base de datos
    try:        #Usa el metodo try para verificar el articulo
        with conexion:          #Con conexion crea un cursor
            with conexion.cursor() as cursor:
                sql = "DELETE FROM articulo WHERE id_articulo=%s"   #Crea un query para eliminar el articulo seleccionado
                cursor.execute(sql, (id_articulo))  #Ejecuta el query
                conexion.commit()   #Guarda los cambios
                print("Registro eliminado")     #Imprime "Registro eliminado"
    except ValueError as error:     #Toma el metodo ValueError y lo imprime 
        print(error)