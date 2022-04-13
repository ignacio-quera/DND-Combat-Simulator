import sys
import os
from PyQt5.QtWidgets import QApplication
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_creacion_party import VentanaCreacionParty
from frontend.ventana_creacion_personaje import VentanaCreacionPersonaje
from backend.logica_ventanas import LogicaInicio, LogicaCreacionParty, LogicaCreacionPersonaje

import json

def hook(type_error, traceback):
    print(type_error)
    print(traceback)

if __name__ == '__main__':

    with open("parametros.json") as j:
        parametros = json.load(j)
    # Inicialización de la aplicación
    sys.__excepthook__ = hook
    app = QApplication(sys.argv)

    ventana_inicio = VentanaInicio()
    logica_inicio = LogicaInicio()


    ventana_creacion_party = VentanaCreacionParty()
    logica_creacion_party = LogicaCreacionParty()

    ventana_creacion_personaje = VentanaCreacionPersonaje()
    logica_creacion_personaje = LogicaCreacionPersonaje()

    
    ventana_inicio.abrir_ventana()

    ventana_inicio.senal_nombre_party.connect(logica_inicio.comprobar_nombre_nuevo)
    logica_inicio.senal_respuesta_validacion.connect(ventana_inicio.recibir_validacion)

    ventana_inicio.senal_nueva_party.connect(ventana_creacion_party.abrir_ventana)

    ventana_creacion_party.senal_nuevo_personaje.connect(ventana_creacion_personaje.abrir_ventana)
    ventana_creacion_personaje.senal_personaje.connect(logica_creacion_personaje.comprobar_personaje)

    sys.exit(app.exec())