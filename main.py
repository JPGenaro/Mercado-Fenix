#Importaciones
import sys

from PySide2.QtWidgets import QMainWindow, QApplication

# Ventanas y archivos
from ventanas.ui_Identificacion import Ui_Identificador
from ventanas.home_ui import Ui_home

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
        self.ui.B_inicio_sesion.clicked.connect(self.w_home)
        self.ui.B_registro.connect(self.w_home)


    #Ventana del home
    def w_home(self):
        self.ui = Ui_home()
        self.ui.setupUi(self)

        #Botones
        # self.ui.B_compras.clicked.connect()
        self.ui.B_salir.clicked.connect(self.w_sesion)
        # self.ui.B_tienda.clicked.connect()



    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()

    sys.exit(app.exec_())