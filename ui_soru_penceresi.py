# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'soru_penceresi.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ui_main_window import Ui_MainWindow




class Ui_Soru_Penceresi(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(911, 731)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 80, 231, 41))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(260, 90, 103, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 231, 31))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(190, 130, 103, 32))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 160, 281, 41))
        self.label_3.setObjectName("label_3")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(340, 170, 51, 22))
        self.spinBox.setMaximum(500)
        self.spinBox.setObjectName("spinBox")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 280, 251, 41))
        self.label_4.setObjectName("label_4")
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(310, 290, 51, 22))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(365)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(50, 320, 271, 41))
        self.label_5.setObjectName("label_5")
        self.spinBox_3 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_3.setGeometry(QtCore.QRect(320, 330, 51, 22))
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(24)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_4.setGeometry(QtCore.QRect(310, 370, 51, 22))
        self.spinBox_4.setMinimum(1)
        self.spinBox_4.setMaximum(1000000)
        self.spinBox_4.setObjectName("spinBox_4")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(50, 360, 261, 41))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(50, 400, 251, 41))
        self.label_7.setObjectName("label_7")
        self.spinBox_5 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_5.setGeometry(QtCore.QRect(310, 410, 51, 22))
        self.spinBox_5.setMinimum(1)
        self.spinBox_5.setMaximum(100000)
        self.spinBox_5.setObjectName("spinBox_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(370, 440, 100, 32))
        self.pushButton.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(240, 20, 481, 41))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(410, 160, 441, 41))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(50, 200, 281, 41))
        self.label_10.setObjectName("label_10")
        self.spinBox_6 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_6.setGeometry(QtCore.QRect(330, 210, 51, 22))
        self.spinBox_6.setMaximum(500)
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_7 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_7.setGeometry(QtCore.QRect(310, 250, 51, 22))
        self.spinBox_7.setMinimum(1)
        self.spinBox_7.setMaximum(3)
        self.spinBox_7.setObjectName("spinBox_7")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(50, 240, 251, 41))
        self.label_11.setObjectName("label_11")

        self.outputBox = QtWidgets.QPlainTextEdit(Dialog)
        self.outputBox.setGeometry(QtCore.QRect(50, 480, 800, 200))  # Adjust these values as necessary
        self.outputBox.setReadOnly(True)

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 690, 100, 32))  # Konumu ve boyutu ayarlayın
        self.pushButton_2.setObjectName("pushButton_2")

        
        self.connect_signals()

        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    
    def collect_values(self):
        max_size = self.spinBox.value()
        min_size = self.spinBox_6.value()
        yearly_work_days = self.spinBox_2.value()
        daily_work_hours = self.spinBox_3.value()
        total_capacity = self.spinBox_4.value()
        hourly_capacity = self.spinBox_5.value()
        shift_count = self.spinBox_7.value()

        return max_size, min_size, yearly_work_days, daily_work_hours, total_capacity, hourly_capacity, shift_count

    def calculate_reduction_ratio(self, max_size, min_size):
        if min_size != 0:  # Avoiding division by zero
            return max_size / min_size
        else:
            return 0  # You can return any value here indicating an error

    def display_output(self):
        max_size, min_size, yearly_work_days, daily_work_hours, total_capacity, hourly_capacity, shift_count = self.collect_values()
        reduction_ratio = self.calculate_reduction_ratio(max_size, min_size)
        
        output_str = f"{total_capacity} ton/gün kapasiteye uygun olarak tesisisin saat bazında {hourly_capacity} ton/saat kapasiteyle çalıştığı kabul edilmiştir. Tesisin kırma devresinin {shift_count} vardiya üzerinden günde {daily_work_hours} saat, çalışacağı kabul edilmiştir. Tesis yıllık çalışma süresi {yearly_work_days} gün baz alınarak hesaplama yapılmıştır. Boyut küçültme oranı {reduction_ratio} olarak hesaplanmıştır"
        
        self.outputBox.setPlainText(output_str)

    def connect_signals(self):
        self.pushButton.clicked.connect(self.display_output)
        self.comboBox.currentIndexChanged.connect(self.check_flowchart)

    def check_flowchart(self):
        choice = self.comboBox.currentText()
        if choice == "Hayır":
            QMessageBox.information(None, 'Bilgi', 'Lütfen akım şemasını hazırlayın ve tekrar deneyin.')

    def switch_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

    def connect_signals(self):
        self.pushButton.clicked.connect(self.display_output)
        self.comboBox.currentIndexChanged.connect(self.check_flowchart) # Yeni sinyal bağlantısı
        self.pushButton_2.clicked.connect(self.switch_window)
        
    def get_hourly_capacity(self):
        return self.hourly_capacity
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Prosesin akım şeması hazır mı? "))
        self.comboBox.setItemText(0, _translate("Dialog", "Evet"))
        self.comboBox.setItemText(1, _translate("Dialog", "Hayır"))
        self.label_2.setText(_translate("Dialog", "Cevher tipini seçiniz."))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Kromit"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Altın"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Bakır"))
        self.label_3.setText(_translate("Dialog", "Cevher maksimum tane boyutunu giriniz (mm):"))
        self.label_4.setText(_translate("Dialog", "Tesisin yıllık çalışma süresini giriniz (gün):"))
        self.label_5.setText(_translate("Dialog", "Tesisin günlük çalışma süresini giriniz (saat):"))
        self.label_6.setText(_translate("Dialog", "Tesisin toplam kapasitesini girin (ton/gün):"))
        self.label_7.setText(_translate("Dialog", "Tesisin saatlik kapasitesini girin (ton/saat):"))
        self.pushButton.setText(_translate("Dialog", "Uygula"))
        self.pushButton_2.setText(_translate("Dialog", "Devam Et"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700;\">GENEL BİLGİLER VE PROJE HEDEFLERİ</span></p></body></html>"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:9pt; font-style:italic;\">Bu değer, ölçüm yapılan cevherin özelliklerine bağlıdır ve genellikle </span><span style=\" font-size:9pt; font-weight:700; font-style:italic;\">1-500 mm</span><span style=\" font-size:9pt; font-style:italic;\"> arasında değişir.</span></p></body></html>"))
        self.label_10.setText(_translate("Dialog", "Cevher minimum tane boyutunu giriniz (mm):"))
        self.label_11.setText(_translate("Dialog", "Tesisin kaç vardiyada çalışacağını giriniz:"))

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Soru_Penceresi()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())