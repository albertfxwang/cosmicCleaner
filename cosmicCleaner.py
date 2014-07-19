# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cosmicCleaner.ui'
#
# Created: Sat Jul 19 23:43:45 2014
#      by: PyQt4 UI code generator 4.10.2
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
        Form.resize(739, 542)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.widget = gingaWidget(self.groupBox)
        self.widget.setMinimumSize(QtCore.QSize(431, 451))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_2.addWidget(self.widget, 0, 0, 3, 1)
        self.listWidget = QtGui.QListWidget(self.groupBox)
        self.listWidget.setMinimumSize(QtCore.QSize(257, 379))
        self.listWidget.setMaximumSize(QtCore.QSize(257, 16777215))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout_2.addWidget(self.listWidget, 0, 1, 1, 2)
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setMinimumSize(QtCore.QSize(125, 23))
        self.pushButton.setMaximumSize(QtCore.QSize(125, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 1, 1, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout_2.addWidget(self.checkBox, 1, 2, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setMinimumSize(QtCore.QSize(125, 23))
        self.pushButton_2.setMaximumSize(QtCore.QSize(125, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setMinimumSize(QtCore.QSize(125, 23))
        self.pushButton_3.setMaximumSize(QtCore.QSize(125, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_2.addWidget(self.pushButton_3, 2, 2, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.groupBox)
        self.progressBar.setMinimumSize(QtCore.QSize(711, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout_2.addWidget(self.progressBar, 3, 0, 1, 3)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "Cosmic Cleaner", None))
        self.pushButton.setText(_translate("Form", "Add", None))
        self.checkBox.setText(_translate("Form", "Mask", None))
        self.pushButton_2.setText(_translate("Form", "Remove", None))
        self.pushButton_3.setText(_translate("Form", ":go", None))

from gingawidgetFile import gingaWidget
