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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QWidget)
import FrameRenamer_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(480, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(480, 400))
        Form.setMaximumSize(QSize(480, 400))
        Form.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(u":/icon/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 3, 461, 111))
        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(80, 80, 371, 21))
        self.lineEdit_3.setReadOnly(True)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 82, 71, 16))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 22, 71, 16))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 52, 71, 16))
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 20, 371, 21))
        self.lineEdit.setReadOnly(True)
        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(80, 50, 371, 21))
        self.lineEdit_2.setReadOnly(True)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 120, 381, 16))
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 118, 461, 81))
        self.checkBox = QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(300, 20, 111, 19))
        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(90, 18, 101, 23))
        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 18, 71, 23))
        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(200, 18, 91, 23))
        self.pushButton_4 = QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 50, 71, 23))
        self.pushButton_5 = QPushButton(self.groupBox_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(90, 50, 81, 23))
        self.pushButton_6 = QPushButton(self.groupBox_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(180, 50, 111, 23))
        self.pushButton_7 = QPushButton(self.groupBox_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(300, 50, 91, 23))
        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 203, 461, 191))
        self.textEdit = QTextEdit(self.groupBox_3)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 20, 441, 161))
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setReadOnly(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5e8f\u5217\u5e27\u91cd\u547d\u540d\u5de5\u5177", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u76ee\u6807\u9009\u62e9", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u76ee\u6807\u6587\u4ef6\u540d\uff1a", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u5939\u8def\u5f84\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u6587\u4ef6\u540d\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u63d0\u793a\u4fe1\u606f\uff1a", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u56fe\u7247\u64cd\u4f5c", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u6267\u884c\u91cd\u547d\u540d", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u67e5\u770b\u91cd\u547d\u540d\u9884\u89c8", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u6267\u884c\u91cd\u547d\u540d", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u5907\u4efd\u6587\u4ef6\u5939", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u586b\u5145600\u5e27", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u586b\u5145360\u5e27", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u63d0\u53d6\u5b50\u6587\u4ef6\u5939\u56fe\u7247", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u5b50\u6587\u4ef6\u5939", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u63d0\u793a\u4fe1\u606f", None))
    # retranslateUi

