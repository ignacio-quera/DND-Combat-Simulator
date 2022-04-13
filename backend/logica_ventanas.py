from PyQt5.QtCore import QObject, pyqtSignal
import json

with open("parametros.json") as j:
    parametros = json.load(j)

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

class LogicaCreacionParty(QObject):

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

class LogicaCreacionPersonaje(QObject):

    def __init__(self) -> None:
        super().__init__()

    senal_respuesta_validacion = pyqtSignal(bool)

    def comprobar_personaje(self, personaje):
        print(personaje)
        if personaje["nombre"].isalnum():
            print("GOOD NAME")
        else:
            print("NAME FAIL")

        if personaje["class"].lower() in parametros["CLASSES"]:
            print("GOOD CLASS")
        else:
            print("CLASS FAIL")

        if personaje["subclass"] in parametros["SUBCLASSES"] or personaje["subclass"] == "NOSUB":
            print("GOOD SUBCLASS")
        else:
            print("SUBCLASS FAIL")

        if personaje["level"].isnumeric():
            if int(personaje["level"]) in range(1, 21):
                print("GOOD LEVEL")
            else:
                print("LEVEL FAIL 1")
        else:
            print("LEVEL FAIL 2")

        if personaje["hp"].isnumeric():
            if int(personaje["hp"]) in range(0, 300):
                print("GOOD HP")
        else:
            print("HP FAIL")

        if personaje["ac"].isnumeric():
            if int(personaje["ac"]) in range(10, 45):
                print("GOOD LEVEL")
            else:
                print("AC FAIL 1")
        else:
            print("AC FAIL 2")

        if personaje["speed"].isnumeric():
            if int(personaje["speed"]) in range(20, 100):
                print("GOD SPEED")
            else:
                print("SPEED FAIL 1")
        else:
            print("SPEED FAIL 2")

        if personaje["str"].isnumeric():
            if int(personaje[""]) in range(1, 21):
                print("GOOD STR")
        else:
            print("STR FAIL")

        if personaje["dex"].isnumeric():
            if int(personaje["dex"]) in range(1, 21):
                print("GOOD DEX")
        else:
            print("DEX FAIL")

        if personaje["con"].isnumeric():
            if int(personaje["con"]) in range(1, 21):
                print("GOOD CON")
        else:
            print("CON FAIL")
        if personaje["int"].isnumeric():
            if int(personaje["int"]) in range(1, 21):
                print("GOOD INT")
        else:
            print("INT FAIL")
        if personaje["wis"].isnumeric():
            if int(personaje["wis"]) in range(1, 21):
                print("GOOD WIS")
        else:
            print("WIS FAIL")
        if personaje["cha"].isnumeric():
            if int(personaje["cha"]) in range(1, 21):
                print("GOOD CHA")
        else:
            print("CHA FAIL")


    def crear_party(self):
        pass
