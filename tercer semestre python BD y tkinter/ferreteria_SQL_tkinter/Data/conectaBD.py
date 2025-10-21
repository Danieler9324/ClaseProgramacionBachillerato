import pymysql  #Importa la libreria de pymysql

#Funcion para conectar la base de datos
def connect():
    return pymysql.connect(    #Metodo para conectar los datos de la base de datos
        host="localhost",       #El host de la base de datos
        user="root",            #El User de la base de datos
        password="",            #El password de la base de datos
        database="ferreteria",  #El nombre de la base de datos
        cursorclass=pymysql.cursors.DictCursor  #Crea un cursor
    )