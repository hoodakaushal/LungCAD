# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Thu Jun 11 09:31:00 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 627)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        self.userNameLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.userNameLineEdit.setObjectName(_fromUtf8("userNameLineEdit"))
        self.horizontalLayout_4.addWidget(self.userNameLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.passwordLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.passwordLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordLineEdit.setObjectName(_fromUtf8("passwordLineEdit"))
        self.horizontalLayout_3.addWidget(self.passwordLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.loginButton = QtGui.QPushButton(self.centralwidget)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.verticalLayout.addWidget(self.loginButton)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.uploadLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.uploadLineEdit.setObjectName(_fromUtf8("uploadLineEdit"))
        self.verticalLayout.addWidget(self.uploadLineEdit)
        self.uploadButton = QtGui.QPushButton(self.centralwidget)
        self.uploadButton.setObjectName(_fromUtf8("uploadButton"))
        self.verticalLayout.addWidget(self.uploadButton)
        self.generateResultsButton = QtGui.QPushButton(self.centralwidget)
        self.generateResultsButton.setObjectName(_fromUtf8("generateResultsButton"))
        self.verticalLayout.addWidget(self.generateResultsButton)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.downloadLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.downloadLineEdit.setObjectName(_fromUtf8("downloadLineEdit"))
        self.horizontalLayout_2.addWidget(self.downloadLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.numResultsSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.numResultsSpinBox.setMinimum(1)
        self.numResultsSpinBox.setMaximum(10)
        self.numResultsSpinBox.setObjectName(_fromUtf8("numResultsSpinBox"))
        self.horizontalLayout.addWidget(self.numResultsSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.downloadButton = QtGui.QPushButton(self.centralwidget)
        self.downloadButton.setObjectName(_fromUtf8("downloadButton"))
        self.verticalLayout.addWidget(self.downloadButton)
        self.statusLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.statusLabel.setFont(font)
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.verticalLayout.addWidget(self.statusLabel)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Transfer Files", None))
        self.label_6.setText(_translate("MainWindow", "Enter Username and Password to login", None))
        self.label_5.setText(_translate("MainWindow", "Username", None))
        self.label_4.setText(_translate("MainWindow", "Password", None))
        self.loginButton.setText(_translate("MainWindow", "Login", None))
        self.label.setText(_translate("MainWindow", "Enter Path of File to Upload", None))
        self.uploadButton.setText(_translate("MainWindow", "Upload!", None))
        self.generateResultsButton.setText(_translate("MainWindow", "Generate Matches", None))
        self.label_2.setText(_translate("MainWindow", "Enter Path to Dowload Matches", None))
        self.label_3.setText(_translate("MainWindow", "Choose Number of Matches to Download (max. 10)", None))
        self.downloadButton.setText(_translate("MainWindow", "Download", None))
        self.statusLabel.setText(_translate("MainWindow", "Idle", None))

