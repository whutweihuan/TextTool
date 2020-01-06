# -*- coding: utf-8 -*-
"""
 author: weihuan
 date: 2020/1/6  9:50
"""
# -*- coding: utf-8 -*-
"""
 author: weihuan
 date: 2020/1/5  19:02
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget, \
    QDesktopWidget, QToolTip, QPushButton, QMessageBox, QMainWindow, QAction, qApp, QMenu, QHBoxLayout, QVBoxLayout, \
    QGridLayout, QLabel, QLineEdit, QTextEdit
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

        # 按钮
        # btnOk = QPushButton('确认')
        # btnCancel = QPushButton('取消')
        # hbox = QHBoxLayout()
        # hbox.addStretch(1)
        # hbox.addWidget(btnOk)
        # hbox.addWidget(btnCancel)
        #
        # vbox = QVBoxLayout()
        # vbox.addStretch(1)
        # vbox.addLayout(hbox)
        # self.setLayout(vbox)

        # btn.setToolTip('这是一个按钮')
        # btn.resize(btn.sizeHint())
        # # btn.move(50, 50)
        # btn.clicked.connect(QApplication.instance().quit)

        grid = QGridLayout()
        self.setLayout(grid)


        self.widget = QWidget()
        self.widget.setLayout(grid)
        self.setCentralWidget(self.widget)

        grid.setSpacing(10)
        title = QLabel('title')
        author = QLabel('author')
        review = QLabel('review')
        titleEdt = QLineEdit()
        authorEdt = QLineEdit()
        reviewEdt = QTextEdit()

        grid.addWidget(title,1,0)
        grid.addWidget(titleEdt,1,1)

        grid.addWidget(author,2,0)
        grid.addWidget(authorEdt,2,1)

        grid.addWidget(review,3,0)
        grid.addWidget(reviewEdt,3,1,5,1)




        # toolbar
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        self.show()

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

