# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Gain(object):
    def setupUi(self, Gain):
        Gain.setObjectName("Gain")
        Gain.resize(640, 480)
        Gain.setMinimumSize(QtCore.QSize(640, 480))
        Gain.setMaximumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/img/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Gain.setWindowIcon(icon)
        Gain.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.cabecalho = QtWidgets.QFrame(Gain)
        self.cabecalho.setGeometry(QtCore.QRect(0, 0, 640, 67))
        self.cabecalho.setStyleSheet("background-color: rgb(218, 165, 32);")
        self.cabecalho.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cabecalho.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cabecalho.setObjectName("cabecalho")
        self.Nome = QtWidgets.QLabel(self.cabecalho)
        self.Nome.setGeometry(QtCore.QRect(20, 6, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Beyond The Mountains")
        font.setPointSize(36)
        self.Nome.setFont(font)
        self.Nome.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.Nome.setObjectName("Nome")
        self.Custo = QtWidgets.QLabel(Gain)
        self.Custo.setGeometry(QtCore.QRect(20, 100, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        self.Custo.setFont(font)
        self.Custo.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.Custo.setObjectName("Custo")
        self.Lucro = QtWidgets.QLabel(Gain)
        self.Lucro.setGeometry(QtCore.QRect(400, 100, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        self.Lucro.setFont(font)
        self.Lucro.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.Lucro.setObjectName("Lucro")
        self.Venda = QtWidgets.QLabel(Gain)
        self.Venda.setGeometry(QtCore.QRect(150, 350, 290, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(36)
        self.Venda.setFont(font)
        self.Venda.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Venda.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Venda.setObjectName("Venda")
        self.Marca = QtWidgets.QLabel(Gain)
        self.Marca.setGeometry(QtCore.QRect(500, 440, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arenq")
        font.setPointSize(22)
        self.Marca.setFont(font)
        self.Marca.setObjectName("Marca")
        self.CalcBTN = QtWidgets.QPushButton(Gain)
        self.CalcBTN.setGeometry(QtCore.QRect(190, 270, 220, 50))
        self.CalcBTN.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.CalcBTN.setStyleSheet("background-color: rgb(195, 195, 195);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 14pt \"Arial\";\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/img/porcentagem.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CalcBTN.setIcon(icon1)
        self.CalcBTN.setIconSize(QtCore.QSize(40, 40))
        self.CalcBTN.setObjectName("CalcBTN")
        self.custinho = QtWidgets.QTextEdit(Gain)
        self.custinho.setGeometry(QtCore.QRect(20, 175, 130, 30))
        self.custinho.setStyleSheet("background-color: rgb(195, 195, 195);\n"
"border-style: none;\n"
"border-radius: 10px;")
        self.custinho.setMidLineWidth(0)
        self.custinho.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.custinho.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.custinho.setObjectName("custinho")
        self.lucrinho = QtWidgets.QTextEdit(Gain)
        self.lucrinho.setGeometry(QtCore.QRect(400, 175, 130, 30))
        self.lucrinho.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.lucrinho.setObjectName("lucrinho")

        self.retranslateUi(Gain)
        QtCore.QMetaObject.connectSlotsByName(Gain)

    def retranslateUi(self, Gain):
        _translate = QtCore.QCoreApplication.translate
        Gain.setWindowTitle(_translate("Gain", "Form"))
        self.Nome.setText(_translate("Gain", "Lucro"))
        self.Custo.setText(_translate("Gain", "Custo:"))
        self.Lucro.setText(_translate("Gain", "Lucro (%):"))
        self.Venda.setText(_translate("Gain", "Venda:"))
        self.Marca.setText(_translate("Gain", "JOTATEC"))
        self.CalcBTN.setText(_translate("Gain", "       Calcular"))
import file_rc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Gain = QtWidgets.QWidget()
    ui = Ui_Gain()
    ui.setupUi(Gain)
    Gain.show()
    sys.exit(app.exec_())
