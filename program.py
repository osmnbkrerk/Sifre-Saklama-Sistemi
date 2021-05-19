import json
import sys
from random import randint
from tkinter import *
from tkinter import messagebox

import onetimepad
from PySide6.QtWidgets import QApplication, QMainWindow
from app_ui import Ui_MainWindow

tut = ""
with open('sifre.json') as json_file:
    sifrem = json.load(json_file)
    tut = onetimepad.decrypt(sifrem["sifre"], 'anasifre')

    if sifrem["sifre"] == "":
        sifrem["sifre"] = onetimepad.encrypt(str(randint(1000, 9999)),"anasifre")
        with open("sifre.json", 'w') as f:
            json.dump(sifrem, f, indent=4)
            tut = onetimepad.decrypt(sifrem["sifre"], 'anasifre')
            sifrem["sifre"] = onetimepad.decrypt(str(sifrem["sifre"]),"anasifre")
            print("ŞİFRE OLUŞTURULDU. ŞİFRENİZ: ", sifrem["sifre"])




sifreGir = input("Şifrenizi Giriniz: ")
if sifreGir == tut:
    print("Girilen şifre doğru. Sisteme giriş yapabilirsiniz.")

    class MainWindow(QMainWindow):
        def __init__(self):
            super(MainWindow, self).__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)


    if __name__ == '__main__':
        app = QApplication(sys.argv)

        window = MainWindow()
        window.show()
        sys.exit(app.exec_())

else:
    print("Girilen Şifre Yanlış. Program Kapatılıyor")

    exit(0)
