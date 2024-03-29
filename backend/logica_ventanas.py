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
    senal_lista_personajes = pyqtSignal(list)

    def comprobar_nombre_nuevo(self, nombre):
        if nombre.isalnum():
            self.senal_respuesta_validacion.emit(True)
        else:
            self.senal_respuesta_validacion.emit(False)

    def personajes_combo(self):
        lista_combo = []
        with open('backend\personajes.txt', 'r') as p:
            a = p.readlines()
        for personaje in a:
            if personaje:
                personaje = personaje.strip('\n')
                personaje_lista = personaje.split(',')
                nombre = personaje_lista[0]
                clase = personaje_lista[1]
                nivel = personaje_lista[3]
                texto_personaje = nombre[0].upper()+nombre[1:]+' '+clase[0].upper()+clase[1:]
                if personaje_lista[2]:
                    subclase = personaje_lista[2]
                    texto_personaje += f"\\{subclase[0].upper()}{subclase[1:]}"
                texto_personaje += nivel
                lista_combo.append(texto_personaje)
        self.senal_lista_personajes.emit(lista_combo)
    
    def crear_party(self):
        pass

class LogicaCreacionPersonaje(QObject):

    def __init__(self) -> None:
        super().__init__()
        self.error = False

    senal_respuesta_personaje = pyqtSignal(str)

    def comprobar_personaje(self, personaje):
        
        self.error = False
        #NAME CHECK
        if personaje["nombre"].isalnum():
            pass
        else:
            self.senal_respuesta_personaje.emit("NAME FAIL")
            self.error = True

        #CLASS CHECK
        if personaje["class"].lower() in parametros["CLASSES"]:
            pass
        else:
            self.senal_respuesta_personaje.emit("CLASS FAIL")
            self.error = True
            

        #SUBCLASS CHECK
        if personaje["subclass"].lower() in parametros["SUBCLASSES"] or personaje["subclass"] == "":
            pass
        else:
            self.senal_respuesta_personaje.emit("SUBCLASS FAIL")
            self.error = True

        #LEVEL CHECK
        if personaje["level"].isnumeric():
            if int(personaje["level"]) in range(1, 21):
                pass
            else:
                self.senal_respuesta_personaje.emit("LEVEL FAIL 1")
                self.error = True
        else:
            self.senal_respuesta_personaje.emit("LEVEL FAIL 2")
            self.error = True

        #HP CHECK
        if personaje["hp"].isnumeric():
            if int(personaje["hp"]) in range(0, 300):
                pass
        else:
            self.senal_respuesta_personaje.emit("HP FAIL")
            self.error = True

        #AC CHECK
        if personaje["ac"].isnumeric():
            if int(personaje["ac"]) in range(10, 45):
                pass
            else:
                self.senal_respuesta_personaje.emit("AC FAIL 1")
                self.error = True
        else:
            self.senal_respuesta_personaje.emit("AC FAIL 2")
            self.error = True

        #SPEED CHECK
        if personaje["speed"].isnumeric():
            if int(personaje["speed"]) in range(20, 100):
                pass
            else:
                self.senal_respuesta_personaje.emit("SPEED FAIL 1")
                self.error = True
        else:
            self.senal_respuesta_personaje.emit("SPEED FAIL 2")
            self.error = True

        #STR CHECK
        if personaje["str"].isnumeric():
            if int(personaje["str"]) in range(1, 21):
                pass
            else:
                self.senal_respuesta_personaje.emit("STR FAIL")
                self.error = True
        else:
            self.senal_respuesta_personaje.emit("STR FAIL")
            self.error = True

        #DEX CHECK
        if personaje["dex"].isnumeric():
            if int(personaje["dex"]) in range(1, 21):
                pass
            else:
                self.senal_respuesta_personaje.emit("DEX FAIL")
                self.error = True
        else:
            self.senal_respuesta_personaje.emit("DEX FAIL")
            self.error = True

        #CON CHECK
        if personaje["con"].isnumeric():
            if int(personaje["con"]) in range(1, 21):
                pass
            else:
                self.senal_respuesta_personaje.emit("CON FAIL")
                self.error = True
        else:
            self.senal_respuesta_personaje.emit("CON FAIL")
            self.error = True

        #INT CHECK
        if personaje["int"].isnumeric():
            if int(personaje["int"]) in range(1, 21):
                pass
            else:
                self.senal_respuesta_personaje.emit("INT FAIL")
                self.error = True
        else:
            self.senal_respuesta_personaje.emit("INT FAIL")
            self.error = True

        #WIS CHECK
        if personaje["wis"].isnumeric():
            if int(personaje["wis"]) in range(1, 21):
                pass
            else:
                self.senal_respuesta_personaje.emit("WIS FAIL")
                self.error = True
        else:
            self.senal_respuesta_personaje.emit("WIS FAIL")
            self.error = True

        #CHA CHECK
        if personaje["cha"].isnumeric():
            if int(personaje["cha"]) in range(1, 21):
                pass
            else:
                self.senal_respuesta_personaje.emit("CHA FAIL")
                self.error = True
        else:
            self.senal_respuesta_personaje.emit("CHA FAIL")
            self.error = True

        if self.error == False:
            nombre = personaje["nombre"]
            clase = personaje["class"]
            subclass = personaje["subclass"]
            level = personaje["level"]
            hp = personaje["hp"]
            ac = personaje["ac"]
            speed = personaje["speed"]
            str = personaje["str"]
            dex = personaje["dex"]
            con = personaje["con"]
            inte = personaje["int"]
            wis = personaje["wis"]
            cha = personaje["cha"]
            personaje = f"{nombre},{clase},{subclass},{level},{hp},{ac},{speed},{str},{dex},"
            personaje += f"{con},{inte},{wis},{cha}"
            with open("backend\personajes.txt", 'r') as p:
                lista_p = p.readlines()
            with open("backend\personajes.txt", 'a+') as p:
                if personaje+"\n" not in lista_p:
                    p.write(personaje)
                    p.write("\n")
            
    def crear_party(self):
        pass
