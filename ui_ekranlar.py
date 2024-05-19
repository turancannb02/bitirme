# ui_ekranlar.py
from PyQt5 import QtWidgets
from ui_eleme_penceresi20071_modified import Ui_ElemePenceresi  # You need to import this class

def eleme_penceresi_ac():
    eleme_penceresi = QtWidgets.QDialog()
    ui = Ui_ElemePenceresi()
    ui.setupUi(eleme_penceresi)
    eleme_penceresi.show()
