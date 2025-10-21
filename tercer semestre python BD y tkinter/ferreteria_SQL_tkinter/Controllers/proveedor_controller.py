import tkinter as tk                    #Importa la libreria tkinter como tk
from tkinter import ttk                 #De la libreria tkinter importar ttk
from tkinter import messagebox          #De la libreria tkinter importar messagebos
from Data.manejabd_proveedor import *   #De la carpeta de Data importar el archivo de manejabd_proveedor

#Funcion para manipulas_proveedor con el parametro de frame
def manipular_proveedor(frame):
    #Funcion para limpiar pantalla
    def limpiar_root():
        for widget in frame.winfo_children():   #Metodo para recorrer todos los datos de los proveedores
            widget.destroy()    #Metodo para eliminar los datos

    #Funcion para recuperar el catalogo de proveedores
    def recuperar_proveedores():
        lista_proveedor = list_proveedor()  #Se crea la variable lista_proveedor, para llamar a la funcion de list_proveedor
        #Regresa los datos de el catalogo de proveedores
        return [(fila["id_proveedor"], fila["razon_social"], fila["id_tipo_proveedor"], fila["rfc"], fila["direccion"], fila["telefono"], fila["correo_electronico"], fila["contacto"]) for fila in lista_proveedor]

    #Funcion para mostrar los proveedores
    def mostrar_proveedor():
        global tree         #Toma la variable tree como global
        filas = recuperar_proveedores()     #Crea la variable filas para llamar a la funcion de recuperar proveedores
        tree.delete(*tree.get_children())   #Borra los datos de tree
        for encabezado in encabezados:      #Crea un ciclo for para definir el tamaño de las columnas
            tree.heading(encabezado, text=encabezado)   
            if encabezado == "Razon Social":
                tree.column(encabezado, width=200)
            elif encabezado == "Correo electronico":
                tree.column(encabezado, width=200)  
            elif encabezado == "Contacto":
                tree.column(encabezado, width=150)
            else:
                tree.column(encabezado, width=100)
        for fila in filas:
            tree.insert("", "end", values=fila)
        tree.pack(padx=10, pady=10)
    
    #Funcion para agregar proveedor
    def agregar_proveedor():
        valor_razon=strRazonSocial.get()                        #Se obtiene el valor de la Razon social
        valor_tipo_proveedor=strTipoProveedor.get()             #Se obtiene el valor de el tipo proveedor
        valor_rfc=strRFC.get()                                  #Se obtiene el valor del RFC
        valor_direccion=strDireccion.get()                      #Se obtiene el valor de la direccion
        valor_telefono=strTelefono.get()                        #Se obtiene el valor del telefono
        valor_correo_electronico=strCorreoElectronico.get()     #Se obtiene el valor del correo electronico
        valor_contacto=strContacto.get()                        #Se obtiene el valor del contacto
        #Si estan los valores necesarios entonces insertar dichos valores
        if valor_razon:
            #Llama a la funcion para insertar los valores
            insert_proveedor(valor_razon,valor_tipo_proveedor,valor_rfc,valor_direccion,valor_telefono,valor_correo_electronico,valor_contacto)
            #Mensaje para notificar el proveedor se agrego
            messagebox.showinfo("Agregar","Se agrego el registro")
            mostrar_proveedor() #Llama a la funcion para mostrar all proveedor
        else:
            messagebox.showinfo("No se ingreso un valor requerido")
    
    #Funcion para modificar al proveedor
    def modificar_proveedor():
        #Obtiene los valores introducidos: Id_proveedor,razon_social,RFC,Direccion,Telefono,correo_electronico y contacto
        id_proveedor=int(strId.get())
        if id_proveedor:
            nueva_razon_social=strRazonSocial.get()
            if nueva_razon_social:
                nueva_rfc=strRFC.get()
                if nueva_rfc:
                    nueva_direccion=strDireccion.get()
                    if nueva_direccion:
                        nuevo_telefono=strTelefono.get()
                        if nuevo_telefono:
                            nuevo_correo_electronico=strCorreoElectronico.get()
                            if nuevo_correo_electronico:
                                nuevo_contacto=strContacto.get()
                                if nuevo_contacto:
                                    #Ejecuta la funcion para actualizar el proveedor
                                    update_proveedor(nueva_razon_social,nueva_rfc,nueva_direccion,nuevo_telefono,nuevo_correo_electronico,nuevo_contacto,id_proveedor)
                                    #Mensaje para notificar que el proveedor se modifico con exito
                                    messagebox.showinfo("Modificar", "Se modifico el registro")
                                    #Llama a la funcion de mostrar_proveedor
                                    mostrar_proveedor()
        else:
            messagebox.showinfo("No se ingreso el ID")
    
    #Funcion para eliminar un proveedodr
    def eliminar_proveedor():
        #Lee le ID introducido
        id_proveedor=int(strId.get())
        #Si se ingreso un valor en id_proveedor entonces ejecutar delete_proveedor   
        if id_proveedor:
            #Llama a la funcion para eliminar al proveedor
            delete_proveedor(id_proveedor)
            mostrar_proveedor()     #Llama la funcion mostrar_proveedor 
            #Mensaje paa notificar que el proveedor se elimino
            messagebox.showinfo("Baja", "Se elimino el registro")
        else:
            messagebox.showinfo("No se ingreso el ID")
    
    #Limpia la pantalla
    limpiar_root()
    global tree     #TOma l avariable tree como global
    keySelect=-1
    
    #Define las variables: strId,strRazonSocial,strTipoProveedor,strRFC,strDireccion,strDireccion,strTelefono,strCorreoElectronico,strContacto como StringsVars para ingresar datos
    strId=tk.StringVar()
    strRazonSocial=tk.StringVar()
    strTipoProveedor=tk.StringVar()
    strRFC=tk.StringVar()
    strDireccion=tk.StringVar()
    strTelefono=tk.StringVar()
    strCorreoElectronico=tk.StringVar()
    strContacto=tk.StringVar()
    
    #Crea una barra de desplazamiento vertical
    scroll_vertical=tk.Scrollbar(frame,orient=tk.VERTICAL)
    scroll_vertical.pack(side=tk.RIGHT,fill="y")    #Define de que lado estara la barra de desplazamiento
    
    #Imprime los encabezados de las columnas
    encabezados=("ID","Razon Social","ID tipo Proveedor","RFC","Direccion","Telefono","Correo electronico","Contacto")
    #Crea una uncion para mostrar los encabezados y establecer la barra de desplazamiento
    tree=ttk.Treeview(frame,columns=encabezados,show="headings",yscrollcommand=scroll_vertical.set)
    mostrar_proveedor()         #Llama a la funcion de mostrar proveedor
    tree.pack(padx=1,pady=1)    #Define la ubicacion de los encabezados
    
    #Define como se mostrara la barra de desplazamiento
    scroll_vertical.config(command=tree.yview)
    
    #Define las etiquetas donde se introducira la informacion, las etiquetas son: ID, Razon Social,ID tipo proveedor, RFC, Direccion, Telefono, Correo electronico, Contacto y define la posicion de cada uno 
    lbl_id=tk.Label(frame,text="ID",bg="black",fg="white")
    lbl_id.pack(padx=50,pady=5)
    
    entry_id=tk.Entry(frame,textvariable=strId)
    entry_id.pack(padx=50,pady=5)
    
    lbl_razon_social=tk.Label(frame,text="Razon Social",bg="black",fg="white")
    lbl_razon_social.pack(padx=150,pady=5)
    
    entry_razon_social=tk.Entry(frame,textvariable=strRazonSocial)
    entry_razon_social.pack(padx=150,pady=5)
    
    lbl_tipo_proveedor=tk.Label(frame,text="ID tipo proveedor",bg="black",fg="white")
    lbl_tipo_proveedor.pack(padx=150,pady=5)
    
    entry_tipo_proveedor=tk.Entry(frame,textvariable=strTipoProveedor)
    entry_tipo_proveedor.pack(padx=150,pady=5)

    lbl_RFC=tk.Label(frame,text="RFC",bg="black",fg="white")
    lbl_RFC.pack(padx=150,pady=5)
    
    entry_RFC=tk.Entry(frame,textvariable=strRFC)
    entry_RFC.pack(padx=150,pady=5)
    
    lbl_Direccion=tk.Label(frame,text="Direccion",bg="black",fg="white")
    lbl_Direccion.pack(padx=150,pady=5)
    
    entry_Direccion=tk.Entry(frame,textvariable=strDireccion)
    entry_Direccion.pack(padx=150,pady=5)
    
    lbl_Telefono=tk.Label(frame,text="Telefono",bg="black",fg="white")
    lbl_Telefono.pack(padx=150,pady=5)
    
    entry_Telefono=tk.Entry(frame,textvariable=strTelefono)
    entry_Telefono.pack(padx=150,pady=5)
    
    lbl_Correo_Electronico=tk.Label(frame,text="Correo Electronico",bg="black",fg="white")
    lbl_Correo_Electronico.pack(padx=150,pady=5)
    
    entry_Correo_Electronico=tk.Entry(frame,textvariable=strCorreoElectronico)
    entry_Correo_Electronico.pack(padx=150,pady=5)
    
    lbl_Contacto=tk.Label(frame,text="Contacto",bg="black",fg="white")
    lbl_Contacto.pack(padx=150,pady=5)
    
    entry_Contacto=tk.Entry(frame,textvariable=strContacto)
    entry_Contacto.pack(padx=150,pady=5)
    
    #Define los botones de: Agregar,Modificar y Borrar a la izquierda de las etiquetas
    boton_enviar=tk.Button(frame,text="Agregar",command=agregar_proveedor,width=20,bg="black",fg="white")
    boton_enviar.place(x=200,y=250)
    
    boton_modificar=tk.Button(frame,text="Modificar",command=modificar_proveedor,width=20,bg="black",fg="white")
    boton_modificar.place(x=200,y=300)
    
    boton_eliminar=tk.Button(frame,text="Eliminar", command=eliminar_proveedor,width=20,bg="black",fg="white")
    boton_eliminar.place(x=200,y=350)
    
    frame.mainloop()    #Carga la ventana