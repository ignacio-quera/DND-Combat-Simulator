from PyQt5.QtCore import QObject, pyqtSignal

class LogicaInicio(QObject):

    def __init__(self) -> None:
        super().__init__()

    senal_respuesta_validacion = pyqtSignal(bool)

    def comprobar_nombre_nuevo(self, nombre):
        if nombre.isalnum():
            self.senal_respuesta_validacion.emit(True)
        else:
            self.senal_respuesta_validacion.emit(False)

    def crear_party(self):
        pass

class LogicaCreacion(QObject):

    def __init__(self) -> None:
        super().__init__()

    senal_respuesta_validacion = pyqtSignal(bool)

    def comprobar_nombre_nuevo(self, nombre):
        if nombre.isalnum():
            self.senal_respuesta_validacion.emit(True)
        else:
            self.senal_respuesta_validacion.emit(False)

    def crear_party(self):
        pass

