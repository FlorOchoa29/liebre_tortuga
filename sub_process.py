import time
from PyQt6.QtCore import QThread, pyqtSignal

#Estaclase no sabe cual Label manipula, si la Liebre o la Tortuga,
#Solo sabe que tiene que mover un label de un punto a otro
#Y también recibe el tiempo que tarda en moverse (si es más rápido es la Liebre)

class SubProceso(QThread):
    actualizar = pyqtSignal(int,int)

    def __init__(self, label, tiempo):
        super().__init__()
        self.label = label
        self.tiempo = tiempo

    def run(self):
        while True:
            x = self.label.x()
            y = self.label.y()
            #programar la lógica de la carrera aquí
            print(f"X: {x} Y:{y}")

            if x < 550:
                x += 10
            elif x > 550 and y < 250:
                y+=10

            elif x>10:
                x-=10

            self.actualizar.emit(x,y)
            time.sleep(self.tiempo / 1000.0)