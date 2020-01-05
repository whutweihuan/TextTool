# -*- coding: utf-8 -*-
"""
 author: weihuan
 date: 2020/1/5  19:02
"""
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QDesktopWidget,QToolTip)
from PyQt5.QtGui import QIcon


class MainUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(800, 500)
        # screen = QDesktopWidget.screenGeometry()
        # screenSize = self.geometry()
        # win.move((screen.width() - screenSize.width()) / 2,
        #          (screen.height() - screenSize.height()) / 2)
        self.setWindowTitle("文本工具")
        self.setWindowIcon(QIcon('res/main_ui_title_icon.png'))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainUI()

    win.show()

    sys.exit(app.exec())
