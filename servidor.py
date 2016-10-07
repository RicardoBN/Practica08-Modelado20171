# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'servidor.ui'
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

class Ui_servidor(object):
    def setupUi(self, servidor):
        servidor.setObjectName(_fromUtf8("servidor"))
        servidor.resize(775, 558)
        self.gridLayout = QtGui.QGridLayout(servidor)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableWidget = QtGui.QTableWidget(servidor)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(15)
        self.tableWidget.setRowCount(15)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(30)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 3, 1)
        self.groupBox = QtGui.QGroupBox(servidor)
        self.groupBox.setMinimumSize(QtCore.QSize(161, 91))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 61, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.spinBox = QtGui.QSpinBox(self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(80, 20, 71, 16))
        self.spinBox.setProperty("value", 20)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox_2 = QtGui.QSpinBox(self.groupBox)
        self.spinBox_2.setGeometry(QtCore.QRect(80, 40, 71, 16))
        self.spinBox_2.setProperty("value", 20)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.spinBox_3 = QtGui.QSpinBox(self.groupBox)
        self.spinBox_3.setGeometry(QtCore.QRect(80, 60, 71, 16))
        self.spinBox_3.setMaximum(500)
        self.spinBox_3.setProperty("value", 250)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(servidor)
        self.groupBox_2.setMinimumSize(QtCore.QSize(161, 111))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 46, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 61, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(60, 20, 91, 16))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.spinBox_4 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_4.setGeometry(QtCore.QRect(60, 40, 91, 16))
        self.spinBox_4.setProperty("value", 0)
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))
        self.spinBox_5 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_5.setGeometry(QtCore.QRect(60, 60, 91, 16))
        self.spinBox_5.setObjectName(_fromUtf8("spinBox_5"))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(10, 80, 141, 21))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(servidor)
        self.pushButton_2.setMinimumSize(QtCore.QSize(141, 21))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)

        self.retranslateUi(servidor)
        QtCore.QMetaObject.connectSlotsByName(servidor)

    def retranslateUi(self, servidor):
        servidor.setWindowTitle(_translate("servidor", "servidor", None))
        self.groupBox.setTitle(_translate("servidor", "Configuración del juego", None))
        self.label.setText(_translate("servidor", "Columnas", None))
        self.label_2.setText(_translate("servidor", "Filas", None))
        self.label_3.setText(_translate("servidor", "Espera(ms)", None))
        self.groupBox_2.setTitle(_translate("servidor", "Conexion", None))
        self.label_4.setText(_translate("servidor", "Url", None))
        self.label_5.setText(_translate("servidor", "Puerto", None))
        self.label_6.setText(_translate("servidor", "Timeout", None))
        self.pushButton.setText(_translate("servidor", "Iniciar Servidor", None))
        self.pushButton_2.setText(_translate("servidor", "Iniciar Juego", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    servidor = QtGui.QWidget()
    ui = Ui_servidor()
    ui.setupUi(servidor)
    servidor.show()
    sys.exit(app.exec_())

