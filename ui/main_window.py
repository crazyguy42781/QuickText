# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(791, 362)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_text = QtWidgets.QLabel(self.centralwidget)
        self.lbl_text.setObjectName("lbl_text")
        self.gridLayout_2.addWidget(self.lbl_text, 0, 0, 1, 1)
        self.ent_text_field = Textbox(self.centralwidget)
        self.ent_text_field.setMaximumSize(QtCore.QSize(800, 16777215))
        self.ent_text_field.setObjectName("ent_text_field")
        self.gridLayout_2.addWidget(self.ent_text_field, 1, 0, 1, 2)
        self.btn_variables = VariableButton(self.centralwidget)
        self.btn_variables.setMaximumSize(QtCore.QSize(71, 16777215))
        self.btn_variables.setObjectName("btn_variables")
        self.gridLayout_2.addWidget(self.btn_variables, 2, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lbl_item = QtWidgets.QLabel(self.centralwidget)
        self.lbl_item.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_item.setObjectName("lbl_item")
        self.gridLayout_3.addWidget(self.lbl_item, 2, 0, 1, 1)
        self.btn_csv_input = QtWidgets.QPushButton(self.centralwidget)
        self.btn_csv_input.setMaximumSize(QtCore.QSize(71, 16777215))
        self.btn_csv_input.setObjectName("btn_csv_input")
        self.gridLayout_3.addWidget(self.btn_csv_input, 2, 1, 1, 1)
        self.tbl_csv_viewer = CsvTable(self.centralwidget)
        self.tbl_csv_viewer.setMaximumSize(QtCore.QSize(1200, 16777215))
        self.tbl_csv_viewer.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbl_csv_viewer.setObjectName("tbl_csv_viewer")
        self.gridLayout_3.addWidget(self.tbl_csv_viewer, 1, 0, 1, 2)
        self.lbl_last_mod = QtWidgets.QLabel(self.centralwidget)
        self.lbl_last_mod.setObjectName("lbl_last_mod")
        self.gridLayout_3.addWidget(self.lbl_last_mod, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 1, 2, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_preview = QtWidgets.QLabel(self.centralwidget)
        self.lbl_preview.setObjectName("lbl_preview")
        self.gridLayout.addWidget(self.lbl_preview, 0, 0, 1, 1)
        self.ent_preview = QtWidgets.QTextEdit(self.centralwidget)
        self.ent_preview.setMaximumSize(QtCore.QSize(800, 16777215))
        self.ent_preview.setObjectName("ent_preview")
        self.gridLayout.addWidget(self.ent_preview, 1, 0, 1, 2)
        self.btn_send_message = QtWidgets.QPushButton(self.centralwidget)
        self.btn_send_message.setMaximumSize(QtCore.QSize(71, 16777215))
        self.btn_send_message.setObjectName("btn_send_message")
        self.gridLayout.addWidget(self.btn_send_message, 2, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 2)
        self.gridLayout_4.setColumnStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 791, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_text.setText(_translate("MainWindow", "Text"))
        self.btn_variables.setText(_translate("MainWindow", "Variables"))
        self.lbl_item.setText(_translate("MainWindow", "Items: 0"))
        self.btn_csv_input.setText(_translate("MainWindow", "Load CSV"))
        self.lbl_last_mod.setText(_translate("MainWindow", "{filename} last modified date:"))
        self.lbl_preview.setText(_translate("MainWindow", "Preview"))
        self.btn_send_message.setText(_translate("MainWindow", "Send"))
from models.ui import CsvTable, Textbox, VariableButton