import tkinter as tk                    #Importa la libreria de tkinter como tk
from tkinter import ttk                 #Importa un parametro de la libreria de tkinter
from tkinter import messagebox          #Importa el parametro de la libreria de tkinter
from Data.manejabd_articulo import *    #De la carpeta de Data importar el archivo de manejabd_articulo

#Funcion para manipular articulos
def manipular_articulos (frame):
    #Funcion para limpiar el root
    def limpiar_root():
        for widget in frame.winfo_children():   #Crea un ciclo for para recorrer cada uno de los datos de los registros
            widget.destroy()            #Elimina los datos
    
    #Funcion para recuperar los articulos
    def recuperar_articulos():
        lista_articulo=list_articulo()  #Crea una variable para ejecutar la funcion de list_articulo
        #Regresa los datos de el catalogo de articulos
        return [(fila["id_articulo"],fila["descripcion"],fila["id_tipo_articulo"],fila["costo"],fila["precio_mayoreo"],fila["precio_menudeo"],fila["cantidad_almacen"],fila["cantidad_tienda"]) for fila in lista_articulo]

    #Funcion para mostrar los articulos
    def mostrar_articulo():
        global tree         #La variable tree se toma como global
        filas=recuperar_articulos()     #Se crea la variable filas para ejecutar la funcion de recuperar articulos
        tree.delete(*tree.get_children())   #Borra los datos de tree
        #Crea un ciclo for para definir el tamaño de las columnas
        for encabezado in encabezados:
            tree.heading(encabezado,text=encabezado)
            if encabezado=="descripcion":
                tree.column(encabezado,width=600)
            else:
                tree.column(encabezado,width=125)
        for fila in filas:
            tree.insert("","end",values=fila)
        
        tree.pack(padx=10,pady=10)

    #Funcion para agregar articulos
    def agregar_articulo():
        valor=strDescripcion.get()                      #Obtiene el valor de la descripcion
        valor_tipo=strTipoArticulo.get()                #Obtiene el valor del tipo articulo 
        valor_costo=strCosto.get()                      #Obtiene el valor del costo
        valor_precio_mayoreo=strPrecioMayoreo.get()     #Obtiene el valor del precio mayoreo
        valor_precio_menudeo=strPrecioMenudeo.get()     #Obtiene el valor del precio menudeo
        valor_cantidad_almacen=strCantidadAlmacen.get() #Obtiene el valor de la cantidad en almacen 
        valor_cantidad_tienda=strCantidadTienda.get()   #Obtiene el valor de la cantidad en tienda
        #Si hay algo en los valores entonces ejecutar insert_articulo
        if valor:
            insert_articulo(valor,valor_tipo,valor_costo,valor_precio_mayoreo,valor_precio_menudeo,valor_cantidad_almacen,valor_cantidad_tienda)
            #Mensaje para notificar que el articulo a sido añadido
            messagebox.showinfo("Agregar", "Se agrego el registro")
            #Llama a la funcion de mostrar_articulo
            mostrar_articulo()
        else:
            #Mensaje para notificar si un valor no a sido introducido
            messagebox.showinfo("No se ingreso un valor requerido")

    #Funcion para modificar articulos
    def modificar_articulo():
        #Obtiene los valores del ID,Descripcion,Costo,Precio mayoreo, Precio menudeo,Cantidad en almacen y Cantidad en la tienda 
        id_articulo=int(strId.get())
        if id_articulo:
            nueva_descripcion=strDescripcion.get()
            if nueva_descripcion:
                nuevo_costo=strCosto.get()
                if nuevo_costo:
                    nuevo_precio_mayoreo=strPrecioMayoreo.get()
                    if nuevo_precio_mayoreo:
                        nuevo_precio_menudeo=strPrecioMenudeo.get()
                        if nuevo_precio_menudeo:
                            nueva_cantidad_almacen=strCantidadAlmacen.get()
                            if nueva_cantidad_almacen:
                                nueva_cantidad_tienda=strCantidadTienda.get()
                                if nueva_cantidad_tienda:
                                    #Si los valores son correctos entonces ejecutar update_articulo
                                    update_articulo(id_articulo,nueva_descripcion,nuevo_costo,nuevo_precio_mayoreo,nuevo_precio_menudeo,nueva_cantidad_almacen,nueva_cantidad_tienda)
                                    messagebox.showinfo("Modificar", "Se modifico el registro")     #Mensaje para notificar que el articulo se modifico
                                    #Llama la funcion de mostrar_articulo
                                    mostrar_articulo()
        else:
            #Mensaje para notificar si se ingreso un ID o no
            messagebox.showinfo("No se ingreso ningun ID")
            
    #Funcion para eliminar articulo
    def eliminar_articulo():
        #Obtiene el valor del id_articulo
        id_articulo=int(strId.get())
        if id_articulo:
            #Si hay algun valor en id articulo entonces, eliminar el id seleccionado
            delete_articulo(id_articulo)
            #Llama a la funcion para mostrar_articulo
            mostrar_articulo()
            #Mensaje para notificar que el articulo se elimino con exito
            messagebox.showinfo("Baja","Se elimino el registro")
        else:
            messagebox.showinfo("No se ingreso ningun ID")
    
    #Llama a la funcion de limpiar root
    limpiar_root()
    global tree     #Toma la variable tree como global
    keySelect=-1
    
    #Crea las variables Id,Descripcion,TipoArticulo,Costo,Precio_Mayoreo,Precio_menudeo,Cantidad_almacen,Cantidad_tienda como StringsVars
    strId=tk.StringVar()
    strDescripcion=tk.StringVar()
    strTipoArticulo=tk.StringVar()
    strCosto=tk.StringVar()
    strPrecioMayoreo=tk.StringVar()
    strPrecioMenudeo=tk.StringVar()
    strCantidadAlmacen=tk.StringVar()
    strCantidadTienda=tk.StringVar()
    
    #Crea una barra de desplazamiento con orientacion vertical
    scroll_vertical=tk.Scrollbar(frame,orient=tk.VERTICAL)
    scroll_vertical.pack(side=tk.RIGHT,fill="y")    #Define la posicion de la barra de desplazamiento
    
    #Imprime los encabezados
    encabezados=("ID","Descipcion","ID tipo articulo","Costo","Precio Mayoreo","Precio Menudeo","Cantidad Almacen","Cantidad Tienda")
    #Crea los encabezados de las columnas y la barra de desplazamiento
    tree=ttk.Treeview(frame,columns=encabezados,show="headings", yscrollcommand=scroll_vertical.set)
    mostrar_articulo()          #Llama a la funcion para mostrar los registros
    tree.pack(padx=1,pady=1)    #Define la ubicacion de los encabezados
    
    #Define como se mostrara la barra de desplazamiento
    scroll_vertical.config(command=tree.yview)
    
    #Define las etiquetas para donde se introducira la informacion, y las etiquetas son:Id,Descripcion_ID tipo articulo, Costo,Precio Mayoreo, Precio Menudeo, Cantidad Almacen, Cantidad Tienda y se define en que posicion estaran
    lbl_id=tk.Label(frame,text="Id ",bg="Black", fg="White")
    lbl_id.pack(padx=50,pady=5)
    
    entry_id=tk.Entry(frame,textvariable=strId)
    entry_id.pack(padx=50,pady=5)
    
    lbl_descripcion=tk.Label(frame, text="Descripcion ",bg="Black", fg="White")
    lbl_descripcion.pack(padx=150,pady=5)
    
    ent_descripcion=tk.Entry(frame,textvariable=strDescripcion)
    ent_descripcion.pack(padx=150,pady=5)
    
    lbl_id_tipo=tk.Label(frame, text="ID tipo articulo ",bg="Black", fg="White")
    lbl_id_tipo.pack(padx=150,pady=5)
    
    ent_id_tipo=tk.Entry(frame,textvariable=strTipoArticulo)
    ent_id_tipo.pack(padx=150,pady=5)
    
    lblcosto=tk.Label(frame, text="Costo ",bg="Black", fg="White")
    lblcosto.pack(padx=150,pady=5)
    
    ent_costo=tk.Entry(frame,textvariable=strCosto)
    ent_costo.pack(padx=150,pady=5)
    
    lblpreciomayoreo=tk.Label(frame, text="Precio Mayoreo ",bg="Black", fg="White")
    lblpreciomayoreo.pack(padx=150,pady=5)
    
    ent_preciomayoreo=tk.Entry(frame,textvariable=strPrecioMayoreo)
    ent_preciomayoreo.pack(padx=150,pady=5)
    
    lblprecioMenudeo=tk.Label(frame, text="Precio Menudeo ",bg="Black", fg="White")
    lblprecioMenudeo.pack(padx=150,pady=5)
    
    ent_precioMenudeo=tk.Entry(frame,textvariable=strPrecioMenudeo)
    ent_precioMenudeo.pack(padx=150,pady=5)
    
    lblcantidadalmacen=tk.Label(frame, text="Cantidad Almacen ",bg="Black", fg="White")
    lblcantidadalmacen.pack(padx=150,pady=5)
    
    ent_cantidadalmacen=tk.Entry(frame,textvariable=strCantidadAlmacen)
    ent_cantidadalmacen.pack(padx=150,pady=5)
    
    lblcantidadTienda=tk.Label(frame, text="Cantidad Tienda ",bg="Black", fg="White")
    lblcantidadTienda.pack(padx=150,pady=5)
    
    ent_cantidadTienda=tk.Entry(frame,textvariable=strCantidadTienda)
    ent_cantidadTienda.pack(padx=150,pady=5)
    
    #Define los botones de: Agregar, Modificar y eliminar a la izquierda de las etiquetas
    boton_enviar=tk.Button(frame,text="Agregar",command=agregar_articulo, width=20,bg="black" ,fg="white")
    boton_enviar.place(x=200,y=250)
    
    boton_modificar=tk.Button(frame,text="Modificar", command=modificar_articulo,width=20, bg="black" ,fg="white")
    boton_modificar.place(x=200,y=300)
    
    boton_borrar=tk.Button(frame,text="Borrar",command=eliminar_articulo,width=20, bg="black" ,fg="white")
    boton_borrar.place(x=200,y=350)
    
    #Carga la pantalla
    frame.mainloop()