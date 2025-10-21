#Crea una lista de las personas
lista_persona=[]
#Crea la clase Persona
class Persona:
    #constructor de la clase persona
    def __init__ (self, nom, apel, eda):
        self.nombre=nom     #Asignacion del parametro nombre
        self.apellido=apel  #Asignacion del parametro apellido
        self.edad=eda       #Asignacion del parametro edad
    #define a nomb como un parametro de nombre
    def set_Nomb(self,nomb):
        self.nombre=nomb    #asigna el valor de nomb a la instancia
    #define a ap como parametro de apellidos
    def set_Apel(self,ap):
        self.apellido= ap   #asigna el valor de ap a la instancia
    #define a edad como parametro de edad
    def set_Eda(self, edad):
        self.edad=edad      #asigna el valor de edad a la instancia
    #Define getNomb con el atributo self 
    def getNomb(self):
        #Regresa de registro del nombre de la persona
        return self.nombre
    #Define getApel con el atributo self 
    def getApel(self):
        #Regresa el registro del apellido de la persona
        return self.apellido
    #Define getEda con el atributo self 
    def getEda(self):
        #Regresa el registro de la edad de la persona
        return self.edad
    
#Define altaPersona
def altaPersona():
    #Crea a lista_persona como una variable global
    global lista_persona
    #Pide los datos de la persona
    print("Escribe los datos de la persona")
    #Ingresa el nombre de la persona
    Nomb=input("Nombre: ")
    #Ingresa el apellido de la persona
    Apelli=input("Apellido: ")
    #Ingresa la edad de la persona
    Edad=int(input("Edad: "))
    #Se invoca la clase Persona
    lista_persona.append (Persona(Nomb , Apelli , Edad))
#Define la listapersona
def listaPersona():
    #Retoma variable global
    global lista_persona
    #Recorre la lista de personas
    for per in lista_persona:
        #Imprime los datos de la persona
        print(per.getNomb(), " " , per.getApel() , " " , per.getEda())

#Define buscaPersona
def buscaPersona(busca):
    #Retoma variable global
    global lista_persona
    #Crea un apuntador 
    indi=0
    #crea un ciclo para buscar
    for per in lista_persona:
        # Crea una variable para encontrar el nombre
        if (busca==per.getNomb()):
            #Regresar el registro del apuntador
            return indi
        #Si no encontro el nombre recorrer el apuntador
        indi=indi+1
    #Si no encontro a ninguna persona notifica al proceso que no se encontro a la persona buscada
    return -1
    
#Define modificaPersona
def modificaPersona():
    #Retoma variables globales
    global lista_persona
    #Caracteristica con la que va a buscar
    busca=input("Persona que desea modificar: ")
    indi= buscaPersona(busca)
    #Si el apuntador es igual a -1 
    if (indi !=-1):
        #Escribir los datos de la persona a modificar
        print("Escribe los datos de la persona")
        #Ingresa el nombre
        Nomb=input("Nombre: ")
        #ingresa el apellido
        Apelli=input("Apellido: ")
        #ingresa la edad
        Edad=int(input("Edad: "))
        #Sustituye el nombre de la persona por el nuevo
        lista_persona[indi].set_Nomb(Nomb)
        #Sustituye el apellido de la persona por el nuevo
        lista_persona[indi].set_Apel(Apelli)   
        #Sustituye la edad de la persona por el nuevo
        lista_persona[indi].set_Eda(Edad)
    else:
        #No se encontro a la persona
        print("La persona no existe")    

#Define el ordenamiento de la persona
def ordenaPersona():
    #Retoma una variable global
    global lista_persona
    #Crea una nueva lista de persona
    lista_persona=sorted(lista_persona, key=lambda lista_persona: lista_persona.nombre)
    
#Se crea la variable opcion como "x"
opcion="x"
#Ciclo para agregar personas a la lista
while opcion!="S":
    print("<A> Alta de una persona")
    print("<M> Modificar")
    print("<L> Lista de personas")  
    print("<O> Ordenar lista")
    print("<S> Salir")
    #Hace que no haya inconvenientes a la hora de poner un caracter minuscula o mayuscula
    opcion=input().upper()
    if (opcion=="A"):
        altaPersona()
    elif (opcion=="L"):
        listaPersona()
    elif (opcion=="M"):
        modificaPersona()
    elif (opcion=="O"):
        ordenaPersona()
        