#Crea la lista de tipo proveedor
lista_tipo_proveedor=[]
class tipo_proveedor:   #Crea la clase tipo_proveedor
    #Crea el constructor para la clase tipo_proveedor
    def __init__(self, identificador_tipo_preveedor, descripcion_tipo_proveedor):
        self.identificador_tipo_proveedor=identificador_tipo_preveedor  #Se crea el valor incial del identificador_tipo_proveedor
        self.descripcion_tipo_proveedor=descripcion_tipo_proveedor      #Se crea el valor incial de la descripcion_tipo_proveedor
        
    #Crea los metodos para establecer los valores
    def set_identificador_tipo_proveedor(self,id_tipo_proveedor):           #Crea el metodo para establecer el valor de identificador_tipo_proveedor
        self.id_tipo_proveedor=id_tipo_proveedor
        
    def set_descripcion_tipo_proveedor(self,descripcion_tipo_proveedor):    #Crea el metodo para establecer el valor de descripcion_tipo_proveedor
        self.descripcion_tipo_proveedor=descripcion_tipo_proveedor
    
    #Crea los metodo para obtener los valores
    def get_identificador_tipo_proveedor(self):                             #Crea el metodo para obtener el valor de el identificador_tipo_proveedor
        return self.identificador_tipo_proveedor

    def get_descripcion_tipo_proveedor(self):                               #Crea el metodo para obtener el valor de la descripcion_tipo_proveedor
        return self.descripcion_tipo_proveedor