# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import json

import onetimepad
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sqlite3



class Ui_MainWindow(object):

    def loadData(self):
        connection = sqlite3.connect("my_db.db")
        query = "SELECT * FROM sitebilgileri"
        result = connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

    def loadData2(self):
        connection = sqlite3.connect("my_db.db")
        query = "SELECT * FROM sitebilgileri WHERE siteAdi LIKE '" + self.aranan.toPlainText() + "%'"

        result = connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

    def insertData(self):
        tut = ""
        with open('sifre.json') as json_file:
            sifrem = json.load(json_file)
            tut = onetimepad.decrypt(sifrem["sifre"], 'anasifre')
            connection = sqlite3.connect('my_db.db')
            database = connection.cursor()
            database.execute("INSERT INTO sitebilgileri (siteAdi,siteAdresi,sifresi) VALUES('" + self.ad.toPlainText() +
                             "','" + self.adres.toPlainText() + "','" + onetimepad.encrypt(self.sifre.toPlainText(),tut) + "')")

            msgBox = QMessageBox()
            msgBox.setText("Ekleme işlemi başarıyla gerçekleşti!")
            msgBox.exec_()

            connection.commit()
            connection.rollback()
            connection.close()

    def encryptedLoadData(self):
        tut = ""
        with open('sifre.json') as json_file:
            sifrem = json.load(json_file)
            tut = onetimepad.decrypt(sifrem["sifre"], 'anasifre')
            self.tableWidget.setItem(self.tableWidget.currentRow(), 2, QTableWidgetItem(str(onetimepad.encrypt(self.tableWidget.item(self.tableWidget.currentRow(),2).text(),tut))))


    def decryptedLoadData(self):
        tut = ""
        with open('sifre.json') as json_file:
            sifrem = json.load(json_file)
            tut = onetimepad.decrypt(sifrem["sifre"], 'anasifre')
            self.tableWidget.setItem(self.tableWidget.currentRow(), 2, QTableWidgetItem(str(onetimepad.decrypt(self.tableWidget.item(self.tableWidget.currentRow(),2).text(),tut))))

    def updatePassword(self):
        tut = ""
        with open('sifre.json') as json_file:
            sifrem = json.load(json_file)
            tut = onetimepad.decrypt(sifrem["sifre"], 'anasifre')
            connection = sqlite3.connect('my_db.db')
            database = connection.cursor()
            database.execute("UPDATE sitebilgileri SET sifresi ='" + onetimepad.encrypt(self.guncelSifre.toPlainText(),tut) +"' WHERE siteAdi = '"+self.ad.toPlainText()+"' AND siteAdresi = '"+ self.adres.toPlainText()+"'")
            msgBox = QMessageBox()
            msgBox.setText("Şifre başarıyla güncellendi!")
            msgBox.exec_()
            connection.commit()

    def tableClickEvent(self):
        self.ad.setPlainText(str(self.tableWidget.item(self.tableWidget.currentRow(), 0).text()))
        self.adres.setPlainText(str(self.tableWidget.item(self.tableWidget.currentRow(), 1).text()))

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1115, 632)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(350, 150, 761, 431))

        self.tableWidget.clicked.connect(self.tableClickEvent)

        self.tableWidget.setColumnCount(3)
        self.btn_load = QPushButton(self.centralwidget)
        self.btn_load.setObjectName(u"btn_load")
        self.btn_load.setGeometry(QRect(720, 100, 121, 31))

        self.btn_load.clicked.connect(self.loadData)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(220, 350, 101, 31))

        self.pushButton.clicked.connect(self.insertData)

        self.ad = QTextEdit(self.centralwidget)
        self.ad.setObjectName(u"ad")
        self.ad.setGeometry(QRect(120, 210, 211, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 210, 111, 31))
        self.adres = QTextEdit(self.centralwidget)
        self.adres.setObjectName(u"adres")
        self.adres.setGeometry(QRect(120, 250, 211, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 250, 111, 31))
        self.sifre = QTextEdit(self.centralwidget)
        self.sifre.setObjectName(u"sifre")
        self.sifre.setGeometry(QRect(120, 290, 211, 31))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 290, 111, 31))
        self.aranan = QTextEdit(self.centralwidget)
        self.aranan.setObjectName(u"aranan")
        self.aranan.setGeometry(QRect(350, 100, 211, 31))
        self.btn_load_2 = QPushButton(self.centralwidget)
        self.btn_load_2.setObjectName(u"btn_load_2")
        self.btn_load_2.setGeometry(QRect(580, 100, 121, 31))

        self.btn_load_2.clicked.connect(self.loadData2)

        self.encryptButton = QPushButton(self.centralwidget)
        self.encryptButton.setObjectName(u"encryptButton")
        self.encryptButton.setGeometry(QRect(860, 100, 101, 31))

        self.encryptButton.clicked.connect(self.encryptedLoadData)

        self.decryptButton = QPushButton(self.centralwidget)
        self.decryptButton.setObjectName(u"decryptButton")
        self.decryptButton.setGeometry(QRect(970, 100, 101, 31))

        self.decryptButton.clicked.connect(self.decryptedLoadData)

        self.guncelSifre = QTextEdit(self.centralwidget)
        self.guncelSifre.setObjectName(u"guncelSifre")
        self.guncelSifre.setGeometry(QRect(20, 490, 211, 31))
        self.sifreGuncelleButton = QPushButton(self.centralwidget)
        self.sifreGuncelleButton.setObjectName(u"sifreGuncelleButton")
        self.sifreGuncelleButton.setGeometry(QRect(240, 490, 101, 31))

        self.sifreGuncelleButton.clicked.connect(self.updatePassword)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.tableWidget, self.btn_load)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Site Ad\u0131", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Adresi", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u015eifresi", None));
        self.btn_load.setText(QCoreApplication.translate("MainWindow", u"T\u00fcm Bilgileri Getir", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Site Ekle", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Site Ad\u0131 :</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Site Adresi :</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u015eifresi : </span></p></body></html>", None))
        self.btn_load_2.setText(QCoreApplication.translate("MainWindow", u"Aranan Siteyi Getir", None))
        self.encryptButton.setText(QCoreApplication.translate("MainWindow", u"Encrypt Et", None))
        self.decryptButton.setText(QCoreApplication.translate("MainWindow", u"Decrypt Et", None))
        self.sifreGuncelleButton.setText(QCoreApplication.translate("MainWindow", u"\u015eifre G\u00fcncelle", None))
    # retranslateUi

