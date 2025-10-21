lista_animales=[]
lista_Mascota=[]
class Animal:
    def __init__ (self, espe, raz):
        self.espec=espe
        self.ra=raz
    
    def set_es(self,es):
        self.es=es
    
    def set_Raz(self, ras):
        self.ra=ras
    
    def getEs(self):
        return self.espec
    
    def getRa(self):
        return self.ra
    
class Mascota (Animal):
    def __init__ (self, nombr, eda, due):
        self.nombr=nombr
        self.eda=eda
        self.due=due
    
    def set_nomb(self,nomb):
        self.nomb=nomb
    
    def set_ed(self,ed):
        self.ed=ed
    
    def set_due(self,due):
        self.due=due
    
    def getNomb(self):
        return self.nombr
    
    def getEda(self):
        return self.eda
    
    def getDue(self):
        return self.due
def altaAnimal(): 
    global lista_animales
    print("Dame los datos del animal")
    espe=input("Dame la especie del animal: ")
    raz=input("Dame la raza del animal: ")
    lista_animales.append(Animal(espe,raz))
def listaAnimales():
    global lista_animales
    for Ani in lista_animales:
        print(Ani.getRa(), "", Ani.getEs())
def buscaAnimales(busca):
    global lista_animales
    apun=0
    for Ani in lista_animales:
        if (busca==Ani.getEs()):
            return apun
        apun=apun+1
    return-1

def modificaAnimal():
    #Retoma variable global
    global lista_animales
    #Caracteristica con la que va a hacer la busqueda
    busca=input("animal a modificar: ")
    ind= buscaAnimales(busca)
    #indica que lo encontro
    if(ind!=-1):
        print("Dame los datos del animal")
        esp=input("Especie: ")
        raz=input("Raza: ")
        lista_animales[ind].set_es(esp)
        lista_animales[ind].set_Raz(raz)
    else:
        print("El Animal no existe")

def eliminaAnimal():
    global lista_animales
    busca=input("Animal a dar de baja: ")
    apun= buscaAnimales(busca)
    if (apun!=-1):
        print("Dar de baja a animal")
        print("Especie ", lista_animales[apun].getEs())
        print ("Raza: ", lista_animales[apun]. getRa())
        elim=input("deseas eliminarlo S N: ").upper()
        if (elim=="S"):
            lista_animales.pop(apun)
    else:
        print("El animal no existe")
def ordenaAnimal():
    global lista_animales
    lista_animales=sorted(lista_animales, key=lambda lista_animales: lista_animales.espec)

########################### Mascotas ##########################################################

def altaMascota(): 
    global lista_Mascota
    print("Dame los datos de la mascota")
    nomb=input("Nombre: ")
    ed=input("Apellido: ")
    due=input("dueno: ")
    lista_Mascota.append(Mascota(nomb,ed,due))
def listaMascotas():
    global lista_Mascota
    for Ani in lista_Mascota:
        print(Ani.getNomb(), "", Ani.getEda(), "", Ani.getDue())
def buscaMascotas(busca):
    global lista_Mascota
    apun=0
    for Ani in lista_Mascota:
        if (busca==Ani.getDue()):
            return apun
        apun=apun+1
    return-1

def modificaMascota():
    global lista_Mascota
    busca=input("Mascota a modificar: ")
    apun=buscaMascotas(busca)
    if (apun!=-1):
        print("Dame los nuevos datos de la mascota")
        no=input("Nombre: ")
        e=input("Edad: ")
        du=input("Dueno")
        lista_Mascota[apun].set_nomb(no)
        lista_Mascota[apun].set_ed(e)
        lista_Mascota[apun].set_due(du)
    else:
        print("La mascota no existe")
def eliminaMascota():
    global listaMascotas
    busca=input("Mascota a dar de baja: ")
    apun= buscaMascotas(busca)
    if (apun!=-1):
        print("Dar de baja a Mascota")
        print("Nombre: ", lista_Mascota[apun].getNomb())
        print ("Edad:  ", lista_Mascota[apun]. getEda())
        print ("Dueno:  ", lista_Mascota[apun]. getDue())
        elim=input("deseas eliminarlo (S/N)").upper()
        if (elim=="S"):
            lista_Mascota.pop(apun)
    else:
        print("La mascota no existe")
def ordenaMascota():
    global lista_Mascota
    lista_Mascota=sorted(lista_Mascota, key=lambda lista_Mascota: lista_Mascota.nombre)

op = ""

while op != "S":
    print("<A> Animales")
    print("<M> Mascotas")
    print("<S> Salir")
    op = input().upper()

    if op == "A":
        print("<A> Alta a animal")
        print("<L> Lista de animales")
        print("<M> Modifica a el animal")
        print("<E> Elimina a el Animal")
        print("<O> Ordena animales")
        print("<S> Salir")
        
        opcion = input().upper()
        if (opcion == "A"):
            altaAnimal()
        elif (opcion == "L"):
            listaAnimales()
        elif (opcion == "M"):
            modificaAnimal()
        elif (opcion == "E"):
            eliminaAnimal()
        elif (opcion == "O"):
            ordenaAnimal()
        elif (opcion == "S"):
            op = "S"
    
    elif op == "M":
        print("<A> Alta a Mascota")
        print("<L> Lista de Mascota")
        print("<M> Modifica la Mascota")
        print("<E> Elimina a la Mascota")
        print("<O> Ordena Mascotas")
        print("<S> Salir")
        
        opcion = input().upper()
        if (opcion == "A"):
            altaMascota()
        elif (opcion == "L"):
            listaMascotas()
        elif (opcion == "M"):
            modificaMascota()
        elif (opcion == "E"):
            eliminaMascota()
        elif (opcion == "O"):
            ordenaMascota()
        elif (opcion == "S"):
            op = "S"