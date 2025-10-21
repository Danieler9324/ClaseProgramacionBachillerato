#Se crea la lista_tipo_articulo
lista_tipo_articulo=[]
class tipo_articulo:    #Crea la clase tipo_articulo
    #Crea el constructor para la clase tipo_articulo
    def __init__ (self, identificador,descripcion):
        self.identificador_tipo=identificador   #Se crea el valor inicial del identificador
        self.descripcion_tipo=descripcion       #Se crea el valor inicial de la descripcion

    #Se crean los metodos para establecer los valores
    def set_id_tipo(self,id_tipo):              #Se establece el valor de el identificador del tipo de articulo
        self.id_tipo=id_tipo    
    
    def set_descripcion_tipo(self,des_tipo):    #Se establece el valor de la descripcion del tipo de articulo
        self.descripcion_tipo=des_tipo

    #Se crean los metodos para obtener los valores 
    def get_id_tipo_a(self):                    #Se obtiene el valor del identificador del tipo articulo   
        return self.identificador_tipo
    
    def get_descripcion_tipo_a(self):           #Se obtiene el valor de la descripcion del tipo articulo
        return self.descripcion_tipo