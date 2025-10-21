#Se genera la clase Calculadora
class Calculadora:
    #Se genera la instancia
    def __init__ (self,numero,memory,op_ante,op):
        self.Numeraso=numero #Atributo para el numero 
        self.memoria=memory # Atributo para el guardado de las operaciones
        self.op_ante = op_ante #Atributo de la operacion anterior
        self.ope=op #Atributo para la operacion actual
    #ingresa el numero
    def set_numero(self, numeraso):
        #establece el valor del numero
        self.Numeraso=numeraso
    #ingresa la operacion a realizar
    def set_opera(self, op_anterio):
        #Establece el signo de la operacion anterior 
        self.op_ante=op_anterio
    #guarda de el resultado de las operaciones anteriores
    def set_memoria(self,mem):
        #Define el atribute memoria como "mem"
        self.memoria=mem
    #Establece el valor de la operacion actual
    def set_opera(self, ope):
        #Define el atributo ope como ope
        self.ope=ope
    #Registra los resultados de la operacion
    def get_memoria(self):
        #Regresa los resultados de la memoria
        return self.memoria
    #Define la ejecucion de la calculadora
    def ejecuta (self):
        #si la operacion es una suma
        if self.op_ante=="+":
            #Ejecutar esta operacion
            self.memoria=self.memoria+self.Numeraso
        #si la operacion es un resta
        elif self.op_ante=="-":
            #Ejecuta la operacion de la resta
            self.memoria=self.memoria-self.Numeraso
        #si la operacion es multiplicacion
        elif self.op_ante=="*":
            #ejecutar la operacion de la multiplicacion
            self.memoria=self.memoria*self.Numeraso
        #si la operacion es una division
        elif self.op_ante=="/":
            #ejecuta la operacion de la division
            self.memoria=self.memoria/self.Numeraso
        #Verifica si no hay ninguna operacion anterior
        elif self.op_ante=="":
            #Ingresar un numero
            self.memoria=self.Numeraso
        #Define la operacion anterior como "ope"
        self.op_ante=self.ope
#Retoma la clase calculadora
calcu=Calculadora(0,0,"","")
#Define a operacion como nada
operaci=""
#ciclo de la calculadora
while operaci!="=":
    numer=int(input("Numero: "))
    operaci=input("operacion: ")
    calcu.set_numero(numer)
    calcu.set_opera(operaci)
    #ejecuta la calculadora
    calcu.ejecuta()
#imprime el resultado de la operacion
print("El resultado es: ", calcu.get_memoria())
