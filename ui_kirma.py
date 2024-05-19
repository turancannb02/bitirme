# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KirmaPenceresi(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(1440, 762)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 20, 1441, 41))
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(80, 290, 361, 41))
        self.label_7.setTextFormat(QtCore.Qt.RichText)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(100, 330, 241, 31))
        self.label_9.setObjectName("label_9")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(400, 330, 62, 31))
        self.doubleSpinBox_2.setMouseTracking(True)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(100, 370, 201, 31))
        self.label_10.setObjectName("label_10")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(400, 370, 62, 31))
        self.doubleSpinBox_3.setMouseTracking(True)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(80, 430, 411, 41))
        self.label_11.setTextFormat(QtCore.Qt.RichText)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(100, 480, 281, 21))
        self.label_12.setObjectName("label_12")
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(400, 480, 62, 22))
        self.doubleSpinBox_4.setMouseTracking(True)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(480, 290, 351, 41))
        self.label_14.setTextFormat(QtCore.Qt.RichText)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(490, 320, 331, 41))
        self.label_15.setTextFormat(QtCore.Qt.RichText)
        self.label_15.setObjectName("label_15")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(510, 360, 311, 21))
        self.label_13.setObjectName("label_13")
        self.spinBox_5 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_5.setGeometry(QtCore.QRect(860, 360, 61, 22))
        self.spinBox_5.setMouseTracking(True)
        self.spinBox_5.setMaximum(10000000)
        self.spinBox_5.setObjectName("spinBox_5")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(510, 420, 331, 21))
        self.label_16.setObjectName("label_16")
        self.spinBox_6 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_6.setGeometry(QtCore.QRect(860, 420, 111, 22))
        self.spinBox_6.setMouseTracking(True)
        self.spinBox_6.setMaximum(999999999)
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_7 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_7.setGeometry(QtCore.QRect(860, 450, 111, 22))
        self.spinBox_7.setMouseTracking(True)
        self.spinBox_7.setMaximum(999999999)
        self.spinBox_7.setObjectName("spinBox_7")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(510, 450, 331, 21))
        self.label_17.setObjectName("label_17")
        self.spinBox_8 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_8.setGeometry(QtCore.QRect(1350, 420, 61, 22))
        self.spinBox_8.setMouseTracking(True)
        self.spinBox_8.setMaximum(999999999)
        self.spinBox_8.setObjectName("spinBox_8")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(990, 450, 331, 21))
        self.label_18.setObjectName("label_18")
        self.spinBox_9 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_9.setGeometry(QtCore.QRect(1350, 450, 61, 22))
        self.spinBox_9.setMouseTracking(True)
        self.spinBox_9.setMaximum(999999999)
        self.spinBox_9.setObjectName("spinBox_9")
        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(990, 420, 341, 21))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(970, 320, 361, 41))
        self.label_21.setTextFormat(QtCore.Qt.RichText)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(Dialog)
        self.label_22.setGeometry(QtCore.QRect(510, 390, 201, 21))
        self.label_22.setObjectName("label_22")
        self.spinBox_11 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_11.setGeometry(QtCore.QRect(860, 390, 61, 22))
        self.spinBox_11.setMouseTracking(True)
        self.spinBox_11.setMaximum(100000)
        self.spinBox_11.setObjectName("spinBox_11")
        self.spinBox_12 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_12.setGeometry(QtCore.QRect(1350, 390, 61, 22))
        self.spinBox_12.setMouseTracking(True)
        self.spinBox_12.setAutoFillBackground(False)
        self.spinBox_12.setWrapping(False)
        self.spinBox_12.setMaximum(10000000)
        self.spinBox_12.setObjectName("spinBox_12")
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(990, 360, 311, 21))
        self.label_19.setObjectName("label_19")
        self.spinBox_10 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_10.setGeometry(QtCore.QRect(1350, 360, 61, 22))
        self.spinBox_10.setMouseTracking(True)
        self.spinBox_10.setMaximum(10000000)
        self.spinBox_10.setObjectName("spinBox_10")
        self.label_23 = QtWidgets.QLabel(Dialog)
        self.label_23.setGeometry(QtCore.QRect(990, 390, 161, 21))
        self.label_23.setMouseTracking(True)
        self.label_23.setObjectName("label_23")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(120, 70, 881, 211))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(790, 690, 111, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 690, 100, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 690, 111, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(1040, 70, 361, 211))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_24 = QtWidgets.QLabel(Dialog)
        self.label_24.setGeometry(QtCore.QRect(100, 410, 301, 21))
        self.label_24.setObjectName("label_24")
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_5.setGeometry(QtCore.QRect(400, 410, 62, 22))
        self.doubleSpinBox_5.setMouseTracking(True)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #self.pushButton.clicked.connect(self.sonraki_ekran)  # This line should be added
        self.pushButton_2.clicked.connect(self.hesapla_fonksiyonu)
        self.pushButton_2.clicked.connect(self.kaydet)

        self.pushButton_3.clicked.connect(self.reset_values)
        
        self.infoButton_1 = QtWidgets.QPushButton(Dialog)
        self.infoButton_1.setGeometry(QtCore.QRect(285, 335, 18, 20))
        self.infoButton_1.setText("i")
        self.infoButton_1.setToolTip("Teorik elek altı miktarı, kırıcıdan çıkan malzemenin %80'i elek altında kalan miktardır.\n"
                    "Bu miktar, kırıcıdan çıkan malzemenin boyutunun ne kadar küçük olduğunu gösterir.\n"
                    "Teorik elek altı miktarı ne kadar küçük olursa, kırıcıdan çıkan malzemenin boyutu o kadar küçük olur.")
        self.infoButton_1.setStyleSheet("QPushButton {border: 1px  solid black; border-radius: 4px; font-size: 12px}") 

        self.infoButton_2 = QtWidgets.QPushButton(Dialog)
        self.infoButton_2.setGeometry(QtCore.QRect(230, 375, 18, 20))
        self.infoButton_2.setText("i")
        self.infoButton_2.setToolTip("Eleme verimi, bir elek kullanılarak belirli bir boyuttaki malzemenin ne kadarının elenip ne kadarının elemeden geçtiğini gösteren bir ölçümdür.\n"
                                     "Eleme verimi, %100 olarak ifade edilir ve 100'e ne kadar yakınsa, elek o kadar verimlidir.")
        self.infoButton_2.setStyleSheet("QPushButton {border: 1px  solid black; border-radius: 4px; font-size: 12px}") 

        self.infoButton_3 = QtWidgets.QPushButton(Dialog)
        self.infoButton_3.setGeometry(QtCore.QRect(347, 410, 18, 20))
        self.infoButton_3.setText("i")
        self.infoButton_3.setToolTip("Bir cevher işleme tesisinin saatlik kapasitesi, tesisin bir saat içinde işleyebileceği cevher miktarıdır.\n"
                                     "Bu miktar, tesisin büyüklüğüne, kullanılan ekipmanlara ve işlenen cevherin özelliklerine bağlıdır.\n\n"
                                     "Lütfen 'Genel Bilgiler' sayfasında girdiğiniz değeri giriniz.")
        self.infoButton_3.setStyleSheet("QPushButton {border: 1px  solid black; border-radius: 4px; font-size: 12px}") 

        self.infoButton_4 = QtWidgets.QPushButton(Dialog)
        self.infoButton_4.setGeometry(QtCore.QRect(340, 480, 18, 20))
        self.infoButton_4.setText("i")
        self.infoButton_4.setToolTip("Kapalı devrede elek üstü miktarı, elek açıklığından daha büyük olan malzemenin miktarıdır.\n"
                                     "Bu miktar, elek açıklığının boyutuna, malzemenin özelliklerine ve kırıcıya beslenen malzemenin miktarına bağlıdır.\n"
                                     "Genel olarak, elek açıklığı ne kadar küçük olursa, elek üstü miktarı o kadar az olur.\n"
                                     "Malzemenin özellikleri ne kadar sert olursa, elek üstü miktarı o kadar fazla olur.\n"
                                     "Kırıcıya beslenen malzemenin miktarı ne kadar fazla olursa, elek üstü miktarı o kadar fazla olur.")
        self.infoButton_4.setStyleSheet("QPushButton {border: 1px  solid black; border-radius: 4px; font-size: 12px}") 


        self.outputBox = QtWidgets.QTextBrowser(Dialog)
        self.outputBox.setGeometry(QtCore.QRect(515, 500, 400, 170))
        self.outputBox.setObjectName("outputBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)



            
    def hesapla_fonksiyonu(self):
        T = self.doubleSpinBox_5.value()       
        C = self.doubleSpinBox_2.value()  # Bu spinBox'ın Teorik elek altı miktarını temsil ettiğini varsayıyorum. Gerekirse düzeltmelisiniz.
        E = self.doubleSpinBox_3.value()  # Bu spinBox'ın eleme verimini temsil ettiğini varsayıyorum. Gerekirse düzeltmelisiniz.

        # K değerini hesapla
        K = T * (1 - C * E)
        self.outputBox.insertPlainText(f"K = {K:.2f} ton/saat Kırıcıya giren malzeme miktarı olarak bulunur.\n")

        a = self.doubleSpinBox_4.value()  # Kapalı devrede elek üstü miktarını temsil ettiğini varsayıyorum. Gerekirse düzeltmelisiniz.
        b = 0.14  # Kırıcıdan çıkan malzemenin öngörülen kırma boyutundan daha iri malzeme miktarı 
        # R değerini hesapla
        R = T * (a / (1 - (b / E)))

        # Sonuçları output'a ekleyin
        self.outputBox.insertPlainText(f"Devreden yük {R:.2f} ton/saat kırıcıya giren malzeme miktarı olarak bulunur.\n")

        # Primer Güç Hesabı
        self.outputBox.insertPlainText(f"Primer Güç Hesabı\n")

        beslenen_malzeme_miktari = self.spinBox_5.value()  # Beslenen Malzeme Miktarını temsil ettiğini varsayıyorum. Gerekirse düzeltmelisiniz.
        Wi = 12.49  # Kabullenilen değer
        D1 = self.spinBox_6.value()  # Kırıcıya beslenen malzemenin d80‟i
        D2 = self.spinBox_7.value()  # Kırıcıdan çıkan malzemenin d80‟i
        K_emniyet = 1.25  # Kabullenilen değer

        # Wt değerini hesapla
        Wt = 10 * Wi * ((1 / (D2 ** 0.5)) - (1 / (D1 ** 0.5)))
        self.outputBox.insertPlainText(f"Wt = {Wt:.2f} kWh/ton olarak bulunmuştur.\n")

        # Güç değerini hesapla
        guc = beslenen_malzeme_miktari * Wt * K_emniyet 
        self.outputBox.insertPlainText(f"Güç (kW) = {guc:.2f} kW olarak bulunmuştur.\n")

        # Güç değerini HP'ye dönüştür ve sonucu output'a ekleyin
        Hp = 1.341
        guc_hp = guc * Hp
        self.outputBox.insertPlainText(f"Güç (HP) = {guc_hp:.2f} HP olarak bulunmuştur.\n")

        # Sekonder Güç Hesabı
        self.outputBox.insertPlainText(f"Sekonder Güç Hesabı\n")
        beslenen_malzeme_miktari_1 = self.spinBox_10.value()  # Beslenen Malzeme Miktarını temsil ettiğini varsayıyorum. Gerekirse düzeltmelisiniz.
        Wi = 12.49  # Kabullenilen değer
        D1_1 = self.spinBox_8.value()  # Kırıcıya beslenen malzemenin d80‟i
        D2_1 = self.spinBox_9.value()  # Kırıcıdan çıkan malzemenin d80‟i
        K_emniyet = 1.25  # Kabullenilen değer
        self.outputBox.insertPlainText(f"Wi: {Wi:.2f} olarak kabul edilmiştir.\n")

        # Wt değerini hesapla
        Wt_1 = 10 * Wi * ((1 / (D2_1 ** 0.5)) - (1 / (D1_1 ** 0.5)))
        self.outputBox.insertPlainText(f"Wt = {Wt_1:.2f} kWh/ton olarak bulunmuştur.\n")

        # Güç değerini hesapla
        guc_1 = beslenen_malzeme_miktari_1 * Wt_1 * K_emniyet 
        self.outputBox.insertPlainText(f"Güç (kW) = {guc_1:.2f} kW olarak bulunmuştur.\n")

        # Güç değerini HP'ye dönüştür ve sonucu output'a ekleyin
        guc_hp_1 = guc * Hp
        self.outputBox.insertPlainText(f"Güç (HP) = {guc_hp_1:.2f} HP olarak bulunmuştur.\n")

    def reset_values(self):
        self.doubleSpinBox_2.setValue(0)
        self.doubleSpinBox_3.setValue(0)
        self.doubleSpinBox_4.setValue(0)
        self.doubleSpinBox_5.setValue(0)
        self.spinBox_5.setValue(0)
        self.spinBox_11.setValue(0)
        self.spinBox_6.setValue(0)
        self.spinBox_7.setValue(0)
        self.spinBox_10.setValue(0)
        self.spinBox_12.setValue(0)
        self.spinBox_8.setValue(0)
        self.spinBox_9.setValue(0)

    def kaydet(self):
        dosya_ismi = "Kırıcı Hesapları.txt" 
        with open(dosya_ismi, 'w') as f:
            f.write(self.outputBox.toPlainText())

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Kırıcı Seçimi ve Hesaplamaları"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">KIRICI SEÇİMİ VE HESAPLAMALARI</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:11pt; font-weight:700;\">1.1 Birinci Kademe Kırıcı Yük Hesabı </span></p></body></html>"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p>Teorik elek altı miktarını giriniz: </p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p>Eleme verimini giriniz:</p></body></html>"))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:11pt; font-weight:700;\">1.2 İkinci Kademe Kırıcı Devreden Yük Hesabı </span></p></body></html>"))
        self.label_12.setText(_translate("Dialog", "<html><head/><body><p>Kapalı devrede elek üstü miktarını giriniz:</p></body></html>"))
        self.label_14.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:11pt; font-weight:700;\">1.3 Kırıcıların Güç Hesapları ve Seçimi </span></p></body></html>"))
        self.label_15.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:11pt; font-weight:700;\">1.3.1 Primer Kırıcı Güç Hesabı</span></p></body></html>"))
        self.label_13.setText(_translate("Dialog", "<html><head/><body><p>Beslenen malzeme miktarını giriniz (ton/saat):</p></body></html>"))
        self.label_16.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman\';\">D1 : Kırıcıya beslenen malzemenin d80\'i giriniz (mikron):</span></p></body></html>"))
        self.label_17.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman\';\">D2 : Kırıcıdan çıkan malzemenin d80\'i giriniz (mikron):</span></p></body></html>"))
        self.label_18.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman\';\">D2 : Kırıcıdan çıkan malzemenin d80\'i giriniz (mikron):</span></p></body></html>"))
        self.label_20.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman\';\">D1 : Kırıcıya beslenen malzemenin d80\'i giriniz (mikron):</span></p></body></html>"))
        self.label_21.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:11pt; font-weight:700;\">1.3.2 Sekonder Çeneli Kırıcı Güç Hesabı</span></p></body></html>"))
        self.label_22.setText(_translate("Dialog", "<html><head/><body><p>Çıkış açıklığını giriniz:</p></body></html>"))
        self.label_19.setText(_translate("Dialog", "<html><head/><body><p>Beslenen malzeme miktarını giriniz (ton/saat):</p></body></html>"))
        self.label_23.setText(_translate("Dialog", "<html><head/><body><p>Çıkış açıklığını giriniz:</p></body></html>"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">Bu program, kırıcıların seçimi ve hesaplanması için tasarlanmıştır. Programı kullanmak için, öncelikle beslenen malzeme miktarını, kırıcıya beslenen malzemenin d80\'ini, kırıcıdan çıkan malzemenin d80\'ini, tesisin günlük çalışma süresini ve tesisin saatlik kapasitesini girmeniz gerekir. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">Ardından &quot;</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt; font-weight:700; font-style:italic;\">Hesapla</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">&quot; butonuna tıklayarak kapasite hesaplamasını yapabilirsiniz. Hesaplama sonucunda, kırıcı için gerekli güç ve kırıcı seçimi görüntülenecektir. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">Programı ilk defa kullanıyorsanız, &quot;</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt; font-weight:700; font-style:italic;\">Geri Dön</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">&quot; tuşuna tıklayarak seçim ekranına geri dönebilirsiniz. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">Aşağıda, programın nasıl kullanılacağına ilişkin bazı bilgiler verilmiştir: </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">- Beslenen malzeme miktarı, kırıcıya beslenen malzemenin d80\'i, kırıcıdan çıkan malzemenin d80\'i, tesisin günlük çalışma süresi ve tesisin saatlik kapasitesi gibi bilgileri girin. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">-&quot;</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt; font-weight:700; font-style:italic;\">Hesapla</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">&quot; butonuna tıklayın. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">-Hesaplama sonucunda, kırıcı için gerekli güç ve kırıcı seçimi görüntülenecektir.</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Devam Et"))
        self.pushButton_2.setText(_translate("Dialog", "Hesapla"))
        self.pushButton_3.setText(_translate("Dialog", "Sıfırla"))
        self.textBrowser_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt; font-weight:700; text-decoration: underline;\">Kabuller</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:11pt; font-weight:700; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt;\">- Kırıcıdan çıkan malzemenin öngörülen kırma boyutundan daha iri malzeme miktarı </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt; font-weight:700; font-style:italic;\">0.14</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt;\"> kabul edilmiştir.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt;\">- Bond iş endeksi, genelde </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt; font-weight:700; font-style:italic;\">10-13 </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt;\">arasında olur. Burada </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt; font-weight:700; font-style:italic;\">12.5</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt;\"> olarak kabul edilmiştir.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt;\">- Emniyet katsayısı </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt; font-weight:700; font-style:italic;\">%20-25</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt;\"> arasında olmaktadır ve burada </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt; font-weight:700; font-style:italic;\">%25</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt;\"> olarak kabul edilmiştir.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt;\">- Horsepower (HP) değeri </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt; font-weight:700; font-style:italic;\">1.34 </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt;\">kabul edilmiştir.</span></p></body></html>"))
        self.label_24.setText(_translate("Dialog", "<html><head/><body><p>Tesisin saatlik kapasitesini girin (ton/saat):</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_KirmaPenceresi()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
