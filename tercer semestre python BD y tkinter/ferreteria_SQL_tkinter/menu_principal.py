import tkinter as tk                                    #Importa la libreria de tkinter como tk
from Controllers.tipo_articulo_controller import *      #De la carpeta de Controllrs importar el archivo tipo articulo
from Controllers.tipo_movimiento_controller import *    #De la carpeta de Controllrs importar el archivo tipo movimiento
from Controllers.tipo_proveedor_controller import *     #De la carpeta de Controllrs importar el archivo de tipo proveedor
from Controllers.articulo_controller import *           #De la carpeta de Controllrs importar el archivo de articulo
from Controllers.proveedor_controller import *          #De la carpeta de Controllrs importar el archivo de proveedor

#Define la funcion de menu tipos articulos
def menu_tipos_articulos():
    manipular_tipo_articulo(frame)

#Define la funcion de menu articulos
def menu_articulos():
    manipular_articulos(frame)

#Define la funcion de menu tipos proveedores
def menu_tipos_proveedores():
    manipular_tipo_proveedor(frame)

#Define la funcion de menu proveedores
def menu_proveedores():
    manipular_proveedor(frame)

#Define la funcion de menu tipo movimientos
def menu_tipo_movimientos():
    manipular_tipo_movimiento(frame)

#Define la funcion de Salir
def salir():
    root.destroy()

#Define la pantalla principal
root=tk.Tk()
root.title("Menu principal")    #Titulo de la pantalla principal
root.resizable(1,1)             #Permite modificar el tamaño de la pantalla principal
root.geometry("1200x750")       #Define el tamaño de la pantalla principal
root.config(bg="white")         #Define el color de la pantalla principal
frame=tk.Frame(root,bg="black",width=1100, height=600)      #Define un marco 
frame.place(x=1,y=50)   #Define la posicion del marco

#Se crean los botones para abrir los tipos de catalogos: tipo articulo, articulo, tipo proveedor, proveedor, tipo movimiento 
botones_tipo_articulo=tk.Button(root,text="Tipo Articulo", command=menu_tipos_articulos, width=20, bg="black" ,fg="white")
botones_tipo_articulo.place(x=50,y=10)      #Define la posicion del boton

botones_articulo=tk.Button(root,text="Articulo",command=menu_articulos, width=20, bg="black", fg="white")
botones_articulo.place(x=200,y=10)          #Define la posicion del boton

botones_tipo_proveedor=tk.Button(root,text="Tipo Proveedor", command=menu_tipos_proveedores,width=20, bg="black" ,fg="white")
botones_tipo_proveedor.place(x=350,y=10)     #Define la posicion del boton

botones_proveedor=tk.Button(root,text="Proveedor",command=menu_proveedores,width=20,bg="black",fg="White")
botones_proveedor.place(x=500,y=10)     #Define la posicion del boton

botones_tipo_movimiento=tk.Button(root,text="Tipo Movimiento",command=menu_tipo_movimientos,width=20, bg="black" ,fg="white")
botones_tipo_movimiento.place(x=650,y=10)   #Define la posicion del boton

#Crea el boton salir 
boton_salir=tk.Button(root,text="Salir",command=salir,width=20,bg="Red",fg="white")
boton_salir.place(x=850,y=10)       #Define la posicion del boton

#Carga la pantalla
root.mainloop()