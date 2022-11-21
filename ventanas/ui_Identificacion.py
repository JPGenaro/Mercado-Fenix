# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'IdentificaciontVVtSA.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Identificador(object):
    def setupUi(self, Identificador):
        if not Identificador.objectName():
            Identificador.setObjectName(u"Identificador")
        Identificador.resize(679, 518)
        Identificador.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(Identificador)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(50, 80, 581, 131))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.txt_inicio_contra = QLineEdit(self.gridLayoutWidget)
        self.txt_inicio_contra.setObjectName(u"txt_inicio_contra")

        self.gridLayout.addWidget(self.txt_inicio_contra, 1, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.txt_inicio_usuario = QLineEdit(self.gridLayoutWidget)
        self.txt_inicio_usuario.setObjectName(u"txt_inicio_usuario")
        self.txt_inicio_usuario.setStyleSheet(u"")

        self.gridLayout.addWidget(self.txt_inicio_usuario, 0, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.B_inicio_sesion = QPushButton(self.gridLayoutWidget)
        self.B_inicio_sesion.setObjectName(u"B_inicio_sesion")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.B_inicio_sesion.setFont(font1)
        self.B_inicio_sesion.setStyleSheet(u"background-color: rgb(69, 150, 255);")

        self.gridLayout.addWidget(self.B_inicio_sesion, 2, 1, 1, 1)

        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(50, 280, 581, 131))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)

        self.txt_registro_usuario = QLineEdit(self.gridLayoutWidget_2)
        self.txt_registro_usuario.setObjectName(u"txt_registro_usuario")

        self.gridLayout_2.addWidget(self.txt_registro_usuario, 1, 1, 1, 1)

        self.txt_registro_contra = QLineEdit(self.gridLayoutWidget_2)
        self.txt_registro_contra.setObjectName(u"txt_registro_contra")

        self.gridLayout_2.addWidget(self.txt_registro_contra, 4, 1, 1, 1)

        self.B_registro = QPushButton(self.gridLayoutWidget_2)
        self.B_registro.setObjectName(u"B_registro")
        self.B_registro.setFont(font1)
        self.B_registro.setStyleSheet(u"background-color: rgb(69, 150, 255);")

        self.gridLayout_2.addWidget(self.B_registro, 5, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 10, 581, 51))
        self.label_5.setStyleSheet(u"")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 230, 581, 31))
        Identificador.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Identificador)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 679, 26))
        Identificador.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Identificador)
        self.statusbar.setObjectName(u"statusbar")
        Identificador.setStatusBar(self.statusbar)

        self.retranslateUi(Identificador)

        QMetaObject.connectSlotsByName(Identificador)
    # setupUi

    def retranslateUi(self, Identificador):
        Identificador.setWindowTitle(QCoreApplication.translate("Identificador", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("Identificador", u"Contrase\u00f1a", None))
        self.label.setText(QCoreApplication.translate("Identificador", u"Usuario:", None))
        self.B_inicio_sesion.setText(QCoreApplication.translate("Identificador", u"Iniciar Sesi\u00f3n", None))
#if QT_CONFIG(tooltip)
        self.gridLayoutWidget_2.setToolTip(QCoreApplication.translate("Identificador", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Registrarse</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.gridLayoutWidget_2.setWhatsThis(QCoreApplication.translate("Identificador", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Registrarse</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_3.setText(QCoreApplication.translate("Identificador", u"Usuario:", None))
        self.label_4.setText(QCoreApplication.translate("Identificador", u"Contrase\u00f1a", None))
        self.B_registro.setText(QCoreApplication.translate("Identificador", u"Registrarse", None))
        self.label_5.setText(QCoreApplication.translate("Identificador", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">Inicio de sesion</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Identificador", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Registrarse</span></p></body></html>", None))
    # retranslateUi

