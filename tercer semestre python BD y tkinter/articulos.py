# Listas globales para almacenar tipos de artículos y artículos
lista_tipoArticulo = []
lista_articulo = []

# Crea la clase Tipo Articulo
class TipoArticulo:
    
    # Crea el constructor de la clase Tipo Articulo
    def __init__(self, id_tipoarticulo, descripcion):
        self.id_tip = id_tipoarticulo
        self.des = descripcion

    def set_id(self, ide):
        self.id_tip = ide
    
    def set_des(self, desc):
        self.des = desc

    def get_id(self):
        return self.id_tip
    
    def get_des(self):
        return self.des

# Crea la clase Articulo
class Articulo:

    # Crea el constructor para la clase Articulo
    def __init__(self, idA, des, idT, co, ma, me, cA, cT):
        self.idA = idA
        self.des = des
        self.idT = idT
        self.co = co
        self.ma = ma
        self.me = me
        self.caA = cA
        self.caT = cT

    def set_idA(self, id):
        self.idA = id
    
    def set_des(self, de):
        self.des = de

    def set_idT(self, idT):
        self.idT = idT
    
    def set_cos(self, co):
        self.co = co

    def set_ma(self, ma):
        self.ma = ma
    
    def set_me(self, me):
        self.me = me

    def set_caA(self, ca):
        self.caA = ca
    
    def set_caT(self, ct):
        self.caT = ct

    def get_idA(self):
        return self.idA
    
    def get_des(self):
        return self.des

    def get_idT(self):
        return self.idT
    
    def get_cos(self):
        return self.co

    def get_ma(self):
        return self.ma
    
    def get_me(self):
        return self.me

    def get_caA(self):
        return self.caA
    
    def get_caT(self):
        return self.caT

# Función para verificar si un ID de tipo de artículo ya existe
def idTipoArticuloExiste(id):
    return any(tipo.get_id() == id for tipo in lista_tipoArticulo)

# Función para verificar si un ID de artículo ya existe
def idArticuloExiste(id):
    return any(art.get_idA() == id for art in lista_articulo)

# Función para dar de alta un nuevo tipo de artículo
def alta_tipo_articulo():
    # Retoma la listaTipoArticulo como una variable global
    global lista_tipoArticulo

    # Llama a la variable de listar articulo para mostrarla antes de hacer la accion deseada


    # Pide los datos del tipo de articulo son: ID, Descripcion
    print("Datos del Tipo de articulo")
    id = input("Identificador: ")
    if idTipoArticuloExiste(id):
        print("El ID introducido ya existe.")
        return
    des = input("Descripcion: ")

    # Retoma la clase TipoArticulo
    lista_tipoArticulo.append(TipoArticulo(id, des))

# Función para listar todos los tipos de artículo
def listar_tipo_articulo():
    # Retoma listaTipoArticulo como variable global
    global lista_tipoArticulo
    if not lista_tipoArticulo:
        print("No hay registros")
    else:
        print("Tipos de articulo registrados: ")
        for tipo in lista_tipoArticulo:
            print("ID: ", tipo.get_id(), "- Descripción:", tipo.get_des())

# Función para buscar un tipo de artículo por ID
def busca_tipo_articulo(busca):
    for tipo in lista_tipoArticulo:
        if busca == tipo.get_id():
            return tipo
    return -1

# Función para modificar un tipo de artículo existente
def modifica_tipo_articulo():
    # Retoma la lista TipoArticulo como variable global
    global lista_tipoArticulo
    listar_tipo_articulo()

    # Ingresa el ID del tipo de articulo a modificar
    busca = input("Tipo de articulo a modificar (ID): ")
    tipo = busca_tipo_articulo(busca)
    if tipo != -1:
        # Ingresa los nuevos datos del tipo de articulo
        print("Ingresa los nuevos datos del tipo de articulo")
        id = input("Identificador: ")
        if id != tipo.get_id() and idTipoArticuloExiste(id):
            print("El ID introducido ya existe.")
            return
        des = input("Descripcion: ")
        tipo.set_id(id)
        tipo.set_des(des)
    else:
        print("El tipo de articulo no existe")

# Función para dar de baja un tipo de artículo
def baja_tipo_articulo():
    # Toma la lista Tipo Articulo como variable global
    global lista_tipoArticulo
    listar_tipo_articulo()
    busca = input("Tipo articulo a eliminar (ID): ")

    # Retoma la funcion de buscar un tipo de articulo
    tipo = busca_tipo_articulo(busca)
    if tipo != -1:
        print("Tipo articulo a eliminar ")
        print("Identificador: ", tipo.get_id())
        print("Descripcion: ", tipo.get_des())

        # Te da la opcion si eliminar o no el tipo de articulo
        se = input("¿Deseas eliminarlo (S/N)? ").upper()

        # Si seleccionas "S" Eliminar el tipo de articulo
        if se == "S":
            lista_tipoArticulo.remove(tipo)
            print("El tipo articulo", tipo.get_des(), "con ID", tipo.get_id(), "ha sido eliminado")
        else:
            print("El tipo articulo no ha sido eliminado")
    else:
        print("El tipo de articulo no existe")

# Función para dar de alta un nuevo artículo
def alta_articulo():
    # Retoma la lista de articulo como un valor global
    global lista_articulo

    # Llama la funcion de listar_tipo_articulo para imprimir la lista antes de alguna accion
    listar_tipo_articulo()

    # Ingresa los datos del Articulo a dar de Alta
    print("Datos del Articulo")
    idA = input("Identificador de articulo: ")
    if idArticuloExiste(idA):
        print("El ID introducido ya existe")
        return
    des = input("Descripcion: ")
    idTipo = input("Identificador del tipo de articulo: ")
    if not any(tipo.get_id() == idTipo for tipo in lista_tipoArticulo):
        print("El tipo de articulo no existe")
        return
    listar_articulo()
    # Define las variables cos, mayo, menu, como valores flotantes
    cos = float(input("Costo: "))
    mayo = float(input("Precio de mayoreo: "))
    menu = float(input("Precio de menudeo: "))

    # Define las variables canAl, canTi como valores enteros
    canAl = int(input("Cantidad en el almacen: "))
    canTi = int(input("Cantidad en la tienda: "))

    # Retoma la clase Articulo
    lista_articulo.append(Articulo(idA, des, idTipo, cos, mayo, menu, canAl, canTi))

# Función para listar todos los artículos
def listar_articulo():
    # Retoma lista_articulo como una variable global
    global lista_articulo

    # Si no hay ningun valor en la lista_articulo imprimir "No hay articulo registrados"
    if not lista_articulo:
        print("No hay registros ")

    # Imprime los articulos registrados
    else:
        print("Articulos registrados:")
        for art in lista_articulo:
            print("ID:", art.get_idA(), "- Descripcion:", art.get_des(), "- Tipo ID:", art.get_idT(), "- Costo:", art.get_cos(), "- Mayoreo:", art.get_ma(), "- Menudeo:", art.get_me(),"- Cantidad en el Almacen:", art.get_caA(), "- Cantidad en la Tienda:", art.get_caT())

# Función para buscar un artículo por ID
def busca_articulo(busca):
    for art in lista_articulo:
        if busca == art.get_idA():
            return art
    return -1

# Función para modificar un artículo existente
def modifica_articulo():
    # Retoma lista_articulo como global
    global lista_articulo

    # Retoma la funcion lista_articulo
    listar_articulo()

    # Pide ingresar el ID del articulo a modificar 
    busca = input("Articulo a modificar (ID): ")
    art = busca_articulo(busca)
    if art != -1:
        # Cuando el Articulo ya fue encontrado pide ingresar los nuevos datos del articulo
        print("Ingresa los nuevos datos del articulo")
        idA = input("Identificador: ")
        if idA != art.get_idA() and idArticuloExiste(idA):
            print("El ID introducido ya existe.")
            return
        des = input("Descripcion: ")
        idTipo = input("Identificador del tipo de articulo: ")
        if not any(tipo.get_id() == idTipo for tipo in lista_tipoArticulo):
            print("El tipo de articulo no existe.")
            return
        listar_tipo_articulo()
        cos = float(input("Costo: "))
        mayo = float(input("Precio de mayoreo: "))
        menu = float(input("Precio de menudeo: "))
        canAl = int(input("Cantidad en el almacen: "))
        canTi = int(input("Cantidad en la tienda: "))
        art.set_idA(idA)
        art.set_des(des)
        art.set_idT(idTipo)
        art.set_cos(cos)
        art.set_ma(mayo)
        art.set_me(menu)
        art.set_caA(canAl)
        art.set_caT(canTi)
    else:
        print("El articulo no existe")

# Función para dar de baja un artículo
def baja_articulo():
    # Retoma lista_articulo como una variable global
    global lista_articulo

    # Retoma la funcion de listar_articulo
    listar_articulo()

    # Ingresa el ID del articulo a eliminar
    busca = input("Articulo a eliminar (ID): ")
    art = busca_articulo(busca)
    if art != -1:
        # Imprime los datos del articulo a eliminar
        print("Articulo a eliminar ")
        print("Identificador: ", art.get_idA())
        print("Descripcion: ", art.get_des())
        print("Identificador del tipo de articulo: ", art.get_idT())
        print("Costo: ", art.get_cos())
        print("Precio de mayoreo: ", art.get_ma())
        print("Precio de menudeo: ", art.get_me())
        print("Cantidad en el almacen: ", art.get_caA())
        print("Cantidad en la tienda: ", art.get_caT())

        # Te pide la confirmacion si eliminarlo o no
        se = input("¿Deseas eliminarlo (S/N)? ").upper()

        # Si seleccionas "S", Eliminar el Articulo
        if se == "S":
            lista_articulo.remove(art)
            print("El artículo ha sido eliminado")
        else:
            print("El artículo no ha sido eliminado")
    else:
        print("El artículo no existe")

# Menú principal del catálogo
opcio = ""

while opcio != "S":
    # Te pide ingresar que catalogo quieres ingresar
    print("<1> Catalogo tipo Articulo")
    print("<2> Catalogo Articulo")
    print("<S> Salir")

    opcio = input().upper()

    # Si seleccionas "1" imprime las opciones del catalogo de tipo Articulo
    if opcio == "1":
        print("<A> Alta tipo articulo")
        print("<M> Modificar tipo de articulo")
        print("<B> Baja de tipo de articulo")
        print("<L> Listado tipo articulo")

        opcio = input().upper()
        
        # Te da la opcion para seleccionar el Alta, Modificacion, Baja o Lista del Articulo
        if opcio == "A":
            alta_tipo_articulo()
        elif opcio == "M":
            modifica_tipo_articulo()
        elif opcio == "B":
            baja_tipo_articulo()
        elif opcio == "L":
            listar_tipo_articulo()
        else:
            print("Opcion no válida")

    # Si la Opcion es 2 entonces imprimir el catalogo de Articulo
    elif opcio == "2":
        print("<A> Alta Articulo")
        print("<M> Modificar articulo")
        print("<B> Baja de articulo")
        print("<L> Listado Articulo")

        opcio = input().upper()

        # Te da la Opcion de dar de Alta, Modificar, Baja o Listar los articulos
        if opcio == "A":
            alta_articulo()
        elif opcio == "M":
            modifica_articulo()
        elif opcio == "B":
            baja_articulo()
        elif opcio == "L":
            listar_articulo()
        else:
            print("Opcion no válida")

    # Si seleccionas "S" entonces imprimir "Saliendo"
    elif opcio == "S":
        print("La lista a sido cerrada")
    else:
        print("Opcion no valida")
