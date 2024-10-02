# -*- coding: utf-8 -*-
import sqlite3

# Form implementation generated from reading ui file 'C:\otelmenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(458, 429)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-20, 10, 531, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(529, 119))
        self.label.setMaximumSize(QtCore.QSize(529, 119))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 160, 411, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.kayit_et = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.kayit_et.setObjectName("kayit_et")
        self.gridLayout.addWidget(self.kayit_et, 0, 0, 1, 1)
        self.odalari_goster = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.odalari_goster.setObjectName("odalari_goster")
        self.gridLayout.addWidget(self.odalari_goster, 2, 0, 1, 1)
        self.giris_yap = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.giris_yap.setObjectName("giris_yap")
        self.gridLayout.addWidget(self.giris_yap, 1, 0, 1, 1)
        self.cikis = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cikis.setObjectName("cikis")
        self.gridLayout.addWidget(self.cikis, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 458, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.baglantiolustur()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.kayit_et.clicked.connect(self.kayit_et_islem)
        self.giris_yap.clicked.connect(self.giris_yapislem)
        self.odalari_goster.clicked.connect(self.odalari_gosterislem)
        self.cikis.clicked.connect(self.cikis_islem)

    def odalari_gosterislem(self):

        try:
            print("Odaları Gösterme İşlemi Seçildi")
            dialog = Goster_Ui_Dialog(self.gosterbaglantiolustur)
            dialog.exec_()

        except Exception as e:
            print(f"Sayfa Oluşturulurken Hata Oluştu : {e}")

    def giris_yapislem(self):

        try:
            print("Giriş İşlemi Seçildi")
            dialog = Giris_Ui_Dialog(self.girisbaglantiolustur)
            dialog.exec_()

        except Exception as e:
            print(f"Sayfa Oluşturulurken Hata Oluştu : {e}")

    def cikis_islem(self):
        try:
            app.quit()
        except Exception as e:
            print(f"Hata Oluştu : {e} ")

    def kayit_et_islem(self):

        try:
            print("Kayıt İşlemi Seçildi")
            dialog = Kayit_Ui_Dialog(self.baglantiolustur)
            dialog.exec_()

        except Exception as e:
            print(f"Sayfa Oluşturulurken Hata Oluştu : {e}")

    def girisbaglantiolustur(self):

        otel = sqlite3.connect("Otel.db")
        self.cursor = otel.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS odalar(isim TEXT,Oda_numarası TEXT,Telefon_numarası TEXT,TC_Kimlik TEXT)")
        otel.commit()
        return otel
    def gosterbaglantiolustur(self):

        otel = sqlite3.connect("Otel.db")
        self.cursor = otel.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS odalar(isim TEXT,Oda_numarası TEXT,Telefon_numarası TEXT,TC_Kimlik TEXT)")
        otel.commit()
        return otel




    def baglantiolustur(self):

        otel = sqlite3.connect("Otel.db")
        self.cursor = otel.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS odalar(isim TEXT,Oda_numarası TEXT,Telefon_numarası TEXT,TC_Kimlik TEXT)")
        otel.commit()
        return otel




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "     Otel"))
        self.kayit_et.setText(_translate("MainWindow", "Kayıt Et"))
        self.odalari_goster.setText(_translate("MainWindow", "Odaları Göster"))
        self.giris_yap.setText(_translate("MainWindow", "Giriş Yap"))
        self.cikis.setText(_translate("MainWindow", "Çıkış"))


class Kayit_Ui_Dialog(QtWidgets.QDialog):

    def __init__(self,baglantiolustur):
        super().__init__()
        self.baglantiolustur = baglantiolustur
        self.setupUi()


    def setupUi(self):
        self.setWindowTitle("Kayıt Et")
        self.resize(518, 406)
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 70, 491, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.kayit_oda_numarasi = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.kayit_oda_numarasi.setObjectName("kayit_oda_numarasi")
        self.gridLayout.addWidget(self.kayit_oda_numarasi, 1, 1, 1, 1)
        self.kayit_isim_soyisim = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.kayit_isim_soyisim.setObjectName("kayit_isim_soyisim")
        self.gridLayout.addWidget(self.kayit_isim_soyisim, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.kayit_telefon_numarasi = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.kayit_telefon_numarasi.setObjectName("kayit_telefon_numarasi")
        self.gridLayout.addWidget(self.kayit_telefon_numarasi, 2, 1, 1, 1)
        self.kayit_tc_numarasi = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.kayit_tc_numarasi.setObjectName("kayit_tc_numarasi")
        self.gridLayout.addWidget(self.kayit_tc_numarasi, 3, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(120, 0, 421, 60))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 280, 301, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.kayit_onay = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.kayit_onay.setObjectName("kayit_onay")
        self.horizontalLayout.addWidget(self.kayit_onay)
        self.kayit_iptal = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.kayit_iptal.setObjectName("kayit_iptal")
        self.horizontalLayout.addWidget(self.kayit_iptal)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.kayit_onay.clicked.connect(self.kayit_onayislem)
        self.kayit_iptal.clicked.connect(self.kayit_iptalislem)

    def kayit_onayislem(self):
        try:
            isim_soyisim = self.kayit_isim_soyisim.text()
            oda_numarasi = self.kayit_oda_numarasi.text()
            telefon_numarasi = self.kayit_telefon_numarasi.text()
            tc_numarasi = self.kayit_tc_numarasi.text()
            if not (isim_soyisim and oda_numarasi and telefon_numarasi and tc_numarasi):
                QtWidgets.QMessageBox.warning(self, "Hata", "Tüm alanları doldurmalısınız.")
                return

            otel = self.baglantiolustur()
            self.cursor = otel.cursor()

            self.cursor.execute("INSERT INTO odalar (isim,Oda_numarası,Telefon_numarası,TC_Kimlik) VALUES (?,?,?,?)",(isim_soyisim,oda_numarasi,telefon_numarasi,tc_numarasi))
            otel.commit()

            self.accept()
        except Exception as e:

            print(f"Hata Bulundu : {e}")
    def kayit_iptalislem(self):

        try:
            self.accept()
        except:
            print("Program Kapatılamadı")


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Oda Numarası : "))
        self.label.setText(_translate("Dialog", "İsim-Soyisim : "))
        self.label_4.setText(_translate("Dialog", "Telefon Numarası :"))
        self.label_5.setText(_translate("Dialog", "TC Kimlik Numarası : "))
        self.label_3.setText(_translate("Dialog", "Kayıt İşlemi"))
        self.kayit_onay.setText(_translate("Dialog", "Onayla"))
        self.kayit_iptal.setText(_translate("Dialog", "İptal"))

class Giris_Ui_Dialog(QtWidgets.QDialog):
    def __init__(self,girisbaglantiolustur):
        super().__init__()
        self.girisbaglantiolustur = girisbaglantiolustur
        self.setupUi()


    def setupUi(self):
        self.resize(535, 434)
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 0, 376, 118))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 140, 491, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.giris_oda_numarasi = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.giris_oda_numarasi.setObjectName("giris_oda_numarasi")
        self.gridLayout.addWidget(self.giris_oda_numarasi, 1, 1, 1, 1)
        self.giris_isim_soyisim = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.giris_isim_soyisim.setObjectName("giris_isim_soyisim")
        self.gridLayout.addWidget(self.giris_isim_soyisim, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.giris_telefon_numarasi = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.giris_telefon_numarasi.setObjectName("giris_telefon_numarasi")
        self.gridLayout.addWidget(self.giris_telefon_numarasi, 2, 1, 1, 1)
        self.giris_tc_numarasi = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.giris_tc_numarasi.setObjectName("giris_tc_numarasi")
        self.gridLayout.addWidget(self.giris_tc_numarasi, 3, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 340, 331, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.giris_sorgula = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.giris_sorgula.setObjectName("giris_sorgula")
        self.horizontalLayout.addWidget(self.giris_sorgula)
        self.giris_cikis = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.giris_cikis.setObjectName("giris_cikis")
        self.horizontalLayout.addWidget(self.giris_cikis)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.giris_sorgula.clicked.connect(self.sorgula)
        self.giris_cikis.clicked.connect(self.giris_cikisislem)

    def giris_cikisislem(self):

        try:
            self.accept()

        except:
            print("Çıkış Yapılamadı")


    def sorgula(self):

        try:

            isim_soyisim = self.giris_isim_soyisim.text()
            oda_numarasi = self.giris_oda_numarasi.text()
            telefon_numarasi = self.giris_telefon_numarasi.text()
            tc_numarasi = self.giris_tc_numarasi.text()
            if not (isim_soyisim and oda_numarasi and telefon_numarasi and tc_numarasi):
                QtWidgets.QMessageBox.warning(self, "Hata", "Tüm alanları doldurmalısınız.")
                return



            otel = self.girisbaglantiolustur()
            self.cursor = otel.cursor()


            self.cursor.execute("SELECT * FROM odalar WHERE LOWER(isim) = LOWER(?) AND Oda_numarası = ? AND Telefon_numarası = ? AND TC_Kimlik = ?",(isim_soyisim,oda_numarasi,telefon_numarasi,tc_numarasi))
            sonuc = self.cursor.fetchone()

            if sonuc:
                print("Odanıza Giriş Yapabilirsiniz")
            else :
                print("Hata : Müşteri Bulunamadı")




        except Exception as e:
            print(f"Sorguda Hata Bulundu {e}")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Giriş Yap"))
        self.label_2.setText(_translate("Dialog", "Oda Numarası : "))
        self.label_3.setText(_translate("Dialog", "İsim-Soyisim : "))
        self.label_4.setText(_translate("Dialog", "Telefon Numarası :"))
        self.label_5.setText(_translate("Dialog", "TC Kimlik Numarası : "))
        self.giris_sorgula.setText(_translate("Dialog", "Sorgula"))
        self.giris_cikis.setText(_translate("Dialog", "Çıkış"))


# -*- coding: utf-8 -*-
import sqlite3

# Form implementation generated from reading ui file 'C:\otelmenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(458, 429)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-20, 10, 531, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(529, 119))
        self.label.setMaximumSize(QtCore.QSize(529, 119))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 160, 411, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.kayit_et = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.kayit_et.setObjectName("kayit_et")
        self.gridLayout.addWidget(self.kayit_et, 0, 0, 1, 1)
        self.odalari_goster = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.odalari_goster.setObjectName("odalari_goster")
        self.gridLayout.addWidget(self.odalari_goster, 2, 0, 1, 1)
        self.giris_yap = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.giris_yap.setObjectName("giris_yap")
        self.gridLayout.addWidget(self.giris_yap, 1, 0, 1, 1)
        self.cikis = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cikis.setObjectName("cikis")
        self.gridLayout.addWidget(self.cikis, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 458, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.baglantiolustur()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.kayit_et.clicked.connect(self.kayit_et_islem)
        self.giris_yap.clicked.connect(self.giris_yapislem)
        self.odalari_goster.clicked.connect(self.odalari_gosterislem)
        self.cikis.clicked.connect(self.cikis_islem)

    def odalari_gosterislem(self):

        try:
            print("Odaları Gösterme İşlemi Seçildi")
            dialog = Goster_Ui_Dialog(self.gosterbaglantiolustur)
            dialog.exec_()

        except Exception as e:
            print(f"Sayfa Oluşturulurken Hata Oluştu : {e}")

    def giris_yapislem(self):

        try:
            print("Giriş İşlemi Seçildi")
            dialog = Giris_Ui_Dialog(self.girisbaglantiolustur)
            dialog.exec_()

        except Exception as e:
            print(f"Sayfa Oluşturulurken Hata Oluştu : {e}")

    def cikis_islem(self):
        try:
            app.quit()
        except Exception as e:
            print(f"Hata Oluştu : {e} ")

    def kayit_et_islem(self):

        try:
            print("Kayıt İşlemi Seçildi")
            dialog = Kayit_Ui_Dialog(self.baglantiolustur)
            dialog.exec_()

        except Exception as e:
            print(f"Sayfa Oluşturulurken Hata Oluştu : {e}")

    def girisbaglantiolustur(self):

        otel = sqlite3.connect("Otel.db")
        self.cursor = otel.cursor()

        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS odalar(isim TEXT,Oda_numarası TEXT,Telefon_numarası TEXT,TC_Kimlik TEXT)")
        otel.commit()
        return otel

    def gosterbaglantiolustur(self):

        otel = sqlite3.connect("Otel.db")
        self.cursor = otel.cursor()

        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS odalar(isim TEXT,Oda_numarası TEXT,Telefon_numarası TEXT,TC_Kimlik TEXT)")
        otel.commit()
        return otel

    def baglantiolustur(self):

        otel = sqlite3.connect("Otel.db")
        self.cursor = otel.cursor()

        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS odalar(isim TEXT,Oda_numarası TEXT,Telefon_numarası TEXT,TC_Kimlik TEXT)")
        otel.commit()
        return otel

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "     Otel"))
        self.kayit_et.setText(_translate("MainWindow", "Kayıt Et"))
        self.odalari_goster.setText(_translate("MainWindow", "Odaları Göster"))
        self.giris_yap.setText(_translate("MainWindow", "Giriş Yap"))
        self.cikis.setText(_translate("MainWindow", "Çıkış"))


class Kayit_Ui_Dialog(QtWidgets.QDialog):

    def __init__(self, baglantiolustur):
        super().__init__()
        self.baglantiolustur = baglantiolustur
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Kayıt Et")
        self.resize(518, 406)
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 70, 491, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.kayit_oda_numarasi = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.kayit_oda_numarasi.setObjectName("kayit_oda_numarasi")
        self.gridLayout.addWidget(self.kayit_oda_numarasi, 1, 1, 1, 1)
        self.kayit_isim_soyisim = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.kayit_isim_soyisim.setObjectName("kayit_isim_soyisim")
        self.gridLayout.addWidget(self.kayit_isim_soyisim, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.kayit_telefon_numarasi = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.kayit_telefon_numarasi.setObjectName("kayit_telefon_numarasi")
        self.gridLayout.addWidget(self.kayit_telefon_numarasi, 2, 1, 1, 1)
        self.kayit_tc_numarasi = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.kayit_tc_numarasi.setObjectName("kayit_tc_numarasi")
        self.gridLayout.addWidget(self.kayit_tc_numarasi, 3, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(120, 0, 421, 60))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 280, 301, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.kayit_onay = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.kayit_onay.setObjectName("kayit_onay")
        self.horizontalLayout.addWidget(self.kayit_onay)
        self.kayit_iptal = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.kayit_iptal.setObjectName("kayit_iptal")
        self.horizontalLayout.addWidget(self.kayit_iptal)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.kayit_onay.clicked.connect(self.kayit_onayislem)
        self.kayit_iptal.clicked.connect(self.kayit_iptalislem)

    def kayit_onayislem(self):
        try:
            isim_soyisim = self.kayit_isim_soyisim.text()
            oda_numarasi = self.kayit_oda_numarasi.text()
            telefon_numarasi = self.kayit_telefon_numarasi.text()
            tc_numarasi = self.kayit_tc_numarasi.text()
            if not (isim_soyisim and oda_numarasi and telefon_numarasi and tc_numarasi):
                QtWidgets.QMessageBox.warning(self, "Hata", "Tüm alanları doldurmalısınız.")
                return

            otel = self.baglantiolustur()
            self.cursor = otel.cursor()

            self.cursor.execute("INSERT INTO odalar (isim,Oda_numarası,Telefon_numarası,TC_Kimlik) VALUES (?,?,?,?)",
                                (isim_soyisim, oda_numarasi, telefon_numarasi, tc_numarasi))
            otel.commit()

            self.accept()
        except Exception as e:

            print(f"Hata Bulundu : {e}")

    def kayit_iptalislem(self):

        try:
            self.accept()
        except:
            print("Program Kapatılamadı")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Oda Numarası : "))
        self.label.setText(_translate("Dialog", "İsim-Soyisim : "))
        self.label_4.setText(_translate("Dialog", "Telefon Numarası :"))
        self.label_5.setText(_translate("Dialog", "TC Kimlik Numarası : "))
        self.label_3.setText(_translate("Dialog", "Kayıt İşlemi"))
        self.kayit_onay.setText(_translate("Dialog", "Onayla"))
        self.kayit_iptal.setText(_translate("Dialog", "İptal"))


class Giris_Ui_Dialog(QtWidgets.QDialog):
    def __init__(self, girisbaglantiolustur):
        super().__init__()
        self.girisbaglantiolustur = girisbaglantiolustur
        self.setupUi()

    def setupUi(self):
        self.resize(535, 434)
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 0, 376, 118))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 140, 491, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.giris_oda_numarasi = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.giris_oda_numarasi.setObjectName("giris_oda_numarasi")
        self.gridLayout.addWidget(self.giris_oda_numarasi, 1, 1, 1, 1)
        self.giris_isim_soyisim = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.giris_isim_soyisim.setObjectName("giris_isim_soyisim")
        self.gridLayout.addWidget(self.giris_isim_soyisim, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.giris_telefon_numarasi = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.giris_telefon_numarasi.setObjectName("giris_telefon_numarasi")
        self.gridLayout.addWidget(self.giris_telefon_numarasi, 2, 1, 1, 1)
        self.giris_tc_numarasi = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.giris_tc_numarasi.setObjectName("giris_tc_numarasi")
        self.gridLayout.addWidget(self.giris_tc_numarasi, 3, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 340, 331, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.giris_sorgula = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.giris_sorgula.setObjectName("giris_sorgula")
        self.horizontalLayout.addWidget(self.giris_sorgula)
        self.giris_cikis = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.giris_cikis.setObjectName("giris_cikis")
        self.horizontalLayout.addWidget(self.giris_cikis)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.giris_sorgula.clicked.connect(self.sorgula)
        self.giris_cikis.clicked.connect(self.giris_cikisislem)

    def giris_cikisislem(self):

        try:
            self.accept()

        except:
            print("Çıkış Yapılamadı")

    def sorgula(self):

        try:

            isim_soyisim = self.giris_isim_soyisim.text()
            oda_numarasi = self.giris_oda_numarasi.text()
            telefon_numarasi = self.giris_telefon_numarasi.text()
            tc_numarasi = self.giris_tc_numarasi.text()
            if not (isim_soyisim and oda_numarasi and telefon_numarasi and tc_numarasi):
                QtWidgets.QMessageBox.warning(self, "Hata", "Tüm alanları doldurmalısınız.")
                return

            otel = self.girisbaglantiolustur()
            self.cursor = otel.cursor()

            self.cursor.execute(
                "SELECT * FROM odalar WHERE LOWER(isim) = LOWER(?) AND Oda_numarası = ? AND Telefon_numarası = ? AND TC_Kimlik = ?",
                (isim_soyisim, oda_numarasi, telefon_numarasi, tc_numarasi))
            sonuc = self.cursor.fetchone()

            if sonuc:
                print("Odanıza Giriş Yapabilirsiniz")
            else:
                print("Hata : Müşteri Bulunamadı")




        except Exception as e:
            print(f"Sorguda Hata Bulundu {e}")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Giriş Yap"))
        self.label_2.setText(_translate("Dialog", "Oda Numarası : "))
        self.label_3.setText(_translate("Dialog", "İsim-Soyisim : "))
        self.label_4.setText(_translate("Dialog", "Telefon Numarası :"))
        self.label_5.setText(_translate("Dialog", "TC Kimlik Numarası : "))
        self.giris_sorgula.setText(_translate("Dialog", "Sorgula"))
        self.giris_cikis.setText(_translate("Dialog", "Çıkış"))


class Goster_Ui_Dialog(QtWidgets.QDialog):
    def __init__(self, gosterbaglantiolustur):
        super().__init__()
        self.otel = gosterbaglantiolustur
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(506, 402)
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 491, 311))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.goster_liste = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.goster_liste.setObjectName("goster_liste")
        self.gridLayout.addWidget(self.goster_liste, 0, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 330, 491, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.goster_cikis = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.goster_cikis.setObjectName("goster_cikis")
        self.verticalLayout.addWidget(self.goster_cikis)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.loadrooms()
        self.goster_cikis.clicked.connect(self.goster_cikis_islem)

    def goster_cikis_islem(self):

        try:
            self.accept()
        except Exception as e:
            print(f"Çıkış Yapılamadı : {e}")

    def loadrooms(self):
        try:
            con = sqlite3.connect("Otel.db")
            cursor = con.cursor()

            cursor.execute("SELECT * FROM odalar")  # 'odalar' tablosundaki tüm verileri seç
            rows = cursor.fetchall()  # Tüm satırları al

            # Listeye verileri ekle
            for row in rows:
                self.goster_liste.addItem(str(row))


        except Exception as e:

            print(f"Hata Bulundu : {e}")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.goster_cikis.setText(_translate("Dialog", "Çıkış"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.goster_cikis.setText(_translate("Dialog", "Çıkış"))







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
