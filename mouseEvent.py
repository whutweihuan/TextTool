# -*- coding: utf-8 -*-
"""
 author: weihuan
 date: 2020/1/6  10:45
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, \
    QDesktopWidget, QToolTip, QPushButton, QMessageBox, QMainWindow, QAction, qApp, QMenu, QHBoxLayout, QVBoxLayout, \
    QGridLayout, QLCDNumber, QSlider, QLabel
from PyQt5.QtGui import QIcon, QFont


class MainUI(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.initUI()

    def initUI (self):
        self.center()
        self.resize(800, 500)
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setWindowTitle("文本工具")
        self.setWindowIcon(QIcon('res/main_ui_title_icon.png'))
        self.setToolTip('This is a <b> QWidget <b/> widget')



        # 活动
        exitAct = QAction(QIcon('./res/exit_app.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        # 状态栏
        self.statusBar().showMessage('Ready')

        # 菜单
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        # 子菜单
        impMenu = QMenu('import', self)
        imact = QAction('import mail', self)
        impMenu.addAction(imact)
        newAct = QAction('New', self)
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        # check menu
        viewStartAct = QAction('View Start statusBar', self, checkable = True)
        viewStartAct.setStatusTip('View status bar')
        viewStartAct.setCheckable(True)
        viewStartAct.triggered.connect(self.toggleMenu)
        viewMenu = menubar.addMenu('Check menu')
        viewMenu.addAction(viewStartAct)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        self.text = QLabel("X: {}, Y: {}".format(0 ,0))
        vbox = QVBoxLayout()
        vbox.addWidget(self.text)
        vbox.addStretch(1)

        widget = QWidget()
        widget.setLayout(vbox)
        widget.setMouseTracking(True)
        self.setCentralWidget(widget)


        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            print('test')
            return
    def mouseMoveEvent(self, e):
        text = "X: {}, Y: {}".format(e.x(),e.y())
        self.text.setText(text)


    def contextMenuEvent (self, event):
        # context menu
        cmenu = QMenu(self)
        newAct2 = cmenu.addAction("New")
        openAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapFromGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()

    def toggleMenu (self, state):
        if state:
            self.statusBar().show()
        else:
            self.statusBar().hide()

    # 退出二次确定
    def closeEvent (self, event):
        reply = QMessageBox.question(self, '退出', '确认退出吗?',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # 居中
    def center (self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainUI()

    sys.exit(app.exec())