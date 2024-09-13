from datetime import datetime
import os
import shutil
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

from FrameRenamer_ui import Ui_Form


previewText = "重命名预览.txt"
backupSuffix = "_备份"


class MainForm(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.setupUi(self)

        self.setAcceptDrops(True)

        self.pushButton.pressed.connect(self.pressedPushButton1)
        self.pushButton_2.pressed.connect(self.pressedPushButton2)
        self.pushButton_3.pressed.connect(self.pressedPushButton3)
        self.checkBox.stateChanged.connect(self.checkBoxChanged)

        self.toolPackage = ToolPackage(self)

        self.toolPackage.tint("请直接拖入含有图片的文件夹")
        self.toolPackage.tint("软件会自动执行备份，支持png，jpg，bmp")
        self.toolPackage.tint("当点击执行重命名时，会将文件夹内图片替换为")
        self.toolPackage.tint("文件夹名+000的递增数字")

    def dragEnterEvent(self, event: QtGui.QDragMoveEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QtGui.QDropEvent):
        urls = event.mimeData().urls()
        if urls:
            self.path = urls[0].toLocalFile()
            self.folder = os.path.basename(self.path)

            self.lineEdit.setText(self.path)
            self.toolPackage.tint("已拖入文件夹：" + self.folder)

            self.updateLineEdit2()
            self.toolPackage.generateBackupFolder(self.path, self.folder)

            imagesWithIndex = []
            for i, k in enumerate(self.images):
                num = f"{i:03}"
                dot = k.rfind(".")
                new = self.folder + num + k[dot:]
                imagesWithIndex.append(new)
            self.lineEdit_3.setText(f"{imagesWithIndex}")

            if self.checkBox.isChecked():
                self.pressedPushButton1()

    def pressedPushButton1(self):
        if self.lineEdit.text().strip():
            images = self.toolPackage.findImages(self.path)
            for i, k in enumerate(images):
                num = f"{i:03}"
                dot = k.rfind(".")
                old = os.path.join(self.path, images[i])
                old = old.replace("\\", "/")
                new = os.path.join(self.path, self.folder + num + k[dot:])
                new = new.replace("\\", "/")
                os.rename(old, new)

            self.toolPackage.tint("执行重命名完成！")
            self.updateLineEdit2()
            # print(old + " -> " + new)

    def pressedPushButton2(self):
        # self.toolPackage.tint("查看重命名预览")
        path = os.path.join(os.path.dirname(__file__), previewText)
        if os.path.exists(path):
            os.startfile(path)

    def pressedPushButton3(self):
        # self.toolPackage.tint("打开备份文件夹")
        os.startfile(os.path.dirname(__file__))

    def checkBoxChanged(self, state):
        # if state:
        #     self.toolPackage.tint("启用自动执行重命名，拖入文件夹执行")
        # else:
        #     self.toolPackage.tint("禁用自动执行")
        pass

    def updateLineEdit2(self):
        self.images = self.toolPackage.findImages(self.path)
        self.lineEdit_2.setText(f"{self.images}")
        self.toolPackage.generatePreviewText(self.folder, self.images)


class ToolPackage:
    def __init__(self, MainForm):
        self.MainForm = MainForm

    def tint(self, text):
        form = self.MainForm.textEdit
        time = datetime.now().strftime("%H:%M:%S")
        form.insertPlainText(f"【{time}】{text}\n")
        form.moveCursor(QtGui.QTextCursor.End)

    def findImages(self, path):
        extensions = (".png", ".jpg", ".bmp")
        images = []
        for image in os.listdir(path):
            if image.lower().endswith(extensions):
                images.append(image)
        return images

    def generatePreviewText(self, folder, images):
        path = os.path.join(os.path.dirname(__file__), previewText)
        with open(path, "w", encoding="utf-8") as file:
            for i, k in enumerate(images):
                num = f"{i:03}"
                dot = k.rfind(".")
                new = folder + num + k[dot:]
                file.write(k + " -> " + new + "\n")

    def generateBackupFolder(self, path, folder):
        target = os.path.join(os.path.dirname(__file__), folder + backupSuffix)

        if os.path.exists(target):
            shutil.rmtree(target)

        shutil.copytree(path, target)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MainForm()
    widget.setWindowTitle("贪玩-序列帧重命名工具v1.0.0@zijun")
    widget.show()
    app.exec()
