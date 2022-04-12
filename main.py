import sys
import os
from PyQt5.QtWidgets import QApplication
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_creacion_party import VentanaCreacion
from backend.logica_ventanas import LogicaInicio, LogicaCreacion

def hook(type_error, traceback):
    print(type_error)
    print(traceback)

if __name__ == '__main__':
    # Inicialización de la aplicación
    sys.__excepthook__ = hook
    app = QApplication(sys.argv)

    ventana_inicio = VentanaInicio()
    logica_inicio = LogicaInicio()


    ventana_creacion = VentanaCreacion()
    logica_creacion = LogicaCreacion()

    
    ventana_inicio.abrir_ventana()

    ventana_inicio.senal_nombre_party.connect(logica_inicio.comprobar_nombre_nuevo)
    logica_inicio.senal_respuesta_validacion.connect(ventana_inicio.recibir_validacion)



    sys.exit(app.exec())