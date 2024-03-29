# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test5.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication , QWidget, QInputDialog , QLineEdit , QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from skimage import io
from skimage.util import img_as_ubyte
import os
from skimage import morphology




class Ui_MainWindow4(object):
   
    def Ouvrir(self):
        filename= QFileDialog.getOpenFileName()
        a= filename[0]
        path=os.path.basename(a)
        s=io.imread(a)
        pixmap = QPixmap(a)
        self.label.setPixmap(QPixmap(pixmap))

        eroded_image = morphology.binary_erosion(s)
        eroded_image = img_as_ubyte(eroded_image)
        print('yes')
        new_mophology = "new_mophology " + path
        saved_image = io.imsave(new_mophology, eroded_image)
        pixmap1 = QPixmap(new_mophology)
        self.label_2.setPixmap(QPixmap(pixmap1))
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(220, 30, 550, 13))
        self.label2.setObjectName("label2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(26, 80, 181, 281))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.setScaledContents(True)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 80, 181, 281))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.setScaledContents(True)
        self.entrer3 = QtWidgets.QPushButton(self.centralwidget)
        self.entrer3.setGeometry(QtCore.QRect(220, 400, 75, 30))
        self.entrer3.setObjectName("entrer")
        self.suivant = QtWidgets.QPushButton(self.centralwidget)
        self.suivant.setGeometry(QtCore.QRect(400, 420, 75, 23))
        self.suivant.setObjectName("suivant")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.suivant.clicked.connect(MainWindow.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.entrer3.clicked.connect(self.Ouvrir)
      
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label2.setText(_translate("MainWindow", "Morphology: Binary erosion with default selem"))
        self.entrer3.setText(_translate("MainWindow", "Appliquer"))
        self.suivant.setText(_translate("MainWindow", "Terminer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow4()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
