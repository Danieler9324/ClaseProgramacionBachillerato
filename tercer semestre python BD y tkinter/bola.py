from tkinter import *

# Se crea la variable pantalla 
pantalla = Tk()

# Se crean los parámetros para la ventana
pantalla.resizable(0, 0)                  # Define si la pantalla puede ser modificada
pantalla.geometry("700x400")              # Define el tamaño de la pantalla
pantalla.config(bg="black")               # Define el color del fondo
pantalla.title("Bola")                    # Título de la pantalla

# Define la bola y el tipo de fuente y color
ec = Label(pantalla, text=".", font="Helvetica 40 bold", bg="black", fg="white")
ec.place(x=0, y=0)

# Variables globales
px, py = 0, 0          # Posición inicial
ix, iy = 5, 2          # Velocidades
ti = 30                # Tiempo en milisegundos (no segundos)

def mover_bola():
    global px, py, ix, iy, ti

    # Rebotes
    if px < 0:
        ix = 5
        ti = max(5, ti // 2)  # Evita que sea menor a 5 ms
    elif px > 680:
        ix = -5
        ti = max(5, ti // 2)
    if py < 0:
        iy = 2
        ti = max(5, ti // 2)
    elif py > 380:
        iy = -2
        ti = max(5, ti // 2)

    # Mover la bola
    px += ix
    py += iy
    ec.place(x=px, y=py)

    # Volver a ejecutar después de "ti" milisegundos
    pantalla.after(int(ti), mover_bola)

# Iniciar movimiento
mover_bola()

pantalla.mainloop()
