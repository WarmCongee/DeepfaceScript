import sys

from until import *
from PyQt6 import QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QDialog, QApplication

import analyze_pic

class PicAnalyzeUI(QDialog, analyze_pic.Ui_Dialog):
    def __init__(self):
        super(PicAnalyzeUI, self).__init__()
        self.setupUi(self)
        self.reset()

    def reset(self):
        self.toolButton.clicked.connect(self.image_file)

    def image_file(self):
        directory = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", "./", "All Files (*);;Text Files (*.txt)")
        pixmap = QPixmap(directory[0])
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        result = Analyze.analyze_emotion(directory)
        JsonStringOperations.print_formatted_result(result)

def choose_pic():
    test_url = QPixmap("face-whiteman.png")
    dialog.label.setPixmap(test_url)
    dialog.label.setScaledContents(True)

def reset_ui(dialog):
    dialog.label.linkActivated.connect(choose_pic)


    dialog.label.setPixmap(test_url)
    dialog.label.setScaledContents(True)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_win = PicAnalyzeUI()
    # reset_ui(my_win)

    my_win.show()
    sys.exit(app.exec())
