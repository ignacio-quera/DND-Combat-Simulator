import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QMessageBox,
    QHBoxLayout, QCheckBox, QPushButton, QLabel, QButtonGroup
)
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtCore import pyqtSignal, Qt, QLine

path = os.path.join("frontend", "assets",  "ventana_inicio.ui")
window_name, base_class = uic.loadUiType(path)

class VentanaInicio(window_name, base_class):
      

      senal_nombre_party = pyqtSignal(str)
      senal_nueva_party = pyqtSignal(str)

      def __init__(self):
         super().__init__()
         self.setupUi(self)

         self.lineEdit.setPlaceholderText("Nombre Party")
         self.pushButton_2.clicked.connect(self.enviar_nombre_party)

      def enviar_nombre_party(self):
        self.senal_nombre_party.emit(self.lineEdit.text())

      def recibir_validacion(self, validado):
        """
        Este método recibe desde el back-end una señal que indica si el nombre enviado es
        valido o no. De ser valido, se sigue a la siguiente ventana. En el caso contrario, se borra
        el texto del QLine y se notifica que el nombre es invalido
        """
        if validado:
            self.hide()
            self.senal_nueva_party.emit(self.lineEdit.text())
        else:
            self.lineEdit.clear()
            self.lineEdit.setPlaceholderText("Nombre inválido")

      def abrir_ventana(self):
        self.show()
