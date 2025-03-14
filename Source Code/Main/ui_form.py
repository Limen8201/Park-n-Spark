# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.welcomeLabel = QLabel(Form)
        self.welcomeLabel.setObjectName(u"welcomeLabel")
        self.welcomeLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.welcomeLabel)

        self.signin_button = QPushButton(Form)
        self.signin_button.setObjectName(u"signin_button")

        self.verticalLayout.addWidget(self.signin_button)

        self.signup_button = QPushButton(Form)
        self.signup_button.setObjectName(u"signup_button")

        self.verticalLayout.addWidget(self.signup_button)

        self.guest_button = QPushButton(Form)
        self.guest_button.setObjectName(u"guest_button")

        self.verticalLayout.addWidget(self.guest_button)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Welcome to Park and Spark", None))
        self.welcomeLabel.setText(QCoreApplication.translate("Form", u"Welcome to Park and Spark", None))
        self.signin_button.setText(QCoreApplication.translate("Form", u"Sign In", None))
        self.signup_button.setText(QCoreApplication.translate("Form", u"Sign Up", None))
        self.guest_button.setText(QCoreApplication.translate("Form", u"Continue as Guest", None))
    # retranslateUi

