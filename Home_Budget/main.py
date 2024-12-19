import sys
from PyQt5 import QtWidgets
from WinMain import WinMain

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = WinMain()
    main_window.show()
    sys.exit(app.exec())
