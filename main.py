import sys

from PySide2 import QtWidgets, QtGui
from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox

# Ventanas y archivos
from ventanas.ui_Identificacion import Ui_MainWindow

#Codigo
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

    #Ventana de inicio de sesion
    def w_sesion(self):
        pass

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()

    sys.exit(app.exec_())