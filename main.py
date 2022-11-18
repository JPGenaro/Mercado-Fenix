#Importaciones
import sys

from PySide2.QtWidgets import QMainWindow, QApplication

# Ventanas y archivos
from ventanas.ui_Identificacion import Ui_Identificador

#Codigo
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.w_sesion()

    #Ventana de inicio de sesion
    def w_sesion(self):
        self.ui = Ui_Identificador()
        self.ui.setupUi(self)

        #Botones
        self.ui.B_inicio_sesion.clicked.connect()

    


    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()

    sys.exit(app.exec_())