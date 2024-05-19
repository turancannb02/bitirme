# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from ui_flotasyon import Ui_Flotasyon_Hucreleri_Hesabi
from ui_sarsintili_masa20007 import Ui_Sarsintili_Masa

class Ui_Zenginlestirme_Ekrani(object):
    def setupUi(self, Dialog):
        self.zenginlestirme_window = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(1205, 516)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 300, 541, 41))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 10, 1201, 71))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(180, 70, 841, 221))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 410, 841, 32))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 450, 841, 32))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(930, 310, 91, 21))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(790, 310, 141, 21))
        self.radioButton.setObjectName("radioButton")

        self.pushButton.clicked.connect(self.islem_yap)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def islem_yap(self):
        if self.radioButton.isChecked():
            self.sarsintili_masa_penceresi_ac()
        elif self.radioButton_2.isChecked():
            self.flotasyon_penceresi_ac()

    def flotasyon_penceresi_ac(self):
        self.zenginlestirme_window.hide()
        self.flotasyon_window = QtWidgets.QMainWindow()
        self.ui_flotasyon = Ui_Flotasyon_Hucreleri_Hesabi()
        self.ui_flotasyon.setupUi(self.flotasyon_window)
        self.flotasyon_window.show()
        self.ui_flotasyon.pushButton_2.clicked.connect(self.zenginlestirme_window.show)  # Show the enrichment screen

    def sarsintili_masa_penceresi_ac(self):
        self.zenginlestirme_window.hide()
        self.sarsintili_masa_window = QtWidgets.QMainWindow()
        self.ui_sarsintili_masa = Ui_Sarsintili_Masa()
        self.ui_sarsintili_masa.setupUi(self.sarsintili_masa_window)
        self.sarsintili_masa_window.show()
        self.ui_sarsintili_masa.pushButton_2.clicked.connect(self.zenginlestirme_window.show)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Zenginleştirme Birimi Hesapları"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Tesisinize kullanmak istediğiniz zenginleştirme tipini seçiniz:</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">ZENGİNLEŞTİRME BİRİMİNİN HESAPLAMALARI</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:12pt;\">Program, bir mineral zenginleştirme birimi tasarlamak için tasarlanmıştır. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:12pt;\">Kullanıcılar, tesislerinde kullanmak istedikleri zenginleştirme türünü seçebilir (</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:12pt; font-weight:700; font-style:italic;\">flotasyon</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:12pt;\"> veya </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:12pt; font-weight:700; font-style:italic;\">sallantılı masa</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:12pt;\">).</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:12pt;\">Ardından &quot;</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:12pt; font-weight:700; font-style:italic;\">Hesapla</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:12pt;\">&quot; düğmesine basabilirler. Program, gerekli parametreleri hesaplayacaktır. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:12pt;\">Kullanıcılar ayrıca &quot;</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:12pt; font-weight:700; font-style:italic;\">Geri Dön</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:12pt;\">&quot; düğmesine basabilir ve kaldıkları yerden devam edebilirler.</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Hesapla"))
        self.pushButton_2.setText(_translate("Dialog", "Geri Dön"))
        self.radioButton_2.setText(_translate("Dialog", "Flotasyon"))
        self.radioButton.setText(_translate("Dialog", "Sallantılı Masa"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Zenginlestirme_Ekrani()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
