import sys
import os
from ui_interface import *
from Custom_Widgets.Widgets import *
from maps import MapCreator
import ctypes
from PySide2 import QtGui

myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        loadJsonStyle(self, self.ui)

        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "output.html"))
        local_url = QUrl.fromLocalFile(file_path)

        self.ui.webEngineView.load(QUrl(local_url))
        self.showMaximized()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.setWindowIcon(QtGui.QIcon("icons/icon.jpg"))
    window.setWindowTitle("PrepQ - Préparations de quart")
    sys.exit(app.exec_())
