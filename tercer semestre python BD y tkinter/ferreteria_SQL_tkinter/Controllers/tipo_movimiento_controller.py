import tkinter as tk                            #Importar la libreria de tkinter como tk
from tkinter import ttk                         #De la libreria de tkinter importar ttk
from tkinter import messagebox                  #De la libreria de tkinter importar messagebox
from Data.manejabd_tipo_movimiento import *     #De la carpeta de Data importar el archivo de manejabd_tipo_movimiento

#Funcion para manipular el tipo movimiento con el parametro de frame
def manipular_tipo_movimiento(frame):
    #Funcion para limpiar_root es decir limpiar la pantalla
    def limpiar_root():
        for widget in frame.winfo_children():      #Recorre cada uno de los datos de el catalogo de tipo movimiento
            widget.destroy()
    
    #Funcion para recuperar los registros de tipo movimiento
    def recupera_registros_tipo_movimiento():
        lista_tipo_movimiento=list_tipo_movimiento()    #Crea la variable lista_tipo_movimiento para llamar a la funcion de list_tipo_movimiento
        #Regresa los datos del catalogo tipo movimiento
        return [(fila["id_tipo_movimiento"],fila["descripcion"],fila["entrada_salida"],fila["almacen_piso"]) for fila in lista_tipo_movimiento]

    #Funcion para mostrar los registros de tipo movimiento
    def mostrar_tipo_movimiento():
        global tree #La variable tree se toma como global
        filas=recupera_registros_tipo_movimiento()  #Se crea la variable filas para llamar a la funcion de recuperar_registros_tipo_movimiento
        tree.delete(*tree.get_children())   #Borra los datos que contiene tree
        #Crea un ciclo for para definir el tamaño de las columnas
        for encabezado in encabezados:      
            tree.heading(encabezado, text=encabezado)
            if encabezado=="descripcion":
                tree.column(encabezado,width=600)
            else:
                tree.column(encabezado,width=200)
        
        for fila in filas:
            tree.insert("","end",values=fila)
        #Define la posicion de las columnas
        tree.pack(padx=10,pady=10)
        
    #Funcion para agregar registros del tipo movimiento
    def agregar_tipo_movimiento():
        valor=strDescripcion.get()              #Obtiene el valor de la descripcion
        valor_entrada=strEntradaSalida.get()    #Obtiene el valor de la Entrada y Salida
        valor_almacen=strAlmacenPiso.get()      #Obtiene el valor de el Almacen y Piso
        #Si estan los valores requeridos entonces insertar el tipo movimiento
        if valor:
            insert_tipo_movimiento(valor,valor_entrada,valor_almacen)   #Llama a la funcion para insertar el tipo movimiento
            #Mensaje para notificar que se agrego el tipo movimiento exitosamente
            messagebox.showinfo("Agregar", "Se agrego el registro")
            mostrar_tipo_movimiento()   #Llama la funcion mostrar_tipo_movimiento
        else:
            messagebox.showinfo("No se ingreso ningun valor")

        
    #Funcion para modificar el tipo movimiento
    def modifica_tipo_movimiento():
        id_tipo_movimiento=int(strId.get())     #Obtiene el valor del id del tipo movimiento
        #Si se ingreso un valor correcto entonces solicitar la nueva descripcion, ueva entrada y salida y nuevo almacen o piso
        if id_tipo_movimiento:
            nueva_descripcion=strDescripcion.get()
            if nueva_descripcion:
                nueva_entrada_salida=strEntradaSalida.get()
                if nueva_entrada_salida:
                    nueva_almacen_piso=strAlmacenPiso.get()
                    if nueva_entrada_salida:
                        #Funcion para ejecutar update_tipo_movimiento, para establecer los nuevos valores
                        update_tipo_movimiento(id_tipo_movimiento,nueva_descripcion,nueva_entrada_salida,nueva_almacen_piso)
                        #Mensaje para notificar que el tipo movimiento se modifico
                        messagebox.showinfo("Modificar", "Se modifico el registro")
                        mostrar_tipo_movimiento()
                else:
                    messagebox.showinfo("No se ingreso ningun ID")

    #Funcion para eliminar el tipo de movimiento
    def elimina_tipo_movimiento():
        id_tipo_movimiento=int(strId.get()) #Obtiene el valor del id tipo movimiento
        #Si el valor obtenido es correcto entonces ejecutar delete_tipo_movimiento
        if id_tipo_movimiento:
            #Ejecuta la funcion de delete_tipo_movimiento, para eliminar el tipo movimiento
            delete_tipo_movimiento(id_tipo_movimiento)
            mostrar_tipo_movimiento()   #Ejecuta la funcion para mostrar el catalogo de tipo movimiento
            #Mensaje para notificar que el tipo movimiento fue dado de baja
            messagebox.showinfo("Baja","Registro eliminado")
        else:
            messagebox.showinfo("No se ingreso ningun ID")

    #Limpia la pantalla
    limpiar_root()
    global tree     #Toma la variable tree como global
    keySelect=-1
    
    #Se definenlos valores strID, strDescripcion, strEntradaSalida, strAlmacenPiso como StringsVars
    strId=tk.StringVar()
    strDescripcion=tk.StringVar()
    strEntradaSalida=tk.StringVar()
    strAlmacenPiso=tk.StringVar()
    
    #Crea una barra de desplazamiento con orientacion vertical
    scrollbar_vertical=tk.Scrollbar(frame,orient=tk.VERTICAL)
    scrollbar_vertical.pack(side=tk.RIGHT,fill="y") #Define la posicion de la barra
    
    #Define las impresiones de los encabezados de las columnas
    encabezados=("ID", "Descripcion", "Entrada Salida", "Almacen Piso")
    #Imprime los enecabezados y establece la barra de desplazmiento
    tree=ttk.Treeview(frame, columns=encabezados, show="headings",yscrollcommand=scrollbar_vertical.set)
    mostrar_tipo_movimiento()   #Ejecuta la funcion para mostrar el tipo movimiento
    tree.pack(padx=10,pady=10)  #Define la poscion de los encabezados del tipo movimiento
    
    #Define como se mostrara la barra de desplazamiento
    scrollbar_vertical.config(command=tree.yview)
    
    #Define las etiquetas de: Id, Descripcion, Entrada Salida, Almacen Piso con sus respectivas posiciones
    lbl_id=tk.Label(frame,text="Id", bg="black", fg="white")
    lbl_id.pack(padx=50,pady=5)
    
    entry_id=tk.Entry(frame,textvariable=strId)
    entry_id.pack(padx=50,pady=5)
    
    lbl_descripcion=tk.Label(frame, text="Descripcion", bg="black", fg="white")
    lbl_descripcion.pack(padx=150,pady=5)
    
    
    ent_descripcion=tk.Entry(frame,textvariable=strDescripcion)
    ent_descripcion.pack(padx=150,pady=5)
    
    lbl_entrada_salida=tk.Label(frame,text="Entrada Salida", bg="black", fg="white")
    lbl_entrada_salida.pack(padx=80,pady=5)
    
    entry_entrada_salida=tk.Entry(frame,textvariable=strEntradaSalida)
    entry_entrada_salida.pack(padx=80,pady=5)

    lbl_almacen_piso=tk.Label(frame,text="Almacen o Piso", bg="black", fg="white")
    lbl_almacen_piso.pack(padx=80,pady=5)
    
    entry_almacen_piso=tk.Entry(frame,textvariable=strAlmacenPiso)
    entry_almacen_piso.pack(padx=80,pady=5)

    #Define los botones: Agregar, Modificar y Borrar
    boton_enviar=tk.Button(frame,text="Agregar",command=agregar_tipo_movimiento, width=20,bg="black" ,fg="white")
    boton_enviar.pack()
    
    boton_modificar=tk.Button(frame,text="Modificar", command=modifica_tipo_movimiento,width=20, bg="black" ,fg="white")
    boton_modificar.pack()
    
    boton_borrar=tk.Button(frame,text="Borrar",command=elimina_tipo_movimiento,width=20, bg="black" ,fg="white")
    boton_borrar.pack()
    
    frame.mainloop()    #Carga la pantalla