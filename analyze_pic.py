# Form implementation generated from reading ui file 'analyze_pic.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(957, 684)
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(340, 580, 241, 61))
        self.pushButton.setObjectName("pushButton")
        self.graphicsView = QtWidgets.QGraphicsView(parent=Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(520, 30, 351, 421))
        self.graphicsView.setObjectName("graphicsView")
        self.lcdNumber = QtWidgets.QLCDNumber(parent=Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(740, 100, 61, 23))
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Mode.Dec)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Filled)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(parent=Dialog)
        self.lcdNumber_2.setGeometry(QtCore.QRect(740, 152, 61, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(parent=Dialog)
        self.lcdNumber_3.setGeometry(QtCore.QRect(740, 204, 61, 23))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(parent=Dialog)
        self.lcdNumber_4.setGeometry(QtCore.QRect(740, 255, 61, 23))
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(660, 40, 71, 31))
        self.label_2.setTextFormat(QtCore.Qt.TextFormat.MarkdownText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lcdNumber_5 = QtWidgets.QLCDNumber(parent=Dialog)
        self.lcdNumber_5.setGeometry(QtCore.QRect(740, 307, 61, 23))
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.lcdNumber_6 = QtWidgets.QLCDNumber(parent=Dialog)
        self.lcdNumber_6.setGeometry(QtCore.QRect(740, 359, 61, 23))
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.lcdNumber_7 = QtWidgets.QLCDNumber(parent=Dialog)
        self.lcdNumber_7.setGeometry(QtCore.QRect(740, 410, 61, 23))
        self.lcdNumber_7.setObjectName("lcdNumber_7")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(580, 100, 57, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(580, 152, 57, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setGeometry(QtCore.QRect(580, 204, 57, 15))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=Dialog)
        self.label_6.setGeometry(QtCore.QRect(580, 255, 57, 15))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=Dialog)
        self.label_7.setGeometry(QtCore.QRect(580, 307, 57, 15))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=Dialog)
        self.label_8.setGeometry(QtCore.QRect(580, 359, 57, 15))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=Dialog)
        self.label_9.setGeometry(QtCore.QRect(580, 410, 57, 15))
        self.label_9.setObjectName("label_9")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(110, 30, 271, 381))
        self.label.setObjectName("label")
        self.toolButton = QtWidgets.QToolButton(parent=Dialog)
        self.toolButton.setGeometry(QtCore.QRect(200, 430, 81, 21))
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Analyze Emotion"))
        self.label_2.setText(_translate("Dialog", "**Result**"))
        self.label_3.setText(_translate("Dialog", "angry"))
        self.label_4.setText(_translate("Dialog", "disgust"))
        self.label_5.setText(_translate("Dialog", "fear"))
        self.label_6.setText(_translate("Dialog", "happy"))
        self.label_7.setText(_translate("Dialog", "neutral"))
        self.label_8.setText(_translate("Dialog", "sad"))
        self.label_9.setText(_translate("Dialog", "surprise"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.toolButton.setText(_translate("Dialog", "..."))
