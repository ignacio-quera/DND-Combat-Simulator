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

        def anadir_personaje(self):
            pass
