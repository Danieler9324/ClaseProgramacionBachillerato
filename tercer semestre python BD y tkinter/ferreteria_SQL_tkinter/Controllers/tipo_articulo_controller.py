import tkinter as tk                            #Importa la libreria de tkinter como tk
from tkinter import ttk                         #Importa un parametro de la libreria de tkinter como ttk
from tkinter import messagebox                  #De la libreria de tkinter importa el parametro de messagebox
from Data.manejabd_tipo_articulos import *      #De la carpeta Data importa el archivo manejabd_tipo_articulos

#Funcion para manipular el tipo articulo, con el parametro de frame
def manipular_tipo_articulo(frame):
    #Funcion para limpiar la pantalla
    def limpia_root():  
        for widget in frame.winfo_children():   #Metodo para recorrer cada uno de los registros de tipo articulo y eliminarlos
            widget.destroy()    #Metodo para eliminar los datos
        
    #Funcion para recuperar los registros de tipo articulo
    def recupera_registros_tipo_articulo():
        lista_tipo_articulo = list_tipo_articulo()  #Se crea la variable lista tipo articulo para ejecutar la funcion de list_tipo_articulo 
        #Regresa los valores de la tabla de tipos articulos
        return [(fila["id_tipo_articulo"], fila["descripcion"]) for fila in lista_tipo_articulo]

    #Funcion para mostrar los tipos de articulos
    def mostrar_registros_tipo_articulo():
        global tree     #tree se toma como un valor global
        filas = recupera_registros_tipo_articulo()  #Se crea la variable filas y llama a la funcion de recupera registros tipo articulo
        tree.delete(*tree.get_children())           #Borra los datos de tree
        #Crea un ciclo for para definir el tamaño de las columnas
        for encabezado in encabezados:
            tree.heading(encabezado, text=encabezado)
            if encabezado == "descripcion":
                tree.column(encabezado, width=600)
            else:
                tree.column(encabezado, width=200)
        for fila in filas:
            tree.insert("", "end", values=fila)
        #Define la ubicacion de las columnas
        tree.pack(padx=10, pady=10)

    #Funcion para agregar un tipo articulo
    def agregar_tipo_articulo():    
        valor = strDescripcion.get()    #Obtiene el valor de la descripcion
        if valor:                       #Si hay algo en valor entonces insertar el tipo articulo ingresado y mostrar un mensaje en la pantalla
            insert_tipo_articulo(valor)
            #Me sja epara notificar que el tipo articulo se agrego al catalogo
            messagebox.showinfo("Agregar", "Se agregó el registro")
            #Llama a la funcion de mostrar_registros_tipo_articulo
            mostrar_registros_tipo_articulo()
        else:
            messagebox.showinfo("Error", "No se ingresó ningún valor en la descripción")

    # Función para modificar un tipo articulo
    def modificar_tipo_articulo():
        #Lee los valores que se ingresaron y pide la descripcion nueva
        id_tipo_articulo = int(strId.get())
        if id_tipo_articulo:
            nueva_descripcion = strDescripcion.get()
            if nueva_descripcion:
                #Ejecuta la funcion para actualizar el tipo articulo
                update_tipo_articulo(id_tipo_articulo, nueva_descripcion)
                messagebox.showinfo("Modificar", "Se modificó el registro")
                #Ejecuta la funcion de mostrar los registros del tipo articulo
                mostrar_registros_tipo_articulo()
        else:
            messagebox.showinfo("Error", "No se ingresó ningún ID")
    
    #Funcion para eliminar un tipo de articulo        
    def eliminar_tipo_articulo():
        #Lee el Id introducido
        id_tipo_articulo=int(strId.get())
        #Si se ingreso un valor en id_tipo_articulo entonces ejecutar delete_tipo_articulo
        if id_tipo_articulo:
            delete_tipo_articulo(id_tipo_articulo)
            #Llama a la funcion de mostrar_registros tipo articulo
            mostrar_registros_tipo_articulo()
            #Mensaje para notificar que el tipo articulo se elimino
            messagebox.showinfo("Eliminar", "Se eliminó el registro")
        else:
            messagebox.showinfo("Error", "No se ingresó ningún ID")
    
    #Limpia la pantalla antes de mostrar el catalogo
    limpia_root()
    global tree     #Toma a tree como global
    ketSelect=-1
    
    #Define las variables: strId,strDescripcion como una barra de cadenas de caracteres con la libreria de tkinter
    strId = tk.StringVar()
    strDescripcion = tk.StringVar()
    #Crea una barra de desplazamiento vertical
    scrollbar_vertical = tk.Scrollbar(frame, orient=tk.VERTICAL)
    scrollbar_vertical.pack(side=tk.RIGHT, fill="y")
    
    encabezados=("ID", "Descripción")     #Imprime los encabezados de las columnas
    #Crea una funcion para mostrar los encabezados y establecer la barra de desplazamiento
    tree = ttk.Treeview(frame, columns=encabezados, show="headings", yscrollcommand=scrollbar_vertical.set)
    mostrar_registros_tipo_articulo()   #Llama a la funcion de mostrar registros
    tree.pack(padx=10, pady=10)         #Define la ubicacion de los encabezados
    
    #Define como se mostrara la barra de desplazamiento
    scrollbar_vertical.config(command=tree.yview)                                       
    
    #Define las etiquetas donde se introducira la informacion, las etiquetas son: ID, Descripcion
    lbl_id = tk.Label(frame, text="Id: ", bg="black", fg="white")
    lbl_id.pack(padx=50, pady=5)
    
    entry_id = tk.Entry(frame, textvariable=strId)
    entry_id.pack(padx=50, pady=5)
    
    lbl_descripcion = tk.Label(frame, text="Descripción: ", bg="black", fg="white")
    lbl_descripcion.pack(padx=150, pady=5)
    
    ent_descripcion = tk.Entry(frame, textvariable=strDescripcion)
    ent_descripcion.pack(padx=150, pady=5)
    
    #Define los botones de: Agregar,Modificar,Borrar
    boton_enviar = tk.Button(frame, text="Agregar", command=agregar_tipo_articulo, width=20, bg="black", fg="white")
    boton_enviar.pack()
    
    boton_modificar = tk.Button(frame, text="Modificar", command=modificar_tipo_articulo, width=20, bg="black", fg="white")
    boton_modificar.pack()
    
    boton_borrar = tk.Button(frame, text="Borrar", command=eliminar_tipo_articulo, width=20, bg="black", fg="white")
    boton_borrar.pack()

    frame.mainloop()    #Carga la ventana
    