#se importan librerias
import os       #libreria para reiniciar la pantalla
import time     #libreria que genera los tiempos de espera
import random   #libreria que genera un numero aleatorio
#Genera la clase caballo
class Caballo:
    #constructor
    def __init__(self, symbol):
        #Se Define la variable "Symbol"
        self.symbol=symbol
        #se define la posicion como una lista
        self.position= []
    #Genera el avance del caballo
    def avanza(self):
        #gener un numero aleatorio
        numero_aleatorio= random.randint(1 , 5)
        #Define el rango con el numero aleatorio 
        for _ in range (numero_aleatorio):
            self.position.append(self.symbol)
    #Definicion para mostrar la posicion del caballo
    def mostrar_position(self):
        for pos in self.position:
            #Imprime la posicion y finaliza la carrera
            print(pos,end="")
        print("")
#Genera la clase Carrera
class Carrera:
    #constructor
    def __init__(self):
        self.caballo1= Caballo("U") #se aplica la clase Caballo
        self.caballo2= Caballo("Q") #se aplica la clase Caballo
        self.caballo3= Caballo("T") #se aplica la clase Caballo
        self.caballo4= Caballo("I") #se aplica la clase Caballo
        self.caballo5= Caballo("O") #se aplica la clase Caballo
        self.caballo6= Caballo("P") #se aplica la clase Caballo
        self.caballo7= Caballo("Z") #se aplica la clase Caballo
        self.caballo8= Caballo("H") #se aplica la clase Caballo
        self.caballo9= Caballo("J") #se aplica la clase Caballo
        self.caballo10= Caballo("A") #se aplica la clase Caballo
    #Define la ejecucion de la carrera
    def ejecutar_carrera(self):
        #Comprueba cual caballo ya llego a el limite de distancia (meta)
        while len (self.caballo1.position)< 50 and len (self.caballo2.position)< 50 and len (self.caballo3.position)< 50 and len (self.caballo4.position)< 50 and len (self.caballo5.position)< 50 and len (self.caballo6.position)< 50 and len (self.caballo7.position)< 50 and len (self.caballo8.position)< 50 and len (self.caballo9.position)< 50 and len (self.caballo10.position)< 50:
            #Reinicia la pantalla
            os.system("cls")
            self.caballo1.avanza()#Muestra el avance del caballo1
            self.caballo2.avanza()#Muestra el avance del caballo2
            self.caballo3.avanza()#Muestra el avance del caballo3
            self.caballo4.avanza()#Muestra el avance del caballo4
            self.caballo5.avanza()#Muestra el avance del caballo5
            self.caballo6.avanza()#Muestra el avance del caballo6
            self.caballo7.avanza()#Muestra el avance del caballo7
            self.caballo8.avanza()#Muestra el avance del caballo8
            self.caballo9.avanza()#Muestra el avance del caballo9
            self.caballo10.avanza()#Muestra el avance del caballo10
            self.mostrar_pista() #Muestra la pista
            #Fuerza los tiempos de espera
            time.sleep(1)
    #Muestra la pista
    def mostrar_pista(self):
        self.caballo1.mostrar_position()#Muestra la posicion del caballo1
        self.caballo2.mostrar_position()#Muestra la posicion del caballo2
        self.caballo3.mostrar_position()#Muestra la posicion del caballo3
        self.caballo4.mostrar_position()#Muestra la posicion del caballo4
        self.caballo5.mostrar_position()#Muestra la posicion del caballo5
        self.caballo6.mostrar_position()#Muestra la posicion del caballo6
        self.caballo7.mostrar_position()#Muestra la posicion del caballo7
        self.caballo8.mostrar_position()#Muestra la posicion del caballo8
        self.caballo9.mostrar_position()#Muestra la posicion del caballo9
        self.caballo10.mostrar_position()#Muestra la posicion del caballo10

carrera=Carrera() #Retoma la clase carrera
carrera.ejecutar_carrera() #Genera la carrera
