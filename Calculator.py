import re

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 820)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonZero = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.numberPressed("0"))
        self.buttonZero.setGeometry(QtCore.QRect(0, 660, 240, 120))
        self.buttonZero.setStyleSheet("background-color: rgb(107, 107, 107);\n""color: rgb(255, 255, 255);\n""font: 75 24pt \"Arial\";")
        self.buttonZero.setObjectName("buttonZero")
        self.buttonComma = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.commaPressed())
        self.buttonComma.setGeometry(QtCore.QRect(240, 660, 120, 120))
        self.buttonComma.setStyleSheet("background-color: rgb(107, 107, 107);\n""color: rgb(255, 255, 255);\n""font: 75 24pt \"Arial\";")
        self.buttonComma.setObjectName("buttonComma")
        self.buttonEqual = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.equalPressed())
        self.buttonEqual.setGeometry(QtCore.QRect(360, 660, 120, 120))
        self.buttonEqual.setStyleSheet("background-color: rgb(255, 170, 0);\n""color: rgb(255, 255, 255);\n""font: 75 24pt \"Arial\";")
        self.buttonEqual.setObjectName("buttonEqual")
        self.buttonPlus = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.operatorPressed("+"))
        self.buttonPlus.setGeometry(QtCore.QRect(360, 540, 120, 120))
        self.buttonPlus.setStyleSheet("background-color: rgb(255, 170, 0);\n""color: rgb(255, 255, 255);\n""font: 75 24pt \"Arial\";")
        self.buttonPlus.setObjectName("buttonPlus")
        self.buttonThree = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.numberPressed("3"))
        self.buttonThree.setGeometry(QtCore.QRect(240, 540, 120, 120))
        self.buttonThree.setStyleSheet("background-color: rgb(107, 107, 107);\n""color: rgb(255, 255, 255);\n""font: 75 24pt \"Arial\";")
        self.buttonThree.setObjectName("buttonThree")
        self.buttonTwo = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.numberPressed("2"))
        self.buttonTwo.setGeometry(QtCore.QRect(120, 540, 120, 120))
        self.buttonTwo.setStyleSheet("background-color: rgb(107, 107, 107);\n""color: rgb(255, 255, 255);\n""font: 75 24pt \"Arial\";")
        self.buttonTwo.setObjectName("buttonTwo")
        self.buttonOne = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.numberPressed("1"))
        self.buttonOne.setGeometry(QtCore.QRect(0, 540, 120, 120))
        self.buttonOne.setStyleSheet("background-color: rgb(107, 107, 107);\n""color: rgb(255, 255, 255);\n""font: 75 24pt \"Arial\";")
        self.buttonOne.setObjectName("buttonOne")
        self.buttonMinus = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.operatorPressed("-"))
        self.buttonMinus.setGeometry(QtCore.QRect(360, 420, 120, 120))
        self.buttonMinus.setStyleSheet("background-color: rgb(255, 170, 0);\n""color: rgb(255, 255, 255);\n""font: 75 24pt \"Arial\";")
        self.buttonMinus.setObjectName("buttonMinus")
        self.buttonSix = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.numberPressed("6"))
        self.buttonSix.setGeometry(QtCore.QRect(240, 420, 120, 120))
        self.buttonSix.setStyleSheet("background-color: rgb(107, 107, 107);\n""color: rgb(255, 255, 255);\n""font: 75 24pt \"Arial\";")
        self.buttonSix.setObjectName("buttonSix")
        self.buttonFive = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.numberPressed("5"))
        self.buttonFive.setGeometry(QtCore.QRect(120, 420, 120, 120))
        self.buttonFive.setStyleSheet("background-color: rgb(107, 107, 107);\n""color: rgb(255, 255, 255);\n""font: 75 24pt \"Arial\";")
        self.buttonFive.setObjectName("buttonFive")
        self.buttonFour = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.numberPressed("4"))
        self.buttonFour.setGeometry(QtCore.QRect(0, 420, 120, 120))
        self.buttonFour.setStyleSheet("background-color: rgb(107, 107, 107);\n""color: rgb(255, 255, 255);\n""font: 75 24pt \"Arial\";")
        self.buttonFour.setObjectName("buttonFour")
        self.buttonMultiply = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.operatorPressed("*"))
        self.buttonMultiply.setGeometry(QtCore.QRect(360, 300, 120, 120))
        self.buttonMultiply.setStyleSheet("background-color: rgb(255, 170, 0);\n""color: rgb(255, 255, 255);\n""font: 75 24pt \"Arial\";")
        self.buttonMultiply.setObjectName("buttonMultiply")
        self.buttonPlusMinus = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.plusMinusPressed())
        self.buttonPlusMinus.setGeometry(QtCore.QRect(120, 180, 120, 120))
        self.buttonPlusMinus.setStyleSheet("background-color: rgb(215, 215, 215);\n""color: rgb(255, 255, 255);\n""font: 75 24pt \"Arial\";")
        self.buttonPlusMinus.setObjectName("buttonPlusMinus")
        self.buttonAC = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.ACPressed())
        self.buttonAC.setGeometry(QtCore.QRect(0, 180, 120, 120))
        self.buttonAC.setStyleSheet("background-color: rgb(215, 215, 215);\n""color: rgb(255, 255, 255);\n""font: 75 24pt \"Arial\";")
        self.buttonAC.setObjectName("buttonAC")
        self.buttonDivided = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.operatorPressed("/"))
        self.buttonDivided.setGeometry(QtCore.QRect(360, 180, 120, 120))
        self.buttonDivided.setStyleSheet("background-color: rgb(255, 170, 0);\n""color: rgb(255, 255, 255);\n""font: 75 24pt \"Arial\";")
        self.buttonDivided.setObjectName("buttonDivided")
        self.buttonEight = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.numberPressed("8"))
        self.buttonEight.setGeometry(QtCore.QRect(120, 300, 120, 120))
        self.buttonEight.setStyleSheet("background-color: rgb(107, 107, 107);\n""color: rgb(255, 255, 255);\n""font: 75 24pt \"Arial\";")
        self.buttonEight.setObjectName("buttonEight")
        self.buttonModulo = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.operatorPressed("%"))
        self.buttonModulo.setGeometry(QtCore.QRect(240, 180, 120, 120))
        self.buttonModulo.setStyleSheet("background-color: rgb(215, 215, 215);\n""color: rgb(255, 255, 255);\n""font: 75 24pt \"Arial\";")
        self.buttonModulo.setObjectName("buttonModulo")
        self.buttonSeven = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.numberPressed("7"))
        self.buttonSeven.setGeometry(QtCore.QRect(0, 300, 120, 120))
        self.buttonSeven.setStyleSheet("background-color: rgb(107, 107, 107);\n""color: rgb(255, 255, 255);\n""font: 75 24pt \"Arial\";")
        self.buttonSeven.setObjectName("buttonSeven")
        self.buttonNine = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.numberPressed("9"))
        self.buttonNine.setGeometry(QtCore.QRect(240, 300, 120, 120))
        self.buttonNine.setStyleSheet("background-color: rgb(107, 107, 107);\n""color: rgb(255, 255, 255);\n""font: 75 24pt \"Arial\";")
        self.buttonNine.setObjectName("buttonNine")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(0, -10, 481, 181))
        self.outputLabel.setStyleSheet("color: rgb(255, 255, 255);\n""font: 75 70pt \"Arial\";")
        self.outputLabel.setText("0")
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def ACPressed(self):
        self.outputLabel.setText("0")

    def numberPressed(self, pressed):
        if self.outputLabel.text() == "0":
            self.outputLabel.setText("")
        self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}')

    def operatorPressed(self, pressed):
        output = self.outputLabel.text()
        if output[-1] in ['+', '-', '*', "/"]:
            pass
        else:
            self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}')

    def commaPressed(self):
        output = self.outputLabel.text()
        if output[-1] == ".":
            pass
        elif output[-1] in ['+', '-', '*', "/"]:
            self.outputLabel.setText(f'{self.outputLabel.text()}{"0."}')
        elif output[-1] == "%":
            pass
        else:
            self.outputLabel.setText(f'{self.outputLabel.text()}.')

    def plusMinusPressed(self):
        if "-" in self.outputLabel.text():
            self.outputLabel.setText(self.outputLabel.text().replace("-", ""))
        else:
            self.outputLabel.setText(f'{"-"}{self.outputLabel.text()}')

    def equalPressed(self):
        try:
            result = eval(self.outputLabel.text())
            self.outputLabel.setText(str(result))
        except:
            self.outputLabel.setText("Error ")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonZero.setText(_translate("MainWindow", "0"))
        self.buttonComma.setText(_translate("MainWindow", ","))
        self.buttonEqual.setText(_translate("MainWindow", "="))
        self.buttonPlus.setText(_translate("MainWindow", "+"))
        self.buttonThree.setText(_translate("MainWindow", "3"))
        self.buttonTwo.setText(_translate("MainWindow", "2"))
        self.buttonOne.setText(_translate("MainWindow", "1"))
        self.buttonMinus.setText(_translate("MainWindow", "-"))
        self.buttonSix.setText(_translate("MainWindow", "6"))
        self.buttonFive.setText(_translate("MainWindow", "5"))
        self.buttonFour.setText(_translate("MainWindow", "4"))
        self.buttonMultiply.setText(_translate("MainWindow", "x"))
        self.buttonPlusMinus.setText(_translate("MainWindow", "+/-"))
        self.buttonAC.setText(_translate("MainWindow", "AC"))
        self.buttonDivided.setText(_translate("MainWindow", "/"))
        self.buttonEight.setText(_translate("MainWindow", "8"))
        self.buttonModulo.setText(_translate("MainWindow", "%"))
        self.buttonSeven.setText(_translate("MainWindow", "7"))
        self.buttonNine.setText(_translate("MainWindow", "9"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
