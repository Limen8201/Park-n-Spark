# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ParkingDashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        self.welcomeLabel = QLabel(Form)
        self.welcomeLabel.setObjectName(u"welcomeLabel")
        self.welcomeLabel.setGeometry(QRect(20, 20, 560, 241))
        self.payButton = QPushButton(Form)
        self.payButton.setObjectName(u"payButton")
        self.payButton.setGeometry(QRect(60, 300, 281, 91))
        self.findParkingButton = QPushButton(Form)
        self.findParkingButton.setObjectName(u"findParkingButton")
        self.findParkingButton.setGeometry(QRect(460, 300, 281, 91))
        self.cancelButton = QPushButton(Form)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(60, 450, 281, 91))
        self.logoutButton = QPushButton(Form)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setGeometry(QRect(460, 450, 281, 91))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Parking Dashboard", None))
        self.welcomeLabel.setText(QCoreApplication.translate("Form", u"Welcome, [User Name]!", None))
        self.payButton.setText(QCoreApplication.translate("Form", u"Pay", None))
        self.findParkingButton.setText(QCoreApplication.translate("Form", u"Find Parking Spot", None))
        self.cancelButton.setText(QCoreApplication.translate("Form", u"Cancellation", None))
        self.logoutButton.setText(QCoreApplication.translate("Form", u"Log Out", None))
    # retranslateUi

