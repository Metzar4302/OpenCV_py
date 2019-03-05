# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lable_design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(379, 339)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 3, 361, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.test_lable = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.test_lable.setObjectName("test_lable")
        self.verticalLayout.addWidget(self.test_lable)
        self.test_lcdNumber = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.test_lcdNumber.setObjectName("test_lcdNumber")
        self.verticalLayout.addWidget(self.test_lcdNumber)
        self.test_horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.test_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.test_horizontalSlider.setObjectName("test_horizontalSlider")
        self.verticalLayout.addWidget(self.test_horizontalSlider)
        self.test_textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.test_textEdit.setObjectName("test_textEdit")
        self.verticalLayout.addWidget(self.test_textEdit)
        self.test_comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.test_comboBox.setObjectName("test_comboBox")
        self.verticalLayout.addWidget(self.test_comboBox)
        self.test_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.test_pushButton.setObjectName("test_pushButton")
        self.verticalLayout.addWidget(self.test_pushButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.test_lable.setText(_translate("MainWindow", "TextLabel"))
        self.test_pushButton.setText(_translate("MainWindow", "PushButton"))

