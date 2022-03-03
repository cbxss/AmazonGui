# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'address.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QGridLayout, QLabel,
    QLineEdit, QSizePolicy, QWidget)

class Ui_Address(object):
    def setupUi(self, Address):
        if not Address.objectName():
            Address.setObjectName(u"Address")
        Address.resize(414, 446)
        self.gridLayout = QGridLayout(Address)
        self.gridLayout.setObjectName(u"gridLayout")
        self.AddressLabel = QLabel(Address)
        self.AddressLabel.setObjectName(u"AddressLabel")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.AddressLabel.setFont(font)

        self.gridLayout.addWidget(self.AddressLabel, 6, 0, 1, 3)

        self.zipLine = QLineEdit(Address)
        self.zipLine.setObjectName(u"zipLine")

        self.gridLayout.addWidget(self.zipLine, 10, 2, 1, 1)

        self.nameLine = QLineEdit(Address)
        self.nameLine.setObjectName(u"nameLine")

        self.gridLayout.addWidget(self.nameLine, 3, 0, 1, 3)

        self.cityLine = QLineEdit(Address)
        self.cityLine.setObjectName(u"cityLine")

        self.gridLayout.addWidget(self.cityLine, 10, 0, 1, 1)

        self.phoneLine = QLineEdit(Address)
        self.phoneLine.setObjectName(u"phoneLine")

        self.gridLayout.addWidget(self.phoneLine, 5, 0, 1, 3)

        self.addressLine2 = QLineEdit(Address)
        self.addressLine2.setObjectName(u"addressLine2")

        self.gridLayout.addWidget(self.addressLine2, 8, 0, 1, 3)

        self.addressLine1 = QLineEdit(Address)
        self.addressLine1.setObjectName(u"addressLine1")

        self.gridLayout.addWidget(self.addressLine1, 7, 0, 1, 3)

        self.cityLabel = QLabel(Address)
        self.cityLabel.setObjectName(u"cityLabel")
        self.cityLabel.setFont(font)

        self.gridLayout.addWidget(self.cityLabel, 9, 0, 1, 1)

        self.stateLabel = QLabel(Address)
        self.stateLabel.setObjectName(u"stateLabel")
        self.stateLabel.setFont(font)

        self.gridLayout.addWidget(self.stateLabel, 9, 1, 1, 1)

        self.countryLabel = QLabel(Address)
        self.countryLabel.setObjectName(u"countryLabel")
        self.countryLabel.setFont(font)

        self.gridLayout.addWidget(self.countryLabel, 0, 0, 1, 3)

        self.phoneLabel = QLabel(Address)
        self.phoneLabel.setObjectName(u"phoneLabel")
        self.phoneLabel.setFont(font)

        self.gridLayout.addWidget(self.phoneLabel, 4, 0, 1, 3)

        self.zipLabel = QLabel(Address)
        self.zipLabel.setObjectName(u"zipLabel")
        self.zipLabel.setFont(font)

        self.gridLayout.addWidget(self.zipLabel, 9, 2, 1, 1)

        self.countryLine = QLineEdit(Address)
        self.countryLine.setObjectName(u"countryLine")
        self.countryLine.setReadOnly(True)

        self.gridLayout.addWidget(self.countryLine, 1, 0, 1, 3)

        self.buttonBox = QDialogButtonBox(Address)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 13, 0, 1, 3)

        self.nameLabel = QLabel(Address)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setFont(font)

        self.gridLayout.addWidget(self.nameLabel, 2, 0, 1, 3)

        self.stateBox = QComboBox(Address)
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.addItem("")
        self.stateBox.setObjectName(u"stateBox")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stateBox.sizePolicy().hasHeightForWidth())
        self.stateBox.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.stateBox, 10, 1, 1, 1)

        self.defaultBox = QCheckBox(Address)
        self.defaultBox.setObjectName(u"defaultBox")

        self.gridLayout.addWidget(self.defaultBox, 12, 0, 1, 3)

        QWidget.setTabOrder(self.countryLine, self.nameLine)
        QWidget.setTabOrder(self.nameLine, self.phoneLine)
        QWidget.setTabOrder(self.phoneLine, self.addressLine1)
        QWidget.setTabOrder(self.addressLine1, self.addressLine2)
        QWidget.setTabOrder(self.addressLine2, self.cityLine)
        QWidget.setTabOrder(self.cityLine, self.stateBox)
        QWidget.setTabOrder(self.stateBox, self.zipLine)
        QWidget.setTabOrder(self.zipLine, self.defaultBox)

        self.retranslateUi(Address)
        self.buttonBox.accepted.connect(Address.accept)
        self.buttonBox.rejected.connect(Address.reject)

        QMetaObject.connectSlotsByName(Address)
    # setupUi

    def retranslateUi(self, Address):
        Address.setWindowTitle(QCoreApplication.translate("Address", u"Dialog", None))
        self.AddressLabel.setText(QCoreApplication.translate("Address", u"Address", None))
        self.addressLine2.setPlaceholderText(QCoreApplication.translate("Address", u"Apt, suite, unit, building, floor, etc.", None))
        self.addressLine1.setPlaceholderText(QCoreApplication.translate("Address", u"Street address or P.O. Box", None))
        self.cityLabel.setText(QCoreApplication.translate("Address", u"City", None))
        self.stateLabel.setText(QCoreApplication.translate("Address", u"State", None))
        self.countryLabel.setText(QCoreApplication.translate("Address", u"Country/Region", None))
        self.phoneLabel.setText(QCoreApplication.translate("Address", u"Phone number", None))
        self.zipLabel.setText(QCoreApplication.translate("Address", u"ZIP Code", None))
        self.countryLine.setText(QCoreApplication.translate("Address", u"United States", None))
        self.nameLabel.setText(QCoreApplication.translate("Address", u"Full name (First and Last name)", None))
        self.stateBox.setItemText(0, QCoreApplication.translate("Address", u"Alabama", None))
        self.stateBox.setItemText(1, QCoreApplication.translate("Address", u"Alaska", None))
        self.stateBox.setItemText(2, QCoreApplication.translate("Address", u"American Samoa", None))
        self.stateBox.setItemText(3, QCoreApplication.translate("Address", u"Arizona", None))
        self.stateBox.setItemText(4, QCoreApplication.translate("Address", u"Arkansas", None))
        self.stateBox.setItemText(5, QCoreApplication.translate("Address", u"California", None))
        self.stateBox.setItemText(6, QCoreApplication.translate("Address", u"Colorado", None))
        self.stateBox.setItemText(7, QCoreApplication.translate("Address", u"Connecticut", None))
        self.stateBox.setItemText(8, QCoreApplication.translate("Address", u"Delaware", None))
        self.stateBox.setItemText(9, QCoreApplication.translate("Address", u"District of Columbia", None))
        self.stateBox.setItemText(10, QCoreApplication.translate("Address", u"Federated States of Micronesia", None))
        self.stateBox.setItemText(11, QCoreApplication.translate("Address", u"Floridia", None))
        self.stateBox.setItemText(12, QCoreApplication.translate("Address", u"Georgia", None))
        self.stateBox.setItemText(13, QCoreApplication.translate("Address", u"Guam", None))
        self.stateBox.setItemText(14, QCoreApplication.translate("Address", u"Hawaii", None))
        self.stateBox.setItemText(15, QCoreApplication.translate("Address", u"Idaho", None))
        self.stateBox.setItemText(16, QCoreApplication.translate("Address", u"Illinois", None))
        self.stateBox.setItemText(17, QCoreApplication.translate("Address", u"Indiana", None))
        self.stateBox.setItemText(18, QCoreApplication.translate("Address", u"Iowa", None))
        self.stateBox.setItemText(19, QCoreApplication.translate("Address", u"Kansas", None))
        self.stateBox.setItemText(20, QCoreApplication.translate("Address", u"Kentucky", None))
        self.stateBox.setItemText(21, QCoreApplication.translate("Address", u"Louisiana", None))
        self.stateBox.setItemText(22, QCoreApplication.translate("Address", u"Maine", None))
        self.stateBox.setItemText(23, QCoreApplication.translate("Address", u"Marshall Islands", None))
        self.stateBox.setItemText(24, QCoreApplication.translate("Address", u"Maryland", None))
        self.stateBox.setItemText(25, QCoreApplication.translate("Address", u"Massachusetts", None))
        self.stateBox.setItemText(26, QCoreApplication.translate("Address", u"Michigan", None))
        self.stateBox.setItemText(27, QCoreApplication.translate("Address", u"Minnesota", None))
        self.stateBox.setItemText(28, QCoreApplication.translate("Address", u"Mississippi", None))
        self.stateBox.setItemText(29, QCoreApplication.translate("Address", u"Missouri", None))
        self.stateBox.setItemText(30, QCoreApplication.translate("Address", u"Montana", None))
        self.stateBox.setItemText(31, QCoreApplication.translate("Address", u"Nebraska", None))
        self.stateBox.setItemText(32, QCoreApplication.translate("Address", u"Nevada", None))
        self.stateBox.setItemText(33, QCoreApplication.translate("Address", u"New Hampshire", None))
        self.stateBox.setItemText(34, QCoreApplication.translate("Address", u"New Jersey", None))
        self.stateBox.setItemText(35, QCoreApplication.translate("Address", u"New Mexico", None))
        self.stateBox.setItemText(36, QCoreApplication.translate("Address", u"New York", None))
        self.stateBox.setItemText(37, QCoreApplication.translate("Address", u"North Carolina", None))
        self.stateBox.setItemText(38, QCoreApplication.translate("Address", u"North Dakota", None))
        self.stateBox.setItemText(39, QCoreApplication.translate("Address", u"Northern Mariana Islands", None))
        self.stateBox.setItemText(40, QCoreApplication.translate("Address", u"Ohio", None))
        self.stateBox.setItemText(41, QCoreApplication.translate("Address", u"Oklahoma", None))
        self.stateBox.setItemText(42, QCoreApplication.translate("Address", u"Oregon", None))
        self.stateBox.setItemText(43, QCoreApplication.translate("Address", u"Palau", None))
        self.stateBox.setItemText(44, QCoreApplication.translate("Address", u"Pennsylvania", None))
        self.stateBox.setItemText(45, QCoreApplication.translate("Address", u"Puerto Rico", None))
        self.stateBox.setItemText(46, QCoreApplication.translate("Address", u"Rhode Island", None))
        self.stateBox.setItemText(47, QCoreApplication.translate("Address", u"South Carolina", None))
        self.stateBox.setItemText(48, QCoreApplication.translate("Address", u"South Dakota", None))
        self.stateBox.setItemText(49, QCoreApplication.translate("Address", u"Tennessee", None))
        self.stateBox.setItemText(50, QCoreApplication.translate("Address", u"Texas", None))
        self.stateBox.setItemText(51, QCoreApplication.translate("Address", u"Utah", None))
        self.stateBox.setItemText(52, QCoreApplication.translate("Address", u"Vermont", None))
        self.stateBox.setItemText(53, QCoreApplication.translate("Address", u"Virgin Islands", None))
        self.stateBox.setItemText(54, QCoreApplication.translate("Address", u"Virginia", None))
        self.stateBox.setItemText(55, QCoreApplication.translate("Address", u"Washington", None))
        self.stateBox.setItemText(56, QCoreApplication.translate("Address", u"West Virginia", u"TAKE ME HOME"))
        self.stateBox.setItemText(57, QCoreApplication.translate("Address", u"Wisconsin", None))
        self.stateBox.setItemText(58, QCoreApplication.translate("Address", u"Wyoming", None))
        self.stateBox.setItemText(59, QCoreApplication.translate("Address", u"Armed Forces - AA", None))
        self.stateBox.setItemText(60, QCoreApplication.translate("Address", u"Armed Forces - AE", None))
        self.stateBox.setItemText(61, QCoreApplication.translate("Address", u"Armed Forces - AP", None))

        self.defaultBox.setText(QCoreApplication.translate("Address", u"Make this my default address", None))
    # retranslateUi

