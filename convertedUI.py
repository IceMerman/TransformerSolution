# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trafos.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(800, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        Form.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/Icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 201, 581))
        self.tabWidget.setMaximumSize(QtCore.QSize(1000, 800))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupBox_8 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_8.setGeometry(QtCore.QRect(1, 10, 191, 201))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.layoutWidget = QtGui.QWidget(self.groupBox_8)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 20, 171, 181))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_4.addWidget(self.label_9)
        self.leLoadS = QtGui.QLineEdit(self.layoutWidget)
        self.leLoadS.setObjectName(_fromUtf8("leLoadS"))
        self.verticalLayout_4.addWidget(self.leLoadS)
        self.label_10 = QtGui.QLabel(self.layoutWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_4.addWidget(self.label_10)
        self.leLoadV = QtGui.QLineEdit(self.layoutWidget)
        self.leLoadV.setObjectName(_fromUtf8("leLoadV"))
        self.verticalLayout_4.addWidget(self.leLoadV)
        self.label_11 = QtGui.QLabel(self.layoutWidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_4.addWidget(self.label_11)
        self.leFP = QtGui.QLineEdit(self.layoutWidget)
        self.leFP.setObjectName(_fromUtf8("leFP"))
        self.verticalLayout_4.addWidget(self.leFP)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.rbLeading = QtGui.QRadioButton(self.layoutWidget)
        self.rbLeading.setObjectName(_fromUtf8("rbLeading"))
        self.horizontalLayout.addWidget(self.rbLeading)
        self.rbLag = QtGui.QRadioButton(self.layoutWidget)
        self.rbLag.setChecked(True)
        self.rbLag.setObjectName(_fromUtf8("rbLag"))
        self.horizontalLayout.addWidget(self.rbLag)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.groupBox_5 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(1, 220, 191, 331))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.layoutWidget1 = QtGui.QWidget(self.groupBox_5)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 20, 171, 301))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_12 = QtGui.QLabel(self.layoutWidget1)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_3.addWidget(self.label_12)
        self.leRatedPower = QtGui.QLineEdit(self.layoutWidget1)
        self.leRatedPower.setObjectName(_fromUtf8("leRatedPower"))
        self.verticalLayout_3.addWidget(self.leRatedPower)
        self.label_13 = QtGui.QLabel(self.layoutWidget1)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_3.addWidget(self.label_13)
        self.lnPrimaryV = QtGui.QLineEdit(self.layoutWidget1)
        self.lnPrimaryV.setObjectName(_fromUtf8("lnPrimaryV"))
        self.verticalLayout_3.addWidget(self.lnPrimaryV)
        self.label_14 = QtGui.QLabel(self.layoutWidget1)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_3.addWidget(self.label_14)
        self.leSecondaryV = QtGui.QLineEdit(self.layoutWidget1)
        self.leSecondaryV.setObjectName(_fromUtf8("leSecondaryV"))
        self.verticalLayout_3.addWidget(self.leSecondaryV)
        self.label_17 = QtGui.QLabel(self.layoutWidget1)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.verticalLayout_3.addWidget(self.label_17)
        self.leSCimpedance = QtGui.QLineEdit(self.layoutWidget1)
        self.leSCimpedance.setEnabled(True)
        self.leSCimpedance.setObjectName(_fromUtf8("leSCimpedance"))
        self.verticalLayout_3.addWidget(self.leSCimpedance)
        self.label_15 = QtGui.QLabel(self.layoutWidget1)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout_3.addWidget(self.label_15)
        self.lePfe = QtGui.QLineEdit(self.layoutWidget1)
        self.lePfe.setObjectName(_fromUtf8("lePfe"))
        self.verticalLayout_3.addWidget(self.lePfe)
        self.label_16 = QtGui.QLabel(self.layoutWidget1)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout_3.addWidget(self.label_16)
        self.leQfd = QtGui.QLineEdit(self.layoutWidget1)
        self.leQfd.setObjectName(_fromUtf8("leQfd"))
        self.verticalLayout_3.addWidget(self.leQfd)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab)
        self.groupBox_4.setGeometry(QtCore.QRect(1, 240, 191, 231))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.layoutWidget_2 = QtGui.QWidget(self.groupBox_4)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 20, 171, 201))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_6 = QtGui.QLabel(self.layoutWidget_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_2.addWidget(self.label_6)
        self.lescVoltage = QtGui.QLineEdit(self.layoutWidget_2)
        self.lescVoltage.setToolTip(_fromUtf8(""))
        self.lescVoltage.setObjectName(_fromUtf8("lescVoltage"))
        self.verticalLayout_2.addWidget(self.lescVoltage)
        self.label_7 = QtGui.QLabel(self.layoutWidget_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_2.addWidget(self.label_7)
        self.leSCcurrent = QtGui.QLineEdit(self.layoutWidget_2)
        self.leSCcurrent.setToolTip(_fromUtf8(""))
        self.leSCcurrent.setObjectName(_fromUtf8("leSCcurrent"))
        self.verticalLayout_2.addWidget(self.leSCcurrent)
        self.label_8 = QtGui.QLabel(self.layoutWidget_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_2.addWidget(self.label_8)
        self.leCUlosses = QtGui.QLineEdit(self.layoutWidget_2)
        self.leCUlosses.setToolTip(_fromUtf8(""))
        self.leCUlosses.setObjectName(_fromUtf8("leCUlosses"))
        self.verticalLayout_2.addWidget(self.leCUlosses)
        self.rbSCsecondary = QtGui.QRadioButton(self.layoutWidget_2)
        self.rbSCsecondary.setChecked(True)
        self.rbSCsecondary.setObjectName(_fromUtf8("rbSCsecondary"))
        self.verticalLayout_2.addWidget(self.rbSCsecondary)
        self.rbSCprimary = QtGui.QRadioButton(self.layoutWidget_2)
        self.rbSCprimary.setObjectName(_fromUtf8("rbSCprimary"))
        self.verticalLayout_2.addWidget(self.rbSCprimary)
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(1, 11, 191, 221))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.layoutWidget2 = QtGui.QWidget(self.groupBox_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(11, 21, 171, 191))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(self.layoutWidget2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.leRatedVoltage = QtGui.QLineEdit(self.layoutWidget2)
        self.leRatedVoltage.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.leRatedVoltage.setAutoFillBackground(False)
        self.leRatedVoltage.setObjectName(_fromUtf8("leRatedVoltage"))
        self.verticalLayout.addWidget(self.leRatedVoltage)
        self.label_4 = QtGui.QLabel(self.layoutWidget2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.l2ocCurrent = QtGui.QLineEdit(self.layoutWidget2)
        self.l2ocCurrent.setToolTip(_fromUtf8(""))
        self.l2ocCurrent.setObjectName(_fromUtf8("l2ocCurrent"))
        self.verticalLayout.addWidget(self.l2ocCurrent)
        self.label_5 = QtGui.QLabel(self.layoutWidget2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.leFELosses = QtGui.QLineEdit(self.layoutWidget2)
        self.leFELosses.setToolTip(_fromUtf8(""))
        self.leFELosses.setObjectName(_fromUtf8("leFELosses"))
        self.verticalLayout.addWidget(self.leFELosses)
        self.rbOCsecondary = QtGui.QRadioButton(self.layoutWidget2)
        self.rbOCsecondary.setChecked(True)
        self.rbOCsecondary.setObjectName(_fromUtf8("rbOCsecondary"))
        self.verticalLayout.addWidget(self.rbOCsecondary)
        self.rbOCprimary = QtGui.QRadioButton(self.layoutWidget2)
        self.rbOCprimary.setObjectName(_fromUtf8("rbOCprimary"))
        self.verticalLayout.addWidget(self.rbOCprimary)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.lblAbout = QtGui.QLabel(self.tab_3)
        self.lblAbout.setGeometry(QtCore.QRect(10, 0, 161, 201))
        self.lblAbout.setObjectName(_fromUtf8("lblAbout"))
        self.lblUdeA = QtGui.QLabel(self.tab_3)
        self.lblUdeA.setGeometry(QtCore.QRect(20, 210, 161, 221))
        self.lblUdeA.setText(_fromUtf8(""))
        self.lblUdeA.setPixmap(QtGui.QPixmap(_fromUtf8(":/image/logoUDEA.png")))
        self.lblUdeA.setScaledContents(True)
        self.lblUdeA.setObjectName(_fromUtf8("lblUdeA"))
        self.laGimel = QtGui.QLabel(self.tab_3)
        self.laGimel.setGeometry(QtCore.QRect(60, 450, 81, 81))
        self.laGimel.setText(_fromUtf8(""))
        self.laGimel.setPixmap(QtGui.QPixmap(_fromUtf8(":/image/gimel.png")))
        self.laGimel.setScaledContents(True)
        self.laGimel.setObjectName(_fromUtf8("laGimel"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(220, 10, 571, 581))
        self.groupBox.setMaximumSize(QtCore.QSize(1000, 800))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 20, 271, 121))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.layoutWidget3 = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 20, 241, 91))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.cbConection = QtGui.QComboBox(self.layoutWidget3)
        self.cbConection.setObjectName(_fromUtf8("cbConection"))
        self.cbConection.addItem(_fromUtf8(""))
        self.cbConection.addItem(_fromUtf8(""))
        self.cbConection.addItem(_fromUtf8(""))
        self.cbConection.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cbConection, 1, 1, 1, 1)
        self.cbMethod = QtGui.QComboBox(self.layoutWidget3)
        self.cbMethod.setObjectName(_fromUtf8("cbMethod"))
        self.cbMethod.addItem(_fromUtf8(""))
        self.cbMethod.addItem(_fromUtf8(""))
        self.cbMethod.addItem(_fromUtf8(""))
        self.cbMethod.addItem(_fromUtf8(""))
        self.cbMethod.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cbMethod, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget3)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lblIMG = QtGui.QLabel(self.groupBox)
        self.lblIMG.setGeometry(QtCore.QRect(70, 330, 421, 191))
        self.lblIMG.setMouseTracking(False)
        self.lblIMG.setText(_fromUtf8(""))
        self.lblIMG.setTextFormat(QtCore.Qt.AutoText)
        self.lblIMG.setPixmap(QtGui.QPixmap(_fromUtf8(":/image/trafoIMG.png")))
        self.lblIMG.setScaledContents(True)
        self.lblIMG.setObjectName(_fromUtf8("lblIMG"))
        self.lblEqImpedance = QtGui.QLabel(self.groupBox)
        self.lblEqImpedance.setGeometry(QtCore.QRect(270, 300, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.lblEqImpedance.setFont(font)
        self.lblEqImpedance.setTextFormat(QtCore.Qt.RichText)
        self.lblEqImpedance.setObjectName(_fromUtf8("lblEqImpedance"))
        self.groupBox_6 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_6.setGeometry(QtCore.QRect(330, 20, 221, 121))
        self.groupBox_6.setToolTip(_fromUtf8(""))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.layoutWidget4 = QtGui.QWidget(self.groupBox_6)
        self.layoutWidget4.setGeometry(QtCore.QRect(10, 20, 201, 91))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.cbTestData = QtGui.QCheckBox(self.layoutWidget4)
        self.cbTestData.setObjectName(_fromUtf8("cbTestData"))
        self.verticalLayout_7.addWidget(self.cbTestData)
        self.btnSolve = QtGui.QPushButton(self.layoutWidget4)
        self.btnSolve.setToolTip(_fromUtf8(""))
        self.btnSolve.setObjectName(_fromUtf8("btnSolve"))
        self.verticalLayout_7.addWidget(self.btnSolve)
        self.lblVLoad = QtGui.QLabel(self.groupBox)
        self.lblVLoad.setGeometry(QtCore.QRect(470, 420, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.lblVLoad.setFont(font)
        self.lblVLoad.setTextFormat(QtCore.Qt.RichText)
        self.lblVLoad.setObjectName(_fromUtf8("lblVLoad"))
        self.lblSLoad = QtGui.QLabel(self.groupBox)
        self.lblSLoad.setGeometry(QtCore.QRect(470, 490, 91, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.lblSLoad.setFont(font)
        self.lblSLoad.setTextFormat(QtCore.Qt.RichText)
        self.lblSLoad.setObjectName(_fromUtf8("lblSLoad"))
        self.lblVIn = QtGui.QLabel(self.groupBox)
        self.lblVIn.setGeometry(QtCore.QRect(30, 400, 71, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.lblVIn.setFont(font)
        self.lblVIn.setTextFormat(QtCore.Qt.RichText)
        self.lblVIn.setObjectName(_fromUtf8("lblVIn"))
        self.lblIload = QtGui.QLabel(self.groupBox)
        self.lblIload.setGeometry(QtCore.QRect(420, 300, 91, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.lblIload.setFont(font)
        self.lblIload.setTextFormat(QtCore.Qt.RichText)
        self.lblIload.setObjectName(_fromUtf8("lblIload"))
        self.lblIIn = QtGui.QLabel(self.groupBox)
        self.lblIIn.setGeometry(QtCore.QRect(120, 290, 91, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblIIn.setFont(font)
        self.lblIIn.setTextFormat(QtCore.Qt.RichText)
        self.lblIIn.setObjectName(_fromUtf8("lblIIn"))
        self.lblIm = QtGui.QLabel(self.groupBox)
        self.lblIm.setGeometry(QtCore.QRect(250, 480, 161, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.lblIm.setFont(font)
        self.lblIm.setTextFormat(QtCore.Qt.RichText)
        self.lblIm.setObjectName(_fromUtf8("lblIm"))
        self.lblVDrop = QtGui.QLabel(self.groupBox)
        self.lblVDrop.setGeometry(QtCore.QRect(300, 360, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.lblVDrop.setFont(font)
        self.lblVDrop.setTextFormat(QtCore.Qt.RichText)
        self.lblVDrop.setObjectName(_fromUtf8("lblVDrop"))
        self.lblZm = QtGui.QLabel(self.groupBox)
        self.lblZm.setGeometry(QtCore.QRect(260, 410, 81, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.lblZm.setFont(font)
        self.lblZm.setTextFormat(QtCore.Qt.RichText)
        self.lblZm.setObjectName(_fromUtf8("lblZm"))
        self.layoutWidget5 = QtGui.QWidget(self.groupBox)
        self.layoutWidget5.setGeometry(QtCore.QRect(70, 160, 491, 100))
        self.layoutWidget5.setObjectName(_fromUtf8("layoutWidget5"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.lblanom = QtGui.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.lblanom.setFont(font)
        self.lblanom.setTextFormat(QtCore.Qt.RichText)
        self.lblanom.setObjectName(_fromUtf8("lblanom"))
        self.verticalLayout_5.addWidget(self.lblanom)
        self.lbla = QtGui.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.lbla.setFont(font)
        self.lbla.setTextFormat(QtCore.Qt.RichText)
        self.lbla.setObjectName(_fromUtf8("lbla"))
        self.verticalLayout_5.addWidget(self.lbla)
        self.lblRm = QtGui.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.lblRm.setFont(font)
        self.lblRm.setTextFormat(QtCore.Qt.RichText)
        self.lblRm.setObjectName(_fromUtf8("lblRm"))
        self.verticalLayout_5.addWidget(self.lblRm)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.lblPfe = QtGui.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.lblPfe.setFont(font)
        self.lblPfe.setTextFormat(QtCore.Qt.RichText)
        self.lblPfe.setObjectName(_fromUtf8("lblPfe"))
        self.verticalLayout_6.addWidget(self.lblPfe)
        self.lblPcu = QtGui.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.lblPcu.setFont(font)
        self.lblPcu.setTextFormat(QtCore.Qt.RichText)
        self.lblPcu.setObjectName(_fromUtf8("lblPcu"))
        self.verticalLayout_6.addWidget(self.lblPcu)
        self.lblXm = QtGui.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.lblXm.setFont(font)
        self.lblXm.setTextFormat(QtCore.Qt.RichText)
        self.lblXm.setObjectName(_fromUtf8("lblXm"))
        self.verticalLayout_6.addWidget(self.lblXm)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.lbleffi = QtGui.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.lbleffi.setFont(font)
        self.lbleffi.setTextFormat(QtCore.Qt.RichText)
        self.lbleffi.setObjectName(_fromUtf8("lbleffi"))
        self.verticalLayout_8.addWidget(self.lbleffi)
        self.lblreg = QtGui.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.lblreg.setFont(font)
        self.lblreg.setTextFormat(QtCore.Qt.RichText)
        self.lblreg.setObjectName(_fromUtf8("lblreg"))
        self.verticalLayout_8.addWidget(self.lblreg)
        self.lblFPin = QtGui.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.lblFPin.setFont(font)
        self.lblFPin.setTextFormat(QtCore.Qt.RichText)
        self.lblFPin.setObjectName(_fromUtf8("lblFPin"))
        self.verticalLayout_8.addWidget(self.lblFPin)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.tabWidget, self.leLoadS)
        Form.setTabOrder(self.leLoadS, self.leLoadV)
        Form.setTabOrder(self.leLoadV, self.leFP)
        Form.setTabOrder(self.leFP, self.rbLeading)
        Form.setTabOrder(self.rbLeading, self.rbLag)
        Form.setTabOrder(self.rbLag, self.leRatedPower)
        Form.setTabOrder(self.leRatedPower, self.lnPrimaryV)
        Form.setTabOrder(self.lnPrimaryV, self.leSecondaryV)
        Form.setTabOrder(self.leSecondaryV, self.leSCimpedance)
        Form.setTabOrder(self.leSCimpedance, self.lePfe)
        Form.setTabOrder(self.lePfe, self.leQfd)
        Form.setTabOrder(self.leQfd, self.cbMethod)
        Form.setTabOrder(self.cbMethod, self.cbConection)
        Form.setTabOrder(self.cbConection, self.cbTestData)
        Form.setTabOrder(self.cbTestData, self.btnSolve)
        Form.setTabOrder(self.btnSolve, self.leRatedVoltage)
        Form.setTabOrder(self.leRatedVoltage, self.l2ocCurrent)
        Form.setTabOrder(self.l2ocCurrent, self.leFELosses)
        Form.setTabOrder(self.leFELosses, self.lescVoltage)
        Form.setTabOrder(self.lescVoltage, self.leSCcurrent)
        Form.setTabOrder(self.leSCcurrent, self.leCUlosses)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Three-Phase transformer solution", None))
        self.groupBox_8.setTitle(_translate("Form", "Load data", None))
        self.label_9.setText(_translate("Form", "Load power [VA]:", None))
        self.leLoadS.setToolTip(_translate("Form", "<html><head/><body><p>Apparent power magnitude in the load</p></body></html>", None))
        self.label_10.setText(_translate("Form", "Load voltage [V]:", None))
        self.leLoadV.setToolTip(_translate("Form", "<html><head/><body><p>Line-line voltage in the load</p></body></html>", None))
        self.label_11.setText(_translate("Form", "Power Factor:", None))
        self.leFP.setToolTip(_translate("Form", "<html><head/><body><p>Power factor</p></body></html>", None))
        self.rbLeading.setText(_translate("Form", "Capacitive\n"
"    (+)", None))
        self.rbLag.setText(_translate("Form", "Inductive\n"
"     (-)", None))
        self.groupBox_5.setTitle(_translate("Form", "Transformer data", None))
        self.label_12.setText(_translate("Form", "Rated power  [VA]", None))
        self.leRatedPower.setToolTip(_translate("Form", "<html><head/><body><p>Transformer apparent power magnitude</p></body></html>", None))
        self.label_13.setText(_translate("Form", "Rated primary voltage [V]:", None))
        self.lnPrimaryV.setToolTip(_translate("Form", "<html><head/><body><p>Line-line rated voltage in transformer primary side</p></body></html>", None))
        self.label_14.setText(_translate("Form", "Rated secondary voltage [V]:", None))
        self.leSecondaryV.setToolTip(_translate("Form", "<html><head/><body><p>Line-line rated voltage in transformer secondary side</p></body></html>", None))
        self.label_17.setText(_translate("Form", "Shortcircuit impedance [p.u.]:", None))
        self.leSCimpedance.setToolTip(_translate("Form", "<html><head/><body><p>Shortcircuit impedance in per unit. <span style=\" font-weight:600;\">Zeq</span> [p.u.]</p><p>Here the shortcircuit impedance can be written in two ways:</p><p>1) Rectangular coordinates as: R+Xj</p><p>    Where R is the resistence an X the reactance.</p><p>2) Polar coordinates as: A,b</p><p>    Where A is the magnitude and b the angle in degrees.</p></body></html>", None))
        self.label_15.setText(_translate("Form", "Nominal iron power losses [%]:", None))
        self.lePfe.setToolTip(_translate("Form", "<html><head/><body><p>If nominal iron power losses are 3%, then the input value must be: 3<br/></p></body></html>", None))
        self.label_16.setText(_translate("Form", "Nominal excitation power [%]:", None))
        self.leQfd.setToolTip(_translate("Form", "<html><head/><body><p>If the excitation power is 2%, then the input value must be: 2</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Parameters", None))
        self.groupBox_4.setToolTip(_translate("Form", "<html><head/><body><p>In these fields write the values obtained from the open circuit test, use the radio buttons to specify in which side the test was made.</p></body></html>", None))
        self.groupBox_4.setTitle(_translate("Form", "Shortcircuit test", None))
        self.label_6.setText(_translate("Form", "Shortcircuit voltage [V]:", None))
        self.label_7.setText(_translate("Form", "Shortcircuit current [A]:", None))
        self.label_8.setText(_translate("Form", "Copper losses [W]:", None))
        self.rbSCsecondary.setToolTip(_translate("Form", "<html><head/><body><p>Check if the test was made in the secondary side.</p></body></html>", None))
        self.rbSCsecondary.setText(_translate("Form", "Secondary side", None))
        self.rbSCprimary.setToolTip(_translate("Form", "<html><head/><body><p>Check if the test was made in the primary side.</p></body></html>", None))
        self.rbSCprimary.setText(_translate("Form", "Primary side", None))
        self.groupBox_3.setToolTip(_translate("Form", "<html><head/><body><p>In these fields write the values obtained from the open circuit test, use the radio buttons to specify in which side the test was made.</p></body></html>", None))
        self.groupBox_3.setTitle(_translate("Form", "Open circuit test", None))
        self.label_3.setText(_translate("Form", "Open-circuit voltage [V]:", None))
        self.leRatedVoltage.setToolTip(_translate("Form", "<html><head/><body><p>Open circuit voltage</p></body></html>", None))
        self.label_4.setText(_translate("Form", "Open circuit current [A]:", None))
        self.label_5.setText(_translate("Form", "Iron losses [W]:", None))
        self.rbOCsecondary.setToolTip(_translate("Form", "<html><head/><body><p>Check if the test was made in the secondary side.</p></body></html>", None))
        self.rbOCsecondary.setText(_translate("Form", "Secondary side", None))
        self.rbOCprimary.setToolTip(_translate("Form", "<html><head/><body><p>Check if the test was made in the primary side.</p></body></html>", None))
        self.rbOCprimary.setText(_translate("Form", "Primary side", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Test", None))
        self.lblAbout.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">V1.0</span></p><p><span style=\" font-weight:600; font-style:italic;\">Design and programming:</span></p><p><span style=\" font-weight:600; font-style:italic;\">- Juan Sierra Aguilar.</span></p><p><span style=\" font-weight:600; font-style:italic;\">- Robin Ortiz Castrillon.</span></p><p><span style=\" font-weight:600; font-style:italic;\">Advisement:</span></p><p><span style=\" font-weight:600; font-style:italic;\">- Alvaro Jaramillo Duque.</span></p><p><span style=\" font-weight:600; font-style:italic;\">- Nicolás Muñoz Galeano.</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "About", None))
        self.groupBox.setTitle(_translate("Form", "Three-Phase transformer solution", None))
        self.groupBox_2.setTitle(_translate("Form", "Solution type", None))
        self.cbConection.setToolTip(_translate("Form", "<html><head/><body><p>Conection type.</p><p>Relataion Primary/Secondary</p></body></html>", None))
        self.cbConection.setItemText(0, _translate("Form", "Delta-wye (Dy)", None))
        self.cbConection.setItemText(1, _translate("Form", "Delta-delta (Dd)", None))
        self.cbConection.setItemText(2, _translate("Form", "Wye-wye (Yy)", None))
        self.cbConection.setItemText(3, _translate("Form", "Wye-delta (Yd)", None))
        self.cbMethod.setToolTip(_translate("Form", "<html><head/><body><p>Choose a solution method.</p></body></html>", None))
        self.cbMethod.setItemText(0, _translate("Form", "Single-Primary (SP)", None))
        self.cbMethod.setItemText(1, _translate("Form", "Single-Secondary (SS)", None))
        self.cbMethod.setItemText(2, _translate("Form", "Three-Primary (TP)", None))
        self.cbMethod.setItemText(3, _translate("Form", "Three-Secondary (TS)", None))
        self.cbMethod.setItemText(4, _translate("Form", "Per Unit (p.u)", None))
        self.label_2.setText(_translate("Form", "Conection", None))
        self.label.setText(_translate("Form", "Solution variant", None))
        self.lblEqImpedance.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.groupBox_6.setTitle(_translate("Form", "Operation mode", None))
        self.cbTestData.setText(_translate("Form", "Use test data", None))
        self.btnSolve.setText(_translate("Form", "Solve", None))
        self.lblVLoad.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>", None))
        self.lblSLoad.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>", None))
        self.lblVIn.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.lblIload.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>", None))
        self.lblIIn.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.lblIm.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>", None))
        self.lblVDrop.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.lblZm.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>", None))
        self.lblanom.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>", None))
        self.lbla.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>", None))
        self.lblRm.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>", None))
        self.lblPfe.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>", None))
        self.lblPcu.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>", None))
        self.lblXm.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>", None))
        self.lbleffi.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>", None))
        self.lblreg.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>", None))
        self.lblFPin.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>", None))

import trafoRSC_rc
