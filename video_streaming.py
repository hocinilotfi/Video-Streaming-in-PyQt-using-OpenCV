import sys
from UI_video_streaming import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)

        self.setupUi(self)
        self.init_properties()
        self.init_connections()


    def init_properties(self):
        self.stream_thread = Stream_thread()
        
    def init_connections(self):
        self.stream_thread.change_pixmap.connect(self.image_label.setPixmap)
        self.start_stop_btn.clicked.connect(self.run_stop_video_streaming)

    @QtCore.pyqtSlot(bool)
    def run_stop_video_streaming(self):
        
        if self.start_stop_btn.isChecked():
            self.stream_thread.start()
            self.update_button_style()
        else:
            self.stream_thread.stop()
            self.update_button_style()
    
    def update_button_style(self):
        if self.start_stop_btn.isChecked():
            icon_stop = QtGui.QIcon()
            icon_stop.addPixmap(QtGui.QPixmap(":/icons/icons/stop_video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.start_stop_btn.setIcon(icon_stop)
            self.start_stop_btn.setStyleSheet("border: 2px solid red; border-radius: 7px;")
        else:
            icon_run = QtGui.QIcon()
            icon_run.addPixmap(QtGui.QPixmap(":/icons/icons/run_video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.start_stop_btn.setIcon(icon_run)
            self.start_stop_btn.setStyleSheet("border: none solid blue; border-radius: 7px;")


class Stream_thread(QtCore.QThread):
    change_pixmap = QtCore.pyqtSignal(QtGui.QPixmap)
    
    def run(self):
        cap = cv2.VideoCapture(0)
        self.thread_is_active = True
        while self.thread_is_active:
            ret, frame = cap.read()
            if ret:
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                flipped_image = cv2.flip(image, 1)
                qt_image = QtGui.QImage(flipped_image.data, flipped_image.shape[1], flipped_image.shape[0], QtGui.QImage.Format_RGB888)
                pic = qt_image.scaled(640, 480, QtCore.Qt.KeepAspectRatio)
                pixmap = QtGui.QPixmap.fromImage(pic)
                self.change_pixmap.emit(pixmap)
                
    def stop(self):
        self.thread_is_active = False
        self.quit()
       
         

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())