#pantalla incial
print("1","|","2","|","3")
print("------------------")
print("4","|","5","|","6")
print("------------------")
print("7","|","8","|","9")
#definir el numero de las variables
p1="1"
p2="2"
p3="3"
p4="4"
p5="5"
p6="6"
p7="7"
p8="8"
p9="9"
#nadie a ganado
gano=""
#contar el numero de jugadas
contador=0
#defino que el primero en jugar lo hace X
turno="X"

def hay_ganador():
    ganador=""
    if (p1==p2 and p1==p3):
        ganador=p1 or p2
    elif (p1==p4 and p1==p7):
        ganador=p1 or p2
    elif (p1==p5 and p1==p9):
        ganador=p1 or p2
    elif (p2==p5 and p2==p8):
        ganador=p1 or p2
    elif (p3==p6 and p3==p9):
        ganador=p1 or p2
    elif (p7==p8 and p7==p9):
        ganador=p1 or p2
    elif (p3==p5 and p3==p7):
        ganador=p1 or p2
    elif (p4==p5 and p4==p6):
        ganador=p1 or p2
    
    print("El ganador es: ", ganador)
    return ganador

#ciclo para jugar
while (gano=="" and contador<9):
    #pide la posicion
    pos=int(input('Dame la posicion: '))
    #Para determinar si la jugada es valida
    val=False

    if (pos== 1 and p1== "1"):
        p1=turno
        val=True
    if (pos==2 and p2=="2"):
        p2=turno
        val=True
    if (pos==3 and p3=="3"):
        p3=turno
        val=True
    if (pos==4 and p4=="4"):
        p4=turno
        val=True
    if (pos==5 and p5=="5"):
        p5=turno
        val=True
    if (pos==6 and p6=="6"):
        p6=turno
        val=True
    if (pos==7 and p7=="7"):
        p7=turno
        val=True
    if (pos==8 and p8=="8"):
        p8=turno
        val=True
    if (pos==9 and p9=="9"):
        p9=turno
        val=True
    #Verifica si la jugada es valida
    if val:
        gano=hay_ganador()
        #intercambia el turno
        if turno=="X":
            turno="O"
        else:
            turno="X"
        contador=contador+1
    else:
        print("El movimiento es invalido, intenta otra vez", turno)
    print(p1,"|",p2,"|",p3)
    print("----------------")
    print(p4, "|",p5,"|",p6)
    print("----------------")
    print(p7,"|",p8,"|",p9)    