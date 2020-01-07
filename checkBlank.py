# -*- coding: utf-8 -*-
"""
 author: weihuan
 date: 2020/1/7  8:39
"""
import re
import sys

# from PyQt5.QtWidgets import QInputDialog, QApplication, QTextEdit, QLineEdit, QMainWindow, QWidget
import clipboard
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class inputUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initView()

    def initView(self):
        self.setWindowTitle('文本')
        self.setWindowIcon(QIcon('res/main_ui_title_icon.png'))

        self.setFixedSize(300,180)

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        vbox = QVBoxLayout()
        self.setLayout(vbox)

        self.text = QTextEdit()
        self.btn = QPushButton()
        self.btn.clicked.connect(self.trans)

        vbox.addWidget(self.text)
        vbox.addWidget(self.btn)

        self.show()

    def trans(self):
        text = self.text.toPlainText()
        text =  CheckUtil.checkText(text)
        clipboard.copy(text)

class CheckUtil:
    @staticmethod
    def checkText (text):
        pattern = re.compile(r'([\u4e00-\u9fa5]+)([a-zA-Z0-9]+?)', re.M)
        text = re.sub(pattern, r'\1 \2', text)
        pattern = re.compile(r'([a-zA-Z0-9]+?)([\u4e00-\u9fa5]+)', re.M)
        res = re.sub(pattern, r'\1 \2', text)

        return res;


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = inputUI()

    sys.exit(app.exec_())


