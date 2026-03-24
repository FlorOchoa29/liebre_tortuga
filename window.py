from PyQt6.QtWidgets import QWidget, QPushButton, QLabel
from PyQt6.QtGui import QPixmap
from sub_process import SubProceso

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Liebre vs Tortuga")
        self.setGeometry(100,100,800,400)

        #Liebre
        self.imgLiebre=QLabel(self)
        self.imgLiebre.setPixmap(QPixmap("./img/liebre.png"))
        self.imgLiebre.setScaledContents(True)
        self.imgLiebre.resize(100,100)
        self.imgLiebre.move(10,50)

        #Tortuga
        self.imgTortuga=QLabel(self)
        self.imgTortuga.setPixmap(QPixmap("./img/tortuga.png"))
        self.imgTortuga.setScaledContents(True)
        self.imgTortuga.resize(100,100)
        self.imgTortuga.move(10,150)

        #Meta
        self.imgMeta= QLabel(self)
        self.imgMeta.setPixmap(QPixmap("./img/meta.png"))
        self.imgMeta.setScaledContents(True)
        self.imgMeta.resize(100,100)
        self.imgMeta.move(10,300)


        #Botón iniciar
        self.btnIniciar = QPushButton("Iniciar", self)
        self.btnIniciar.move(350,300)
        self.btnIniciar.clicked.connect(self.iniciar)

        #Crear subprocesos
        self.pLiebre = SubProceso(self.imgLiebre,5,"liebre")
        self.pTortuga = SubProceso(self.imgTortuga,50,"tortuga")

        #Conectar señales
        self.pLiebre.actualizar.connect(self.moverLiebre)
        self.pTortuga.actualizar.connect(self.moverTortuga)

    def iniciar(self):
        if self.btnIniciar.text() == "Iniciar":
            self.btnIniciar.setStyleSheet("background-color: green")
            self.btnIniciar.setText("Detener")
            self.pLiebre.start()
            self.pTortuga.start()
        else:
            self.btnIniciar.setStyleSheet("background-color: red")
            self.btnIniciar.setText("Iniciar")
            self.pLiebre.stop()
            self.pTortuga.stop()

    def moverLiebre(self,x,y):
        self.imgLiebre.move(x,y)
    
    def moverTortuga(self,x,y):
        self.imgTortuga.move(x,y)