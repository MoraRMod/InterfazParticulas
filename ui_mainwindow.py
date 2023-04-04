# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(791, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 791, 561))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Grafica_GraphicsView = QGraphicsView(self.layoutWidget)
        self.Grafica_GraphicsView.setObjectName(u"Grafica_GraphicsView")

        self.gridLayout.addWidget(self.Grafica_GraphicsView, 0, 0, 1, 2)

        self.Dibujar_PushButton = QPushButton(self.layoutWidget)
        self.Dibujar_PushButton.setObjectName(u"Dibujar_PushButton")

        self.gridLayout.addWidget(self.Dibujar_PushButton, 1, 0, 1, 1)

        self.Limpiar_PushButton = QPushButton(self.layoutWidget)
        self.Limpiar_PushButton.setObjectName(u"Limpiar_PushButton")

        self.gridLayout.addWidget(self.Limpiar_PushButton, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 791, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Dibujar_PushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.Limpiar_PushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
    # retranslateUi

