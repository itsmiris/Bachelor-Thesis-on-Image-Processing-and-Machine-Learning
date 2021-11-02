# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_egalizare.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import os
import pickle
import random

import cv2
import numpy as np
from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(479, 296)
        palette = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(245, 228, 219))
        gradient.setColorAt(0.09, QtGui.QColor(246, 215, 242))
        gradient.setColorAt(0.14, QtGui.QColor(212, 220, 246))
        gradient.setColorAt(0.1875, QtGui.QColor(232, 221, 224))
        gradient.setColorAt(0.25, QtGui.QColor(215, 222, 248))
        gradient.setColorAt(0.32, QtGui.QColor(243, 248, 224))
        gradient.setColorAt(0.385, QtGui.QColor(249, 204, 215))
        gradient.setColorAt(0.47, QtGui.QColor(216, 225, 230))
        gradient.setColorAt(0.58, QtGui.QColor(251, 220, 218))
        gradient.setColorAt(0.65, QtGui.QColor(229, 221, 232))
        gradient.setColorAt(0.75, QtGui.QColor(252, 232, 220))
        gradient.setColorAt(0.805, QtGui.QColor(241, 226, 243))
        gradient.setColorAt(0.86, QtGui.QColor(254, 239, 215))
        gradient.setColorAt(0.91, QtGui.QColor(254, 236, 244))
        gradient.setColorAt(1.0, QtGui.QColor(255, 191, 221))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(245, 228, 219))
        gradient.setColorAt(0.09, QtGui.QColor(246, 215, 242))
        gradient.setColorAt(0.14, QtGui.QColor(212, 220, 246))
        gradient.setColorAt(0.1875, QtGui.QColor(232, 221, 224))
        gradient.setColorAt(0.25, QtGui.QColor(215, 222, 248))
        gradient.setColorAt(0.32, QtGui.QColor(243, 248, 224))
        gradient.setColorAt(0.385, QtGui.QColor(249, 204, 215))
        gradient.setColorAt(0.47, QtGui.QColor(216, 225, 230))
        gradient.setColorAt(0.58, QtGui.QColor(251, 220, 218))
        gradient.setColorAt(0.65, QtGui.QColor(229, 221, 232))
        gradient.setColorAt(0.75, QtGui.QColor(252, 232, 220))
        gradient.setColorAt(0.805, QtGui.QColor(241, 226, 243))
        gradient.setColorAt(0.86, QtGui.QColor(254, 239, 215))
        gradient.setColorAt(0.91, QtGui.QColor(254, 236, 244))
        gradient.setColorAt(1.0, QtGui.QColor(255, 191, 221))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(245, 228, 219))
        gradient.setColorAt(0.09, QtGui.QColor(246, 215, 242))
        gradient.setColorAt(0.14, QtGui.QColor(212, 220, 246))
        gradient.setColorAt(0.1875, QtGui.QColor(232, 221, 224))
        gradient.setColorAt(0.25, QtGui.QColor(215, 222, 248))
        gradient.setColorAt(0.32, QtGui.QColor(243, 248, 224))
        gradient.setColorAt(0.385, QtGui.QColor(249, 204, 215))
        gradient.setColorAt(0.47, QtGui.QColor(216, 225, 230))
        gradient.setColorAt(0.58, QtGui.QColor(251, 220, 218))
        gradient.setColorAt(0.65, QtGui.QColor(229, 221, 232))
        gradient.setColorAt(0.75, QtGui.QColor(252, 232, 220))
        gradient.setColorAt(0.805, QtGui.QColor(241, 226, 243))
        gradient.setColorAt(0.86, QtGui.QColor(254, 239, 215))
        gradient.setColorAt(0.91, QtGui.QColor(254, 236, 244))
        gradient.setColorAt(1.0, QtGui.QColor(255, 191, 221))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.NoRole, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(245, 228, 219))
        gradient.setColorAt(0.09, QtGui.QColor(246, 215, 242))
        gradient.setColorAt(0.14, QtGui.QColor(212, 220, 246))
        gradient.setColorAt(0.1875, QtGui.QColor(232, 221, 224))
        gradient.setColorAt(0.25, QtGui.QColor(215, 222, 248))
        gradient.setColorAt(0.32, QtGui.QColor(243, 248, 224))
        gradient.setColorAt(0.385, QtGui.QColor(249, 204, 215))
        gradient.setColorAt(0.47, QtGui.QColor(216, 225, 230))
        gradient.setColorAt(0.58, QtGui.QColor(251, 220, 218))
        gradient.setColorAt(0.65, QtGui.QColor(229, 221, 232))
        gradient.setColorAt(0.75, QtGui.QColor(252, 232, 220))
        gradient.setColorAt(0.805, QtGui.QColor(241, 226, 243))
        gradient.setColorAt(0.86, QtGui.QColor(254, 239, 215))
        gradient.setColorAt(0.91, QtGui.QColor(254, 236, 244))
        gradient.setColorAt(1.0, QtGui.QColor(255, 191, 221))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(245, 228, 219))
        gradient.setColorAt(0.09, QtGui.QColor(246, 215, 242))
        gradient.setColorAt(0.14, QtGui.QColor(212, 220, 246))
        gradient.setColorAt(0.1875, QtGui.QColor(232, 221, 224))
        gradient.setColorAt(0.25, QtGui.QColor(215, 222, 248))
        gradient.setColorAt(0.32, QtGui.QColor(243, 248, 224))
        gradient.setColorAt(0.385, QtGui.QColor(249, 204, 215))
        gradient.setColorAt(0.47, QtGui.QColor(216, 225, 230))
        gradient.setColorAt(0.58, QtGui.QColor(251, 220, 218))
        gradient.setColorAt(0.65, QtGui.QColor(229, 221, 232))
        gradient.setColorAt(0.75, QtGui.QColor(252, 232, 220))
        gradient.setColorAt(0.805, QtGui.QColor(241, 226, 243))
        gradient.setColorAt(0.86, QtGui.QColor(254, 239, 215))
        gradient.setColorAt(0.91, QtGui.QColor(254, 236, 244))
        gradient.setColorAt(1.0, QtGui.QColor(255, 191, 221))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(245, 228, 219))
        gradient.setColorAt(0.09, QtGui.QColor(246, 215, 242))
        gradient.setColorAt(0.14, QtGui.QColor(212, 220, 246))
        gradient.setColorAt(0.1875, QtGui.QColor(232, 221, 224))
        gradient.setColorAt(0.25, QtGui.QColor(215, 222, 248))
        gradient.setColorAt(0.32, QtGui.QColor(243, 248, 224))
        gradient.setColorAt(0.385, QtGui.QColor(249, 204, 215))
        gradient.setColorAt(0.47, QtGui.QColor(216, 225, 230))
        gradient.setColorAt(0.58, QtGui.QColor(251, 220, 218))
        gradient.setColorAt(0.65, QtGui.QColor(229, 221, 232))
        gradient.setColorAt(0.75, QtGui.QColor(252, 232, 220))
        gradient.setColorAt(0.805, QtGui.QColor(241, 226, 243))
        gradient.setColorAt(0.86, QtGui.QColor(254, 239, 215))
        gradient.setColorAt(0.91, QtGui.QColor(254, 236, 244))
        gradient.setColorAt(1.0, QtGui.QColor(255, 191, 221))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.NoRole, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(245, 228, 219))
        gradient.setColorAt(0.09, QtGui.QColor(246, 215, 242))
        gradient.setColorAt(0.14, QtGui.QColor(212, 220, 246))
        gradient.setColorAt(0.1875, QtGui.QColor(232, 221, 224))
        gradient.setColorAt(0.25, QtGui.QColor(215, 222, 248))
        gradient.setColorAt(0.32, QtGui.QColor(243, 248, 224))
        gradient.setColorAt(0.385, QtGui.QColor(249, 204, 215))
        gradient.setColorAt(0.47, QtGui.QColor(216, 225, 230))
        gradient.setColorAt(0.58, QtGui.QColor(251, 220, 218))
        gradient.setColorAt(0.65, QtGui.QColor(229, 221, 232))
        gradient.setColorAt(0.75, QtGui.QColor(252, 232, 220))
        gradient.setColorAt(0.805, QtGui.QColor(241, 226, 243))
        gradient.setColorAt(0.86, QtGui.QColor(254, 239, 215))
        gradient.setColorAt(0.91, QtGui.QColor(254, 236, 244))
        gradient.setColorAt(1.0, QtGui.QColor(255, 191, 221))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(245, 228, 219))
        gradient.setColorAt(0.09, QtGui.QColor(246, 215, 242))
        gradient.setColorAt(0.14, QtGui.QColor(212, 220, 246))
        gradient.setColorAt(0.1875, QtGui.QColor(232, 221, 224))
        gradient.setColorAt(0.25, QtGui.QColor(215, 222, 248))
        gradient.setColorAt(0.32, QtGui.QColor(243, 248, 224))
        gradient.setColorAt(0.385, QtGui.QColor(249, 204, 215))
        gradient.setColorAt(0.47, QtGui.QColor(216, 225, 230))
        gradient.setColorAt(0.58, QtGui.QColor(251, 220, 218))
        gradient.setColorAt(0.65, QtGui.QColor(229, 221, 232))
        gradient.setColorAt(0.75, QtGui.QColor(252, 232, 220))
        gradient.setColorAt(0.805, QtGui.QColor(241, 226, 243))
        gradient.setColorAt(0.86, QtGui.QColor(254, 239, 215))
        gradient.setColorAt(0.91, QtGui.QColor(254, 236, 244))
        gradient.setColorAt(1.0, QtGui.QColor(255, 191, 221))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(245, 228, 219))
        gradient.setColorAt(0.09, QtGui.QColor(246, 215, 242))
        gradient.setColorAt(0.14, QtGui.QColor(212, 220, 246))
        gradient.setColorAt(0.1875, QtGui.QColor(232, 221, 224))
        gradient.setColorAt(0.25, QtGui.QColor(215, 222, 248))
        gradient.setColorAt(0.32, QtGui.QColor(243, 248, 224))
        gradient.setColorAt(0.385, QtGui.QColor(249, 204, 215))
        gradient.setColorAt(0.47, QtGui.QColor(216, 225, 230))
        gradient.setColorAt(0.58, QtGui.QColor(251, 220, 218))
        gradient.setColorAt(0.65, QtGui.QColor(229, 221, 232))
        gradient.setColorAt(0.75, QtGui.QColor(252, 232, 220))
        gradient.setColorAt(0.805, QtGui.QColor(241, 226, 243))
        gradient.setColorAt(0.86, QtGui.QColor(254, 239, 215))
        gradient.setColorAt(0.91, QtGui.QColor(254, 236, 244))
        gradient.setColorAt(1.0, QtGui.QColor(255, 191, 221))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.NoRole, brush)
        Dialog.setPalette(palette)
        Dialog.setStyleSheet("\n"
                             "QDialog{\n"
                             "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 228, 219, 255), stop:0.09 rgba(246, 215, 242, 255), stop:0.14 rgba(212, 220, 246, 255), stop:0.1875 rgba(232, 221, 224, 255), stop:0.25 rgba(215, 222, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 204, 215, 255), stop:0.47 rgba(216, 225, 230, 255), stop:0.58 rgba(251, 220, 218, 255), stop:0.65 rgba(229, 221, 232, 255), stop:0.75 rgba(252, 232, 220, 255), stop:0.805 rgba(241, 226, 243, 255), stop:0.86 rgba(254, 239, 215, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));\n"
                             "}\n"
                             "\n"
                             "pushButton_2{\n"
                             "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0))\n"
                             "}")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 30, 441, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(140, 50, 27, 16))
        self.label_5.setObjectName("label_5")

        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(180, 50, 106, 31))
        self.textBrowser.setObjectName("textBrowser")

        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 10, 284, 28))
        self.layoutWidget.setObjectName("layoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setStyleSheet("font: 9pt \"Sitka Text\";\n"
                                      "background-color: rgb(255, 193, 161);")
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.openCall)

        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 193, 161);\n"
                                        "font: 9pt \"Sitka Text\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.imgviz)

        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 193, 161);\n"
                                        "font: 9pt \"Sitka Text\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(self.nota)

        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(270, 90, 101, 26))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 193, 161);\n"
                                        "font: 9pt \"Sitka Text\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.nouanota)

        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 90, 211, 26))
        self.pushButton_6.setStyleSheet("font: 9pt \"Sitka Text\";\n"
                                        "background-color: rgb(255, 193, 161);")
        self.pushButton_6.setDefault(False)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.vizEgalizat)

        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(120, 130, 61, 20))
        self.label_7.setObjectName("label_7")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_2.setGeometry(QtCore.QRect(180, 130, 106, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 0, 421, 31))
        self.label.setStyleSheet("font: 18pt \"Sitka\";")
        self.label.setObjectName("label")

        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(20, 200, 441, 91))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.layoutWidget1 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 10, 431, 64))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setStyleSheet("font: 12pt \"Sitka\";")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget1)
        self.spinBox.setMinimum(3)
        self.spinBox.setMaximum(8)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_2.addWidget(self.spinBox)

        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 193, 161);\n"
                                        "font: 9pt \"Sitka Text\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_4.clicked.connect(self.vizualizare)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.current_image_path = os.getcwd() + "/53.jpg"
        self.image = QtGui.QImage()
        self.cv2Image = cv2.imread(self.current_image_path, 0)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "Nota:"))
        self.pushButton.setText(_translate("Dialog", "Alege imagine"))
        self.pushButton_2.setText(_translate("Dialog", "Vizualizare"))
        self.pushButton_3.setText(_translate("Dialog", "Dă-i o nota!"))
        self.pushButton_5.setText(_translate("Dialog", "Dă-i o nota!"))
        self.pushButton_6.setText(_translate("Dialog", "Îmbunătățire imagine și vizualizare"))
        self.label_7.setText(_translate("Dialog", "Noua notă:"))
        self.label.setText(_translate("Dialog",
                                      "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Estimarea și îmbunătățirea atractivității unei imagini</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Compară cu o imagine (din baza AVA style) cu nota:</span></p></body></html>"))
        self.pushButton_4.setText(_translate("Dialog", "Vizualizare"))

    def openCall(self):
        dlg = QFileDialog()
        # dlg.setFileMode(QFileDialog.AnyFile)
        if dlg.exec_():
            self.current_image_path = dlg.selectedFiles()[0]
            self.cv2Image = cv2.imread(self.current_image_path)
            # print(self.cv2Image.shape)

    def imgviz(self):
        cv2.imshow('imaginea selectată', self.cv2Image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def calcDescriptori(self):

        img = self.cv2Image
        hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        levels = 8
        hhist = cv2.calcHist([hsv_image], [0], None, [levels], [0, 180])
        sumhhist = np.sum(hhist)
        hhist[:] = [x / sumhhist for x in hhist]
        shist = cv2.calcHist([hsv_image], [1], None, [levels], [0, 255])
        sumshist = np.sum(shist)
        shist[:] = [x / sumshist for x in shist]
        vhist = cv2.calcHist([hsv_image], [2], None, [levels], [0, 255])
        sumvhist = np.sum(vhist)
        vhist[:] = [x / sumvhist for x in vhist]
        colordescriptor = np.concatenate([hhist, shist, vhist]).flatten()

        img = self.cv2Image
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        layer = img.copy()
        gp = [layer]
        descriptor_contrast = 0
        for i in range(6):
            layer = cv2.pyrDown(layer)
            gp.append(layer)
        layer = gp[5]
        lap_pyr = [layer]
        for i in range(5, 0, -1):
            size = (gp[i - 1].shape[1], gp[i - 1].shape[0])
            gaussian_extend = cv2.pyrUp(gp[i], dstsize=size)
            laplacian = cv2.subtract(gp[i - 1], gaussian_extend)
            lap_pyr.append(laplacian)
        for i in range(1, 6):
            m, n = lap_pyr[i].shape
            contrast_lvl = 0
            for j in range(m):
                for k in range(n):
                    contrast_lvl = contrast_lvl + int(lap_pyr[i][j][k]) * int(lap_pyr[i][j][k])
            contrast_lvl = contrast_lvl / (m * n * np.power(2, 5 - i))
            descriptor_contrast = descriptor_contrast + contrast_lvl

        v = np.zeros((1, 25))
        for i in range(24):
            v[0][i] = (colordescriptor)[i]
        v[0][24] = descriptor_contrast
        v.reshape(1, -1)
        return (v)

    def egalizare(self):
        img = self.cv2Image
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.equalizeHist(img)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

        hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        levels = 8
        hhist = cv2.calcHist([hsv_image], [0], None, [levels], [0, 180])
        sumhhist = np.sum(hhist)
        hhist[:] = [x / sumhhist for x in hhist]
        shist = cv2.calcHist([hsv_image], [1], None, [levels], [0, 255])
        sumshist = np.sum(shist)
        shist[:] = [x / sumshist for x in shist]
        vhist = cv2.calcHist([hsv_image], [2], None, [levels], [0, 255])
        sumvhist = np.sum(vhist)
        vhist[:] = [x / sumvhist for x in vhist]
        colordescriptor = np.concatenate([hhist, shist, vhist]).flatten()

        img = self.cv2Image
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        layer = img.copy()
        gp = [layer]
        descriptor_contrast = 0
        for i in range(6):
            layer = cv2.pyrDown(layer)
            gp.append(layer)
        layer = gp[5]
        lap_pyr = [layer]
        for i in range(5, 0, -1):
            size = (gp[i - 1].shape[1], gp[i - 1].shape[0])
            gaussian_extend = cv2.pyrUp(gp[i], dstsize=size)
            laplacian = cv2.subtract(gp[i - 1], gaussian_extend)
            lap_pyr.append(laplacian)
        for i in range(1, 6):
            m, n = lap_pyr[i].shape
            contrast_lvl = 0
            for j in range(m):
                for k in range(n):
                    contrast_lvl = contrast_lvl + int(lap_pyr[i][j][k]) * int(lap_pyr[i][j][k])
            contrast_lvl = contrast_lvl / (m * n * np.power(2, 5 - i))
            descriptor_contrast = descriptor_contrast + contrast_lvl

        e = np.zeros((1, 25))
        for i in range(24):
            e[0][i] = (colordescriptor)[i]
        e[0][24] = descriptor_contrast
        e.reshape(1, -1)
        return (e)

    def vizEgalizat(self):
        img = self.cv2Image
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        hsv_planes = cv2.split(hsv)
        clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(8, 8))
        hsv_planes[2] = clahe.apply(hsv_planes[2])
        hsv = cv2.merge(hsv_planes)
        img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        img = cv2.fastNlMeansDenoisingColored(img, None, 3, 3, 7, 21)
        cv2.imshow('histograma egalizată', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def nouanota(self):
        filename = 'finalized_model.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        result = loaded_model.predict(self.egalizare())
        # print(result)
        self.textBrowser_2.setText(str(result))
        return (result)

    def nota(self):
        filename = 'finalized_model.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        result = loaded_model.predict(self.calcDescriptori())
        # print(result)
        self.textBrowser.setText(str(result))
        return (result)

    def vizualizare(self):
        if self.spinBox.value() == 3:
            k = 0
            lines = open('C:\\Users\\user\\Desktop\\licenta\\ultima incercare\\scores.txt').read().splitlines()
            while k == 0:
                myline = random.choice(lines)
                token = myline.split()
                nume = int(token[0])
                nota = float(token[1])
                if 2.50 <= nota < 3.50:
                    imagine = cv2.imread(
                        'C:\\Users\\user\\Desktop\\licenta\\15000\\AVA_dataset\\images\\images\\' + str(nume) + '.jpg')
                    cv2.imshow('imagine', imagine)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    print(nume)
                    k = 1

        if self.spinBox.value() == 4:
            k = 0
            lines = open('C:\\Users\\user\\Desktop\\licenta\\ultima incercare\\scores.txt').read().splitlines()
            while k == 0:
                myline = random.choice(lines)
                token = myline.split()
                nume = int(token[0])
                nota = float(token[1])
                if 3.50 <= nota < 4.50:
                    imagine = cv2.imread(
                        'C:\\Users\\user\\Desktop\\licenta\\15000\\AVA_dataset\\images\\images\\' + str(nume) + '.jpg')
                    cv2.imshow('imagine', imagine)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    print(nume)
                    k = 1

        if self.spinBox.value() == 5:
            k = 0
            lines = open('C:\\Users\\user\\Desktop\\licenta\\ultima incercare\\scores.txt').read().splitlines()
            while k == 0:
                myline = random.choice(lines)
                token = myline.split()
                nume = int(token[0])
                nota = float(token[1])
                if 4.50 <= nota < 5.50:
                    imagine = cv2.imread(
                        'C:\\Users\\user\\Desktop\\licenta\\15000\\AVA_dataset\\images\\images\\' + str(nume) + '.jpg')
                    cv2.imshow('imagine', imagine)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    print(nume)
                    k = 1

        if self.spinBox.value() == 6:
            k = 0
            lines = open('C:\\Users\\user\\Desktop\\licenta\\ultima incercare\\scores.txt').read().splitlines()
            while k == 0:
                myline = random.choice(lines)
                token = myline.split()
                nume = int(token[0])
                nota = float(token[1])
                if 5.50 <= nota < 6.50:
                    imagine = cv2.imread(
                        'C:\\Users\\user\\Desktop\\licenta\\15000\\AVA_dataset\\images\\images\\' + str(nume) + '.jpg')
                    cv2.imshow('imagine', imagine)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    print(nume)
                    k = 1

        if self.spinBox.value() == 7:
            k = 0
            lines = open('C:\\Users\\user\\Desktop\\licenta\\ultima incercare\\scores.txt').read().splitlines()
            while k == 0:
                myline = random.choice(lines)
                token = myline.split()
                nume = int(token[0])
                nota = float(token[1])
                if 6.50 <= nota < 7.50:
                    imagine = cv2.imread(
                        'C:\\Users\\user\\Desktop\\licenta\\15000\\AVA_dataset\\images\\images\\' + str(nume) + '.jpg')
                    cv2.imshow('imagine', imagine)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    print(nume)
                    k = 1

        if self.spinBox.value() == 8:
            k = 0
            lines = open('C:\\Users\\user\\Desktop\\licenta\\ultima incercare\\scores.txt').read().splitlines()
            while k == 0:
                myline = random.choice(lines)
                token = myline.split()
                nume = int(token[0])
                nota = float(token[1])
                if 7.50 <= nota:
                    imagine = cv2.imread(
                        'C:\\Users\\user\\Desktop\\licenta\\15000\\AVA_dataset\\images\\images\\' + str(nume) + '.jpg')
                    cv2.imshow('imagine', imagine)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    print(nume)
                    k = 1


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

