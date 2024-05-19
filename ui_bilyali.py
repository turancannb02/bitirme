# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BilyaliDegirmen(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(986, 763)
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(750, 290, 111, 22))
        self.spinBox_2.setMouseTracking(True)
        self.spinBox_2.setMaximum(999999999)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(100, 350, 381, 21))
        self.label_17.setObjectName("label_17")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(100, 320, 401, 21))
        self.label_16.setObjectName("label_16")
        self.spinBox_14 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_14.setGeometry(QtCore.QRect(750, 380, 111, 22))
        self.spinBox_14.setMouseTracking(True)
        self.spinBox_14.setMaximum(999999999)
        self.spinBox_14.setObjectName("spinBox_14")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(100, 290, 431, 21))
        self.label_10.setObjectName("label_10")
        self.spinBox_7 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_7.setGeometry(QtCore.QRect(750, 350, 111, 22))
        self.spinBox_7.setMouseTracking(True)
        self.spinBox_7.setMaximum(999999999)
        self.spinBox_7.setObjectName("spinBox_7")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 1011, 61))
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(750, 260, 111, 22))
        self.spinBox.setMouseTracking(True)
        self.spinBox.setMaximum(999999999)
        self.spinBox.setObjectName("spinBox")
        self.label_25 = QtWidgets.QLabel(Dialog)
        self.label_25.setGeometry(QtCore.QRect(100, 380, 271, 21))
        self.label_25.setObjectName("label_25")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(100, 260, 431, 21))
        self.label_9.setObjectName("label_9")
        self.spinBox_6 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_6.setGeometry(QtCore.QRect(750, 320, 111, 22))
        self.spinBox_6.setMouseTracking(True)
        self.spinBox_6.setMaximum(999999999)
        self.spinBox_6.setObjectName("spinBox_6")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(100, 90, 761, 151))
        self.textBrowser.setObjectName("textBrowser")
        self.outputBox = QtWidgets.QTextBrowser(Dialog)
        self.outputBox.setGeometry(QtCore.QRect(390, 430, 481, 221))
        self.outputBox.setObjectName("outputBox")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(580, 690, 111, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 690, 111, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 690, 100, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(100, 430, 271, 221))
        self.textBrowser_3.setObjectName("textBrowser_3")

        #self.pushButton.clicked.connect(self.devam_et) 
        self.pushButton_2.clicked.connect(self.calculate_results)
        self.pushButton_2.clicked.connect(self.kaydet)
        self.pushButton_3.clicked.connect(self.reset_values)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def calculate_results(self):
        try:
            self.outputBox.clear()
            bilyali_degirmen_besleme = self.spinBox.value()
            bilyali_degirmen_cikis = self.spinBox_2.value()
            deger_1 = bilyali_degirmen_besleme / 1000
            deger_2 = bilyali_degirmen_cikis / 1000
            self.outputBox.insertPlainText(f"Çubuklu değirmen ünitesi, kırma tesisinden gelen –{round(deger_1)} mm'lik malzemeyi -{round(deger_2)} mm'e indirmek için konulmuştur.\n")

            saatlik_kapasite = self.spinBox_14.value()

            self.outputBox.insertPlainText(f"Çubuklu Değirmene besleme = -{round(bilyali_degirmen_besleme)} mikron\n"
                                           f"Çubuklu değirmen çıkışı = -{round(bilyali_degirmen_cikis)} mikron olur.\n")
            
            bko = bilyali_degirmen_besleme / bilyali_degirmen_cikis
            self.outputBox.insertPlainText(f"Boyut Küçültme Oranı (BKO) = {round(bko)} Rr olarak bulunmuştur.\n")

            Wi = 12.5 # Kabul

            d1 = self.spinBox_6.value()
            d2 = self.spinBox_7.value()
            self.outputBox.insertPlainText(f"D1 (beslenen malzemenin %80‟nin geçtiği boyut): {round(d1)} mikron\n"
                                           f"D2 (çıkan malzemenin %80‟nin geçtiği boyut): {round(2)} mikron olur.\n")

            Wt = 10 * Wi * ((1 / (d2 ** 0.5)) - (1 / (d1 ** 0.5)))
            self.outputBox.insertPlainText(f"Güç hesabı sonucu {round(Wt)} kWh/t olarak bulunur.\n")
            

            horse_power = 1.341 # Kabul 
            Wt_2 = Wt * horse_power 
            self.outputBox.insertPlainText(f"Horsepower (HP) güç düzeltilmesi güç hesabına eklenirse Wt = {round(Wt_2)} HP/ton olarak bulunur.\n")

            horse_power_2 = Wt_2 * saatlik_kapasite * 1.15
            self.outputBox.insertPlainText(f"Bulunan bu değer ton başına bulunan değerdir anca değirmene saatte {round(saatlik_kapasite)} ton cevher beslemesi yapılmaktadır; {horse_power_2} HP\n")

            ef3 = 0.94 # Kabul
            self.outputBox.insertPlainText(f"Belirli malzeme şarjı ön görüldüğünde değirmen güç kataloğundan 753 HP gücüne sahip değirmen 3,35 metre çapa, 3,35 uzunluğa sahiptir\n"
                                           f"L ve D değerleri bulunduğundan EF3 = {round(ef3)} faktörleri hesaplanır.\n")

            Wt_3 = horse_power_2 * ef3 
            self.outputBox.insertPlainText(f"Hesap edilen düzeltme faktörleri güç hesabına dahil edilir ve {round(Wt_3)} HP bulunur.\n")

            guc_duzeltme_faktor = Wt_3 / 753
            self.outputBox.insertPlainText(f"Güç Düzeltme Faktörü = {round(guc_duzeltme_faktor)} olarak bulunur.\n")

            L_2 = 3.35 * guc_duzeltme_faktor
            self.outputBox.insertPlainText(f"Bilyalı değirmenlerde güç ile boyunun doğru orantılı olarak arttığı kabul edildiğinde;\n"
                                           f"Nihai değirmen boyu {round(L_2)} metre olarak bulunur.\n")

            B = (bilyali_degirmen_besleme**0.75 / 350) * ((Wi * 2.7 / (0.67 * (3.281 * 3.05)**0.5))**(1/3)) * 25.4
            self.outputBox.insertPlainText(f"Bilya çapı {round(B)} mm olarak bulunur.\n")
        except Exception as e:
                print(f"Hesaplama sırasında bir hata oluştu: {e}")

    def kaydet(self):
        try:
                dosya_ismi = "Bilyalı Değirmen Hesapaları.txt" 
                with open(dosya_ismi, 'w') as f:
                        f.write(self.outputBox.toPlainText())
        except Exception as e:
                print(f"Sonuçları dosyaya yazma sırasında bir hata oluştu: {e}")
                
    def reset_values(self):
            self.spinBox.setValue(0)
            self.spinBox_2.setValue(0)
            self.spinBox_6.setValue(0)
            self.spinBox_7.setValue(0)
            self.spinBox_14.setValue(0)
            self.retranslateUi(Dialog)
            QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Biyalı Değirmen Hesapları"))
        self.label_17.setText(_translate("Dialog", "<html><head/><body><p>D1 : Kırıcıdan çıkan malzemenin d80\'i giriniz (mikron):</p></body></html>"))
        self.label_16.setText(_translate("Dialog", "<html><head/><body><p>D1 : Kırıcıya beslenen malzemenin d80\'i giriniz (mikron):</p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p>Bilyalı Değirmenden çıkan malzeme miktarını giriniz (mikron):</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">BİLYALI DEĞİRMEN HESAPLARI</span></p></body></html>"))
        self.label_25.setText(_translate("Dialog", "<html><head/><body><p>Tesisin saatlik kapasitesini giriniz:</p></body></html>"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p>Bilyalı Değirmene beslenen malzeme miktarını giriniz (mikron):</p></body></html>"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:10pt; color:#1f1f1f; background-color:#ffffff;\">Biyalı değirmenler, iki dönen bilyeden oluşan bir öğütücü tipleridir. Bilyalar, malzemeyi öğütmek için birbirine çarparlar. Biyalı değirmenler, sert malzemeleri öğütmek için kullanılır.</span></p>\n"
"<p style=\" margin-top:24px; margin-bottom:24px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:10pt; color:#1f1f1f; background-color:#ffffff;\">Bu program, bilyalı değirmenler için kapasite hesaplamalarını yapmak için kullanılabilir. Program, öncelikle öğütücü tipini seçmenizi, ardından malzemenin boyutunu ve nem içeriğini girmeniz ve son olarak öğütücü hızını ve öğütme oranını seçmenizi ister. </span></p>\n"
"<p style=\" margin-top:24px; margin-bottom:24px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:10pt; color:#1f1f1f; background-color:#ffffff;\">Program, bu bilgileri kullanarak malzemeyi öğütmek için gereken kapasiteyi hesaplayacaktır. Hesaplanan kapasite, ton/h olarak belirtilecektir.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:24px; margin-bottom:24px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:10pt; color:#1f1f1f; background-color:#ffffff;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Devam Et"))
        self.pushButton_3.setText(_translate("Dialog", "Sıfırla"))
        self.pushButton_2.setText(_translate("Dialog", "Hesapla"))
        self.textBrowser_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt; font-weight:700; text-decoration: underline;\">Kabuller</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:10pt; font-weight:700; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\';\">- Bond iş endeksi, genelde </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-weight:700; font-style:italic;\">10-13 </span><span style=\" font-family:\'.AppleSystemUIFont\';\">arasında olur. Burada </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-weight:700; font-style:italic;\">12.5</span><span style=\" font-family:\'.AppleSystemUIFont\';\"> olarak kabul edilmiştir.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\';\">- Emniyet katsayısı </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-weight:700; font-style:italic;\">%20-25</span><span style=\" font-family:\'.AppleSystemUIFont\';\"> arasında olmaktadır ve burada </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-weight:700; font-style:italic;\">%25</span><span style=\" font-family:\'.AppleSystemUIFont\';\"> olarak kabul edilmiştir.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\';\">- Horsepower (HP) değeri </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-weight:700; font-style:italic;\">1.34 </span><span style=\" font-family:\'.AppleSystemUIFont\';\">kabul edilmiştir.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\';\">- Kritik hız </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-weight:700; font-style:italic;\">0.72</span><span style=\" font-family:\'.AppleSystemUIFont\';\"> kabul edilmiştir.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\';\">- Astarlı değirmen çapı </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-weight:700; font-style:italic;\">3.17</span><span style=\" font-family:\'.AppleSystemUIFont\';\"> olarak kabul edilmiştir.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_BilyaliDegirmen()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
