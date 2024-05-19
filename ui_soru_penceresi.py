# -*- coding: utf-8 -*-



from PyQt5 import QtCore, QtGui, QtWidgets
from ui_islem_secim_penceresi19 import Ui_MainWindow
from ui_kirma import Ui_KirmaPenceresi
from ui_eleme import Ui_ElemePenceresi
from ui_ogutme import Ui_OgutmeSecimi
from ui_bilyali import Ui_BilyaliDegirmen
from ui_cubuklu import Ui_CubukluPencere
from ui_zenginlestirme import Ui_Zenginlestirme_Ekrani
from ui_flotasyon import Ui_Flotasyon_Hucreleri_Hesabi
from ui_sarsintili_masa20007 import Ui_Sarsintili_Masa
from ui_stok import Ui_StokHesaplari
from ui_bant import Ui_Bant

class Ui_SoruPenceresi(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(1440, 763)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 300, 281, 41))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(610, 310, 103, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(210, 350, 241, 31))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(610, 350, 103, 32))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(210, 380, 391, 41))
        self.label_3.setObjectName("label_3")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(610, 390, 101, 22))
        self.spinBox.setMaximum(500)
        self.spinBox.setObjectName("spinBox")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(780, 300, 351, 41))
        self.label_4.setObjectName("label_4")
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(1180, 310, 51, 22))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(365)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(780, 340, 381, 41))
        self.label_5.setObjectName("label_5")
        self.spinBox_3 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_3.setGeometry(QtCore.QRect(1180, 350, 51, 22))
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(24)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_4.setGeometry(QtCore.QRect(1180, 390, 51, 22))
        self.spinBox_4.setMinimum(1)
        self.spinBox_4.setMaximum(1000000)
        self.spinBox_4.setObjectName("spinBox_4")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(780, 380, 371, 41))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(780, 420, 371, 41))
        self.label_7.setObjectName("label_7")
        self.spinBox_5 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_5.setGeometry(QtCore.QRect(1180, 430, 51, 22))
        self.spinBox_5.setMinimum(1)
        self.spinBox_5.setMaximum(100000)
        self.spinBox_5.setObjectName("spinBox_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(740, 490, 100, 32))
        self.pushButton.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 1421, 71))
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(210, 420, 371, 41))
        self.label_10.setObjectName("label_10")
        self.spinBox_6 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_6.setGeometry(QtCore.QRect(610, 430, 101, 22))
        self.spinBox_6.setMaximum(500)
        self.spinBox_6.setObjectName("spinBox_6")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(80, 80, 1281, 191))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 490, 100, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(700, 690, 100, 32))
        self.pushButton_3.setText("Devam Et")  
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(150, 280, 1141, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.soru_penceresi = Ui_KirmaPenceresi()

        self.outputBox = QtWidgets.QPlainTextEdit(Dialog)
        self.outputBox.setGeometry(QtCore.QRect(350, 530, 750, 150))  # Adjust these values as necessary
        self.outputBox.setReadOnly(True)

        self.connect_signals()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.comboBox, self.comboBox_2)
        Dialog.setTabOrder(self.comboBox_2, self.spinBox)
        Dialog.setTabOrder(self.spinBox, self.spinBox_6)
        Dialog.setTabOrder(self.spinBox_6, self.spinBox_2)
        Dialog.setTabOrder(self.spinBox_2, self.spinBox_3)
        Dialog.setTabOrder(self.spinBox_3, self.spinBox_4)
        Dialog.setTabOrder(self.spinBox_4, self.spinBox_5)
        Dialog.setTabOrder(self.spinBox_5, self.pushButton)
        Dialog.setTabOrder(self.pushButton, self.pushButton_2)
        Dialog.setTabOrder(self.pushButton_2, self.textBrowser)
    
    def get_spinBox_5_value(self):
        return self.spinBox_5.value()
    
    def update_hourly_capacity(self, value):
        self.hourly_capacity = value
        self.soru_penceresi.set_hourly_capacity(value)

    def collect_values(self):
        max_size = self.spinBox.value()
        min_size = self.spinBox_6.value()
        yearly_work_days = self.spinBox_2.value()
        daily_work_hours = self.spinBox_3.value()
        total_capacity = self.spinBox_4.value()
        hourly_capacity = self.spinBox_5.value()

        return max_size, min_size, yearly_work_days, daily_work_hours, total_capacity, hourly_capacity

    def calculate_reduction_ratio(self, max_size, min_size):
        if min_size != 0:  # Avoiding division by zero
            return max_size / min_size
        else:
            return 0  # You can return any value here indicating an error

    def get_spinBox_value(self):
        self.spinBox_value = self.spinBox_5.value()
        
    def display_output(self):
        max_size, min_size, yearly_work_days, daily_work_hours, total_capacity, hourly_capacity = self.collect_values()
        reduction_ratio = self.calculate_reduction_ratio(max_size, min_size)
        
        shift_count = round(daily_work_hours / 8)
        output_str = (f"{total_capacity} ton/gün kapasiteye uygun olarak tesisisin saat bazında {hourly_capacity} ton/saat kapasiteyle çalıştığı kabul edilmiştir.\n"
              f"Tesisin kırma devresinin {shift_count} vardiya üzerinden günde {daily_work_hours} saat, çalışacağı kabul edilmiştir.\n"
              f"Tesis yıllık çalışma süresi {yearly_work_days} gün baz alınarak hesaplama yapılmıştır.\n"
              f"Boyut küçültme oranı {'{:.2f}'.format(reduction_ratio)} olarak hesaplanmıştır")

        self.outputBox.setPlainText(output_str)

    def reset_values(self):
        self.spinBox.setValue(0)
        self.spinBox_2.setValue(1)
        self.spinBox_3.setValue(1)
        self.spinBox_4.setValue(1)
        self.spinBox_5.setValue(1)
        self.spinBox_6.setValue(0)
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)

    def connect_signals(self):
        self.pushButton.clicked.connect(self.display_output)
        self.pushButton_2.clicked.connect(self.reset_values)
        self.pushButton_3.clicked.connect(self.switch_window)
        self.comboBox.currentTextChanged.connect(self.check_combo_box)

    def check_combo_box(self, text):
        if text == "Hayır":
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Bilgi Eksikliği")
            msg.setText("Lütfen gerekli bilgileri edinip tekrar deneyiniz.")
            retryButton = msg.addButton('Tekrar Dene', QtWidgets.QMessageBox.YesRole)
            msg.exec_()
            if msg.clickedButton() == retryButton:
                self.comboBox.setCurrentIndex(0)

    def switch_window(self):
        self.islem_secim_penceresi = QtWidgets.QMainWindow()  # Create a new window
        self.ui = Ui_MainWindow()  # Create a new Ui_MainWindow object
        self.ui.setupUi(self.islem_secim_penceresi)  # Set up the new window
        self.islem_secim_penceresi.show()
        self.Dialog.hide()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Genel Bilgiler ve Proje Hedefleri"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt;\">Prosesin akım şeması hazır mı? </span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("Dialog", "Evet"))
        self.comboBox.setItemText(1, _translate("Dialog", "Hayır"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt;\">Cevher tipini seçiniz.</span></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Kromit"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Altın"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Bakır"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt;\">Cevher maksimum tane boyutunu giriniz (mm):</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt;\">Tesisin yıllık çalışma süresini giriniz (gün):</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt;\">Tesisin günlük çalışma süresini giriniz (saat):</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt;\">Tesisin toplam kapasitesini girin (ton/gün):</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt;\">Tesisin saatlik kapasitesini girin (ton/saat):</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Uygula"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">GENEL BİLGİLER VE PROJE HEDEFLERİ</span></p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt;\">Cevher minimum tane boyutunu giriniz (mm):</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">Bu program, bir cevher işleme tesisinin kapasitesini hesaplamak için kullanılmaktadır. Program, tesisin akım şemasına, cevher tipine, cevher maksimum tane boyutuna, tesisin yıllık çalışma süresine, tesisin günlük çalışma süresine, tesisin toplam kapasitesine, tesisin saatlik kapasitesine, tesisin minimum tane boyutuna ve tesisin kaç vardiyada çalışacağına ilişkin bilgiler kullanılarak çalışmaktadır. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">Programı kullanmak için, öncelikle programın ana ekranında yer alan \'Prosesin akım şeması hazır mı?\' sorusuna \'</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt; font-weight:700; font-style:italic;\">Evet</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">\' veya \'</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt; font-weight:700; font-style:italic;\">Hayır</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">\' cevabını vermeniz gerekmektedir. \'</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt; font-weight:700; font-style:italic;\">Evet</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">\' cevabını vermeniz durumunda, programın ana ekranında yer alan \'</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt; font-weight:700; font-style:italic;\">Cevher tipini seçiniz</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">.\' ve \'</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt; font-weight:700; font-style:italic;\">Cevher maksimum tane boyutunu giriniz (mm):</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">\' kutularına cevherin tipini ve maksimum tane boyutunu girmeniz gerekmektedir. \'</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt; font-weight:700; font-style:italic;\">Hayır</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">\' cevabını vermeniz durumunda, uygulama maalesef çalışmayacaktır ve lütfen gerekli bilgileri edinip tekrar deneyiniz. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">Programın ana ekranında yer alan \'</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt; font-weight:700; font-style:italic;\">Tesisin yıllık çalışma süresini giriniz (gün):</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">\', \'</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt; font-weight:700; font-style:italic;\">Tesisin günlük çalışma süresini giriniz (saat):</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">\', \'</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt; font-weight:700; font-style:italic;\">Tesisin toplam kapasitesini girin (ton/gün):</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">\' ve \'</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt; font-weight:700; font-style:italic;\">Tesisin saatlik kapasitesini girin (ton/saat):</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">\' kutularına cevher işleme tesisinin ilgili bilgilerini girmeniz gerekmektedir. Programın ana ekranında yer alan \'</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt; font-weight:700; font-style:italic;\">Tesisin kaç vardiyada çalışacağını giriniz:</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">\' kutusuna cevher işleme tesisinin kaç vardiyada çalışacağını girmeniz gerekmektedir. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">Tüm bilgileri girdikten sonra, programın ana ekranında yer alan \'</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt; font-weight:700; font-style:italic;\">Uygula</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">\' butonuna tıklayarak cevher işleme tesisinin kapasitesini hesaplayabilirsiniz.</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", "Sıfırla"))
        self.pushButton_3.setText(_translate("Dialog", "Devam Et"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_SoruPenceresi()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
