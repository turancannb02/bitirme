# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Bant(object):
    def __init__(self):
        self.tablo = {
            300: 0.004527,
            400: 0.009144,
            500: 0.015369,
            650: 0.027692,
            800: 0.043639,
            1000: 0.070519,
            1200: 0.103654,
            1400: 0.143262,
        }
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1316, 762)
        self.label_31 = QtWidgets.QLabel(Dialog)
        self.label_31.setGeometry(QtCore.QRect(750, 430, 231, 21))
        self.label_31.setObjectName("label_31")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setGeometry(QtCore.QRect(630, 310, 62, 22))
        self.doubleSpinBox.setMouseTracking(True)
        self.doubleSpinBox.setMaximum(99999999.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.spinBox_4 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_4.setGeometry(QtCore.QRect(630, 400, 61, 22))
        self.spinBox_4.setMouseTracking(True)
        self.spinBox_4.setMaximum(9999999)
        self.spinBox_4.setObjectName("spinBox_4")
        self.label_28 = QtWidgets.QLabel(Dialog)
        self.label_28.setGeometry(QtCore.QRect(750, 340, 211, 21))
        self.label_28.setObjectName("label_28")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(750, 400, 221, 21))
        self.label_12.setObjectName("label_12")
        self.spinBox_3 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_3.setGeometry(QtCore.QRect(1210, 370, 61, 22))
        self.spinBox_3.setMouseTracking(True)
        self.spinBox_3.setMaximum(9999999)
        self.spinBox_3.setObjectName("spinBox_3")
        self.label_24 = QtWidgets.QLabel(Dialog)
        self.label_24.setGeometry(QtCore.QRect(160, 340, 231, 21))
        self.label_24.setObjectName("label_24")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(-70, 30, 1441, 51))
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label_30 = QtWidgets.QLabel(Dialog)
        self.label_30.setGeometry(QtCore.QRect(750, 460, 291, 21))
        self.label_30.setObjectName("label_30")
        self.spinBox_14 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_14.setGeometry(QtCore.QRect(630, 460, 61, 22))
        self.spinBox_14.setMouseTracking(True)
        self.spinBox_14.setMaximum(9999999)
        self.spinBox_14.setObjectName("spinBox_14")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(150, 260, 251, 41))
        self.label_8.setTextFormat(QtCore.Qt.RichText)
        self.label_8.setObjectName("label_8")
        self.spinBox_16 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_16.setGeometry(QtCore.QRect(1210, 430, 61, 22))
        self.spinBox_16.setMouseTracking(True)
        self.spinBox_16.setMaximum(24)
        self.spinBox_16.setObjectName("spinBox_16")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(130, 100, 641, 121))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(840, 100, 331, 121))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(630, 370, 61, 22))
        self.spinBox_2.setMouseTracking(True)
        self.spinBox_2.setMaximum(9999999)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_13 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_13.setGeometry(QtCore.QRect(630, 430, 61, 22))
        self.spinBox_13.setMouseTracking(True)
        self.spinBox_13.setMaximum(24)
        self.spinBox_13.setObjectName("spinBox_13")
        self.label_26 = QtWidgets.QLabel(Dialog)
        self.label_26.setGeometry(QtCore.QRect(160, 300, 251, 41))
        self.label_26.setTextFormat(QtCore.Qt.RichText)
        self.label_26.setObjectName("label_26")
        self.label_25 = QtWidgets.QLabel(Dialog)
        self.label_25.setGeometry(QtCore.QRect(160, 460, 291, 21))
        self.label_25.setObjectName("label_25")
        self.spinBox_6 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_6.setGeometry(QtCore.QRect(1210, 340, 61, 22))
        self.spinBox_6.setMouseTracking(True)
        self.spinBox_6.setMaximum(360)
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_15 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_15.setGeometry(QtCore.QRect(1210, 460, 61, 22))
        self.spinBox_15.setMouseTracking(True)
        self.spinBox_15.setMaximum(9999999)
        self.spinBox_15.setObjectName("spinBox_15")
        self.label_27 = QtWidgets.QLabel(Dialog)
        self.label_27.setGeometry(QtCore.QRect(160, 430, 231, 21))
        self.label_27.setObjectName("label_27")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(740, 260, 251, 41))
        self.label_11.setTextFormat(QtCore.Qt.RichText)
        self.label_11.setObjectName("label_11")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(1210, 310, 62, 22))
        self.doubleSpinBox_2.setMouseTracking(True)
        self.doubleSpinBox_2.setMaximum(99999999.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(630, 340, 61, 22))
        self.spinBox.setMouseTracking(True)
        self.spinBox.setMaximum(360)
        self.spinBox.setObjectName("spinBox")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 700, 111, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(160, 400, 321, 21))
        self.label_9.setObjectName("label_9")
        self.label_29 = QtWidgets.QLabel(Dialog)
        self.label_29.setGeometry(QtCore.QRect(750, 300, 251, 41))
        self.label_29.setTextFormat(QtCore.Qt.RichText)
        self.label_29.setObjectName("label_29")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(160, 370, 441, 21))
        self.label_10.setObjectName("label_10")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(750, 370, 441, 21))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(700, 260, 41, 41))
        self.label_14.setTextFormat(QtCore.Qt.RichText)
        self.label_14.setObjectName("label_14")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(690, 700, 100, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(110, 260, 31, 41))
        self.label_7.setTextFormat(QtCore.Qt.RichText)
        self.label_7.setObjectName("label_7")
        self.spinBox_5 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_5.setGeometry(QtCore.QRect(1210, 400, 61, 22))
        self.spinBox_5.setMouseTracking(True)
        self.spinBox_5.setMaximum(9999999)
        self.spinBox_5.setObjectName("spinBox_5")

        self.outputBox = QtWidgets.QTextBrowser(Dialog)
        self.outputBox.setGeometry(QtCore.QRect(480, 510, 391, 181))
        self.outputBox.setObjectName("outputBox")

        self.pushButton_2.clicked.connect(self.hesapla_fonksiyonu)
        self.pushButton_2.clicked.connect(self.kaydet)
        self.pushButton_3.clicked.connect(self.reset_values)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def hesapla_fonksiyonu(self):
        #Yatay Bant
        Q = self.doubleSpinBox.value()
        V = self.spinBox.value()
        P = self.spinBox_2.value()
        F = ((Q) / (3600 * V * P))
        self.F = round(F, 2)  # Store the calculated F value
        self.outputBox.insertPlainText(f"Yatay Bant Hesabı\n"
                                       f"Bant kesit alanı {round(self.F)} m2 olarak bulunur.\n")

        tablo_keys = sorted(list(self.tablo.keys()))
        for i in range(len(tablo_keys) - 1):
            if tablo_keys[i] <= self.F < tablo_keys[i+1]:
                bant_genisligi = self.tablo[tablo_keys[i]]
                break
        else:
            bant_genisligi = self.tablo[tablo_keys[-1]]
        
        self.outputBox.insertPlainText(f"Bant genişliği yaklaşık olarak {round(bant_genisligi)} mm bulunur.\n")

        #N1
        q = self.spinBox_4.value()
        L = self.spinBox_13.value()
        M = self.spinBox_14.value()
        N1 = ((q * L * M * V) / 75)
        self.outputBox.insertPlainText(f"Toplam bant gücünü bulmak N1, N2 ve N3 güç faktörlerinin bulunması gerekmektedir.\n"
                                       f"N1 güç eşitliği  {round(N1)} HP bulunur.\n")
        
        #N2
        N2 = ((Q * L * M) / 270)
        self.outputBox.insertPlainText(f"N2 güç eşitliği  {round(N2)} HP bulunur.\n")

        toplam = N1 + N2
        self.outputBox.insertPlainText(f"N3 güç faktörü bant yatay olduğu için sıfır olarak alınacaktır.\n"
                                       f"Buna göre toplam bant gücü {round(toplam)} HP olarak bulunmuştır.\n"
                                       f"Bunu 1.2 güvenlik katsayısı ile çarptığımızda gerekli olan güç {round(toplam*1.2)} HP olarak bulunacaktır.\n\n")
                                       
        #Eğimli Bant
        Q1 = self.doubleSpinBox_2.value()
        V1 = self.spinBox_6.value()
        P1 = self.spinBox_3.value()
        F1 = ((Q1) / (3600 * V1 * P1))
        self.F1 = round(F1, 2)  # Store the calculated F value
        self.outputBox.insertPlainText(f"Eğimli Bant Hesabı\n"
                                       f"Bant kesit alanı {round(self.F1)} m2 olarak bulunur.\n")

        tablo_keys = sorted(list(self.tablo.keys()))
        for i in range(len(tablo_keys) - 1):
            if tablo_keys[i] <= self.F < tablo_keys[i+1]:
                bant_genisligi1 = self.tablo[tablo_keys[i]]
                break
        else:
            bant_genisligi1 = self.tablo[tablo_keys[-1]]
        
        self.outputBox.insertPlainText(f"Bant genişliği yaklaşık olarak {round(bant_genisligi1)} mm bulunur.\n")

        #N1_2
        q1 = self.spinBox_5.value()
        L1= self.spinBox_16.value()
        M1 = self.spinBox_15.value()
        N1_2 = ((q1 * L1 * M1 * V1) / 75)
        self.outputBox.insertPlainText(f"Toplam bant gücünü bulmak N1, N2 ve N3 güç faktörlerinin bulunması gerekmektedir.\n"
                                       f"N1 güç eşitliği  {round(N1_2)} HP bulunur.\n")
        
        #N2
        N2_2 = ((Q1 * L1* M1) / 270)
        self.outputBox.insertPlainText(f"N2 güç eşitliği  {round(N2_2)} HP bulunur.\n")


        #N3
        N3 = ((Q1 * 15) / 270)
        toplam1 = N1_2 + N2_2 + N3

        self.outputBox.insertPlainText(f"N3 güç eşitliği  {round(N3)} HP bulunur.\n"
                                       f"Buna göre toplam bant gücü {round(toplam1)} HP olarak bulunmuştır.\n"
                                       f"Bunu 1.2 güvenlik katsayısı ile çarptığımızda gerekli olan güç {round(toplam1*1.2)} HP olarak bulunacaktır.")


                   



    def kaydet(self):
        dosya_ismi = "Bant Konveyör Hesapaları.txt" 
        with open(dosya_ismi, 'w') as f:
            f.write(self.outputBox.toPlainText())

    def reset_values(self):
        self.doubleSpinBox.setValue(0)
        self.doubleSpinBox_2.setValue(0)
        self.spinBox.setValue(0)
        self.spinBox_2.setValue(0)
        self.spinBox_3.setValue(0)
        self.spinBox_4.setValue(0)
        self.spinBox_5.setValue(0)
        self.spinBox_6.setValue(0)
        self.spinBox_13.setValue(0)
        self.spinBox_14.setValue(0)
        self.spinBox_15.setValue(0)
        self.spinBox_16.setValue(0)
 
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Bant Konveyör Hesaplamaları"))
        self.label_31.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Bant uzunluğunu giriniz (m):</span></p></body></html>"))
        self.label_28.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Bant hızını giriniz (m/sn):</span></p></body></html>"))
        self.label_12.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">1 metre bantın ağırlığını giriniz (kg/m):</span></p></body></html>"))
        self.label_24.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Bant hızını giriniz (m/sn):</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">STOK HESAPLAMALARI - BANT KONVEYÖR HESAPLARI</span></p></body></html>"))
        self.label_30.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Tesisin saatlik kapasitesini giriniz: </span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:12pt; font-weight:700;\">Yatay Bantlar Hesabı</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:12pt; font-weight:700; text-decoration: underline; text-decoration-color:#000000; color:#1f1f1f; background-color:#ffffff;\">Bant Konveyör Hesaplamaları </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:12pt; font-weight:700; text-decoration: underline; text-decoration-color:#000000; color:#1f1f1f;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:11pt; color:#1f1f1f; background-color:#ffffff;\">Bu program, yatay ve eğimli bant konveyörler için kapasite hesaplamalarını yapmak için kullanılabilir. Program, öncelikle bant uzunluğunu, bant hızını, taşınacak malzemenin bulk yoğunluğunu ve bantın ağırlığını girmeniz ister. Program, bu bilgileri kullanarak bantın kapasitesini hesaplayacaktır. Hesaplanan kapasite, ton/saat olarak belirtilecektir. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:11pt; color:#1f1f1f;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:12pt; font-weight:700; text-decoration: underline; text-decoration-color:#000000; color:#1f1f1f; background-color:#ffffff;\">Yatay Bantlar </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:12pt; font-weight:700; text-decoration: underline; text-decoration-color:#000000; color:#1f1f1f;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:11pt; color:#1f1f1f; background-color:#ffffff;\">Yatay bantlar, malzemeleri düz bir yüzeyde taşımak için kullanılır. Yatay bantların kapasitesi, bant uzunluğu, bant hızı ve taşınacak malzemenin bulk yoğunluğuna bağlıdır. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:12pt; color:#1f1f1f;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:12pt; font-weight:700; text-decoration: underline; text-decoration-color:#000000; color:#1f1f1f; background-color:#ffffff;\">Eğimli Bantlar </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:12pt; font-weight:700; text-decoration: underline; text-decoration-color:#000000; color:#1f1f1f;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:11pt; color:#1f1f1f; background-color:#ffffff;\">Eğimli bantlar, malzemeleri bir eğim boyunca taşımak için kullanılır. Eğimli bantların kapasitesi, bant uzunluğu, bant hızı, taşınacak malzemenin bulk yoğunluğu ve eğim açısına bağlıdır. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:12pt; color:#1f1f1f;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:12pt; font-weight:700; text-decoration: underline; text-decoration-color:#000000; color:#1f1f1f; background-color:#ffffff;\">Programın Kullanımı </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:12pt; font-weight:700; text-decoration: underline; text-decoration-color:#000000; color:#1f1f1f;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Google Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:11pt; color:#1f1f1f; background-color:#ffffff;\">Programı kullanmak için, öncelikle yatay veya eğimli bant seçmeniz gerekir. Ardından, bant uzunluğunu, bant hızını, taşınacak malzemenin bulk yoğunluğunu ve bantın ağırlığını girmeniz gerekir. Program, bu bilgileri kullanarak bantın kapasitesini hesaplayacaktır. Hesaplanan kapasite, ton/saat olarak belirtilecektir.</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:12pt; font-weight:700; text-decoration: underline;\">Kabuller</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:12pt; font-weight:700; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">- </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt; font-weight:700;\">N1 Gücü:</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\"> Yatay durumdaki boş bantın hareket ettirilmesi için gerekli olan güç. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">- </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt; font-weight:700;\">N2 Gücü:</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\"> Bant üzerindeki malzemenin hareket ettirilmesi için gerekli olan güç. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">- </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt; font-weight:700;\">N3 Gücü: </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">Bantın eğimli olması durumunda kot farkı dolayısıyla gerekli olan ek güç.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">- Bant genişlik değerleri bant kesit alanları tablosundan çekilmiştir ve en yakın değeri vermektedir.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">- Güvenlik katsayısı </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt; font-weight:700; font-style:italic;\">%20</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\"> seçilmiştir.</span></p></body></html>"))
        self.label_26.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Kapasite giriniz (ton/saat):</span></p></body></html>"))
        self.label_25.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Tesisin saatlik kapasitesini giriniz: </span></p></body></html>"))
        self.label_27.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Bant uzunluğunu giriniz (m):</span></p></body></html>"))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:12pt; font-weight:700;\">Eğimli Bantlar Hesabı</span></p></body></html>"))
        self.pushButton_3.setText(_translate("Dialog", "Sıfırla"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">1 metre bantın ağırlığını giriniz (kg/m):</span></p></body></html>"))
        self.label_29.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Kapasite giriniz (ton/saat):</span></p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Taşınacak malzemenin bulk yoğunluğunu giriniz (ton/m3):</span></p></body></html>"))
        self.label_13.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Taşınacak malzemenin bulk yoğunluğunu giriniz (ton/m3):</span></p></body></html>"))
        self.label_14.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:14pt; font-weight:700;\">1.2</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", "Hesapla"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:14pt; font-weight:700;\">1.1</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Bant()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
