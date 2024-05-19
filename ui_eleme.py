# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import math


class Ui_ElemePenceresi(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1440, 763)
        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(610, 310, 241, 21))
        self.label_20.setObjectName("label_20")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(70, 250, 351, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(70, 280, 241, 21))
        self.label_11.setObjectName("label_11")
        self.spinBox_16 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_16.setGeometry(QtCore.QRect(980, 370, 61, 21))
        self.spinBox_16.setMouseTracking(True)
        self.spinBox_16.setMaximum(1000000000)
        self.spinBox_16.setObjectName("spinBox_16")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(130, 150, 291, 41))
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setObjectName("label_5")
        self.spinBox_17 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_17.setGeometry(QtCore.QRect(980, 340, 61, 21))
        self.spinBox_17.setMouseTracking(True)
        self.spinBox_17.setMaximum(1000000000)
        self.spinBox_17.setObjectName("spinBox_17")
        self.spinBox_3 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_3.setGeometry(QtCore.QRect(440, 220, 71, 22))
        self.spinBox_3.setMouseTracking(True)
        self.spinBox_3.setMaximum(100)
        self.spinBox_3.setObjectName("spinBox_3")
        self.label_21 = QtWidgets.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(610, 340, 271, 21))
        self.label_21.setObjectName("label_21")
        self.spinBox_10 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_10.setGeometry(QtCore.QRect(980, 250, 61, 21))
        self.spinBox_10.setMouseTracking(True)
        self.spinBox_10.setMaximum(1000000000)
        self.spinBox_10.setObjectName("spinBox_10")
        self.spinBox_13 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_13.setGeometry(QtCore.QRect(440, 310, 71, 21))
        self.spinBox_13.setMouseTracking(True)
        self.spinBox_13.setMaximum(1000000000)
        self.spinBox_13.setObjectName("spinBox_13")
        self.spinBox_5 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_5.setGeometry(QtCore.QRect(980, 190, 61, 22))
        self.spinBox_5.setMouseTracking(True)
        self.spinBox_5.setMaximum(1000000)
        self.spinBox_5.setObjectName("spinBox_5")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(610, 280, 241, 21))
        self.label_12.setObjectName("label_12")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(440, 280, 71, 21))
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.spinBox_18 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_18.setGeometry(QtCore.QRect(980, 310, 61, 21))
        self.spinBox_18.setMouseTracking(True)
        self.spinBox_18.setMaximum(1000000000)
        self.spinBox_18.setObjectName("spinBox_18")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(610, 190, 281, 21))
        self.label_13.setObjectName("label_13")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setGeometry(QtCore.QRect(440, 250, 71, 21))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 150, 31, 41))
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(580, 150, 31, 41))
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setObjectName("label_6")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(70, 370, 211, 21))
        self.label_18.setObjectName("label_18")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(440, 190, 71, 21))
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1441, 71))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 220, 351, 21))
        self.label_4.setObjectName("label_4")
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(70, 160, 51, 22))
        self.spinBox_2.setMouseTracking(True)
        self.spinBox_2.setMaximum(1000000)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 190, 291, 21))
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(670, 150, 281, 41))
        self.label_8.setTextFormat(QtCore.Qt.RichText)
        self.label_8.setObjectName("label_8")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(70, 340, 271, 21))
        self.label_17.setObjectName("label_17")
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(610, 370, 211, 21))
        self.label_19.setObjectName("label_19")
        self.spinBox_11 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_11.setGeometry(QtCore.QRect(980, 280, 61, 21))
        self.spinBox_11.setMouseTracking(True)
        self.spinBox_11.setMaximum(1000000000)
        self.spinBox_11.setObjectName("spinBox_11")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(610, 250, 221, 21))
        self.label_15.setObjectName("label_15")
        self.spinBox_4 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_4.setGeometry(QtCore.QRect(610, 160, 51, 22))
        self.spinBox_4.setMouseTracking(True)
        self.spinBox_4.setMaximum(1000000)
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_14 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_14.setGeometry(QtCore.QRect(440, 340, 71, 21))
        self.spinBox_14.setMouseTracking(True)
        self.spinBox_14.setMaximum(1000000000)
        self.spinBox_14.setObjectName("spinBox_14")
        self.spinBox_15 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_15.setGeometry(QtCore.QRect(440, 370, 71, 21))
        self.spinBox_15.setMouseTracking(True)
        self.spinBox_15.setMaximum(1000000000)
        self.spinBox_15.setObjectName("spinBox_15")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(610, 220, 351, 21))
        self.label_14.setObjectName("label_14")
        self.spinBox_12 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_12.setGeometry(QtCore.QRect(980, 220, 61, 22))
        self.spinBox_12.setMouseTracking(True)
        self.spinBox_12.setMaximum(100)
        self.spinBox_12.setObjectName("spinBox_12")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(70, 310, 241, 21))
        self.label_16.setObjectName("label_16")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(50, 400, 351, 41))
        self.label_7.setTextFormat(QtCore.Qt.RichText)
        self.label_7.setObjectName("label_7")
        self.label_22 = QtWidgets.QLabel(Dialog)
        self.label_22.setGeometry(QtCore.QRect(80, 440, 261, 21))
        self.label_22.setObjectName("label_22")
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(440, 440, 71, 21))
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.label_23 = QtWidgets.QLabel(Dialog)
        self.label_23.setGeometry(QtCore.QRect(80, 470, 261, 21))
        self.label_23.setObjectName("label_23")
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_5.setGeometry(QtCore.QRect(440, 470, 71, 21))
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.label_24 = QtWidgets.QLabel(Dialog)
        self.label_24.setGeometry(QtCore.QRect(80, 500, 311, 21))
        self.label_24.setObjectName("label_24")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(430, 500, 91, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(430, 530, 91, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_25 = QtWidgets.QLabel(Dialog)
        self.label_25.setGeometry(QtCore.QRect(80, 530, 311, 21))
        self.label_25.setObjectName("label_25")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(430, 560, 91, 21))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_26 = QtWidgets.QLabel(Dialog)
        self.label_26.setGeometry(QtCore.QRect(80, 560, 311, 21))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(Dialog)
        self.label_27.setGeometry(QtCore.QRect(80, 590, 261, 21))
        self.label_27.setObjectName("label_27")
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_6.setGeometry(QtCore.QRect(440, 590, 71, 21))
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.comboBox_4 = QtWidgets.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(430, 620, 91, 21))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_28 = QtWidgets.QLabel(Dialog)
        self.label_28.setGeometry(QtCore.QRect(80, 620, 311, 21))
        self.label_28.setObjectName("label_28")
        self.comboBox_5 = QtWidgets.QComboBox(Dialog)
        self.comboBox_5.setGeometry(QtCore.QRect(430, 650, 91, 21))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.label_29 = QtWidgets.QLabel(Dialog)
        self.label_29.setGeometry(QtCore.QRect(80, 650, 311, 21))
        self.label_29.setObjectName("label_29")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(580, 410, 351, 41))
        self.label_9.setTextFormat(QtCore.Qt.RichText)
        self.label_9.setObjectName("label_9")
        self.comboBox_6 = QtWidgets.QComboBox(Dialog)
        self.comboBox_6.setGeometry(QtCore.QRect(960, 570, 91, 21))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.label_30 = QtWidgets.QLabel(Dialog)
        self.label_30.setGeometry(QtCore.QRect(610, 450, 261, 21))
        self.label_30.setObjectName("label_30")
        self.comboBox_7 = QtWidgets.QComboBox(Dialog)
        self.comboBox_7.setGeometry(QtCore.QRect(960, 540, 91, 21))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.label_31 = QtWidgets.QLabel(Dialog)
        self.label_31.setGeometry(QtCore.QRect(610, 480, 261, 21))
        self.label_31.setObjectName("label_31")
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_7.setGeometry(QtCore.QRect(970, 450, 71, 21))
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.comboBox_8 = QtWidgets.QComboBox(Dialog)
        self.comboBox_8.setGeometry(QtCore.QRect(960, 510, 91, 21))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_8.setGeometry(QtCore.QRect(970, 600, 71, 21))
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.comboBox_9 = QtWidgets.QComboBox(Dialog)
        self.comboBox_9.setGeometry(QtCore.QRect(960, 660, 91, 21))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_10 = QtWidgets.QComboBox(Dialog)
        self.comboBox_10.setGeometry(QtCore.QRect(960, 630, 91, 21))
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.label_32 = QtWidgets.QLabel(Dialog)
        self.label_32.setGeometry(QtCore.QRect(610, 510, 311, 21))
        self.label_32.setObjectName("label_32")
        self.doubleSpinBox_9 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_9.setGeometry(QtCore.QRect(970, 480, 71, 21))
        self.doubleSpinBox_9.setObjectName("doubleSpinBox_9")
        self.label_33 = QtWidgets.QLabel(Dialog)
        self.label_33.setGeometry(QtCore.QRect(610, 630, 311, 21))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(Dialog)
        self.label_34.setGeometry(QtCore.QRect(610, 660, 311, 21))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(Dialog)
        self.label_35.setGeometry(QtCore.QRect(610, 600, 261, 21))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(Dialog)
        self.label_36.setGeometry(QtCore.QRect(610, 570, 311, 21))
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(Dialog)
        self.label_37.setGeometry(QtCore.QRect(610, 540, 311, 21))
        self.label_37.setObjectName("label_37")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 710, 111, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 710, 111, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(820, 710, 111, 32))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(70, 60, 971, 81))
        self.textBrowser.setObjectName("textBrowser")

        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(1100, 60, 281, 81))
        self.textBrowser_3.setObjectName("textBrowser_3")

        self.pushButton_2.clicked.connect(self.hesapla_fonksiyonu)
        self.pushButton_2.clicked.connect(self.kaydet)
        self.pushButton_3.clicked.connect(self.reset_values)

        self.outputBox = QtWidgets.QTextBrowser(Dialog)
        self.outputBox.setGeometry(QtCore.QRect(1100, 190, 291, 431))
        self.outputBox.setObjectName("outputBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def reset_values(self):
        # QSpinBox widgetlarının değerlerini sıfırla
        self.spinBox_2.setValue(0)
        self.spinBox_3.setValue(0)
        self.spinBox_4.setValue(0)
        self.spinBox_5.setValue(0)
        self.spinBox_10.setValue(0)
        self.spinBox_11.setValue(0)
        self.spinBox_12.setValue(0)
        self.spinBox_13.setValue(0)
        self.spinBox_14.setValue(0)
        self.spinBox_15.setValue(0)
        self.spinBox_16.setValue(0)
        self.spinBox_17.setValue(0)
        self.spinBox_18.setValue(0)

        
        # QDoubleSpinBox widgetlarının değerlerini sıfırla
        self.doubleSpinBox.setValue(0.0)
        self.doubleSpinBox_2.setValue(0.0)
        self.doubleSpinBox_3.setValue(0.0)
        self.doubleSpinBox_4.setValue(0.0)
        self.doubleSpinBox_5.setValue(0.0)
        self.doubleSpinBox_6.setValue(0.0)
        self.doubleSpinBox_7.setValue(0.0)
        self.doubleSpinBox_8.setValue(0.0)
        self.doubleSpinBox_9.setValue(0.0)


        # QComboBox widgetlarının değerlerini sıfırla
        # QComboBox için, genellikle ilk seçeneği (index 0) varsayılan olarak ayarlarız.
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(0)
        self.comboBox_6.setCurrentIndex(0)
        self.comboBox_7.setCurrentIndex(0)
        self.comboBox_8.setCurrentIndex(0)
        self.comboBox_9.setCurrentIndex(0)
        self.comboBox_10.setCurrentIndex(0)

    sieve_sizes = [3, 5, 6, 8, 10, 11, 13, 16, 19, 22, 25, 38, 50, 63, 75]
    percentages = [40, 45, 46, 49, 53, 54, 55, 58, 61, 63, 64, 68, 70, 72, 73]
    mapping_table = dict(zip(sieve_sizes, percentages))

    def get_nearest_value(input_value):
        closest_sieve_size = min(Ui_ElemePenceresi.mapping_table.keys(), key=lambda x:abs(x-input_value))
        return Ui_ElemePenceresi.mapping_table[closest_sieve_size]


    def hesapla_fonksiyonu(self):
        ilk_elek_alani = self.spinBox_2.value()
        self.outputBox.insertPlainText(f"{round(ilk_elek_alani, 2)} mm'lik Elek Alanının Hesaplanması\n")
        beslenecek_cevher_miktari = self.doubleSpinBox_2.value()
        self.outputBox.insertPlainText(f"{round(beslenecek_cevher_miktari, 2)} ton/saattir (tüvenan cevherde -{ilk_elek_alani} mm miktarı.)\n")
        ideal_kapasite = self.spinBox_3.value()
        self.outputBox.insertPlainText(f"İdeal koşullar eğrisinden {round(ilk_elek_alani, 2)} mm'ye karşılık gelen değer {ideal_kapasite} ton/m2/saat'dir.\n")
        elek_u_duzeltme = self.doubleSpinBox.value()
        self.outputBox.insertPlainText(f"İdeal koşullar elek üstü eğrisinden karşılık gelen değer {round(elek_u_duzeltme, 2)}'dir.\n")
        yarim_aciklik_duzeltme_faktoru = self.doubleSpinBox_3.value()
        self.outputBox.insertPlainText(f"Yarım açıklık düzeltme faktörü {round(yarim_aciklik_duzeltme_faktoru, 2)}'dir.\n")
        self.Q1 = (self.doubleSpinBox_4.value() / 2.7 )

        try:
            ag_boyutu = self.doubleSpinBox_5.value()
        except ValueError:
            self.showdialog()
        else:
            self.Q2 = Ui_ElemePenceresi.get_nearest_value(ag_boyutu) / 100

        selection = self.comboBox.currentText()
        if selection == "Kübik":
            self.Q3 = 1
        elif selection == "Yuvarlak":
            self.Q3 = 1.2
        elif selection == "Yassi":
            self.Q3 = 0.90
        else:
            selection = "Diger"
            self.Q3 = 1

        selection = self.comboBox_2.currentText()
        if selection == "Kübik":
            self.Q4 = 1
        elif selection == "Yuvarlak":
            self.Q4 = 1.2
        else:
            selection = "Yassi"
            self.Q4 = 0.90

        selection_q5 = self.comboBox_3.currentText()
        if selection_q5 == "<%3":
            self.Q5 = 1.0
        elif selection_q5 == "%3-%5":
            self.Q5 = 0.85
        elif selection_q5 == "%6-%8":
            self.Q5 = 0.75
        elif selection_q5 == "Yaş Eleme":
            self.Q5 = 1.0
        else:
            self.Q5 = 1.0  # Q5'in varsayılan değeri


        q6_table = {
            70: 1.4,
            75: 1.25,
            80: 1.1,
            85: 1.05,
            90: 1.0,
            92: 0.98,
            94: 0.95,
            96: 0.9
        }
        input_q6 = float(self.doubleSpinBox_6.value())
        closest_verim = min(q6_table.keys(), key=lambda x:abs(x-input_q6))
        self.Q6 = q6_table[closest_verim]

        q7_table = {
                "1": 1.0,
                "2": 0.9,
                "3": 0.8,
                "4": 0.7
            }
        input_q7 = self.comboBox_4.currentText()
        if input_q7 in q7_table:
            self.Q7 = q7_table[input_q7]
        else:
            QMessageBox.warning(None, "Error", "Invalid selection for Q7. Please select a value between 1 and 4.")

        q8_table = {
                "20°": 1.0,
                "Yatay": 0.9
            }
        input_q8 = self.comboBox_5.currentText()
        if input_q8 in q8_table:
            self.Q8 = q8_table[input_q8]
        else:
            QMessageBox.warning(None, "Error", "Invalid selection for Q8. Please select either '20°' or 'Yatay'.")

        q_t = self.Q1 * self.Q2 * self.Q3 * self.Q4 * self.Q5 * self.Q6 * self.Q7 * self.Q8
        self.outputBox.insertPlainText(f"Qtoplam değeri {round(q_t, 2)} olarak hesaplanmıştır.\n")

        K_emniyet = 1.25 # Kabul
        T = ((beslenecek_cevher_miktari ) * K_emniyet)
        net_elek_alani = (T) / (ideal_kapasite * elek_u_duzeltme * yarim_aciklik_duzeltme_faktoru * q_t)
        self.outputBox.insertPlainText(f"Net elek alanı {round(net_elek_alani, 2)} m2 olarak bulunmuştur.\n")
        
        hacimsel_kapasite = self.spinBox_14.value()
        self.outputBox.insertPlainText(f"Hacimsel kapasite değeri {round(hacimsel_kapasite, 2)} m3/saat'tir.\n")
        elek_ustu_hizi = 36 # Kabul
        nominal_elek_genisligi = self.doubleSpinBox_5.value()
        self.outputBox.insertPlainText(f"Nominal elek genişlliği {round(nominal_elek_genisligi, 2)} m'dir.\n")

        elek_ustu_malzeme_kalinligi = (100 * T) / (6 * elek_ustu_hizi * (nominal_elek_genisligi - 0.15))
        self.outputBox.insertPlainText(f"Elek Üstü Malzeme Kalınlığı {round(elek_ustu_malzeme_kalinligi, 2)} olarak bulunmuştur. Bu hesaplama uygundur.\n")

        #######

        ikinci_elek_alani = self.spinBox_4.value()
        self.outputBox.insertPlainText(f"{round(ikinci_elek_alani, 2)} mm'lik Elek Alanının Hesaplanması\n")
        beslenecek_cevher_miktari_2 = self.doubleSpinBox_2.value()
        self.outputBox.insertPlainText(f"{round(beslenecek_cevher_miktari_2, 2)} ton/saattir (tüvenan cevherde -{ilk_elek_alani} mm miktarı.)\n")
        ideal_kapasite_2 = self.spinBox_3.value()
        self.outputBox.insertPlainText(f"İdeal koşullar eğrisinden {round(ikinci_elek_alani, 2)} mm'ye karşılık gelen değer {ideal_kapasite_2} ton/m2/saat'dir.\n")
        elek_u_duzeltme_2 = self.doubleSpinBox.value()
        self.outputBox.insertPlainText(f"İdeal koşullar elek üstü eğrisinden karşılık gelen değer {round(elek_u_duzeltme_2, 2)}'dir.\n")
        yarim_aciklik_duzeltme_faktoru_2 = self.doubleSpinBox_3.value()
        self.outputBox.insertPlainText(f"Yarım açıklık düzeltme faktörü {round(yarim_aciklik_duzeltme_faktoru_2, 2)}'dir.\n")
       
        K_emniyet = 1.25 # Kabul
        
        T_2 = ((beslenecek_cevher_miktari_2) * K_emniyet)
        net_elek_alani_2 = (T_2) / (ideal_kapasite_2 * elek_u_duzeltme_2 * yarim_aciklik_duzeltme_faktoru_2 * q_t)
        self.outputBox.insertPlainText(f"Net elek alanı {round(net_elek_alani_2, 2)} m2 olarak bulunmuştur.\n")

        ####
        
        
        
        hacimsel_kapasite_2 = self.spinBox_14.value()
        self.outputBox.insertPlainText(f"Hacimsel kapasite değeri {round(hacimsel_kapasite_2, 2)} m3/saat'tir.\n")
        elek_ustu_hizi_2 = 0,6 # Kabul
        nominal_elek_genisligi_2 = self.doubleSpinBox_5.value()
        self.outputBox.insertPlainText(f"Nominal elek genişlliği {round(nominal_elek_genisligi_2, 2)} m'dir.\n")
        
    def kaydet(self):
        dosya_ismi = "Eleme Hesapları.txt" 
        with open(dosya_ismi, 'w') as f:
            f.write(self.outputBox.toPlainText())

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Eleme Hesapları"))
        self.label_20.setText(_translate("Dialog", "Elek üstü malzeme kalınlığı giriniz(mm):"))
        self.label_10.setText(_translate("Dialog", "Elek üstü düzeltme faktörünü giriniz: "))
        self.label_11.setText(_translate("Dialog", "Yarım açıklık düzeltme faktörünü giriniz:"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">mm </span><span style=\" font-family:\'Times New Roman,Bold\'; font-size:10pt; font-weight:700;\">Elek Alanının Hesaplanması </span></p></body></html>"))
        self.label_21.setText(_translate("Dialog", "Hacimsel kapasite değerini giriniz (m3/saat):"))
        self.label_12.setText(_translate("Dialog", "Yarım açıklık düzeltme faktörünü giriniz:"))
        self.label_13.setText(_translate("Dialog", "Beslenecek cevher miktarını giriniz (ton/saat) :"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:12pt; font-weight:700;\">2.1 </span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:12pt; font-weight:700;\">2.2</span></p></body></html>"))
        self.label_18.setText(_translate("Dialog", "Nominal elek genişliğini giriniz (m):"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">ELEME HESAPLAMALARI</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p>Eleme boyutu için ideal koşullardaki kapasite (ton/m2/saat):</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "Beslenecek cevher miktarını giriniz (ton/saat) :"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">mm </span><span style=\" font-family:\'Times New Roman,Bold\'; font-size:10pt; font-weight:700;\">Elek Alanının Hesaplanması </span></p></body></html>"))
        self.label_17.setText(_translate("Dialog", "Hacimsel kapasite değerini giriniz (m3/saat):"))
        self.label_19.setText(_translate("Dialog", "Nominal elek genişliğini giriniz (m):"))
        self.label_15.setText(_translate("Dialog", "Elek üstü düzeltme faktörünü giriniz: "))
        self.label_14.setText(_translate("Dialog", "<html><head/><body><p>Eleme boyutu için ideal koşullardaki kapasite (ton/m2/saat):</p></body></html>"))
        self.label_16.setText(_translate("Dialog", "Elek üstü malzeme kalınlığı giriniz(mm):"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:10pt; font-weight:700;\">2.1.1 Düzeltme Faktörlerinin Hesaplanması</span></p></body></html>"))
        self.label_22.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:700;\">Q1</span>: Yarım açıklık düzeltme faktörünü giriniz:</p></body></html>"))
        self.label_23.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:700;\">Q2</span>: Elek açık alanı seçimi:</p></body></html>"))
        self.label_24.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:700;\">Q3</span>: Elek açıklığı şekli düzeltme faktörünü seçiniz:</p></body></html>"))
        self.comboBox.setItemText(0, _translate("Dialog", "Kübik"))
        self.comboBox.setItemText(1, _translate("Dialog", "Yuvarlak"))
        self.comboBox.setItemText(2, _translate("Dialog", "Yassı"))
        self.comboBox.setItemText(3, _translate("Dialog", "Diğer"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Kübik"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Yuvarlak"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Yassı"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "Diğer"))
        self.label_25.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:700;\">Q4</span>: Tane şeklini seçiniz:</p></body></html>"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "< %3"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "%3 - %5"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "%6 - %8"))
        self.comboBox_3.setItemText(3, _translate("Dialog", "Yaş Eleme"))
        self.label_26.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:700;\">Q5</span>: Nem oranını seçiniz:</p></body></html>"))
        self.label_27.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:700;\">Q6</span>: Elek verimi düzeltme faktörünü giriniz:</p></body></html>"))
        self.comboBox_4.setItemText(0, _translate("Dialog", "1"))
        self.comboBox_4.setItemText(1, _translate("Dialog", "2"))
        self.comboBox_4.setItemText(2, _translate("Dialog", "3"))
        self.comboBox_4.setItemText(3, _translate("Dialog", "4"))
        self.label_28.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:700;\">Q7</span>: Elek katını seçiniz:</p></body></html>"))
        self.comboBox_5.setItemText(0, _translate("Dialog", "20°"))
        self.comboBox_5.setItemText(1, _translate("Dialog", "Yatay"))
        self.label_29.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:700;\">Q8</span>: Elek eğimini seçiniz:</p></body></html>"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,Bold\'; font-size:10pt; font-weight:700;\">2.2.1 Düzeltme Faktörlerinin Hesaplanması</span></p></body></html>"))
        self.comboBox_6.setItemText(0, _translate("Dialog", "< %3"))
        self.comboBox_6.setItemText(1, _translate("Dialog", "%3 - %5"))
        self.comboBox_6.setItemText(2, _translate("Dialog", "%6 - %8"))
        self.comboBox_6.setItemText(3, _translate("Dialog", "Yaş Eleme"))
        self.label_30.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:700;\">Q1</span>: Yarım açıklık düzeltme faktörünü giriniz:</p></body></html>"))
        self.comboBox_7.setItemText(0, _translate("Dialog", "Kübik"))
        self.comboBox_7.setItemText(1, _translate("Dialog", "Yuvarlak"))
        self.comboBox_7.setItemText(2, _translate("Dialog", "Yassı"))
        self.comboBox_7.setItemText(3, _translate("Dialog", "Diğer"))
        self.label_31.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:700;\">Q2</span>: Elek açık alanı seçimi:</p></body></html>"))
        self.comboBox_8.setItemText(0, _translate("Dialog", "Kübik"))
        self.comboBox_8.setItemText(1, _translate("Dialog", "Yuvarlak"))
        self.comboBox_8.setItemText(2, _translate("Dialog", "Yassı"))
        self.comboBox_8.setItemText(3, _translate("Dialog", "Diğer"))
        self.comboBox_9.setItemText(0, _translate("Dialog", "20°"))
        self.comboBox_9.setItemText(1, _translate("Dialog", "Yatay"))
        self.comboBox_10.setItemText(0, _translate("Dialog", "1"))
        self.comboBox_10.setItemText(1, _translate("Dialog", "2"))
        self.comboBox_10.setItemText(2, _translate("Dialog", "3"))
        self.comboBox_10.setItemText(3, _translate("Dialog", "4"))
        self.label_32.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:700;\">Q3</span>: Elek açıklığı şekli düzeltme faktörünü seçiniz:</p></body></html>"))
        self.label_33.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:700;\">Q7</span>: Elek katını seçiniz:</p></body></html>"))
        self.label_34.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:700;\">Q8</span>: Elek eğimini seçiniz:</p></body></html>"))
        self.label_35.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:700;\">Q6</span>: Elek verimi düzeltme faktörünü giriniz:</p></body></html>"))
        self.label_36.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:700;\">Q5</span>: Nem oranını seçiniz:</p></body></html>"))
        self.label_37.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:700;\">Q4</span>: Tane şeklini seçiniz:</p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", "Hesapla"))
        self.pushButton_3.setText(_translate("Dialog", "Sıfırla"))
        self.pushButton.setText(_translate("Dialog", "Devam Et"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">Eleme, bir malzemeyi boyutlarına göre ayırmak için kullanılan bir işlemdir. Bu program, bir elek kullanarak bir malzemeyi ayırmak için gereken kapasiteyi hesaplamak için kullanılabilir. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">Programı kullanmak için, öncelikle elek boyutunu ve malzemenin boyutunu girmeniz gerekir. Ardından, malzemenin nem içeriğini ve elek üzerindeki malzeme kalınlığını girmeniz gerekir. Son olarak, elek üzerindeki malzemenin şeklini ve elek eğimini seçmeniz gerekir. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">Program, bu bilgileri kullanarak malzemeyi ayırmak için gereken kapasiteyi hesaplayacaktır. Hesaplanan kapasite, to/m2/saat olarak belirtilecektir. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">Bu program, bir elek kullanarak bir malzemeyi ayırmak için gereken kapasiteyi hesaplamak için kullanışlı bir araçtır. Program, farklı elek boyutları, malzeme boyutları, nem içeriği, malzeme şekli ve elek eğimi için kapasiteyi hesaplamak için kullanılabilir.</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt; font-weight:700; text-decoration: underline;\">Kabuller</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:700; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt;\">- Kırıcıdan çıkan malzemenin öngörülen kırma boyutundan daha iri malzeme miktarı </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt; font-weight:700; font-style:italic;\">0.14</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt;\"> kabul edilmiştir.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt;\">- Bond iş endeksi, genelde </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt; font-weight:700; font-style:italic;\">10-13 </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt;\">arasında olur. Burada </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt; font-weight:700; font-style:italic;\">12.5</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt;\"> olarak kabul edilmiştir.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt;\">- Emniyet katsayısı </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt; font-weight:700; font-style:italic;\">%20-25</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt;\"> arasında olmaktadır ve burada </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt; font-weight:700; font-style:italic;\">%25</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt;\"> olarak kabul edilmiştir.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt;\">- Horsepower (HP) değeri </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt; font-weight:700; font-style:italic;\">1.34 </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt;\">kabul edilmiştir.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_ElemePenceresi()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
