# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrameRenamer.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QWidget)
import FrameRenamer_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        Form.setMinimumSize(QSize(400, 300))
        Form.setMaximumSize(QSize(400, 300))
        icon = QIcon()
        icon.addFile(u":/icon/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 160, 71, 23))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 381, 16))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 30, 381, 21))
        self.lineEdit.setReadOnly(True)
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(90, 160, 61, 23))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 60, 381, 16))
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 80, 381, 21))
        self.lineEdit_2.setReadOnly(True)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 110, 381, 16))
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(10, 130, 381, 21))
        self.lineEdit_3.setReadOnly(True)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 190, 381, 16))
        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(270, 162, 111, 19))
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 210, 381, 81))
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setReadOnly(True)
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(160, 160, 91, 23))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5e8f\u5217\u5e27\u6279\u91cf\u91cd\u547d\u540d\u5de5\u5177", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u6267\u884c\u91cd\u547d\u540d", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u6587\u4ef6\u5939\u5730\u5740\uff1a", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u67e5\u770b\u9884\u89c8", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u6587\u4ef6\u540d\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u76ee\u6807\u6587\u4ef6\u540d\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u63d0\u793a\u4fe1\u606f\uff1a", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u6267\u884c\u91cd\u547d\u540d", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u5907\u4efd\u6587\u4ef6\u5939", None))
    # retranslateUi

