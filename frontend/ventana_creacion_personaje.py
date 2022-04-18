import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QMessageBox,
    QHBoxLayout, QCheckBox, QPushButton, QLabel, QButtonGroup
)
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtCore import pyqtSignal, Qt, QLine

path = os.path.join("frontend", "assets",  "ventana_creacion_personaje.ui")
window_name, base_class = uic.loadUiType(path)

class VentanaCreacionPersonaje(window_name, base_class):

        senal_anadir_personaje = pyqtSignal(str)
        senal_nuevo_personaje = pyqtSignal()
        senal_personaje = pyqtSignal(dict)
        
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.pushButton.clicked.connect(self.enviar_personaje)
            self.lineEdit_3.setPlaceholderText("Blank if N/A")

        def abrir_ventana(self):
            self.show()

        def enviar_personaje(self):
            personaje = {
                "nombre": self.lineEdit_1.text(),
                "class": self.lineEdit_2.text(),
                "subclass":self.lineEdit_3.text(),
                "level":self.lineEdit_4.text(),
                "hp":self.lineEdit_5.text(),
                "ac":self.lineEdit_6.text(),
                "speed":self.lineEdit_7.text(),
                "str":self.lineEdit_8.text(),
                "dex":self.lineEdit_9.text(),
                "con":self.lineEdit_10.text(),
                "int":self.lineEdit_11.text(),
                "wis":self.lineEdit_12.text(),
                "cha":self.lineEdit_13.text(),
            }
            self.senal_personaje.emit(personaje)

        def recibir_personaje(self, str):
            if str == "NAME FAIL":
                self.lineEdit_1.setText("")
                self.lineEdit_1.setPlaceholderText("Invalid Name")
            elif str == "CLASS FAIL":
                self.lineEdit_2.setText("")
                self.lineEdit_2.setPlaceholderText("Invalid Class")
            elif str == "SUBCLASS FAIL":
                self.lineEdit_3.setText("")
                self.lineEdit_3.setPlaceholderText("Invalid Subclass")
            elif str == "LEVEL FAIL 1" or str == "LEVEL FAIL 2":
                self.lineEdit_4.setText("")
                self.lineEdit_4.setPlaceholderText("Invalid LEVEL")
            elif str == "HP FAIL":
                self.lineEdit_5.setText("")
                self.lineEdit_5.setPlaceholderText("Invalid HP")
            elif str == "AC FAIL 1" or str == "AC FAIL 2":
                self.lineEdit_6.setText("")
                self.lineEdit_6.setPlaceholderText("Invalid AC")
            elif str == "SPEED FAIL 1" or str == "SPEED FAIL 2":
                self.lineEdit_7.setText("")
                self.lineEdit_7.setPlaceholderText("Invalid SPEED")
            elif str == "STR FAIL":
                self.lineEdit_8.setText("")
                self.lineEdit_8.setPlaceholderText("1 - 20")
            elif str == "DEX FAIL":
                self.lineEdit_9.setText("")
                self.lineEdit_9.setPlaceholderText("1 - 20")
            elif str == "CON FAIL":
                self.lineEdit_10.setText("")
                self.lineEdit_10.setPlaceholderText("1 - 20")
            elif str == "INT FAIL":
                self.lineEdit_11.setText("")
                self.lineEdit_11.setPlaceholderText("1 - 20")
            elif str == "WIS FAIL":
                self.lineEdit_12.setText("")
                self.lineEdit_12.setPlaceholderText("1 - 20")
            elif str == "CHA FAIL":
                self.lineEdit_13.setText("")
                self.lineEdit_13.setPlaceholderText("1 - 20")
            self.update()
