# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_home(object):
    def setupUi(self, home):
        if not home.objectName():
            home.setObjectName(u"home")
        home.resize(800, 600)
        home.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(home)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 801, 111))
        self.label.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setMargin(0)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(120, 160, 571, 191))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.B_tienda = QPushButton(self.verticalLayoutWidget)
        self.B_tienda.setObjectName(u"B_tienda")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.B_tienda.setFont(font)

        self.verticalLayout.addWidget(self.B_tienda)

        self.B_compras = QPushButton(self.verticalLayoutWidget)
        self.B_compras.setObjectName(u"B_compras")
        self.B_compras.setFont(font)

        self.verticalLayout.addWidget(self.B_compras)

        self.B_salir = QPushButton(self.verticalLayoutWidget)
        self.B_salir.setObjectName(u"B_salir")
        font1 = QFont()
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setWeight(75)
        self.B_salir.setFont(font1)
        self.B_salir.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.B_salir)

        home.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(home)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        home.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(home)
        self.statusbar.setObjectName(u"statusbar")
        home.setStatusBar(self.statusbar)

        self.retranslateUi(home)

        QMetaObject.connectSlotsByName(home)
    # setupUi

    def retranslateUi(self, home):
        home.setWindowTitle(QCoreApplication.translate("home", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("home", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; text-decoration: underline; color:#e7ff0b;\">Mercado Fenix</span></p></body></html>", None))
        self.B_tienda.setText(QCoreApplication.translate("home", u"Entrar a la tienda", None))
        self.B_compras.setText(QCoreApplication.translate("home", u"Ver compras", None))
        self.B_salir.setText(QCoreApplication.translate("home", u"Salir", None))
    # retranslateUi

