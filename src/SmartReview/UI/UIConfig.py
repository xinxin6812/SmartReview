# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIConfig.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(462, 464)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(370, 10, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.extractGroupBox = QtWidgets.QGroupBox(Dialog)
        self.extractGroupBox.setGeometry(QtCore.QRect(50, 360, 311, 61))
        self.extractGroupBox.setObjectName("extractGroupBox")
        self.radioProportion = QtWidgets.QRadioButton(self.extractGroupBox)
        self.radioProportion.setGeometry(QtCore.QRect(180, 30, 100, 20))
        self.radioProportion.setChecked(True)
        self.radioProportion.setObjectName("radioProportion")
        self.radioPriority = QtWidgets.QRadioButton(self.extractGroupBox)
        self.radioPriority.setGeometry(QtCore.QRect(30, 30, 100, 20))
        self.radioPriority.setChecked(False)
        self.radioPriority.setObjectName("radioPriority")
        self.radioPriority.raise_()
        self.radioProportion.raise_()
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 330, 381, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.countLabel = QtWidgets.QLabel(self.layoutWidget)
        self.countLabel.setObjectName("countLabel")
        self.horizontalLayout.addWidget(self.countLabel)
        self.countSlider = QtWidgets.QSlider(self.layoutWidget)
        self.countSlider.setOrientation(QtCore.Qt.Horizontal)
        self.countSlider.setObjectName("countSlider")
        self.horizontalLayout.addWidget(self.countSlider)
        self.countLCD = QtWidgets.QLCDNumber(self.layoutWidget)
        self.countLCD.setObjectName("countLCD")
        self.horizontalLayout.addWidget(self.countLCD)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(210, 10, 141, 301))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.timesLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.timesLabel.setObjectName("timesLabel")
        self.verticalLayout.addWidget(self.timesLabel)
        self.timesTable = QtWidgets.QTableWidget(self.layoutWidget1)
        self.timesTable.setColumnCount(2)
        self.timesTable.setObjectName("timesTable")
        self.timesTable.setRowCount(0)
        self.verticalLayout.addWidget(self.timesTable)
        self.layoutWidget2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(50, 10, 141, 301))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ranksLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.ranksLabel.setObjectName("ranksLabel")
        self.verticalLayout_2.addWidget(self.ranksLabel)
        self.ranksTable = QtWidgets.QTableWidget(self.layoutWidget2)
        self.ranksTable.setLineWidth(1)
        self.ranksTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ranksTable.setProperty("showDropIndicator", True)
        self.ranksTable.setDragDropOverwriteMode(True)
        self.ranksTable.setGridStyle(QtCore.Qt.SolidLine)
        self.ranksTable.setColumnCount(2)
        self.ranksTable.setObjectName("ranksTable")
        self.ranksTable.setRowCount(0)
        self.verticalLayout_2.addWidget(self.ranksTable)
        self.selectedLabel = QtWidgets.QLabel(Dialog)
        self.selectedLabel.setGeometry(QtCore.QRect(380, 90, 71, 20))
        self.selectedLabel.setObjectName("selectedLabel")
        self.selectedLCD = QtWidgets.QLCDNumber(Dialog)
        self.selectedLCD.setGeometry(QtCore.QRect(380, 120, 64, 23))
        self.selectedLCD.setObjectName("selectedLCD")
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.buttonBox.raise_()
        self.extractGroupBox.raise_()
        self.layoutWidget.raise_()
        self.selectedLabel.raise_()
        self.selectedLCD.raise_()

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "复习词提取"))
        self.extractGroupBox.setTitle(_translate("Dialog", "提取方式:"))
        self.radioProportion.setText(_translate("Dialog", "比例均摊"))
        self.radioPriority.setText(_translate("Dialog", "优先级"))
        self.countLabel.setText(_translate("Dialog", "复习量:"))
        self.timesLabel.setText(_translate("Dialog", "截止时间:"))
        self.timesTable.setSortingEnabled(True)
        self.ranksLabel.setText(_translate("Dialog", "掌握程度:"))
        self.ranksTable.setSortingEnabled(True)
        self.selectedLabel.setText(_translate("Dialog", "待背数量:"))

