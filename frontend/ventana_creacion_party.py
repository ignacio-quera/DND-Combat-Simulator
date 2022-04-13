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
            self.pushButton1.clicked.connect(self.anadir_personaje)

        def abrir_ventana(self, nombre):
            self.show()
            self.label_nombre.setText(nombre)

        def anadir_personaje(self):
            if self.comboBox.currentText() == "Create character":
                self.senal_nuevo_personaje.emit()
            else:
                pass

    