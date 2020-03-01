from lista_palabras import *
from tkinter import *
import sqlite3

# ----------------------Por consola con lista de palabras en un diccionario python----------------------------

'''palabra = input("Escribe la palabra en quechua que buscas: ")

print(palabra.upper() + ". " + dicc_qu_esp[palabra.upper()])'''


def buscarPalabra():
    if varOption.get() == 1:
        try:
            palabraBuscada = (miBusqueda.get()).lower()
            palabra_y_definicion = palabraBuscada + ". " + dicc_esp_qu[palabraBuscada.lower()]
            resultado.delete(1.0, END)
            resultado.insert(1.0, palabra_y_definicion)
            # # En caso de que el resultado se muestre en un Entry() y no en un Text()
            # resultado.config(text=palabra_y_definicion)
        except KeyError:
            resultado.delete(1.0, END)
            resultado.insert(1.0, "No hay resultado para la palabra que buscas...")
    elif varOption.get() == 2:
        try:
            palabraBuscada = (miBusqueda.get()).lower()
            palabra_y_definicion = palabraBuscada + ". " + dicc_qu_esp[palabraBuscada.lower()]
            resultado.delete(1.0, END)
            resultado.insert(1.0, palabra_y_definicion)
            # # En caso de que el resultado se muestre en un Entry() y no en un Text()
            # resultado.config(text=palabra_y_definicion)
        except KeyError:
            resultado.delete(1.0, END)
            resultado.insert(1.0, "No hay resultado para la palabra que buscas...")
    else:
        resultado.delete(1.0, END)
        resultado.insert(1.0, "Por favor, elige un diccionario.")


# ----------------------------------- Interfaz ----------------------------------------------

raiz = Tk()
raiz.title("Programa para la reunion en quechua")
raiz.iconbitmap("llama.ico")
raiz.config(bg="grey")

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
frameTitulo.config(bg="grey", width="850", height="350", bd=35)

titulo = Label(frameTitulo, text="Diccionario Quechua - Español")
titulo.grid(row=0, column=0, columnspan=2, padx=5, pady=10)
titulo.config(font=('bold', 20))

varOption = IntVar()
opcion_esp_qu = Radiobutton(frameTitulo, text ="Español - Quechua", variable=varOption, value=1)
opcion_esp_qu.grid(row=1, column=0)
opcion_qu_esp = Radiobutton(frameTitulo, text ="Quechua - Español", variable=varOption, value=2)
opcion_qu_esp.grid(row=1, column=1)

# ------------------------------Frame para el contenido-----------------------------------------

frameContenido = Frame()
frameContenido.pack()
frameContenido.config(bg="grey", width="850", height="350", bd=20)

miBusqueda = StringVar()
busquedaLabel = Label(frameContenido, text="Busqueda: ")
busquedaLabel.grid(row=0, column=0, sticky="e", padx=1)
cuadroTexto1 = Entry(frameContenido, textvariable=miBusqueda)
cuadroTexto1.grid(row=0, column=1)
cuadroTexto1.config(fg="red", justify="center")

#--------------------------------------Botón----------------------------------------------
calcularBoton = Button(frameContenido, text="Buscar", command=buscarPalabra)
calcularBoton.grid(row=1, column=0, padx=5, pady=10, columnspan=2)

# resultado = Label(frameContenido)
# resultado. grid(row=7, column=0, padx=5, pady=10, columnspan=4)
# resultado.config(width="50", height="5")

resultado = Text(frameContenido, width=40, height=12)
resultado.grid(row=3, column=0, sticky="e", padx=10, pady=10, columnspan=2)


raiz.mainloop()

