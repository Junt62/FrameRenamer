from datetime import datetime
import os
import re
import shutil
from PySide6 import QtCore, QtWidgets, QtGui
from PIL import Image

from FrameRenamer_ui import Ui_Form

title = "序列帧重命名工具v1.1.0.2@zijun"
previewText = "重命名预览.txt"
backupFolder = "backup"
backupSuffix = "_备份"
extensions = ".png", ".jpg", ".bmp"


class MainForm(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.pressed.connect(self.pressedPushButton1)
        self.pushButton_2.pressed.connect(self.pressedPushButton2)
        self.pushButton_3.pressed.connect(self.pressedPushButton3)
        self.pushButton_4.pressed.connect(self.pressedPushButton4)
        self.pushButton_5.pressed.connect(self.pressedPushButton5)
        self.pushButton_6.pressed.connect(self.pressedPushButton6)
        self.pushButton_7.pressed.connect(self.pressedPushButton7)
        self.checkBox.stateChanged.connect(self.checkBoxChanged)

        self.toolPackage = ToolPackage(self)

        self.toolPackage.tint("请直接拖入含有图片的文件夹")
        self.toolPackage.tint("支持png，jpg，bmp")
        self.toolPackage.tint("关闭软件时，会自动清空备份")

    def dragEnterEvent(self, event: QtGui.QDragMoveEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QtGui.QDropEvent):
        urls = event.mimeData().urls()
        if urls:
            self.path = urls[0].toLocalFile()

            self.updateLineEdit1()

            self.updateLineEdit2()

            self.updateLineEdit3()

            self.toolPackage.generatePreviewText(self.path, self.images)

            self.toolPackage.generateBackupFolder(self.path)

            if self.checkBox.isChecked():
                self.pressedPushButton1()

    def pressedPushButton1(self):
        if self.lineEdit.text().strip():
            self.images = self.toolPackage.findImages(self.path)
            self.images = sorted(self.images, key=self.toolPackage.sortImages)

            self.toolPackage.renameImages(self.path, self.images)
            self.toolPackage.tint("执行重命名完成！")

            self.updateLineEdit2()
            self.updateLineEdit3()
            self.toolPackage.generatePreviewText(self.path, self.images)
        else:
            self.toolPackage.tint("未设置目标路径！")

    def pressedPushButton2(self):
        path = os.path.join(os.path.dirname(__file__), previewText)
        if os.path.exists(path):
            os.startfile(path)
            self.toolPackage.tint("查看重命名预览")
        else:
            self.toolPackage.tint("无重命名预览")

    def pressedPushButton3(self):
        path = os.path.join(os.path.dirname(__file__), backupFolder)
        if os.path.exists(path):
            os.startfile(path)
            self.toolPackage.tint("打开备份文件夹")
        else:
            self.toolPackage.tint("无备份文件夹")

    def pressedPushButton4(self):
        if self.lineEdit.text().strip():
            self.images = self.toolPackage.findImages(self.path)
            self.images = sorted(self.images, key=self.toolPackage.sortImages)

            if len(self.images) >= 600:
                self.toolPackage.tint("文件夹中图片大于600张，请检查文件夹")

            else:
                self.toolPackage.generateEmptyImagesFolder(600)
                self.toolPackage.fillImages(self.path)
                self.toolPackage.removeEmptyImagesFolder()

                self.updateLineEdit2()
                self.updateLineEdit3()
                self.toolPackage.tint("填充600帧空白图片")
        else:
            self.toolPackage.tint("未设置目标路径！")

    def pressedPushButton5(self):
        if self.lineEdit.text().strip():
            self.images = self.toolPackage.findImages(self.path)
            self.images = sorted(self.images, key=self.toolPackage.sortImages)

            if len(self.images) >= 360:
                self.toolPackage.tint("文件夹中图片大于360张，请检查文件夹")

            else:
                self.toolPackage.generateEmptyImagesFolder(360)
                self.toolPackage.fillImages(self.path)
                self.toolPackage.removeEmptyImagesFolder()

                self.updateLineEdit2()
                self.updateLineEdit3()
                self.toolPackage.tint("填充360帧空白图片")
        else:
            self.toolPackage.tint("未设置目标路径！")

    def pressedPushButton6(self):
        if self.lineEdit.text().strip():
            self.toolPackage.extractSubfolders(self.path)

            self.updateLineEdit2()
            self.updateLineEdit3()
            self.toolPackage.tint("提取所有子文件夹图片")
        else:
            self.toolPackage.tint("未设置目标路径！")

    def pressedPushButton7(self):
        if self.lineEdit.text().strip():
            self.toolPackage.deleteSubfolders(self.path)

            self.updateLineEdit2()
            self.updateLineEdit3()
            self.toolPackage.tint("删除所有子文件夹")
        else:
            self.toolPackage.tint("未设置目标路径！")

    def checkBoxChanged(self, state):
        if state:
            self.toolPackage.tint("启用自动执行")
        else:
            self.toolPackage.tint("禁用自动执行")
        pass

    def updateLineEdit1(self):
        self.toolPackage.tint("已拖入文件夹：" + os.path.basename(self.path))
        self.lineEdit.setText(self.path)

    def updateLineEdit2(self):
        self.images = self.toolPackage.findImages(self.path)
        self.images = sorted(self.images, key=self.toolPackage.sortImages)
        self.lineEdit_2.setText(f"{self.images}")

    def updateLineEdit3(self):
        imagesNew = []
        for i, k in enumerate(self.images):
            num = f"{i:03}"
            dot = k.rfind(".")
            new = os.path.basename(self.path) + num + k[dot:]
            imagesNew.append(new)
        self.lineEdit_3.setText(f"{imagesNew}")


class ToolPackage:
    def __init__(self, MainForm):
        self.MainForm = MainForm

    def tint(self, text):
        form = self.MainForm.textEdit
        time = datetime.now().strftime("%H:%M:%S")
        form.insertPlainText(f"【{time}】{text}\n")
        form.moveCursor(QtGui.QTextCursor.End)

    # iamges = sorted(images, key=self.sortImages)
    def sortImages(self, images):
        match = re.search(r"(\d+)", images)
        if match:
            return int(match.group(1))
        return images

    def findImages(self, path):
        imagesSource = os.listdir(path)
        imagesFiltered = []
        for image in imagesSource:
            if image.lower().endswith(extensions):
                imagesFiltered.append(image)
        return imagesFiltered

    def renameImages(self, path, images):
        for i, k in enumerate(images):
            num = f"{i:03}"
            dot = k.rfind(".")
            old = os.path.join(path, images[i])
            old = old.replace("\\", "/")
            new = os.path.join(path, os.path.basename(path) + num + k[dot:])
            new = new.replace("\\", "/")
            os.rename(old, new)

    def generatePreviewText(self, path, images):
        backupPath = os.path.join(os.path.dirname(__file__), previewText)
        with open(backupPath, "w", encoding="utf-8") as file:
            for i, k in enumerate(images):
                num = f"{i:03}"
                dot = k.rfind(".")
                new = os.path.basename(path) + num + k[dot:]
                file.write(k + " -> " + new + "\n")

    def generateBackupFolder(self, path):
        folder = os.path.basename(path)
        target = os.path.join(os.path.dirname(__file__), backupFolder)
        target = os.path.join(target, folder + backupSuffix)

        if os.path.exists(target):
            shutil.rmtree(target)

        shutil.copytree(path, target)

    def generateEmptyImagesFolder(self, frameCount: int):
        path = os.path.join(os.path.dirname(__file__), backupFolder, "empty_frame")
        if not os.path.exists(path):
            os.makedirs(path)

        image = Image.new("RGBA", (1, 1), color=(255, 255, 255, 0))
        imageEmpty = os.path.join(path, "00" + str(frameCount - 1) + ".png")
        image.save(imageEmpty)

        for i in range(frameCount - 1):
            name = f"{str(i).zfill(5)}.png"
            shutil.copy(imageEmpty, os.path.join(path, name))

    def fillImages(self, imagesOriginAddr):
        imagesOrigin = self.findImages(imagesOriginAddr)
        imagesOrigin = sorted(imagesOrigin, key=self.sortImages)

        imagesEmptyAddr = os.path.join(os.path.dirname(__file__), backupFolder)
        imagesEmptyAddr = os.path.join(imagesEmptyAddr, "empty_frame")

        imagesEmpty = self.findImages(imagesEmptyAddr)
        for imageEmpty in imagesEmpty:
            imageEmptyAddr = os.path.join(imagesEmptyAddr, imageEmpty)
            imageOriginAddr = os.path.join(imagesOriginAddr, imageEmpty)

            if not os.path.exists(imageOriginAddr):
                shutil.copy2(imageEmptyAddr, imageOriginAddr)

    def removeEmptyImagesFolder(self):
        path = os.path.join(os.path.dirname(__file__), backupFolder, "empty_frame")
        if os.path.exists(path):
            shutil.rmtree(path)

    def extractSubfolders(self, path):
        for root, dirs, files in os.walk(path):
            if root == path:
                continue
            for file in files:
                if file.lower().endswith(extensions):
                    inside = os.path.join(root, file)
                    inside = inside.replace("\\", "/")
                    outside = os.path.join(path, file)
                    outside = outside.replace("\\", "/")

                    shutil.copy2(inside, outside)

    def deleteSubfolders(self, path):
        for item in os.listdir(path):
            itemPath = os.path.join(path, item)
            if os.path.isdir(itemPath):
                shutil.rmtree(itemPath)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MainForm()
    widget.setWindowTitle(title)
    widget.show()
    app.exec()
