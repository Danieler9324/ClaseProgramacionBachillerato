#Se define lista_tipo_movimiento como una lista
lista_tipo_movimiento=[]
class tipo_movimiento:  #Se crea la calse tipo_movimiento
    #Se crea el constructor de la calse tipo_movimiento
    def __init__(self, id_tipo_movimiento, descripcion_tipo_movimiento,entrada_salida,almacen_piso):
        self.id_tipo_movimiento=int(id_tipo_movimiento)                     #Se crea el valor inicial del id_tipo_movimiento
        self.descripcion_tipo_movimiento=str(descripcion_tipo_movimiento)   #Se crea el valor inicial de la descripcion_tipo_movimiento
        self.entrada_salida=entrada_salida                                  #Se crea el valor inicial de la entrada_salida
        self.almacen_piso=almacen_piso                                      #Se crea el valor inicial de almacen_piso
    
    #Se definen los metodos para establecer los valores de:
    def set_id_tipo_movimiento(self,id_tipo_movimiento):                    #Establece el valor de id_tipo_movimiento     
        self.id_tipo_movimiento=id_tipo_movimiento
    
    def set_descripcion_tipo_movimiento(self,descripcion_tipo_movimiento):  #Establece el valor de la descripcion tipo_movimiento
        self.descripcion_tipo_movimiento=descripcion_tipo_movimiento

    def set_entrada_salida(self,entrada_salida):                            #Establece el valor de la entrada_salida
        self.entrada_salida=entrada_salida
    
    def set_almacen_piso(self,almacen_piso):                                #Establece el valor del almacen_piso
        self.almacen_piso=almacen_piso
    
    #Se definen los metodos para obtener los valores de: 
    def get_id_tipo_movimiento(self):                                       #Obtiene el valor del id_tipo_movimiento
        return self.id_tipo_movimiento
    
    def get_descripcion_tipo_movimiento(self):                              #Obtiene el valor de la descripcion_tipo_movimiento
        return self.descripcion_tipo_movimiento

    def get_entrada_salida(self):                                           #Obtiene el valor de la entrada_salida
        return self.entrada_salida

    def get_almacen_piso(self):                                             #Obtiene el valor del almacen_piso
        return self.almacen_piso   