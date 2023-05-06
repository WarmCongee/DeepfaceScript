import sys

from until import *
from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QDialog, QApplication

import analyze_pic

class PicAnalyzeUI(QDialog, analyze_pic.Ui_Dialog):
    def __init__(self):
        super(PicAnalyzeUI, self).__init__()
        self.image_path = ''
        self.setupUi(self)
        self.reset()

    def reset(self):
        self.toolButton.clicked.connect(self.image_file)
        self.pushButton.clicked.connect(self.image_analyze)


    def image_file(self):
        directory = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", "/home", "All Files (*);;Text Files (*.txt)")
        self.image_path = directory[0]
        pixmap = QPixmap(directory[0])
        pixmap = pixmap.scaled(self.label.size(), QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)

    def image_analyze(self):
        result = Analyze.analyze_emotion(self.image_path)
        main_emotion, emotions = JsonStringOperations.emotion_result_extractor(result)
        self.progressBar.setValue(emotions["angry"])
        self.progressBar_2.setValue(emotions["disgust"])
        self.progressBar_3.setValue(emotions["fear"])
        self.progressBar_4.setValue(emotions["happy"])
        self.progressBar_5.setValue(emotions["neutral"])
        self.progressBar_6.setValue(emotions["sad"])
        self.progressBar_7.setValue(emotions["surprise"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_win = PicAnalyzeUI()

    my_win.show()
    sys.exit(app.exec())
