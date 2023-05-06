import sys

from until import *
from PyQt6 import QtWidgets
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
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)

    def image_analyze(self):
        result = Analyze.analyze_emotion(self.image_path)
        main_emotion, emotions = JsonStringOperations.emotion_result_extractor(result)
        self.angryNumber.setDigitCount(4)
        self.angryNumber.display(emotions["angry"])

        self.disgustNumber.setDigitCount(4)
        self.disgustNumber.display(emotions["disgust"])

        self.fearNumber.setDigitCount(4)
        self.fearNumber.display(emotions["fear"])

        self.happyNumber.setDigitCount(4)
        self.happyNumber.display(emotions["happy"])

        self.neutralNumber.setDigitCount(4)
        self.neutralNumber.display(emotions["neutral"])

        self.sadNumber.setDigitCount(4)
        self.sadNumber.display(emotions["sad"])

        self.surpriseNumber.setDigitCount(4)
        self.surpriseNumber.display(emotions["surprise"])





if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_win = PicAnalyzeUI()
    # reset_ui(my_win)

    my_win.show()
    sys.exit(app.exec())
