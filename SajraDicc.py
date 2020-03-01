from lista_palabras import *
from tkinter import *
import sqlite3


# ----------------------------------------Funciones--------------------------------------------

def buscarPalabra(event):
    """
    :param event: el parametro no tiene ninguna aplicación mas que permitir que al presionar 'enter' se ejecute
    la funcion. Por eso en el bind del entry, el parametro event tiene solo un string de relleno.
    :return: La funcion no devuelve ningun valor, sino mas bien, rellena el widge Text() con la definicion y traducción
    de la palabra buscada.
    """
    if varOption.get() == 1:
        try:
            palabraBuscada = (miBusqueda.get()).lower()
            if palabraBuscada != "":
                palabra_y_definicion = palabraBuscada + ". " + dicc_esp_qu[palabraBuscada.lower()]
                resultado.delete(1.0, END)
                resultado.insert(1.0, palabra_y_definicion)
            else:
                resultado.delete(1.0, END)
                resultado.insert(1.0, "Por favor, escribe una palabra...")
        except KeyError:
            resultado.delete(1.0, END)
            resultado.insert(1.0, "No hay resultado para la palabra que buscas...")
    elif varOption.get() == 2:
        try:
            palabraBuscada = (miBusqueda.get()).lower()
            if palabraBuscada != "":
                palabra_y_definicion = palabraBuscada + ". " + dicc_qu_esp[palabraBuscada.lower()]
                resultado.delete(1.0, END)
                resultado.insert(1.0, palabra_y_definicion)
            else:
                resultado.delete(1.0, END)
                resultado.insert(1.0, "Por favor, escribe una palabra...")
        except KeyError:
            resultado.delete(1.0, END)
            resultado.insert(1.0, "No hay resultado para la palabra que buscas...")
    else:
        resultado.delete(1.0, END)
        resultado.insert(1.0, "Por favor, elige un diccionario.")


# -----------------------------------Variables-----------------------------------------------

color_fondo = "#FFF6C7"
color_cuadro_texto = "#D9C8A9"

# ----------------------------------- Interfaz ----------------------------------------------

raiz = Tk()
raiz.title("Diccionario Quechua-Español")
raiz.iconbitmap("llama2.ico")
raiz.config(bg=color_fondo)

# ----------------------------------Barra de Menú-----------------------------------------

barraMenu = Menu(raiz)
raiz.config(menu=barraMenu)

archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Imprimir")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Salir")
ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Ayuda de Diccionario Quechua-Español")
ayudaMenu.add_command(label="Licencia")

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

# ------------------------------Frame para el titulo-----------------------------------------

frameTitulo = Frame()
frameTitulo.pack()
frameTitulo.config(bg=color_fondo, width="850", height="350", bd=35)

titulo = Label(frameTitulo, text="Diccionario Quechua - Español")
titulo.grid(row=0, column=0, columnspan=2, padx=5, pady=10)
titulo.config(font=('bold', 20), bg=color_fondo)

# ---------------------------Botones para cambiar de diccionario-----------------------------

varOption = IntVar()
opcion_esp_qu = Radiobutton(frameTitulo, text="Español - Quechua", variable=varOption, value=1)
opcion_esp_qu.grid(row=1, column=0)
opcion_esp_qu.config(bg=color_fondo)
opcion_qu_esp = Radiobutton(frameTitulo, text="Quechua - Español", variable=varOption, value=2)
opcion_qu_esp.grid(row=1, column=1)
opcion_qu_esp.config(bg=color_fondo)

# ------------------------------Frame para el contenido-----------------------------------------

frameContenido = Frame()
frameContenido.pack()
frameContenido.config(bg=color_fondo, width="850", height="350", bd=20)

# -----------------Sección donde se coloca la palabra que se quiere buscar-------------------

miBusqueda = StringVar()
busquedaLabel = Label(frameContenido, text="Busqueda: ")
busquedaLabel.grid(row=0, column=0, sticky="e", padx=1)
busquedaLabel.config(bg=color_fondo)

cuadroTexto1 = Entry(frameContenido, textvariable=miBusqueda)
cuadroTexto1.grid(row=0, column=1, columnspan=2)
cuadroTexto1.config(fg="#261201", justify="center", bg=color_cuadro_texto)
#  Esto es para que cuando se apreta 'enter', se ejecute la misma función que con el botón 'buscar'
cuadroTexto1.bind('<Return>', buscarPalabra)

# --------------------------------------Botón----------------------------------------------
# El parámetro de relleno de la siguiente línea es explicado en la documentacion de la función buscarPalabra()
calcularBoton = Button(frameContenido, text="Buscar", command=lambda: buscarPalabra("parametro_de_relleno"))
calcularBoton.grid(row=1, column=0, padx=5, pady=10, columnspan=3)

# -----------------Cuadro donde se muestra el resultado de la búsqueda---------------------
resultado = Text(frameContenido, width=40, height=12)
resultado.grid(row=3, column=0, sticky="e", padx=10, pady=10, columnspan=3)
resultado.config(bg=color_cuadro_texto)

raiz.mainloop()
