import sys
from PyQt6.QtWidgets import QApplication
from window import Window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Window()  
    ventana.show()
    sys.exit(app.exec())

