# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAccounts = QAction(MainWindow)
        self.actionAccounts.setObjectName(u"actionAccounts")
        self.actionProxies = QAction(MainWindow)
        self.actionProxies.setObjectName(u"actionProxies")
        self.actionHeadless = QAction(MainWindow)
        self.actionHeadless.setObjectName(u"actionHeadless")
        self.actionHeadless.setCheckable(True)
        self.actionHeadless.setChecked(False)
        self.actionUpdate = QAction(MainWindow)
        self.actionUpdate.setObjectName(u"actionUpdate")
        self.actionImages = QAction(MainWindow)
        self.actionImages.setObjectName(u"actionImages")
        self.actionImages.setCheckable(True)
        self.actionImages.setChecked(False)
        self.actionUseProxies = QAction(MainWindow)
        self.actionUseProxies.setObjectName(u"actionUseProxies")
        self.actionUseProxies.setCheckable(True)
        self.actionChangelog = QAction(MainWindow)
        self.actionChangelog.setObjectName(u"actionChangelog")
        self.actionBilling = QAction(MainWindow)
        self.actionBilling.setObjectName(u"actionBilling")
        self.actionAddress = QAction(MainWindow)
        self.actionAddress.setObjectName(u"actionAddress")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftLayout = QVBoxLayout()
        self.leftLayout.setObjectName(u"leftLayout")

        self.horizontalLayout.addLayout(self.leftLayout)

        self.rightLayout = QVBoxLayout()
        self.rightLayout.setObjectName(u"rightLayout")
        self.emailLabel = QLabel(self.centralwidget)
        self.emailLabel.setObjectName(u"emailLabel")
        font = QFont()
        font.setBold(True)
        self.emailLabel.setFont(font)

        self.rightLayout.addWidget(self.emailLabel)

        self.email = QLabel(self.centralwidget)
        self.email.setObjectName(u"email")

        self.rightLayout.addWidget(self.email)

        self.passwordLabel = QLabel(self.centralwidget)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setFont(font)

        self.rightLayout.addWidget(self.passwordLabel)

        self.password = QLabel(self.centralwidget)
        self.password.setObjectName(u"password")

        self.rightLayout.addWidget(self.password)

        self.totpLabel = QLabel(self.centralwidget)
        self.totpLabel.setObjectName(u"totpLabel")
        self.totpLabel.setFont(font)

        self.rightLayout.addWidget(self.totpLabel)

        self.totp = QLabel(self.centralwidget)
        self.totp.setObjectName(u"totp")

        self.rightLayout.addWidget(self.totp)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.rightLayout.addItem(self.verticalSpacer)

        self.loginButton = QPushButton(self.centralwidget)
        self.loginButton.setObjectName(u"loginButton")

        self.rightLayout.addWidget(self.loginButton)

        self.addCardButton = QPushButton(self.centralwidget)
        self.addCardButton.setObjectName(u"addCardButton")

        self.rightLayout.addWidget(self.addCardButton)

        self.changeRecentButton = QPushButton(self.centralwidget)
        self.changeRecentButton.setObjectName(u"changeRecentButton")

        self.rightLayout.addWidget(self.changeRecentButton)

        self.addAddressButton = QPushButton(self.centralwidget)
        self.addAddressButton.setObjectName(u"addAddressButton")

        self.rightLayout.addWidget(self.addAddressButton)


        self.horizontalLayout.addLayout(self.rightLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 28))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionAccounts)
        self.menuEdit.addAction(self.actionProxies)
        self.menuEdit.addAction(self.actionBilling)
        self.menuEdit.addAction(self.actionAddress)
        self.menuView.addAction(self.actionHeadless)
        self.menuView.addAction(self.actionImages)
        self.menuView.addAction(self.actionUseProxies)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionUpdate)
        self.menuHelp.addAction(self.actionChangelog)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionAccounts.setText(QCoreApplication.translate("MainWindow", u"Accounts.txt", None))
        self.actionProxies.setText(QCoreApplication.translate("MainWindow", u"Proxies.txt", None))
        self.actionHeadless.setText(QCoreApplication.translate("MainWindow", u"Headless", None))
        self.actionUpdate.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.actionImages.setText(QCoreApplication.translate("MainWindow", u"Images", None))
        self.actionUseProxies.setText(QCoreApplication.translate("MainWindow", u"Proxies", None))
        self.actionChangelog.setText(QCoreApplication.translate("MainWindow", u"Changelog", None))
        self.actionBilling.setText(QCoreApplication.translate("MainWindow", u"Billing", None))
        self.actionAddress.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.emailLabel.setText(QCoreApplication.translate("MainWindow", u"Account Email", None))
        self.email.setText("")
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"Account Password", None))
        self.password.setText("")
        self.totpLabel.setText(QCoreApplication.translate("MainWindow", u"TOTP", None))
        self.totp.setText("")
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.addCardButton.setText(QCoreApplication.translate("MainWindow", u"Add Card", None))
        self.changeRecentButton.setText(QCoreApplication.translate("MainWindow", u"Change Recent Order", None))
        self.addAddressButton.setText(QCoreApplication.translate("MainWindow", u"Add Address", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

