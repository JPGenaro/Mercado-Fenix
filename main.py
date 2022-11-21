#Importaciones
import sys

from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox

# Ventanas y archivos
from ventanas.ui_Identificacion import Ui_Identificador
from ventanas.home_ui import Ui_home
from clases import Usuario, Producto, productos

#Variables y listas
prueba = Usuario(
    "s",
    "s"
)
usuarios = [prueba]

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
        self.ui.B_registro.clicked.connect(self.registrar)

    def w_home(self):
        self.ui = Ui_home()
        self.ui.setupUi(self)

        #Botones
        #self.ui.B_compras.clicked.connect()
        #self.ui.B_tienda.clicked.connect()
        self.ui.B_salir.clicked.connect(self.w_sesion)


    #Registrar usuarios
    def registrar(self):
        mensaje = QMessageBox(self)
        mensaje.setWindowTitle('Mensaje')
        registro_nombre = self.ui.txt_registro_usuario.text().strip()
        registro_contra = self.ui.txt_registro_contra.text().strip()
        passed = False
        for i in range(len(usuarios)):
            if not usuarios[i].nombre == registro_nombre:
                passed = True
            else:
                passed = False
                mensaje.setIcon(QMessageBox.Warning)
                mensaje.setText('El nombre deseado ya ha sido elegido por otro usuario')
        if passed == True:
            molde = Usuario(
                registro_nombre,
                registro_contra
            )
            usuarios.append(molde)
            mensaje.setIcon(QMessageBox.Information)
            mensaje.setText('Usuario registrado correctamente')
        mensaje.exec_()

    #Iniciar usuarios
    def iniciar_sesion(self):
        pass



    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()

    sys.exit(app.exec_())