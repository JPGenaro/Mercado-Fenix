# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Identificacion.ui'
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
        Identificador.resize(800, 600)
        self.centralwidget = QWidget(Identificador)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(230, 150, 371, 92))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.txt_inicio_contra = QLineEdit(self.gridLayoutWidget)
        self.txt_inicio_contra.setObjectName(u"txt_inicio_contra")

        self.gridLayout.addWidget(self.txt_inicio_contra, 1, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.txt_inicio_usuario = QLineEdit(self.gridLayoutWidget)
        self.txt_inicio_usuario.setObjectName(u"txt_inicio_usuario")

        self.gridLayout.addWidget(self.txt_inicio_usuario, 0, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.B_inicio_sesion = QPushButton(self.gridLayoutWidget)
        self.B_inicio_sesion.setObjectName(u"B_inicio_sesion")

        self.gridLayout.addWidget(self.B_inicio_sesion, 2, 1, 1, 1)

        Identificador.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Identificador)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
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
        self.label.setText(QCoreApplication.translate("Identificador", u"Ingresar Usuario", None))
        self.B_inicio_sesion.setText(QCoreApplication.translate("Identificador", u"Iniciar Sesi\u00f3n", None))
    # retranslateUi

