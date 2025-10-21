#Crea la lista de proveedor
lista_proveedor=[]
#Crea la clase proveedor
class proveedor:
    #Crea el constructor para la clase proveedor
    def __init__(self,identificador_proveedor,razon_social,identificador_tipo_proveedor,rfc,direccion,telefono,correo_electronico,contacto):
        self.identificador_proveedor=identificador_proveedor            #Crea el valor inical de el identificador_proveedor
        self.razon_social=razon_social                                  #Crea el valor incial de la razon_social
        self.identificador_tipo_proveedor=identificador_tipo_proveedor  #Crea el valor inical del identificador_tipo_proveedor
        self.rfc=rfc                                                    #Crea el valor inical del rfc
        self.direccion=direccion                                        #Crea el valor incial de la direccion
        self.telefono=telefono                                          #Crea el valor incial del telefono
        self.correo_electronico=correo_electronico                      #Crea el valor incial del correo electronico
        self.contacto=contacto                                          #Crea el valor incial del contacto

    
    #Crea los metodos para esbalecer los valores
    def set_identificador_proveedor(self,identificador_proveedor):                  #Se crea el metodo para establecer el valor del identificador
        self.identificador_proveedor=identificador_proveedor
        
    def set_razon_social(self,razon_social):                                        #Se crea el metodo para establecer el valor de la razon_social
        self.razon_social=razon_social
        
    def set_identificador_tipo_proveedor(self,identificador_tipo_proveedor):        #Se crea el metodo para establecer el valor del identificador_tipo_proveedor
        self.identificador_tipo_proveedor=identificador_tipo_proveedor
        
    def set_rfc(self,rfc):                                                          #Se crea el metodo para establecer el valor del rfc
        self.rfc=rfc
        
    def set_direccion(self,direccion):                                              #Se crea el metodo para establecer el valor de la direccion
        self.direccion=direccion
        
    def set_telefono(self,telefono):                                                #Se crea el metodo para establecer el valor del telefono
        self.telefono=telefono
        
    def set_correo_electronico(self,correo_electronico):                            #Se crea el metodo para establecer el valor del correo electronico
        self.correo_electronico=correo_electronico
        
    def set_contacto(self,contacto):                                                #Se crea el metodo para establecer el valor del contacto
        self.contacto=contacto
    
    #Crea los metodos para obtener los valores
    def get_identificador_proveedor(self):                                           #Se crea el metodo para obtener el valor del identificador
        return self.identificador_proveedor
        
    def get_razon_social(self):                                                      #Se crea el metodo para obtener el valor de la razon social
        return self.razon_social

    def get_identificador_tipo_proveedor(self):                                      #Se crea el metodo para obtener el valor del identificador_tipo_proveedor
        return self.identificador_tipo_proveedor
        
    def get_rfc(self):                                                               #Se crea el metodo para obtener el valor del rfc
        return self.rfc
    
    def get_direccion(self):                                                         #Se crea el metodo para obtener el valor de la direccion
        return self.direccion
        
    def get_telefono(self):                                                          #Se crea el metodo para obtener el valor del telefono
        return self.telefono
        
    def get_correo_electronico(self):                                                #Se crea el metodo para obtener el valor del correo electronico
        return self.correo_electronico
        
    def get_contacto(self):                                                          #Se crea el metodo para obtener el valor del contacto
        return self.contacto
        
