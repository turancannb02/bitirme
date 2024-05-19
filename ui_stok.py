# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from ui_bant import Ui_Bant
import math

class Ui_StokHesaplari(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1440, 761)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(510, 700, 111, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(640, 700, 100, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(510, 230, 351, 41))
        self.label_14.setTextFormat(QtCore.Qt.RichText)
        self.label_14.setObjectName("label_14")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(90, 80, 881, 121))
        self.textBrowser.setObjectName("textBrowser")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(50, 230, 41, 41))
        self.label_7.setTextFormat(QtCore.Qt.RichText)
        self.label_7.setObjectName("label_7")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 1441, 51))
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(530, 270, 351, 21))
        self.label_13.setObjectName("label_13")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(760, 700, 201, 32))
        self.pushButton.setObjectName("pushButton")
        self.label_22 = QtWidgets.QLabel(Dialog)
        self.label_22.setGeometry(QtCore.QRect(530, 300, 361, 21))
        self.label_22.setObjectName("label_22")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(1010, 80, 361, 121))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(190, 230, 211, 41))
        self.label_8.setTextFormat(QtCore.Qt.RichText)
        self.label_8.setObjectName("label_8")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(90, 231, 101, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(100, 370, 221, 21))
        self.label_9.setObjectName("label_9")
        self.spinBox_14 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_14.setGeometry(QtCore.QRect(430, 430, 61, 22))
        self.spinBox_14.setMouseTracking(True)
        self.spinBox_14.setMaximum(9999999)
        self.spinBox_14.setObjectName("spinBox_14")
        self.spinBox_4 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_4.setGeometry(QtCore.QRect(430, 370, 61, 22))
        self.spinBox_4.setMouseTracking(True)
        self.spinBox_4.setMaximum(9999999)
        self.spinBox_4.setObjectName("spinBox_4")
        self.label_25 = QtWidgets.QLabel(Dialog)
        self.label_25.setGeometry(QtCore.QRect(100, 430, 291, 21))
        self.label_25.setObjectName("label_25")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setGeometry(QtCore.QRect(430, 280, 62, 22))
        self.doubleSpinBox.setMouseTracking(True)
        self.doubleSpinBox.setMaximum(99999999.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(100, 340, 191, 21))
        self.label_10.setObjectName("label_10")
        self.label_24 = QtWidgets.QLabel(Dialog)
        self.label_24.setGeometry(QtCore.QRect(100, 310, 181, 21))
        self.label_24.setObjectName("label_24")
        self.label_26 = QtWidgets.QLabel(Dialog)
        self.label_26.setGeometry(QtCore.QRect(100, 270, 321, 41))
        self.label_26.setTextFormat(QtCore.Qt.RichText)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(Dialog)
        self.label_27.setGeometry(QtCore.QRect(100, 400, 301, 21))
        self.label_27.setObjectName("label_27")
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(430, 340, 61, 22))
        self.spinBox_2.setMouseTracking(True)
        self.spinBox_2.setMaximum(9999999)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(430, 310, 61, 22))
        self.spinBox.setMouseTracking(True)
        self.spinBox.setMaximum(360)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_13 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_13.setGeometry(QtCore.QRect(430, 400, 61, 22))
        self.spinBox_13.setMouseTracking(True)
        self.spinBox_13.setMaximum(24)
        self.spinBox_13.setObjectName("spinBox_13")
        self.label_29 = QtWidgets.QLabel(Dialog)
        self.label_29.setGeometry(QtCore.QRect(530, 330, 321, 21))
        self.label_29.setObjectName("label_29")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(900, 270, 62, 22))
        self.doubleSpinBox_2.setMouseTracking(True)
        self.doubleSpinBox_2.setMaximum(99999999.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(900, 300, 62, 22))
        self.doubleSpinBox_3.setMouseTracking(True)
        self.doubleSpinBox_3.setMaximum(999999999.0)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(900, 330, 62, 22))
        self.doubleSpinBox_4.setMouseTracking(True)
        self.doubleSpinBox_4.setMaximum(99999999.0)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.label_28 = QtWidgets.QLabel(Dialog)
        self.label_28.setGeometry(QtCore.QRect(990, 300, 261, 21))
        self.label_28.setObjectName("label_28")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(990, 270, 261, 21))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(970, 230, 351, 41))
        self.label_16.setTextFormat(QtCore.Qt.RichText)
        self.label_16.setObjectName("label_16")
        self.spinBox_15 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_15.setGeometry(QtCore.QRect(1330, 270, 61, 22))
        self.spinBox_15.setMouseTracking(True)
        self.spinBox_15.setMaximum(100)
        self.spinBox_15.setObjectName("spinBox_15")
        self.spinBox_16 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_16.setGeometry(QtCore.QRect(1250, 270, 61, 22))
        self.spinBox_16.setMouseTracking(True)
        self.spinBox_16.setMaximum(9999999)
        self.spinBox_16.setObjectName("spinBox_16")
        self.spinBox_17 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_17.setGeometry(QtCore.QRect(1250, 300, 61, 22))
        self.spinBox_17.setMouseTracking(True)
        self.spinBox_17.setMaximum(9999999)
        self.spinBox_17.setObjectName("spinBox_17")
        self.spinBox_18 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_18.setGeometry(QtCore.QRect(1330, 300, 61, 22))
        self.spinBox_18.setMouseTracking(True)
        self.spinBox_18.setMaximum(100)
        self.spinBox_18.setObjectName("spinBox_18")
        self.spinBox_19 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_19.setGeometry(QtCore.QRect(1250, 380, 61, 22))
        self.spinBox_19.setMouseTracking(True)
        self.spinBox_19.setMaximum(9999999)
        self.spinBox_19.setObjectName("spinBox_19")
        self.spinBox_20 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_20.setGeometry(QtCore.QRect(1250, 410, 61, 22))
        self.spinBox_20.setMouseTracking(True)
        self.spinBox_20.setMaximum(9999999)
        self.spinBox_20.setObjectName("spinBox_20")
        self.label_30 = QtWidgets.QLabel(Dialog)
        self.label_30.setGeometry(QtCore.QRect(1000, 410, 251, 21))
        self.label_30.setObjectName("label_30")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(1000, 380, 251, 21))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(980, 340, 351, 41))
        self.label_18.setTextFormat(QtCore.Qt.RichText)
        self.label_18.setObjectName("label_18")
        self.spinBox_21 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_21.setGeometry(QtCore.QRect(1330, 380, 61, 22))
        self.spinBox_21.setMouseTracking(True)
        self.spinBox_21.setMaximum(100)
        self.spinBox_21.setObjectName("spinBox_21")
        self.spinBox_22 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_22.setGeometry(QtCore.QRect(1330, 410, 61, 22))
        self.spinBox_22.setMouseTracking(True)
        self.spinBox_22.setMaximum(100)
        self.spinBox_22.setObjectName("spinBox_22")

        self.outputBox = QtWidgets.QTextBrowser(Dialog)
        self.outputBox.setGeometry(QtCore.QRect(510, 480, 451, 191))
        self.outputBox.setObjectName("outputBox")

        self.pushButton.clicked.connect(self.bant_penceresi_ac)
        self.pushButton_2.clicked.connect(self.hesapla_fonksiyonu)
        self.pushButton_2.clicked.connect(self.kaydet)
        self.pushButton_3.clicked.connect(self.reset_values)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def hesapla_fonksiyonu(self):
        #Silo Hesabı
        cevher_turu = self.comboBox.currentText()
        self.outputBox.insertPlainText(f"{cevher_turu} Cevher Stok Sahası Tasarımı ve Boyutlandırılması Hesapları.\n")
        iri_tuvenan_cevher_yogunlugu = self.doubleSpinBox.value()
        kabarma_faktoru = 1.5  # Kabarma faktörünün değeri burada sabit alınmıştır.
        bulk_yogunluk = iri_tuvenan_cevher_yogunlugu / kabarma_faktoru
        self.outputBox.insertPlainText(f"Bulk Yoğunluğu: {round(bulk_yogunluk)} ton/m3 bulunmuştur.\n")
        saatlik_kapasite = self.spinBox_14.value()
        hacim = saatlik_kapasite / bulk_yogunluk
        self.outputBox.insertPlainText(f"{round(saatlik_kapasite)} ton için gereken hacim {round(hacim)} ton/m3 bulunmuştur.\n")
        yukseklik = self.spinBox_2.value()
        uzunluk = self.spinBox_4.value()
        prizma1 = yukseklik * uzunluk
        self.outputBox.insertPlainText(f"Toplam silo hacmi {round(prizma1)} m3 olarak bulunmuştur.\n")

        #Ara Ürün Çöktürme Tankı Hesabı
        F = self.doubleSpinBox_2.value()
        D = self.doubleSpinBox_3.value()
        V = 9.7
        dp = self.doubleSpinBox_4.value()
        tank_hesabi = ((1.33 * (F - D) / (V * dp))) * 408 * 0.093
        self.outputBox.insertPlainText(f"24 saatte 1 ton kuru katı için gerekli çökme alanı {round(tank_hesabi)} m2 olarak bulunmuştur.\n")

        r = math.sqrt(tank_hesabi / math.pi)
        self.outputBox.insertPlainText(f"Çöktürme konisinin yarıçapı {round(r)} m olarak bulunur.\n")

        #Konsantre Tikineri Hesabı
        kati_yuzdesi = self.spinBox_15.value()
        su_yuzdesi = self.spinBox_18.value()
        kati_miktari = self.spinBox_16.value()
        su_miktari = self.spinBox_17.value()
        sivi_kati = su_miktari / kati_miktari
        Co = (kati_yuzdesi / ((kati_yuzdesi / 3.8) + (su_yuzdesi)))
        tikiner_hesabi = ((kati_miktari * 0.2) / (Co * 0.4))
        self.outputBox.insertPlainText(f"Tikiner alanı {round(tikiner_hesabi)} m2 olarak bulunur.\n")
        r1 = math.sqrt(tikiner_hesabi / math.pi)
        self.outputBox.insertPlainText(f"Tikiner yarıçapı {round(r1)} m ve çapı ise {round(r1*2)} m olarak bulunur.\n")
        H = (((kati_miktari*0.2)/tikiner_hesabi) * ((1 / 3.8)) + (((sivi_kati + 0.33)/2)))
        Hyeni = H + 1.5
        self.outputBox.insertPlainText(f"Toplam yükseklik {round(Hyeni)} m olarak bulunur.\n")

        #Artık Tikineri Hesabı
        kati_yuzdesi_2 = self.spinBox_21.value()
        su_yuzdesi_2 = self.spinBox_22.value()
        kati_miktari_2 = self.spinBox_19.value()
        su_miktari_2 = self.spinBox_20.value()
        sivi_kati_2 = su_miktari_2 / kati_miktari_2
        Co_2 = (kati_yuzdesi_2 / ((kati_yuzdesi_2 / 3.8) + (su_yuzdesi_2)))
        tikiner_hesabi_2 = ((kati_miktari_2 * 0.2) / (Co_2 * 0.4))
        self.outputBox.insertPlainText(f"Tikiner alanı {round(tikiner_hesabi_2)} m2 olarak bulunur.\n")
        r1_2 = math.sqrt(tikiner_hesabi_2 / math.pi)
        self.outputBox.insertPlainText(f"Tikiner yarıçapı {round(r1_2)} m ve çapı ise {round(r1_2*2)} m olarak bulunur.\n")
        H_2 = (((kati_miktari_2*0.2)/tikiner_hesabi_2) * ((1 / 3.8)) + (((sivi_kati_2 + 0.33)/2)))
        Hyeni_2 = H_2 + 1.5
        self.outputBox.insertPlainText(f"Toplam yükseklik {round(Hyeni_2)} m olarak bulunur.\n")




    def bant_penceresi_ac(self):
        self.bant_window = QtWidgets.QMainWindow()
        self.ui_bant = Ui_Bant()  # Assuming you have a Ui_Bant class defined in a separate file
        self.ui_bant.setupUi(self.bant_window)
        self.bant_window.show()

    def kaydet(self):
        dosya_ismi = "Stoklama Hesapları.txt" 
        with open(dosya_ismi, 'w') as f:
            f.write(self.outputBox.toPlainText())
    def reset_values(self):
        self.doubleSpinBox.setValue(0)
        self.doubleSpinBox_2.setValue(0)
        self.doubleSpinBox_3.setValue(0)
        self.doubleSpinBox_4.setValue(0)
        self.spinBox.setValue(0)
        self.spinBox_2.setValue(0)
        self.spinBox_4.setValue(0)
        self.spinBox_13.setValue(0)
        self.spinBox_14.setValue(0)
        self.spinBox_15.setValue(0)
        self.spinBox_16.setValue(0)
        self.spinBox_17.setValue(0)
        self.spinBox_18.setValue(0)
        self.spinBox_19.setValue(0)
        self.spinBox_20.setValue(0)
        self.spinBox_21.setValue(0)
        self.spinBox_22.setValue(0)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Stok Hesaplamaları"))
        self.pushButton_3.setText(_translate("Dialog", "Sıfırla"))
        self.pushButton_2.setText(_translate("Dialog", "Hesapla"))
        self.label_14.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:12pt; font-weight:700;\">1.2 Ara Ürün Çöktürme Tankı Hesabı</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:12pt; font-weight:700; text-decoration: underline;\">Stok Hesaplamaları </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:12pt; font-weight:700; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">Bu program, stok hacmini ve stok kapasitesini hesaplamak için kullanılabilir. Program, öncelikle stok uzunluğunu, stok yüksekliğini ve stok şev açısını girmeniz ister. Ardından, stok malzemesinin yoğunluğunu girmeniz gerekir. Program, bu bilgileri kullanarak stok hacmini ve stok kapasitesini hesaplayacaktır. Hesaplanan stok hacmi ve stok kapasitesi, m3 ve ton olarak belirtilecektir. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:12pt; font-weight:700; text-decoration: underline;\">Cevher Silosu Hesabı </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:12pt; font-weight:700; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">Bu program, cevher silosunda depolanan cevher miktarını hesaplamak için kullanılabilir. Program, öncelikle silonun uzunluğunu, yüksekliğini ve kesit alanını girmeniz ister. Ardından, cevherin yoğunluğunu girmeniz gerekir. Program, bu bilgileri kullanarak cevher silosunda depolanan cevher miktarını hesaplayacaktır. Hesaplanan cevher miktarı, ton olarak belirtilecektir. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:12pt; font-weight:700; text-decoration: underline;\">Ara Ürün Çöktürme Tankı Hesabı </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:12pt; font-weight:700; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">Ara ürün çöktürme tankı, bir tesiste cevheri sudan ayırmak için kullanılan bir tanktır. Stok hacmi, çöktürme tankına beslenen pülpün su/katı oranı ve çöktürme tankı altından alınan pülpün su/katı oranı kullanılarak hesaplanabilir.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:12pt; font-weight:700; text-decoration: underline;\">Konsantre Tikineri Hesabı </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:12pt; font-weight:700; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">Bu program, konsantre tikinirin stok hacmini ve stok kapasitesini hesaplamak için kullanılabilir. Program, öncelikle stok uzunluğunu, stok yüksekliğini ve stok şev açısını girmeniz ister. Ardından, konsantre tikinirin yoğunluğunu girmeniz gerekir. Program, bu bilgileri kullanarak stok hacmini ve stok kapasitesini hesaplayacaktır. Hesaplanan stok hacmi ve stok kapasitesi, m3 ve ton olarak belirtilecektir. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:12pt; font-weight:700; text-decoration: underline;\">Artık Tikineri Hesabı </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:12pt; font-weight:700; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">Bu program, artık tikinirin stok hacmini ve stok kapasitesini hesaplamak için kullanılabilir. Program, öncelikle stok uzunluğunu, stok yüksekliğini ve stok şev açısını girmeniz ister. Ardından, artık tikinirin yoğunluğunu girmeniz gerekir. Program, bu bilgileri kullanarak stok hacmini ve stok kapasitesini hesaplayacaktır. Hesaplanan stok hacmi ve stok kapasitesi, m3 ve ton olarak belirtilecektir. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:12pt; font-weight:700; text-decoration: underline;\">Kullanım </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:12pt; font-weight:700; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">Programı kullanmak için, öncelikle programın ana ekranında bulunan stok türüne göre bir seçenek seçmelisiniz. Ardından, ilgili stok için gerekli bilgileri girin. Program, bu bilgileri kullanarak stok hacmini ve stok kapasitesini hesaplayacaktır. Hesaplanan stok hacmi ve stok kapasitesi, ekranın alt kısmında bulunan metin alanlarında gösterilecektir.</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:14pt; font-weight:700;\">1.1</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">STOK HESAPLAMALARI</span></p></body></html>"))
        self.label_13.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Tanka beslenen pülpün su/katı oranını giriniz:</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Bant Konveyöre Devam Et"))
        self.label_22.setText(_translate("Dialog", "<html><head/><body><p>Tankın altından alınan pülpün su/katı oranını giriniz:</p></body></html>"))
        self.textBrowser_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:12pt; font-weight:700; text-decoration: underline;\">Kabuller</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:12pt; font-weight:700; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">- </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt; font-weight:700; font-style:italic;\">1 ft2 = 0,093 m2</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\"> olarak alınmıştır.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:11pt;\"><br /></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:12pt; font-weight:700;\">Cevher Silosu Hesabı</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("Dialog", "İri"))
        self.comboBox.setItemText(1, _translate("Dialog", "İnce"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Stok uzunluğunu giriniz:</span></p></body></html>"))
        self.label_25.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Tesisin saatlik kapasitesini giriniz: </span></p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Stok yüksekliğini giriniz:</span></p></body></html>"))
        self.label_24.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Stok şev açısını giriniz:</span></p></body></html>"))
        self.label_26.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">İri Tüvenan Cevher Yoğunluğu (ton/m3):</span></p></body></html>"))
        self.label_27.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Tesisin günlük çalışma süresini giriniz: </span></p></body></html>"))
        self.label_29.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Pülpün özgün ağırlığı (gr/cm3):</span></p></body></html>"))
        self.label_28.setText(_translate("Dialog", "<html><head/><body><p>Su miktarını giriniz (t/saat), (%):</p></body></html>"))
        self.label_15.setText(_translate("Dialog", "<html><head/><body><p>Katı miktarını giriniz (t/saat), (%):</p></body></html>"))
        self.label_16.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:12pt; font-weight:700;\">1.3 Konsantre Tikineri Hesabı</span></p></body></html>"))
        self.label_30.setText(_translate("Dialog", "<html><head/><body><p>Su miktarını giriniz (t/saat), (%):</p></body></html>"))
        self.label_17.setText(_translate("Dialog", "<html><head/><body><p>Katı miktarını giriniz (t/saat), (%):</p></body></html>"))
        self.label_18.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:12pt; font-weight:700;\">1.4 Artık Tikineri Hesabı</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_StokHesaplari()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
