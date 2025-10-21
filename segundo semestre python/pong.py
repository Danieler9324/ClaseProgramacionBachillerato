from tkinter import *
import time

pantalla = Tk()
pantalla.resizable(0, 0)
pantalla.geometry("700x400")
pantalla.config(bg="black")
pantalla.title("PingPong")

bola = Label(pantalla, text=".", font="Helvetica 40 bold", bg="black", fg="white")
bola.place(x=340, y=190)

paleta1 = Label(pantalla, bg="white", width=2, height=10)
paleta1.place(x=20, y=150)

paleta2 = Label(pantalla, bg="white", width=2, height=10)
paleta2.place(x=660, y=150)

px, py = 340, 190  
ix, iy = 5, 3  
ti = 30  

paleta1_y = 150
paleta2_y = 150
velocidad_paleta = 20

def mover_paleta1_arriba(event):
    global paleta1_y
    if paleta1_y > 0:
        paleta1_y -= velocidad_paleta
        paleta1.place(x=20, y=paleta1_y)

def mover_paleta1_abajo(event):
    global paleta1_y
    if paleta1_y < 300:  
        paleta1_y += velocidad_paleta
        paleta1.place(x=20, y=paleta1_y)

def mover_paleta2_arriba(event):
    global paleta2_y
    if paleta2_y > 0:
        paleta2_y -= velocidad_paleta
        paleta2.place(x=660, y=paleta2_y)

def mover_paleta2_abajo(event):
    global paleta2_y
    if paleta2_y < 300:  
        paleta2_y += velocidad_paleta
        paleta2.place(x=660, y=paleta2_y)

pantalla.bind("w", mover_paleta1_arriba)
pantalla.bind("s", mover_paleta1_abajo)
pantalla.bind("<Up>", mover_paleta2_arriba)
pantalla.bind("<Down>", mover_paleta2_abajo)

def mover_bola():
    global px, py, ix, iy, ti

    px += ix
    py += iy

    # Rebotar en los bordes
    if py < 0 or py > 360:  # 400 altura - 40 tamaño bola
        iy = -iy
    if px < 0 or px > 680:  # 700 ancho - 20 ancho bola
        ix = -ix

    bola.place(x=px, y=py)
    pantalla.after(ti, mover_bola)

# Iniciar animación
mover_bola()
pantalla.mainloop()