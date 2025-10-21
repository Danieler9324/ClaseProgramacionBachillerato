from Controllers.proveedor_controller import *
from Data.conectaBD import *

def list_proveedor():
    conexion=connect()     #Conecta con la base de datos
    lista_proveedor=[]
    with conexion:       #Con conexion crea un cursor
        with conexion.cursor() as cursor:
            sql="SELECT * FROM proveedor"   #Crea un query para mostrar todos los registros de la tabla de proveedor
            cursor.execute(sql)     #Ejecuta el query
            resultado=cursor.fetchall()     #Muestra los registros  
            for row in resultado:           #Crea un ciclo for para recorrer toda la tabla de proveedor
                lista_proveedor.append(row)
    return lista_proveedor

def insert_proveedor(razon_social,id_tipo_proveedor,rfc,direccion,telefono,correo_electronico,contacto):
    conexion=connect()     #Conecta con la base de datos
    try:       #Se usa el metodo try        
        with conexion:       #Con conexion crea un cursor
            with conexion.cursor() as cursor:
                #Crea un query para ingresar un proveedor a la tabla
                sql="INSERT INTO proveedor (razon_social,id_tipo_proveedor,rfc,direccion,telefono,correo_electronico,contacto) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                #Ejecuta el query
                cursor.execute(sql,(razon_social,id_tipo_proveedor,rfc,direccion,telefono,correo_electronico,contacto))
                conexion.commit()   #Guarda los cambios
                print("Registro ingresado")     #Imprime "Registro ingresado"
    except ValueError as error:     #Toma el metodo ValueError y lo imprime
        print(error)
        
def update_proveedor(nueva_razon_social,nuevo_rfc,nueva_direccion,nuevo_telefono,nuevo_correo_electronico,nuevo_contacto,id_proveedor):
    conexion=connect()     #Conecta con la base de datos
    try:       #Se usa el metodo try para verificar el proveedor
        with conexion:       #Con conexion crea un cursor
            with conexion.cursor() as cursor:
                #Crea un query para actualizar el proveedor seleccionado
                sql = "UPDATE proveedor SET razon_social=%s, rfc=%s, direccion=%s, telefono=%s, correo_electronico=%s, contacto=%s WHERE id_proveedor=%s"
                #Ejecuta el query
                cursor.execute(sql, (nueva_razon_social, nuevo_rfc, nueva_direccion, nuevo_telefono, nuevo_correo_electronico, nuevo_contacto, id_proveedor))
                conexion.commit()   #Guarda los cambios
                print("Registro actualizado")   #Imprime "Registro actualizado"
    except ValueError as error:     #Toma el metodo ValueError y lo imprime
        print(error)
        
def delete_proveedor(id_proveedor):
    conexion=connect()     #Conecta con la base de datos
    try:       #Se usa el metodo try para verificar el proveedor
        with conexion:       #Con conexion crea un cursor
            with conexion.cursor() as cursor:
                sql = "DELETE FROM proveedor WHERE id_proveedor=%s"     #Crea un query para eliminar el proveedor seleccionado
                cursor.execute(sql, (id_proveedor,))     #Se ejecuta el query
                conexion.commit()       #Guarda los cambios
                print("Registro eliminado")     #Imprime "Registro eliminado"
    except ValueError as e:     #Toma el metodo ValueErroor y lo imprime
        print(e)