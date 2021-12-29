import sys
from UI_video_streaming import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)

        self.setupUi(self)
        #self.init_properties()
        #self.init_connections()


    #def init_properties(self):
        #self.side_menu.setMaximumWidth(0)


    #def init_connections(self):
        #self.button_1.clicked.connect(self.function_1)


    #@QtCore.pyqtSlot(bool)
    #def function_1(self):
    #    self.label_1.setText("Item 1 is clicked")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())