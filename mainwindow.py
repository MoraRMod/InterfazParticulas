from PySide2.QtWidgets import *
from ui_mainwindow import Ui_MainWindow
from PySide2.QtGui import *
from PySide2.QtCore import Slot
from random import randint

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.scene = QGraphicsScene()
        self.ui.Grafica_GraphicsView.setScene(self.scene)

        self.ui.Dibujar_PushButton.clicked.connect(self.dibujar)
        self.ui.Limpiar_PushButton.clicked.connect(self.limpiar)

    @Slot()
    def dibujar(self):
        print("dibujar")
    
    @Slot()
    def limpiar(self):
        print("limpiar")

        self.scene.clear()

    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)

        for i in range(0, 1000):
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)

            color = QColor(r, g, b)
            pen.setColor(color)

            x_origin = randint(0, 500)
            y_origin = randint(0, 500)
            x_destin = randint(0, 500)
            y_destin = randint(0, 500)

            self.scene.addEllipse(x_origin, y_origin, 6, 6, pen)
            self.scene.addEllipse(x_destin, y_destin, 6, 6, pen)
            self.scene.addLine(x_origin, y_origin, x_destin, y_destin, pen)

    def wheelEvent(self, event):
        print(event.delta())

        if event.delta() > 0:
            self.ui.Grafica_GraphicsView.scale(1.2, 1.2)
        else:
            self.ui.Grafica_GraphicsView.scale(0.8, 0.8)