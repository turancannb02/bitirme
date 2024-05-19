# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sarsintili_Masa(object):
    def setupUi(self, Dialog, zenginlestirme_window=None):
        self.sarsintili_masa_window = Dialog
        if zenginlestirme_window is not None:
            self.zenginlestirme_window = zenginlestirme_window
        Dialog.setObjectName("Dialog")
        Dialog.resize(1014, 717)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(190, 250, 161, 21))
        self.label_2.setObjectName("label_2")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(610, 220, 21, 21))
        self.label_14.setTextFormat(QtCore.Qt.RichText)
        self.label_14.setObjectName("label_14")
        self.doubleSpinBox_10 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_10.setGeometry(QtCore.QRect(210, 310, 51, 21))
        self.doubleSpinBox_10.setObjectName("doubleSpinBox_10")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(190, 280, 171, 21))
        self.label_4.setObjectName("label_4")
        self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_8.setGeometry(QtCore.QRect(210, 220, 51, 21))
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(190, 370, 171, 21))
        self.label_10.setObjectName("label_10")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(270, 220, 21, 21))
        self.label_7.setTextFormat(QtCore.Qt.RichText)
        self.label_7.setObjectName("label_7")
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(390, 280, 71, 21))
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(270, 310, 21, 21))
        self.label_13.setTextFormat(QtCore.Qt.RichText)
        self.label_13.setObjectName("label_13")
        self.doubleSpinBox_11 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_11.setGeometry(QtCore.QRect(280, 310, 51, 21))
        self.doubleSpinBox_11.setObjectName("doubleSpinBox_11")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(390, 250, 71, 21))
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(200, 220, 21, 21))
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setObjectName("label_6")
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_5.setGeometry(QtCore.QRect(390, 370, 71, 21))
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(760, 220, 31, 21))
        self.label_16.setTextFormat(QtCore.Qt.RichText)
        self.label_16.setObjectName("label_16")
        self.doubleSpinBox_13 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_13.setGeometry(QtCore.QRect(690, 220, 61, 21))
        self.doubleSpinBox_13.setDecimals(3)
        self.doubleSpinBox_13.setObjectName("doubleSpinBox_13")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(600, 250, 161, 21))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(680, 220, 21, 21))
        self.label_18.setTextFormat(QtCore.Qt.RichText)
        self.label_18.setObjectName("label_18")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(200, 310, 21, 21))
        self.label_8.setTextFormat(QtCore.Qt.RichText)
        self.label_8.setObjectName("label_8")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(340, 220, 31, 21))
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 10, 1011, 61))
        self.label.setObjectName("label")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(340, 310, 31, 21))
        self.label_9.setTextFormat(QtCore.Qt.RichText)
        self.label_9.setObjectName("label_9")
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(600, 280, 171, 21))
        self.label_19.setObjectName("label_19")
        self.doubleSpinBox_12 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_12.setGeometry(QtCore.QRect(620, 220, 51, 21))
        self.doubleSpinBox_12.setObjectName("doubleSpinBox_12")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(390, 340, 71, 21))
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(190, 340, 161, 21))
        self.label_12.setObjectName("label_12")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(170, 300, 21, 41))
        self.label_11.setTextFormat(QtCore.Qt.RichText)
        self.label_11.setObjectName("label_11")
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_6.setGeometry(QtCore.QRect(810, 250, 71, 21))
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_7.setGeometry(QtCore.QRect(810, 280, 71, 21))
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(170, 210, 21, 41))
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setObjectName("label_3")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(580, 210, 21, 41))
        self.label_15.setTextFormat(QtCore.Qt.RichText)
        self.label_15.setObjectName("label_15")
        self.doubleSpinBox_9 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_9.setGeometry(QtCore.QRect(280, 220, 51, 21))
        self.doubleSpinBox_9.setObjectName("doubleSpinBox_9")
        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(600, 370, 171, 21))
        self.label_20.setObjectName("label_20")
        self.doubleSpinBox_14 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_14.setGeometry(QtCore.QRect(690, 310, 61, 21))
        self.doubleSpinBox_14.setDecimals(3)
        self.doubleSpinBox_14.setObjectName("doubleSpinBox_14")
        self.label_21 = QtWidgets.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(680, 310, 21, 21))
        self.label_21.setTextFormat(QtCore.Qt.RichText)
        self.label_21.setObjectName("label_21")
        self.doubleSpinBox_15 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_15.setGeometry(QtCore.QRect(810, 370, 71, 21))
        self.doubleSpinBox_15.setObjectName("doubleSpinBox_15")
        self.label_22 = QtWidgets.QLabel(Dialog)
        self.label_22.setGeometry(QtCore.QRect(600, 340, 161, 21))
        self.label_22.setObjectName("label_22")
        self.doubleSpinBox_16 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_16.setGeometry(QtCore.QRect(620, 310, 51, 21))
        self.doubleSpinBox_16.setObjectName("doubleSpinBox_16")
        self.label_23 = QtWidgets.QLabel(Dialog)
        self.label_23.setGeometry(QtCore.QRect(610, 310, 21, 21))
        self.label_23.setTextFormat(QtCore.Qt.RichText)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(Dialog)
        self.label_24.setGeometry(QtCore.QRect(760, 310, 31, 21))
        self.label_24.setTextFormat(QtCore.Qt.RichText)
        self.label_24.setObjectName("label_24")
        self.doubleSpinBox_17 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_17.setGeometry(QtCore.QRect(810, 340, 71, 21))
        self.doubleSpinBox_17.setObjectName("doubleSpinBox_17")
        self.label_25 = QtWidgets.QLabel(Dialog)
        self.label_25.setGeometry(QtCore.QRect(580, 300, 21, 41))
        self.label_25.setTextFormat(QtCore.Qt.RichText)
        self.label_25.setObjectName("label_25")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 600, 721, 32))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 640, 721, 32))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(170, 60, 711, 141))
        self.textBrowser.setObjectName("textBrowser")

        self.outputBox = QtWidgets.QTextBrowser(Dialog)
        self.outputBox.setGeometry(QtCore.QRect(330, 420, 401, 161))
        self.outputBox.setObjectName("outputBox")

        self.pushButton.clicked.connect(self.hesapla)
        self.pushButton.clicked.connect(self.kaydet)
        self.pushButton_2.clicked.connect(self.geri_don)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def hesapla(self):
        try:
        # Değerleri al
            vals_1 = [self.doubleSpinBox_8.value(), self.doubleSpinBox_9.value()]
            vals_2 = [self.doubleSpinBox_10.value(), self.doubleSpinBox_11.value()]
            vals_3 = [self.doubleSpinBox_12.value(), self.doubleSpinBox_13.value()]
            solid_feed = [self.doubleSpinBox_2.value(), self.doubleSpinBox_3.value(), self.doubleSpinBox_6.value()]
            table_capacity = [self.doubleSpinBox_4.value(), self.doubleSpinBox_5.value(), self.doubleSpinBox_7.value()]

            # Hesaplamaları yap
            machine_counts = [feed/capacity for feed, capacity in zip(solid_feed, table_capacity)]
            total_machines = sum(machine_counts)

            # Sonuçları string olarak formatla 
            introduction = (f"Proses tasarımında belirlendiği gibi 3 boyut grubu için ({'-'+str(vals_1[0])+'+'+str(vals_1[1])},  "
                            f"{'-'+str(vals_2[0])+'+'+str(vals_2[1])}, {'-'+str(vals_3[0])+'+'+str(vals_3[1])}) sarsıntılı masa "
                            "zenginleştirmesi uygulanacaktır. Hidrosizerda farklı boyut gruplarına ayrılan cevher doğrudan "
                            "sarsıntılı masalara beslenecektir.\n")
            results = [introduction]
            for i, (val_1, val_2, feed, capacity, machine_count) in enumerate(zip([vals_1[0], vals_2[0], vals_3[0]], 
                                                                                [vals_1[1], vals_2[1], vals_3[1]], 
                                                                                solid_feed, table_capacity, machine_counts)):
                result = (f"-{val_1}+{val_2} mm boyut aralığı için de çift katlı masa seçimi yapılmıştır.\n"
                        f"Katı beslemesi: {feed} ton/saat\n"
                        f"Masa kapasitesi: {capacity} ton/saat\n"
                        f"{feed} / {capacity} = {machine_count} adet masa gereklidir.\n")
                results.append(result)
            total_result = (f"Toplam {total_machines} adet masa gereklidir. Bu masaların gücü 2,2 kW, "
                            "boyut ölçüleri ise standart olarak 6800 mm uzunluğa, 2400 mm genişliğe, "
                            "2900 mm yüksekliğe sahiptir.")
            results.append(total_result)

            # Sonuçları 'outputBox'a yaz
            self.outputBox.setText('\n'.join(results))
        except Exception as e:
                print(f"Hesaplama sırasında bir hata oluştu: {e}")

    def geri_don(self):
        if hasattr(self, 'zenginlestirme_window'):
            self.zenginlestirme_window.show()
        self.sarsintili_masa_window.close()  # Close the Sarsintili

    def kaydet(self):
        try:
            dosya_ismi = "Sarsıntılı Masa Hesapları.txt" 
            with open(dosya_ismi, 'w') as f:
                f.write(self.outputBox.toPlainText())
        except Exception as e:
                print(f"Sonuçları dosyaya yazma sırasında bir hata oluştu: {e}")
                
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Katı Beslemesi (ton/saat) :"))
        self.label_14.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:12pt; font-weight:700;\">-</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p>Masa Kapasitesi (ton/saat):</p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p>Masa Kapasitesi (ton/saat):</p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:12pt; font-weight:700;\">+</span></p></body></html>"))
        self.label_13.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:12pt; font-weight:700;\">+</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:12pt; font-weight:700;\">-</span></p></body></html>"))
        self.label_16.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:700;\">mm</span></p></body></html>"))
        self.label_17.setText(_translate("Dialog", "Katı Beslemesi (ton/saat) :"))
        self.label_18.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:12pt; font-weight:700;\">+</span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:12pt; font-weight:700;\">-</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:700;\">mm</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">SARSINTILI MASA HESAPLAMALARI</span></p></body></html>"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:700;\">mm</span></p></body></html>"))
        self.label_19.setText(_translate("Dialog", "<html><head/><body><p>Masa Kapasitesi (ton/saat):</p></body></html>"))
        self.label_12.setText(_translate("Dialog", "Katı Beslemesi (ton/saat) :"))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:12pt; font-weight:700;\">4.2</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:12pt; font-weight:700;\">4.1</span></p></body></html>"))
        self.label_15.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:12pt; font-weight:700;\">4.3</span></p></body></html>"))
        self.label_20.setText(_translate("Dialog", "<html><head/><body><p>Masa Kapasitesi (ton/saat):</p></body></html>"))
        self.label_21.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:12pt; font-weight:700;\">+</span></p></body></html>"))
        self.label_22.setText(_translate("Dialog", "Katı Beslemesi (ton/saat) :"))
        self.label_23.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:12pt; font-weight:700;\">-</span></p></body></html>"))
        self.label_24.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:700;\">mm</span></p></body></html>"))
        self.label_25.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:12pt; font-weight:700;\">4.4</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Hesapla"))
        self.pushButton_2.setText(_translate("Dialog", "Geri Dön"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sarsıntılı masa, mineral zenginleştirmede kullanılan bir tür ayırma cihazıdır. Sallantılı masa, eğimli bir yüzeye sahip bir tabladan oluşur. Tabla, bir motor tarafından ileri geri hareket ettirilir. Tablaya beslenen mineraller, eğim ve hareket nedeniyle farklı hızlarda hareket eder. Ağır mineraller, daha yavaş hareket eder ve tablanın alt kısmında toplanır. Hafif mineraller, daha hızlı hareket eder ve tablanın üst kısmında toplanır. Sallantılı masa, altın, gümüş, bakır ve diğer minerallerin zenginleştirilmesinde kullanılır. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Bu program, sallantılı masa ile mineral zenginleştirme için gerekli parametreleri hesaplamak için tasarlanmıştır. Kullanıcı, katı beslemesi, besleme aralığı, masa kapasitesi ve eğim açısını girerek, program gerekli parametreleri hesaplayacaktır.</p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Sarsintili_Masa()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
