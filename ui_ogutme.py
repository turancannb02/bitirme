# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from ui_bilyali import Ui_BilyaliDegirmen
from ui_cubuklu import Ui_CubukluPencere

class Ui_OgutmeSecimi(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(1203, 518)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(210, 310, 521, 41))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1201, 61))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 450, 841, 32))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 410, 841, 32))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(210, 70, 841, 221))
        self.textBrowser.setObjectName("textBrowser")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(780, 320, 141, 21))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(920, 320, 151, 21))
        self.radioButton_2.setObjectName("radioButton_2")

        self.radioButton.clicked.connect(self.check_selection)  # radioButton'a tıklanma olayını kontrol etmek için check_selection fonksiyonunu bağlıyoruz
        self.pushButton.clicked.connect(self.calculate)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def check_selection(self):
        if self.radioButton.isChecked():  # radioButton seçiliyse
            self.selection = "bilya"
        elif self.radioButton_2.isChecked():  # radioButton_2 seçiliyse
            self.selection = "cubuk"
        else:
            self.selection = None

    def calculate(self):
        self.check_selection()  # check_selection fonksiyonunu çağırıyoruz
        if self.selection == "bilya":
            self.open_new_window() 
        else:
            self.selection == "cubuk"
            self.open_new_window_2() 

    def open_new_window(self):
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_BilyaliDegirmen()  # Yeni ekranın UI'ını tanımlıyoruz
        self.ui.setupUi(self.Window)
        self.Dialog.close()
        self.Window.show()
    
    def open_new_window_2(self):
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_CubukluPencere()  # Yeni ekranın UI'ını tanımlıyoruz
        self.ui.setupUi(self.Window)
        self.Dialog.close()
        self.Window.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Öğütücü Seçimi Ekranı"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Tesisinize kullanmak istediğiniz öğütücü tipini seçiniz:</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">ÖĞÜTME HESAPLAMALARI</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", "Geri Dön"))
        self.pushButton.setText(_translate("Dialog", "Hesapla"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:11pt; color:#1f1f1f; background-color:#ffffff;\">Öğütücüler, bir malzemeyi küçük parçalara ayırmak için kullanılan makinelerdir. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:11pt; color:#1f1f1f;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:11pt; color:#1f1f1f; background-color:#ffffff;\">Öğütücüler, farklı tiplerde ve boyutlarda mevcuttur ve her tip, farklı malzemeler için uygundur. En yaygın öğütücü türleri arasında bilyali değirmenler, çubuklu değirmenler, tambur değirmenler ve disk değirmenler bulunur. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:11pt; color:#1f1f1f;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:11pt; color:#1f1f1f; background-color:#ffffff;\">Öğütücüler, gıda işleme, kimyasal işleme, metal işleme ve madencilik dahil olmak üzere birçok endüstride kullanılmaktadır. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:11pt; color:#1f1f1f;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:11pt; color:#1f1f1f; background-color:#ffffff;\">Bu ekranda ise tesisinizde kullanmak istediğiniz öğütücü tipini seçip ilerlemeniz gerekmektedir. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:11pt; color:#1f1f1f;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:11pt; color:#1f1f1f; background-color:#ffffff;\">Seçiminizi yaptıktan sonra &quot;</span><span style=\" font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:11pt; font-weight:700; font-style:italic; color:#1f1f1f; background-color:#ffffff;\">Hesapla</span><span style=\" font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:11pt; color:#1f1f1f; background-color:#ffffff;\">&quot; tuşuna tıklayıp hesaplamalara başlayabilirsiniz. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:11pt; color:#1f1f1f;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:11pt; color:#1f1f1f; background-color:#ffffff;\">Eğer bu işlemi iptal etmek isterseniz de &quot;</span><span style=\" font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:11pt; font-weight:700; font-style:italic; color:#1f1f1f; background-color:#ffffff;\">Geri Dön</span><span style=\" font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:11pt; color:#1f1f1f; background-color:#ffffff;\">&quot; tuşuna tıklayıp kaldığınız yerden devam edebilirsiniz.</span></p></body></html>"))
        self.radioButton.setText(_translate("Dialog", "Biyalı Değirmen"))
        self.radioButton_2.setText(_translate("Dialog", "Çubuklu Değirmen"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_OgutmeSecimi()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
