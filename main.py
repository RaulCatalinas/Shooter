# Librerias a usar
import sys
import tkinter as tk
from tkinter import Tk
from tkinter import messagebox

import pygame as pyg
from pygame import QUIT

# Colores en hexadecimal
negro = "#000000"
azulEtiquetas = "#33FFFF"
verdeEtiquetas = "#00CC66"
amarillo = "#FFFF00"
amarilloOscuro = "#333300"
verdeOscuro = "#003300"
verde = "#00FF00"
azul = "#00FFFF"
azulOscuro = "#000033"
rojoOscuro = "#330000"
rojo = "#FF0000"

# Variables para la ventana de pygma
jugar = True


class CambiarColor:
    def FuncionCambiarColor(self, button, colorRatonDentro, colorRatonFuera):
        """
        Toma un botón y dos colores, y vincula el botón para cambiar de color cuando el mouse ingresa y deja el botón

        :param button: El botón al que desea cambiar el color
        :param colorRatonDentro: El color del botón cuando el mouse está sobre él
        :param colorRatonFuera: El color del botón cuando el mouse no está sobre él
        """
        button.bind(
            "<Enter>", func=lambda e: button.config(background=colorRatonDentro, cursor="hand2")
        )

        button.bind("<Leave>", func=lambda e: button.config(background=colorRatonFuera))


class Salir:
    def FuncionSalir(self, ventanaACerrar):
        """
        Le pregunta al usuario si quiere salir del juego, y si dice que sí, cierra la ventana

        :param ventanaACerrar: La ventana para cerrar
        """
        self.Tk = ventanaACerrar

        self.cerrar = messagebox.askquestion(
            "Salir del juego", "¿Seguro que quieres salir del juego?"
        )

        if self.cerrar == "yes":
            self.Tk.destroy()

    def FuncionSalirPygame(self, ventanaACerrar):
        self.Tk = ventanaACerrar

        self.cerrar = messagebox.askquestion(
            "Salir del juego", "¿Seguro que quieres salir del juego?"
        )

        if self.cerrar == "yes":
            jugando = False
            pyg.quit()
            sys.exit()


class Main:
    def FuncionMain(self):
        """
        Crea una ventana y luego crea una etiqueta, tres botones y un color de fondo.
        """
        # Crear instancias de las clases necesarias para que el programa funcione
        self.cambiarColor = CambiarColor()
        self.salir = Salir()
        self.jugar = Jugar()
        self.creditos = Creditos()

        # Crear la ventana + configuararla + Fijar tamaño + Cambiar el icono
        self.ventana = Tk()
        self.ventana.title("Shooter")
        self.ventana.resizable(False, False)
        self.ventana.config(bg=negro)

        # Centrar ventana
        self.ancho_ventana = 1280
        self.alto_ventana = 720
        self.x_ventana = self.ventana.winfo_screenwidth() // 2 - self.ancho_ventana // 2
        self.y_ventana = self.ventana.winfo_screenheight() // 2 - self.alto_ventana // 2
        self.posicion = (
                str(self.ancho_ventana)
                + "x"
                + str(self.alto_ventana)
                + "+"
                + str(self.x_ventana)
                + "+"
                + str(self.y_ventana)
        )
        self.ventana.geometry(self.posicion)

        # Crear los elementos de la interfaz
        self.tituloDelJuego = tk.Label(
            text="Shooter",
            font="Helvetica 65",
            bg=azulEtiquetas,
            width=46
        )
        self.tituloDelJuego.pack(pady=20)

        self.botonJugar = tk.Button(
            text="Jugar",
            bg=verdeOscuro,
            font="Helvetica 40",
            command=lambda: [
                self.ventana.destroy(),
                self.jugar.FuncionJugar()
            ],
            width=30
        )
        self.botonJugar.pack(pady=25)

        self.cambiarColor.FuncionCambiarColor(self.botonJugar, verde, verdeOscuro)

        self.botonCreditos = tk.Button(
            text="Creditos",
            bg=azulOscuro,
            font="Helvetica 40",
            command=lambda: [
                self.ventana.destroy(),
                self.creditos.FuncionCreditos()
            ],
            width=30
        )
        self.botonCreditos.pack(pady=30)

        self.cambiarColor.FuncionCambiarColor(self.botonCreditos, azul, azulOscuro)

        self.botonSalir = tk.Button(
            text="Salir",
            bg=rojoOscuro,
            font="Helvetica 40",
            command=lambda: [self.salir.FuncionSalir(self.ventana)],
            width=30
        )
        self.botonSalir.pack(pady=35)

        self.cambiarColor.FuncionCambiarColor(self.botonSalir, rojo, rojoOscuro)

        # Actualizar ventana
        self.ventana.mainloop()


class Jugar:
    def __init__(self):
        """
        La función inicializa el módulo pygame.
        """
        pyg.init()

    def FuncionJugar(self):
        """
        "Cree una instancia de las clases que no requieren que se inicialice la pantalla: Principal, Cambiar color, Salir.
        Cree la ventana + configúrela + Corrija el tamaño + Cambie el icono".
        </código>
        """
        # Crear instancia de las clases que no requieren que se inicie el display: Main, CambiarColor, Salir
        self.volverAlMenu = Main()
        self.cambiarColor = CambiarColor()
        self.salir = Salir()

        # Crear la ventana + configuararla + Fijar tamaño + Cambiar el icono
        self.ancho = 1280
        self.alto = 720

        self.ventanaJugar = pyg.display.set_mode((self.ancho, self.alto))
        pyg.display.set_caption("Shooter")

        while jugar:
            for event in pyg.event.get():
                if event.type == QUIT:
                    # Finalizar bucle + finalizar pygame + cerrar la ventana
                    self.salir.FuncionSalirPygame(self.ventanaJugar)

            # Limitar FPS
            pyg.time.Clock().tick(60)

            pyg.display.update()


class Creditos:
    def FuncionCreditos(self):
        """
        Crea una ventana, le pone una etiqueta y dos botones, y luego ejecuta la ventana
        """
        # Crear instancia de la clase Main para poder volver al menu y Salir
        self.volverAlMenu = Main()
        self.salir = Salir()
        self.cambiarColor = CambiarColor()

        # Crear la ventana + configuararla + Fijar tamaño + Cambiar el icono
        self.ventanaCreditos = Tk()
        self.ventanaCreditos.title("Shooter")
        self.ventanaCreditos.resizable(False, False)
        self.ventanaCreditos.config(bg=negro)

        # Centrar ventana
        self.ancho_ventana = 1280
        self.alto_ventana = 720
        self.x_ventana = self.ventanaCreditos.winfo_screenwidth() // 2 - self.ancho_ventana // 2
        self.y_ventana = self.ventanaCreditos.winfo_screenheight() // 2 - self.alto_ventana // 2
        self.posicion = (
                str(self.ancho_ventana)
                + "x"
                + str(self.alto_ventana)
                + "+"
                + str(self.x_ventana)
                + "+"
                + str(self.y_ventana)
        )
        self.ventanaCreditos.geometry(self.posicion)

        # Elementos de la interfaz
        self.etiquetaCreditos = tk.Label(
            text="Creditos",
            font="Helvetica 65",
            bg=azulEtiquetas,
            width=46
        )
        self.etiquetaCreditos.pack(pady=20)

        self.autor = tk.Label(
            text="Hecho por: Raul Catalinas Esteban",
            bg=verdeEtiquetas,
            font="Helvetica 40",
            width=30
        )
        self.autor.pack(pady=25)

        self.botonVolverAlMenu = tk.Button(
            text="Volver al menu",
            font="Helvetica 40",
            bg=amarilloOscuro,
            command=lambda: [
                self.ventanaCreditos.destroy(),
                self.volverAlMenu.FuncionMain()
            ],
            width=30
        )
        self.botonVolverAlMenu.pack(pady=20)

        self.cambiarColor.FuncionCambiarColor(self.botonVolverAlMenu, amarillo, amarilloOscuro)

        self.botonSalir = tk.Button(
            text="Salir",
            font="Helvetica 40",
            bg=rojoOscuro,
            command=lambda: [self.salir.FuncionSalir(self.ventanaCreditos)],
            width=30
        )
        self.botonSalir.pack(pady=20)

        self.cambiarColor.FuncionCambiarColor(self.botonSalir, rojo, rojoOscuro)

        self.ventanaCreditos.mainloop()


# Crear instancia de la clase principal
menu = Main()

# Ejecutar la funcion que inicia el juego
menu.FuncionMain()
