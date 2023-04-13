import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QDialog, QApplication

import analyze_pic

class PicAnalyzeUI(QDialog, analyze_pic.Ui_Dialog):
    def __init__(self):
        super(PicAnalyzeUI, self).__init__()
        self.setupUi(self)


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


    my_win.show()
    sys.exit(app.exec())
