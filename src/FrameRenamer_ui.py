# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrameRenamer.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QGridLayout,
    QGroupBox,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QTabWidget,
    QTextEdit,
    QWidget,
)
import src.FrameRenamer_rc


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(500, 375)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(500, 375))
        Form.setMaximumSize(QSize(500, 375))
        Form.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(":/icon/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setGeometry(QRect(4, 4, 492, 367))
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.setContentsMargins(4, 4, 4, 2)
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setAutoFillBackground(True)
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_4.setContentsMargins(4, 4, 4, 4)
        self.pushButton_5 = QPushButton(self.groupBox_2)
        self.pushButton_5.setObjectName("pushButton_5")

        self.gridLayout_4.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.groupBox_2)
        self.pushButton_7.setObjectName("pushButton_7")

        self.gridLayout_4.addWidget(self.pushButton_7, 1, 3, 1, 1)

        self.pushButton_4 = QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName("pushButton_4")

        self.gridLayout_4.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.groupBox_2)
        self.pushButton_6.setObjectName("pushButton_6")

        self.gridLayout_4.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName("pushButton")

        self.gridLayout_4.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName("pushButton_2")

        self.gridLayout_4.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName("pushButton_3")

        self.gridLayout_4.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.checkBox = QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName("checkBox")

        self.gridLayout_4.addWidget(self.checkBox, 0, 3, 1, 1)

        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setAutoFillBackground(True)
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_5.setContentsMargins(4, 4, 4, 4)
        self.textEdit = QTextEdit(self.groupBox_3)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.textEdit.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.textEdit.setReadOnly(True)

        self.gridLayout_5.addWidget(self.textEdit, 0, 0, 1, 1)

        self.gridLayout_3.addWidget(self.groupBox_3, 2, 0, 1, 1)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setAutoFillBackground(True)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName("label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(
            QCoreApplication.translate(
                "Form", "\u5e8f\u5217\u5e27\u91cd\u547d\u540d\u5de5\u5177", None
            )
        )
        self.groupBox_2.setTitle(
            QCoreApplication.translate("Form", "\u56fe\u7247\u64cd\u4f5c", None)
        )
        self.pushButton_5.setText(
            QCoreApplication.translate("Form", "\u586b\u5145360\u5e27", None)
        )
        self.pushButton_7.setText(
            QCoreApplication.translate(
                "Form", "\u5220\u9664\u5b50\u6587\u4ef6\u5939", None
            )
        )
        self.pushButton_4.setText(
            QCoreApplication.translate("Form", "\u586b\u5145600\u5e27", None)
        )
        self.pushButton_6.setText(
            QCoreApplication.translate(
                "Form", "\u63d0\u53d6\u5b50\u6587\u4ef6\u5939\u56fe\u7247", None
            )
        )
        self.pushButton.setText(
            QCoreApplication.translate("Form", "\u6267\u884c\u91cd\u547d\u540d", None)
        )
        self.pushButton_2.setText(
            QCoreApplication.translate(
                "Form", "\u67e5\u770b\u91cd\u547d\u540d\u9884\u89c8", None
            )
        )
        self.pushButton_3.setText(
            QCoreApplication.translate(
                "Form", "\u6253\u5f00\u5907\u4efd\u6587\u4ef6\u5939", None
            )
        )
        self.checkBox.setText(
            QCoreApplication.translate(
                "Form", "\u81ea\u52a8\u6267\u884c\u91cd\u547d\u540d", None
            )
        )
        self.groupBox_3.setTitle(
            QCoreApplication.translate("Form", "\u63d0\u793a\u4fe1\u606f", None)
        )
        self.groupBox.setTitle(
            QCoreApplication.translate("Form", "\u76ee\u6807\u9009\u62e9", None)
        )
        self.label.setText(
            QCoreApplication.translate(
                "Form", "\u6587\u4ef6\u5939\u8def\u5f84\uff1a", None
            )
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "Form", "\u5f53\u524d\u6587\u4ef6\u540d\uff1a", None
            )
        )
        self.label_3.setText(
            QCoreApplication.translate(
                "Form", "\u76ee\u6807\u6587\u4ef6\u540d\uff1a", None
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            QCoreApplication.translate("Form", "\u56fe\u7247\u5904\u7406", None),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            QCoreApplication.translate("Form", "\u5173\u4e8e", None),
        )

    # retranslateUi
