#Se ejecuta la librerias
import random   #Genera numero aleatorios
import time     #Fuerza tiempos de espera
import os       #Funciones del sistema operativo
#Se asigna cada caballo como un vector
caballo1=[]
caballo2=[]
caballo3=[]
caballo4=[]
caballo5=[]
caballo6=[]
caballo7=[]
caballo8=[]
caballo9=[]
caballo10=[] 
#Se define avanza para que los caballo1  
def avanza1():
    global caballo1
    numero_aleatorio = random.randint(1,5)
    for cont in range(0,numero_aleatorio):
        caballo1.append("#")
#Se define avanza para que los caballo2
def avanza2():
    global caballo2
    numero_aleatorio = random.randint(1,5)
    for cont in range(0,numero_aleatorio):
        caballo2.append("@")
#Se define avanza para que los caballo3
def avanza3():
    global caballo3
    numero_aleatorio = random.randint(1,5)
    for cont in range(0,numero_aleatorio):
        caballo3.append("<")
def avanza4():
#Se define avanza para que los caballo4
    global caballo4
    numero_aleatorio = random.randint(1,5)
    for cont in range(0,numero_aleatorio):
        caballo4.append(">")
#Se define avanza para que los caballo5
def avanza5():
    global caballo5
    numero_aleatorio = random.randint(1,5)
    for cont in range(0,numero_aleatorio):
        caballo5.append("5")
#Se define avanza para que los caballo6
def avanza6():
    global caballo6
    numero_aleatorio = random.randint(1,5)
    for cont in range(0,numero_aleatorio):
        caballo6.append("8")
#Se define avanza para que los caballo7
def avanza7():
    global caballo7
    numero_aleatorio = random.randint(1,5)
    for cont in range(0,numero_aleatorio):
        caballo7.append("*")
#Se define avanza para que los caballo8  
def avanza8():
    global caballo8
    numero_aleatorio = random.randint(1,5)
    for cont in range(0,numero_aleatorio):
        caballo8.append("3")
#Se define avanza para que los caballo9  
def avanza9():
    global caballo9
    numero_aleatorio = random.randint(1,5)
    for cont in range(0,numero_aleatorio):
        caballo9.append("0")
#Se define avanza para que los caballo10  
def avanza10():
    global caballo10
    numero_aleatorio = random.randint(1,5)
    for cont in range(0,numero_aleatorio):
        caballo10.append(":") 
#Se define la pista para poder poner el limite de esta
def pista():
#Se definen globales los caballos
    global caballo1, caballo2, caballo3, caballo4, caballo5, caballo6, caballo7, caballo8, caballo9, caballo10
#Imprime a los caballos y calcula la distancia del caballo1
    for cont2 in range (0,len(caballo1)):
        print(caballo1[cont2], end="")
    print("")

#Imprime a los caballos y calcula la distancia del caballo2
    for cont2 in range (0,len(caballo2)):
        print(caballo2[cont2], end="")
    print("")
#Imprime a los caballos y calcula la distancia del caballo3
    for cont2 in range (0,len(caballo3)):
        print(caballo3[cont2], end="")
    print("")
#Imprime a los caballos y calcula la distancia del caballo4
    for cont2 in range (0,len(caballo4)):
        print(caballo4[cont2], end="")
    print("")
#Imprime a los caballos y calcula la distancia del caballo5
    for cont2 in range (0,len(caballo5)):
        print(caballo5[cont2], end="")
    print("")
#Imprime a los caballos y calcula la distancia del caballo6
    for cont2 in range (0,len(caballo6)):
        print(caballo6[cont2], end="")
    print("")
#Imprime a los caballos y calcula la distancia del caballo7
    for cont2 in range (0,len(caballo7)):
        print(caballo7[cont2], end="")
    print("")
#Imprime a los caballos y calcula la distancia del caballo8
    for cont2 in range (0,len(caballo8)):
        print(caballo8[cont2], end="")
    print("")
#Imprime a los caballos y calcula la distancia del caballo9
    for cont2 in range (0,len(caballo9)):
        print(caballo9[cont2], end="")
    print("")
#Imprime a los caballos y calcula la distancia del caballo10
    for cont2 in range (0,len(caballo10)):
        print(caballo10[cont2], end="")
    print("")
#preguta si se repite la carrera o no
seguir="s"
while seguir=="s":
    caballo1=[]
    caballo2=[]
    caballo3=[]
    caballo4=[]
    caballo5=[]
    caballo6=[]
    caballo7=[]
    caballo8=[]
    caballo9=[]
    caballo10=[]
#Defina el avance de cada caballo y tambien cual es el que gana
    while(len(caballo1)<50 and len(caballo2)<50 and len(caballo3)<50 and len(caballo4)<50 and len(caballo5)<50 and len(caballo6)<50 and len(caballo7)<50 and len(caballo8)<50 and len(caballo9)<50 and len(caballo10)<50):
        _=os.system("cls")
        avanza1()
        avanza2()
        avanza3()
        avanza4()
        avanza5()
        avanza6()
        avanza7()
        avanza8()
        avanza9()
        avanza10()
        pista()
#Caballo 1 gano
        if len (caballo1)>=50:
            print("gano el caballo #")
#Caballo 2 gano
        if len (caballo2)>=50:
            print("gano el caballo @")
#Caballo 3 gano
        if len (caballo3)>=50:
            print("gano el caballo <")
#Caballo 4 gano
        if len (caballo4)>=50:
            print("gano el caballo >")
#Caballo 5 gano
        if len (caballo5)>=50:
                print("gano el caballo 5")
#Caballo 6 gano
        if len (caballo6)>=50:
            print("gano el caballo 8")
#Caballo 7 gano
        if len (caballo7)>=50:
            print("gano el caballo *")
#Caballo 8 gano
        if len (caballo8)>=50:
            print("gano el caballo 3")
#Caballo 9 gano
        if len (caballo9)>=50:
            print("gano el caballo 0")
#Caballo 10 gano
        if len (caballo10)>=50:
            print("gano el caballo :")
#Define la velocidad de los caballos
        time.sleep(1)
#pregunta si quieres continuar jugando
    seguir=input("Quieres seguir?")
