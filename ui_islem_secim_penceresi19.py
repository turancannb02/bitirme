# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from ui_kirma import Ui_KirmaPenceresi
from ui_eleme import Ui_ElemePenceresi
from ui_ogutme import Ui_OgutmeSecimi
from ui_zenginlestirme import Ui_Zenginlestirme_Ekrani
from ui_stok import Ui_StokHesaplari

class Ui_MainWindow(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(1206, 528)
        self.checkBoxGrinding = QtWidgets.QCheckBox(Dialog)
        self.checkBoxGrinding.setGeometry(QtCore.QRect(190, 270, 782, 21))
        self.checkBoxGrinding.setMaximumSize(QtCore.QSize(782, 21))
        self.checkBoxGrinding.setAutoFillBackground(False)
        self.checkBoxGrinding.setObjectName("checkBoxGrinding")
        self.checkBoxCrushing = QtWidgets.QCheckBox(Dialog)
        self.checkBoxCrushing.setGeometry(QtCore.QRect(190, 190, 782, 20))
        self.checkBoxCrushing.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBoxCrushing.setAutoFillBackground(False)
        self.checkBoxCrushing.setIconSize(QtCore.QSize(20, 20))
        self.checkBoxCrushing.setObjectName("checkBoxCrushing")
        self.checkBoxScreening = QtWidgets.QCheckBox(Dialog)
        self.checkBoxScreening.setGeometry(QtCore.QRect(190, 230, 782, 20))
        self.checkBoxScreening.setAutoFillBackground(False)
        self.checkBoxScreening.setObjectName("checkBoxScreening")
        self.checkBoxStockpiling = QtWidgets.QCheckBox(Dialog)
        self.checkBoxStockpiling.setGeometry(QtCore.QRect(190, 350, 782, 20))
        self.checkBoxStockpiling.setAutoFillBackground(False)
        self.checkBoxStockpiling.setObjectName("checkBoxStockpiling")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 400, 841, 32))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.hesapla)
        self.pushButton.clicked.connect(self.kirma_penceresi_ac)
        self.pushButton.clicked.connect(self.eleme_penceresi_ac)
        self.pushButton.clicked.connect(self.ogutme_penceresi_ac)
        self.pushButton.clicked.connect(self.zenginlestirme_penceresi_ac)
        self.pushButton.clicked.connect(self.stoklama_penceresi_ac)
        self.checkBoxEnrichment = QtWidgets.QCheckBox(Dialog)
        self.checkBoxEnrichment.setGeometry(QtCore.QRect(190, 310, 782, 20))
        self.checkBoxEnrichment.setAutoFillBackground(False)
        self.checkBoxEnrichment.setObjectName("checkBoxEnrichment")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(180, 80, 841, 81))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1201, 91))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 440, 841, 32))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.soru_penceresi_ac)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def connect_signals(self):
        self.pushButton.clicked.connect(self.hesapla)

    def soru_penceresi_ac(self):
        from ui_soru_penceresi import Ui_SoruPenceresi
        self.soru_window = QtWidgets.QMainWindow()
        self.ui_soru = Ui_SoruPenceresi()
        self.ui_soru.setupUi(self.soru_window)
        self.soru_window.show()
        self.Dialog.close()

    def hesapla(self):
        self.ekranlar = []
        self.kirma_kontrol()
        self.eleme_kontrol()
        self.ogutme_kontrol()
        self.zenginlestirme_kontrol()
        self.stoklama_kontrol()
        self.ekranlar.reverse()  # Listeyi ters çevir
        self.sonraki_ekran()


    def kirma_kontrol(self):
        if self.checkBoxCrushing.isChecked():
            self.ekranlar.append(self.kirma_penceresi_ac)

    def eleme_kontrol(self):
        if self.checkBoxScreening.isChecked():
            self.ekranlar.append(self.eleme_penceresi_ac)

    def ogutme_kontrol(self):
        if self.checkBoxGrinding.isChecked():
            self.ekranlar.append(self.ogutme_penceresi_ac)

    def zenginlestirme_kontrol(self):
        if self.checkBoxEnrichment.isChecked():
            self.ekranlar.append(self.zenginlestirme_penceresi_ac)

    def stoklama_kontrol(self):
        if self.checkBoxStockpiling.isChecked():
            self.ekranlar.append(self.stoklama_penceresi_ac)


    def sonraki_ekran(self):
        if self.ekranlar:
            # Pop the first screen from the list and open it
            ekran = self.ekranlar.pop(0)
            ekran()

    def kirma_penceresi_ac(self):
        if self.checkBoxCrushing.isChecked():  
            self.kirma_window = QtWidgets.QMainWindow()  
            self.ui_kirma = Ui_KirmaPenceresi()  # Her bir pencerenin kendi UI sınıfı olmalı
            self.ui_kirma.setupUi(self.kirma_window)  
            self.kirma_window.show()  
            self.ui_kirma.pushButton.clicked.connect(self.sonraki_ekran)


    def eleme_penceresi_ac(self):
        if self.checkBoxScreening.isChecked():  
            self.eleme_window = QtWidgets.QMainWindow()  
            self.ui_eleme = Ui_ElemePenceresi()  # Her bir pencerenin kendi UI sınıfı olmalı
            self.ui_eleme.setupUi(self.eleme_window)  
            self.eleme_window.show()
            self.ui_eleme.pushButton.clicked.connect(self.sonraki_ekran)
    
    def ogutme_penceresi_ac(self):
        if self.checkBoxGrinding.isChecked():  
            self.ogutme_window = QtWidgets.QMainWindow()  
            self.ui_ogutme = Ui_OgutmeSecimi()  # Her bir pencerenin kendi UI sınıfı olmalı
            self.ui_ogutme.setupUi(self.ogutme_window)  
            self.ogutme_window.show()
            self.ui_ogutme.pushButton.clicked.connect(self.sonraki_ekran)

    def zenginlestirme_penceresi_ac(self):
        if self.checkBoxEnrichment.isChecked():   
            self.zenginlestirme_window = QtWidgets.QMainWindow()
            self.ui_zenginlestirme = Ui_Zenginlestirme_Ekrani()
            self.ui_zenginlestirme.setupUi(self.zenginlestirme_window)
            self.zenginlestirme_window.show()
            self.ui_zenginlestirme.pushButton.clicked.connect(self.sonraki_ekran)  # Add this line

    def stoklama_penceresi_ac(self):
        if  self.checkBoxStockpiling.isChecked():
            self.stoklama_window = QtWidgets.QMainWindow()
            self.ui_stoklama = Ui_StokHesaplari()
            self.ui_stoklama.setupUi(self.stoklama_window)
            self.stoklama_window.show()
            self.ui_stoklama.pushButton.clicked.connect(self.sonraki_ekran)  # Add this line



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "İşlem Seçim Ekranı"))
        self.checkBoxGrinding.setText(_translate("Dialog", "Öğütme"))
        self.checkBoxCrushing.setText(_translate("Dialog", "Kırma"))
        self.checkBoxScreening.setText(_translate("Dialog", "Eleme"))
        self.checkBoxStockpiling.setText(_translate("Dialog", "Stoklama"))
        self.pushButton.setText(_translate("Dialog", "Hesapla"))
        self.checkBoxEnrichment.setText(_translate("Dialog", "Zenginleştirme"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">İşlem Seçim Ekranı, cevher işleme tesisiniz için uygun işlemleri seçmenize yardımcı olacak bir programdır. Programı kullanmak için, sadece tesisinizde kullanmak istediğiniz işlemlerin yanındaki kutuları işaretleyin ve ayarlarını yapın. İşlemlerinizi seçip ayarları ayarladıktan sonra, &quot;Hesapla&quot; düğmesine tıklayarak bir rapor oluşturabilirsiniz. Rapor, her işlemin kapasitesi, tesisinizin toplam kapasitesi ve her işlemin maliyeti hakkında bilgi içerecektir.</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">İŞLEM SEÇİM EKRANI</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", "Geri Dön"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
