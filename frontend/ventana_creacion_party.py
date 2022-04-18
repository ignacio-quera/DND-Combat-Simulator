import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QMessageBox,
    QHBoxLayout, QCheckBox, QPushButton, QLabel, QButtonGroup
)
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtCore import pyqtSignal, Qt, QLine

path = os.path.join("frontend", "assets",  "ventana_creacion_party.ui")
window_name, base_class = uic.loadUiType(path)

class VentanaCreacionParty(window_name, base_class):

        senal_anadir_personaje = pyqtSignal(str)
        senal_nuevo_personaje = pyqtSignal()
        
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.nueva_columna = False
            self.n_personaje = 1
            self.pushButton1.clicked.connect(self.anadir_personaje)

        def abrir_ventana(self, nombre):
            self.label_nombre.setText(nombre)
            self.show()

        def anadir_personaje(self):
            if self.comboBoxP.currentText() == "Create character":
                self.senal_nuevo_personaje.emit()
            else:
                label_personaje = QLabel()
                pass

        def actualizar(self, listacombo):
            for personaje in listacombo:
                self.comboBoxP.addItem(personaje)

        def listar_nuevo_personaje(self, personaje):
            pass


    