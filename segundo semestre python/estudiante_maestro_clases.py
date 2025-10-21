#Crea una lista de maestros
lista_maestro=[]
#Crea una lista de estudiantes
lista_estudiante=[]
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
#Se crea una clase estudiante que hereda las propiedades de la clase Persona
class estudiante(Persona):
    def __init__ (self,no,ap,ed,co,fi):
        #Se retoma el constructor de persona
        Persona.__init__(self,no,ap,ed)
        #Crea el valor co para el atributo codigo
        self.codigo=co
        #Crea el valor fi para el atributo nota
        self.nota=fi
    #Define setCodigo con el atributo co
    def setCodigo(self,co):
        #Se vuelve a crear el valor co para codigo
        self.codigo=co
    #Define setNota con el atributo del fi
    def setNota(self,fi):
        #Se vuelve a crear el valor fi para nota
        self.nota=fi
    #Define getCodigo con el atributo self 
    def getCodigo(self):
        #Regresa el valor de self.codigo
        return self.codigo
    #Define getNota con el atributo self
    def getNota(self):
        #Regresa el valor de self.nota
        return self.nota
#Se crea una clase maestro que hereda las propiedades de la clase persona
class maestro(Persona):
    def __init__ (self,no,ap,ed,rf,pr):
        #Se retoma el valor de persona
        Persona.__init__(self,no,ap,ed)
        #Se crea el valor rf para rfc
        self.rfc=rf
        #Se crea el valor pr para profesion
        self.profesion=pr
    #Se define setRfc con el atriburo de rf
    def setRfc(self,rf):
        #Se vuelve a crear el valor rf para rfc
        self.rfc=rf
    #Se define setProfesion con el atributo de pr
    def setProfesion(self,pr):
        #Se vuelve a crear el valor pr para profesion
        self.profesion=pr
    #Define getRfc con el atributo self
    def getRfc(self):
        #Regresa el valor de self.rfc
        return self.rfc
    #Define getProfesion con el atributo self
    def getProfesion(self):
        #Regresa el valor de self.profesion
        return self.profesion
#Se define altamaestro
def altaMaestro():
    #Se genera una variable global
    global lista_maestro
    #Pide los datos del maestro
    print("Dame los datos del maestro")
    #Ingresa el nombre del maestro
    nom=input("Nombre: ")
    #Ingresa el apellido del maestro
    ape=input("Apellido: ")
    #Ingresa la edad del maestro
    ed=int(input("edad: "))
    #Ingresa el RFC del maestro
    rf=input("RFC: ")
    #Ingresa la profesion del maestro
    pr=input("Profesion: ")
    #Se invoca la clase maestro
    lista_maestro.append(maestro(nom,ape,ed,rf,pr))
#Se define la lista del maestro
def listaMaestro():
    #Retoma variables globales
    global lista_maestro
    #Recorre la lista de maestros
    for per in lista_maestro:
        #imprime los datos del maestro
        print(per.getNomb()," ",per.getApel()," ",per.getEda()," ",per.getRfc()," ",per.getProfesion())
#Se define la variable para buscarMaestro
def buscaMaestro(busca):
    #Se retoman variables globales
    global lista_maestro
    #Se genera un apuntador con el valor de 0
    ind=0
    #Recorre la lista de maestros
    for per in lista_maestro:
        #Busca a el maestro por medio del RFC
        if (busca==per.getRfc()):
            #Regresa al indice
            return ind
        #Si no son iguales ira incrementando el indice
        ind=ind+1
    #Si no lo encuentra indicara al proceso que no encontro a el maestro
    return-1
#Define modificar maestro
def modificaMaestro():
    #Retoma variable global
    global lista_maestro
    #Caracteristica con la que va a hacer la busqueda
    busca=input("maestro a modificar: ")
    ind= buscaMaestro(busca)
    #indica que lo encontro
    if(ind!=-1):
        #ingresa los datos del maestro
        print("Dame los datos de el maestro")
        nom=input("Nombre: ")
        ape=input("Apellido: ")
        ed=int(input("Edad: "))
        rf=input("RFC: ")
        pr=input("Profesion: ")
        #Asignar el nuevo nombre del maestro
        lista_maestro[ind].set_Nomb(nom)
        #Asignar el nuevo apellido del maestro
        lista_maestro[ind].set_Apel(ape)
        #Asignar la nueva edad del maestro
        lista_maestro[ind].set_Eda(ed)
        #Asignar el nuevo RFC del maestro
        lista_maestro[ind].setRfc(rf)
        #Asignar la nuevo profesion del maestro
        lista_maestro[ind].setProfesion(pr)
    else:
        #Si el indice es menos 1 imprimir que el maestro no existe
        print("El maestro no existe")
#Define eliminar maestro
def eliminaMaestro():
    global lista_maestro
    #Caracteristica con la que va a hacer la busqueda
    busca=input("maestro a eliminar: ")
    ind= buscaMaestro(busca)
    #indica que lo encontro
    if(ind!=-1):
        #imprime los datos del maestro a eliminar
        print("Maestro a eliminar ")
        print("Nombre ", lista_maestro[ind].getNomb())
        print("Apellido ", lista_maestro[ind].getApel())
        #Pregunta si deseas eliminar al maestro 
        se=input("deseas eliminarlo (S/N)").upper()
        #Si "se" es igual a "S" eliminarlo
        if(se=="S"):
            #Elimina a el maestro
            lista_maestro.pop(ind)
    else:
        #Si el indice es menos 1 imprimir que el maestro no existe
        print("El maestro no existe")
#Define el ordenamiento del maestro
def ordenaMaestro():
    #Retoma una variable global
    global lista_maestro
    #Crea una nueva lista de maestros
    lista_maestro=sorted(lista_maestro, key=lambda lista_maestro: lista_maestro.nombre)



################################### Estudiante ###############################################



#se define altaEstudiante
def altaEstudiante():
    #Se genera una variable global
    global lista_estudiante
    #Pide los datos del Estudiante
    print("Dame los datos del Estudiante")
    #Ingresa el nombre del Estudiante
    nom=input("Nombre: ")
    #Ingresa el apellido del Estudiante
    ape=input("Apellido: ")
    #Ingresa la edad del Estudiante
    ed=int(input("edad: "))
    #Ingresa el codigo del Estudiante
    co=input("Codigo: ")
    #Ingresa la Nota del Estudiante
    no=input("Nota: ")
    #Se invoca la clase Estudiante
    lista_estudiante.append(estudiante(nom,ape,ed,co,no))
#Se define la lista del Estudiante
def listaEstudiante():
    #Retoma variables globales
    global lista_estudiante
    #Recorre la lista de estudiantes
    for per in lista_estudiante:
        #imprime los datos del Estudiante
        print(per.getNomb()," ",per.getApel()," ",per.getEda()," ",per.getCodigo()," ",per.getNota())
#Se define la variable para buscar estudiante
def buscaEstudiante(busca):
    #Se retoman variables globales
    global lista_estudiante
    #Se genera un apuntador con el valor de 0
    ind=0
    #Recorre la lista de estudiantes
    for per in lista_estudiante:
        #Busca a el estudiante por medio del codigo
        if (busca==per.getCodigo()):
            #Regresa al indice
            return ind
        #Si no son iguales ira incrementando el indice
        ind=ind+1
    #Si no lo encuentra indicara que no encontro a el estudiante
    return-1
#Define modificar estudiante
def modificaEstudiante():
    #Retoma variable global
    global lista_maestro
    #Caracteristica con la que va a hacer la busqueda
    busca=input("estudiante a modificar: ")
    ind= buscaEstudiante(busca)
    #indica que lo encontro
    if(ind!=-1):
        #ingresa los datos del estudiante
        print("Dame los datos de el estudiante")
        nom=input("Nombre: ")
        ape=input("Apellido: ")
        ed=int(input("Edad: "))
        co=input("Codigo: ")
        no=input("Nota: ")
        #Asignar el nuevo nombre del estudiante
        lista_estudiante[ind].set_Nomb(nom)
        #Asignar el nuevo apellido del estudiante
        lista_estudiante[ind].set_Apel(ape)
        #Asignar la nueva edad del estudiante
        lista_estudiante[ind].set_Eda(ed)
        #Asignar el nuevo codigo del estudiante
        lista_estudiante[ind].setCodigo(co)
        #Asignar la nueva Nota del estudiante
        lista_estudiante[ind].setNota(no)
    else:
        #Si el indice es menos 1 imprimir que el estudiante no existe
        print("El estudiante no existe")
#Define eliminar estudiante
def eliminaEstudiante():
    global lista_estudiante
    #Caracteristica con la que va a hacer la busqueda
    busca=input("estudiante a eliminar: ")
    ind= buscaEstudiante(busca)
    #indica que lo encontro
    if(ind!=-1):
        #imprime los datos del estudiante a eliminar
        print("estudiante a eliminar ")
        print("Nombre ", lista_estudiante[ind].getNomb())
        print("Apellido ", lista_estudiante[ind].getApel())
        #Pregunta si deseas eliminar al estudiante
        se=input("deseas eliminarlo (S/N)").upper()
        #Si se es igual a "S" eliminarlo
        if(se=="S"):
            #Elimina a el estudiante
            lista_estudiante.pop(ind)
    else:
        #Si el indice es menos 1 imprimir que el estudiante no existe
        print("El estudiante no existe")
#Define el ordenamiento del estudiante
def ordenaEstudiante():
    #Retoma una variable global
    global lista_estudiante
    #Crea una nueva lista de estudiantes
    lista_estudiante=sorted(lista_estudiante, key=lambda lista_estudiante: lista_estudiante.nombre)

#Genera la variable operacion en vacio
opc=""
#Crea el ciclo para las listas
while opc!="S":
    #pregunta que lista quieres ver
    print("<M> Maestros")
    print("<E> Estudiantes")
    print("<S> Salir")
    opc=input().upper()
    #Si "opc" es igual a "M" imprimir las opciones de la lista de maestros
    if opc=="M":
        print("<A> Alta de maestro")
        print ("<L> Listado de maestro")
        print ("<M> Modificacion de maestro")
        print ("<E> Elimina el maestro")
        print("<O> Ordena maestro")
        #Hace que no haya inconvenientes a la hora de poner un caracter minuscula o mayuscula 
        opcion=input().upper()
        if (opcion=="A"):
            altaMaestro()
        elif (opcion=="L"):
            listaMaestro()
        elif (opcion=="M"):
            modificaMaestro()
        elif (opcion=="E"):
            eliminaMaestro()
        elif (opcion=="O"):
            ordenaMaestro()

    #Si "opc" es igual a "E" imprimir las opciones de la lista de estudiantes
    elif opc=="E":
        print("<A> Alta de estudiante")
        print ("<L> Lista de Estudiantes")
        print ("<M> Modificacion de estudiante")
        print ("<E> Elimina el estudiante")
        print("<O> Ordena estudiante")
        #Hace que no haya inconvenientes a la hora de poner un caracter minuscula o mayuscula
        opcion=input().upper()
        if (opcion=="A"):
            altaEstudiante()
        elif (opcion=="L"):
            listaEstudiante()
        elif (opcion=="M"):
            modificaEstudiante()
        elif (opcion=="E"):
            eliminaEstudiante()
        elif (opcion=="O"):
            ordenaEstudiante()