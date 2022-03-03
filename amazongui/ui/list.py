# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'list.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QPlainTextEdit, QSizePolicy, QWidget)

class Ui_List(object):
    def setupUi(self, List):
        if not List.objectName():
            List.setObjectName(u"List")
        List.resize(640, 480)
        self.gridLayout = QGridLayout(List)
        self.gridLayout.setObjectName(u"gridLayout")
        self.plainTextEdit = QPlainTextEdit(List)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(List)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(List)
        self.buttonBox.accepted.connect(List.accept)
        self.buttonBox.rejected.connect(List.reject)

        QMetaObject.connectSlotsByName(List)
    # setupUi

    def retranslateUi(self, List):
        List.setWindowTitle(QCoreApplication.translate("List", u"Dialog", None))
    # retranslateUi

