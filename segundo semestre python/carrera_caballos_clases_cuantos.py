#importamos librerias
import os       #Libreria para el sistema operativo                                   
import time     #Libreria para los tiempos de espera                                                     
import random   #Libreria para generar un numero aleatorio                                                    
#Genera la clase Caballo
class Caballo:                                                 
    #constructor
    def __init__(self, symbol): 
        #Define la variable "symbol"                                 
        self.symbol = symbol  
        #Define la posicion como una lista                                  
        self.position = []   
    #Genera el avance de los caballos                                    
    def avanza (self):               
        #Generaun numero aleatorio                           
        numero_aleatorio = random.randint (1,3)
        #define el rango con el numero aleatorio 
        for _ in range (numero_aleatorio):
            self.position.append(self.symbol)
    #Definicion para mostrar la posicion del caballo
    def mostrar_position(self):
        for pos in self.position:
            #Imprime la posicion y acaba la carrera
            print(pos, end='')
        print('')
#Genera la clase Carrera
class Carrera:
    #constructor
    def __init__ (self, cuantos):
        #Genera los caballos como una lista
        self.caballos = []
        #Generan los caballos que el usuario ingreso
        for i in range(0, cuantos):
            #Los caballos se definieron como enteros
            self.caballos.append (Caballo(str(i)))
    #Se define la ejecucion de la carrera
    def ejecutar_carrera(self):
        #Empieza la carrera
        continuar = True
        #Inicia el ciclo para continuar la carrera
        while continuar:
            #Reinicia la pantalla 
            os.system('cls')
            
            for caballo in self.caballos:
                if continuar: 
                    #Genera el avanze de el caballo
                    caballo.avanza()
                #Verifica si la posicion de un caballo es mayor que 50
                if(len(caballo.position)>50):
                #Termina la carrera
                    continuar = False
                    #imprime a el ganador
                    print('ganador: ',caballo.symbol)
            #Muestra la pista
            self.mostrar_pista()
            #Tiempo de carga de los caballos
            time.sleep(1)
    #Defina la demostracion de la pista
    def mostrar_pista(self):
        for caballo in self.caballos:
            #Muestra la posicion del caballo
            caballo.mostrar_position()
#Define la variable seguir como una "s"
seguir = 's'
#ciclo de juego
while seguir.upper() == 'S':
    #Pregunta a el usuario la cantidad de caballos que desea
    numeroCaballos=int(input('¿Cuantos caballos quieres?'))
    #Se define la carrera como el numero de caballos
    carrera_obj = Carrera (numeroCaballos)
    #ejecuta la carrera
    carrera_obj.ejecutar_carrera()
    #Pregunta a el usuario si quiere otra carrera
    seguir=input('Quieres hacer otra carrera?')












