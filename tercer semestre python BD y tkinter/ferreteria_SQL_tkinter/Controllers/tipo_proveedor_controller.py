import tkinter as tk                            #Importa la libreria tkinter como tk
from tkinter import ttk                         #De la librera de tkinter importar ttk
from tkinter import messagebox                  #De la libreria de tkinter importar messagebos
from Data.manejabd_tipo_proveedor import *      #De la carpeta de Data importar el archivo manejabd_tipo_proveedor

#Funcion para manipular el tipo proveedor con el parametro de frame
def manipular_tipo_proveedor(frame):
    #Funcion para limpiar la pantalla
    def limpiar_root():
        for widget in frame.winfo_children():   #Recorre cada uno de los datos del catalogo de tipo proveedores
            widget.destroy()
    
    #Funcion para recuperar los registros de tipo proveedor   
    def recupera_registros_tipo_proveedor():
        lista_tipo_proveedor=list_tipo_proveedor()  #Crea la variable lista_tipo proveedor para llamar a la funcion de list_tipo_proveedor
        #Regresa los datos de tipo proveedor
        return[(fila["id_tipo_proveedor"],fila["descripcion"]) for fila in lista_tipo_proveedor]

    #Funcion para mostrar el tipo proveedor
    def mostrar_tipo_proveedor():
        global tree #La variable tree se toma como global
        filas=recupera_registros_tipo_proveedor()   #Se crea la variable filas y llama la funcion de recupera_registros_tipo_proveedor
        tree.delete(*tree.get_children())   #Borra los datos de tree
        #Crea un ciclo for para definir el tamaño de las columnas
        for encabezado in encabezados:
            tree.heading(encabezado,text=encabezado)
            if encabezado=="descripcion":
                tree.column(encabezado,width=600)
            else:
                tree.column(encabezado,width=200)
                
        for fila in filas:
            tree.insert("","end",values=fila)
        #Define la posicion de las columnas
        tree.pack(padx=10,pady=10)
        
    
    #Funcion para agrega el tipo proveedor
    def agregar_tipo_proveedor():
        valor=strDescripcion.get()  #Obtiene el valor de la descripcion ingresada
        #Si hay algun valor entonces insertar el tipo proveedor
        if valor:
            insert_tipo_proveedor(valor)    #Llama a la funcion para insertar el tipo proveedor
            #Mensaje para notificar que se agrego el tipo proveedor exitosamente
            messagebox.showinfo("Agregar", "Se agtego el registro")
            mostrar_tipo_proveedor()    #Llama la funcion mostrar_tipo_proveedor
        else:
            messagebox.showinfo("No se ingreso ningun valor")
                

    #Funcion para modificar el tipo proveedor
    def modifica_tipo_proveedor():
        id_tipo_proveedor=int(strid.get())  #Obtiene el valor del id_tipo_proveedor
        #Si se ingreso un valor correcto entonces solicitar la descripcion nueva
        if id_tipo_proveedor:   
            nueva_descripcion=strDescripcion.get()
            if nueva_descripcion:
                #Funcion para ejecutar update_tipo proveedor, para establecer el valor nuevo de la descripcion
                update_tipo_proveedor(id_tipo_proveedor,nueva_descripcion)
                #Mensaje para notificar que el tipo proveedor se modifico
                messagebox.showinfo("Modificar", "Se modifico el registro")
                #Funcion para mostrar el tipo proveedor
                mostrar_tipo_proveedor()
        else:
            messagebox.showinfo("No se ingreso ningun ID")

    #Funcion para eliminar el tipo proveedor
    def eliminar_tipo_proveedor():
        id_tipo_proveedor=int(strid.get())     #Obtiene el valor del id del tipo proveedor
        #Sui se ingreso un valor correcto entonces ejecutar delete_tipo_proveedor
        if id_tipo_proveedor:       
            #Ejecuta la funcion de delete_tipo_proveedor, para eliminar el tipo proveedor selecionado
            delete_tipo_proveedor(id_tipo_proveedor)
            #Mensaje para notificar que el tipo proveedor se a eliminado
            messagebox.showinfo("Eliminar", "Se elimino el registro")
            mostrar_tipo_proveedor()    #Funcion para mostrar el catalogo de tipo proveedor
        else:
            messagebox.showinfo("No se ingreso ningun ID")
    
    #Llama a la funcion limpiar_rrot para limpiar la pantalla
    limpiar_root()     
    global tree     #Toma la variable tree como global
    keySelect=-1
    
    #Se definen los valores strid, strDescripcion como stringsVars
    strid=tk.StringVar()
    strDescripcion=tk.StringVar()
    
    #Crea una barra de desplazamiento con orientacion vertical
    scrollbar_vertical=tk.Scrollbar(frame,orient=tk.VERTICAL)
    scrollbar_vertical.pack(side=tk.RIGHT,fill="y") #Define la posicion de la barra
    
    #Define las impresiones de los encabezados de las columnas
    encabezados=("ID", "Descripcion")
    #Imprime los encabezados y establece la barra de desplazamiento
    tree=ttk.Treeview(frame, columns=encabezados, show="headings", yscrollcommand=scrollbar_vertical.set)
    mostrar_tipo_proveedor()    #Ejecuta la funcion para mostrar el tipo proveedor
    tree.pack(padx=10,pady=10)  #Define la posicion de  los encabezados del tipo proveedor
    
    #Define como se mostrara la barra de desplazamiento
    scrollbar_vertical.config(command=tree.yview)
    
    #Define las etiquetas de: Id y Descripcion con sus posiciones
    lbl_id=tk.Label(frame,text="Id ", bg="black", fg="white")
    lbl_id.pack(padx=50,pady=5)
    
    entry_id=tk.Entry(frame,textvariable=strid)
    entry_id.pack(padx=50,pady=5)
    
    lbl_descripcion=tk.Label(frame, text="Descripcion ", bg="black", fg="white")
    lbl_descripcion.pack(padx=150,pady=5)
    
    ent_descripcion=tk.Entry(frame,textvariable=strDescripcion)
    ent_descripcion.pack(padx=150,pady=5)
    
    #Define los botones: Agregar, Modificar y Borrar  
    boton_enviar=tk.Button(frame,text="Agregar",command=agregar_tipo_proveedor, width=20,bg="black" ,fg="white")
    boton_enviar.pack()
    
    boton_modificar=tk.Button(frame,text="Modificar", command=modifica_tipo_proveedor,width=20, bg="black" ,fg="white")
    boton_modificar.pack()
    
    boton_borrar=tk.Button(frame,text="Borrar",command=eliminar_tipo_proveedor,width=20, bg="black" ,fg="white")
    boton_borrar.pack()
    
    frame.mainloop()    #Carga la pantalla