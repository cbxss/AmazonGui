# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'billing.ui'
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

class Ui_Billing(object):
    def setupUi(self, Billing):
        if not Billing.objectName():
            Billing.setObjectName(u"Billing")
        Billing.resize(300, 169)
        self.gridLayout = QGridLayout(Billing)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cardLabel = QLabel(Billing)
        self.cardLabel.setObjectName(u"cardLabel")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.cardLabel.setFont(font)

        self.gridLayout.addWidget(self.cardLabel, 0, 0, 1, 1)

        self.cardLine = QLineEdit(Billing)
        self.cardLine.setObjectName(u"cardLine")

        self.gridLayout.addWidget(self.cardLine, 0, 1, 1, 2)

        self.nameLabel = QLabel(Billing)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setFont(font)

        self.gridLayout.addWidget(self.nameLabel, 1, 0, 1, 1)

        self.nameLine = QLineEdit(Billing)
        self.nameLine.setObjectName(u"nameLine")

        self.gridLayout.addWidget(self.nameLine, 1, 1, 1, 2)

        self.expirationLabel = QLabel(Billing)
        self.expirationLabel.setObjectName(u"expirationLabel")
        self.expirationLabel.setFont(font)

        self.gridLayout.addWidget(self.expirationLabel, 2, 0, 1, 1)

        self.monthBox = QComboBox(Billing)
        self.monthBox.addItem("")
        self.monthBox.addItem("")
        self.monthBox.addItem("")
        self.monthBox.addItem("")
        self.monthBox.addItem("")
        self.monthBox.addItem("")
        self.monthBox.addItem("")
        self.monthBox.addItem("")
        self.monthBox.addItem("")
        self.monthBox.addItem("")
        self.monthBox.addItem("")
        self.monthBox.addItem("")
        self.monthBox.setObjectName(u"monthBox")

        self.gridLayout.addWidget(self.monthBox, 2, 1, 1, 1)

        self.yearBox = QComboBox(Billing)
        self.yearBox.addItem("")
        self.yearBox.addItem("")
        self.yearBox.addItem("")
        self.yearBox.addItem("")
        self.yearBox.addItem("")
        self.yearBox.addItem("")
        self.yearBox.addItem("")
        self.yearBox.addItem("")
        self.yearBox.addItem("")
        self.yearBox.addItem("")
        self.yearBox.addItem("")
        self.yearBox.addItem("")
        self.yearBox.addItem("")
        self.yearBox.addItem("")
        self.yearBox.addItem("")
        self.yearBox.addItem("")
        self.yearBox.addItem("")
        self.yearBox.addItem("")
        self.yearBox.addItem("")
        self.yearBox.addItem("")
        self.yearBox.addItem("")
        self.yearBox.setObjectName(u"yearBox")

        self.gridLayout.addWidget(self.yearBox, 2, 2, 1, 1)

        self.defaultCardBox = QCheckBox(Billing)
        self.defaultCardBox.setObjectName(u"defaultCardBox")

        self.gridLayout.addWidget(self.defaultCardBox, 3, 0, 1, 3)

        self.buttonBox = QDialogButtonBox(Billing)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 3)

        QWidget.setTabOrder(self.cardLine, self.nameLine)
        QWidget.setTabOrder(self.nameLine, self.monthBox)
        QWidget.setTabOrder(self.monthBox, self.yearBox)

        self.retranslateUi(Billing)
        self.buttonBox.accepted.connect(Billing.accept)
        self.buttonBox.rejected.connect(Billing.reject)

        QMetaObject.connectSlotsByName(Billing)
    # setupUi

    def retranslateUi(self, Billing):
        Billing.setWindowTitle(QCoreApplication.translate("Billing", u"Dialog", None))
        self.cardLabel.setText(QCoreApplication.translate("Billing", u"Card number", None))
        self.nameLabel.setText(QCoreApplication.translate("Billing", u"Name on card", None))
        self.expirationLabel.setText(QCoreApplication.translate("Billing", u"Expiration date", None))
        self.monthBox.setItemText(0, QCoreApplication.translate("Billing", u"01", u"January"))
        self.monthBox.setItemText(1, QCoreApplication.translate("Billing", u"02", u"Febuary"))
        self.monthBox.setItemText(2, QCoreApplication.translate("Billing", u"03", u"March"))
        self.monthBox.setItemText(3, QCoreApplication.translate("Billing", u"04", u"April"))
        self.monthBox.setItemText(4, QCoreApplication.translate("Billing", u"05", u"May"))
        self.monthBox.setItemText(5, QCoreApplication.translate("Billing", u"06", u"June"))
        self.monthBox.setItemText(6, QCoreApplication.translate("Billing", u"07", u"July"))
        self.monthBox.setItemText(7, QCoreApplication.translate("Billing", u"08", u"August"))
        self.monthBox.setItemText(8, QCoreApplication.translate("Billing", u"09", u"September"))
        self.monthBox.setItemText(9, QCoreApplication.translate("Billing", u"10", u"October"))
        self.monthBox.setItemText(10, QCoreApplication.translate("Billing", u"11", u"November"))
        self.monthBox.setItemText(11, QCoreApplication.translate("Billing", u"12", u"December"))

        self.yearBox.setItemText(0, QCoreApplication.translate("Billing", u"2022", None))
        self.yearBox.setItemText(1, QCoreApplication.translate("Billing", u"2023", None))
        self.yearBox.setItemText(2, QCoreApplication.translate("Billing", u"2024", None))
        self.yearBox.setItemText(3, QCoreApplication.translate("Billing", u"2025", None))
        self.yearBox.setItemText(4, QCoreApplication.translate("Billing", u"2026", None))
        self.yearBox.setItemText(5, QCoreApplication.translate("Billing", u"2027", None))
        self.yearBox.setItemText(6, QCoreApplication.translate("Billing", u"2028", None))
        self.yearBox.setItemText(7, QCoreApplication.translate("Billing", u"2029", None))
        self.yearBox.setItemText(8, QCoreApplication.translate("Billing", u"2030", None))
        self.yearBox.setItemText(9, QCoreApplication.translate("Billing", u"2031", None))
        self.yearBox.setItemText(10, QCoreApplication.translate("Billing", u"2032", None))
        self.yearBox.setItemText(11, QCoreApplication.translate("Billing", u"2033", None))
        self.yearBox.setItemText(12, QCoreApplication.translate("Billing", u"2034", None))
        self.yearBox.setItemText(13, QCoreApplication.translate("Billing", u"2035", None))
        self.yearBox.setItemText(14, QCoreApplication.translate("Billing", u"2036", None))
        self.yearBox.setItemText(15, QCoreApplication.translate("Billing", u"2037", None))
        self.yearBox.setItemText(16, QCoreApplication.translate("Billing", u"2038", None))
        self.yearBox.setItemText(17, QCoreApplication.translate("Billing", u"2039", None))
        self.yearBox.setItemText(18, QCoreApplication.translate("Billing", u"2040", None))
        self.yearBox.setItemText(19, QCoreApplication.translate("Billing", u"2041", None))
        self.yearBox.setItemText(20, QCoreApplication.translate("Billing", u"2042", None))

        self.defaultCardBox.setText(QCoreApplication.translate("Billing", u"Make this my default address", None))
    # retranslateUi

