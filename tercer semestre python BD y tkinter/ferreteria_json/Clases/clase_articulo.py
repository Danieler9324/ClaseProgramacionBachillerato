#Crea la lista de articulo
lista_articulo = []
#Define la clase articulo
class articulo:
    #Crea el constructor para la clase articulo
    def __init__ (self, identificador,descripcion,identificador_tipo_articulo,costo,precio_mayoreo,precio_menudeo,cantidad_almacen,cantidad_tienda):
        self.identificado=identificador                             #Se crea el valor inicial del identficador
        self.descripcio=descripcion                                 #Se crea el valor inicial de la descripcion
        self.identificador_tipo_articul=identificador_tipo_articulo #Se crea el valor incial del identificador de tipo articulo
        self.cost=costo                                             #Se crea el valor incial del costo del articulo
        self.precio_mayore=precio_mayoreo                           #Se crea el valor incial del precio de mayoreo
        self.precio_menude=precio_menudeo                           #Se crea el valor incial del precio de menudeo
        self.cantidad_almace=cantidad_almacen                       #Se crea el valor incial de la cantidad en el almacen
        self.cantidad_tiend=cantidad_tienda                         #Se crea el valor incial de la cantidad en la tienda
    
    def set_identificad(self,identificad):                              #Se establece el valor del identificador del articulo
        self.identificad=identificad

    def set_descripcio(self,descripci):                                 #Se establece el valor de la descripcion del articulo
        self.descripcio=descripci

    def set_identificador_tipo_articu(self,identificador_tipo_articu):  #Se establece el valor del identificador del tipo articulo
        self.identificador_tipo_articu=identificador_tipo_articu
    
    def set_cos(self,cos):                                              #Se establece el valor del costo del articulo
        self.cost=cos
    
    def set_precio_mayor(self,precio_mayor):                            #Se establce el valor del precio de mayoreo al artiuclo
        self.precio_mayore=precio_mayor
    
    def set_precio_menud(self,precio_menud):                            #Se establece el valor del precio de menudeo al articulo
        self.precio_menude=precio_menud
    
    def set_cantidad_almace(self,cantidad_almac):                       #Se establece el valor de la canitdad en el almacen al articulo
        self.cantidad_almace=cantidad_almac
    
    def set_cantidad_tien(self,cantidad_tien):                          #Se establece el valor de la canitdad en la tienda al artiuclo
        self.cantidad_tiend=cantidad_tien

    def get_Identifica(self):                                           #Se obtiene el valor del identificador del articulo
        return self.identificado
    
    def get_Descripci(self):                                            #Se obtiene el valor de la descripcion del articulo
        return self.descripcio

    def get_Identificador_Tipo_Articu(self):                            #Se obtiene el valor de el identificador del tipo articulo
        return self.identificador_tipo_articul
    
    def get_Cos (self):                                                 #Se obtiene el valor del costo del articulo
        return self.cost
    
    def get_Precio_Mayor (self):                                        #Se obtiene el valor del precio de mayoreo del articulo
        return self.precio_mayore
    
    def get_Precio_Menud (self):                                        #Se obtiene el valor del precio de menudeo del articulo
        return self.precio_menude
    
    def get_Cantidad_Almac (self):                                      #Se obtiene el valor de la cantidad en el almacen del articulo
        return self.cantidad_almace
    
    def get_Cantidad_Tien (self):                                       #Se obtiene el valor de la cantidad en la tienda del articulo
        return self.cantidad_tiend