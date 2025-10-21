from Controllers.tipo_proveedor_controller import *     #De la carpeta Controllers importa el archivo tipo_proveeedor
from Data.conectaBD import *

def list_tipo_proveedor():
    conexion=connect()      #Conecta con la base de datos
    lista_tipo_proveedor=[] #Crea la variable lista_tipo_proveedor como un vector vaciox
    with conexion:   #Con conexion crear un cursor
        with conexion.cursor() as cursor:
            sql="SELECT * FROM tipo_proveedor"      #Crea un query para mostrar todos los registros de la tabla tipo proveedor
            cursor.execute(sql)         #Ejecuta el query
            resultado=cursor.fetchall() #Muestra la tabla
            for row in resultado:       #Crea un ciclo for para recorrer toda la tabla de tipo proveedor
                lista_tipo_proveedor.append(row)    #La lista ingresa todos los datos de la lista_tipo_proveedor
    return lista_tipo_proveedor     #Regresa los datos de lista_tipo_proveedor

def insert_tipo_proveedor(descripcion):
    conexion=connect()      #Conecta la base de datos retomando la funcion de connect
    with conexion:          #Con la funcion connect se crea un cursor
        with conexion.cursor() as cursor:
            sql="INSERT INTO tipo_proveedor (descripcion) VALUES (%s)"   #Se crea un quer para insertar los registros
            cursor.execute(sql, (descripcion,))     #Ejecuta el quer
            conexion.commit()                       #Guarda los datos insertados
            print("Registro ingresado")             #Imprime "Registro Ingresado" si se a agregado exitosamente
            
def update_tipo_proveedor(id_tipo_proveedor,nueva_descripcion):
    conexion= connect()     #Conecta la base de datos retomando la funcion de connect
    #Se usa el metodo try para comprobar si el tipo articulo existe
    try:
        with conexion:      #Con la funcion connect se crea un cursor
            with conexion.cursor() as cursor:
                sql = "UPDATE tipo_proveedor SET descripcion=%s WHERE id_tipo_proveedor=%s"   #Se crea un quer para actualizar el valor de la descripcion
                cursor.execute(sql, (nueva_descripcion, id_tipo_proveedor))  #Ejecuta el quer
                conexion.commit()       #Guarda los datos insertados
                print("Registro actualizado")   #Imprime "Registro actualizado" en caso de que se haya actualizado correctamente
    except ValueError as error:     #Toma el metodo ValueError y lo imprime
        print(error)
        
def delete_tipo_proveedor(id_tipo_proveedor):
    conexion= connect()     #Conecta la base de datos retomando la funcion de connect
    #Se usa el metodo try para comprobar si el tipo articulo existe
    try:
        with conexion:    #Con la funcion connect se crea un cursor  
            with conexion.cursor() as cursor:   
                sql="DELETE FROM tipo_proveedor WHERE id_tipo_proveedor=%s"   #Se crea un quer para borrar el tipo de proveedor seleccionado
                cursor.execute(sql, (id_tipo_proveedor,))    #Ejecuta el quer
                conexion.commit()   #Guarda los datos insertados
                print("Registro eliminado") #Imprime "Registro eliminado" en caso de que se haya eliminado correctamente
    except ValueError as e:     #Toma el metodo ValueError y lo imprime
        print(e)