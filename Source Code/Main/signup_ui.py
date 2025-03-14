# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_SignUp(object):
    def setupUi(self, SignUp):
        if not SignUp.objectName():
            SignUp.setObjectName(u"SignUp")
        SignUp.resize(800, 600)
        self.titleLabel = QLabel(SignUp)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(20, 20, 200, 40))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.firstNameInput = QLineEdit(SignUp)
        self.firstNameInput.setObjectName(u"firstNameInput")
        self.firstNameInput.setGeometry(QRect(20, 80, 760, 30))
        self.lastNameInput = QLineEdit(SignUp)
        self.lastNameInput.setObjectName(u"lastNameInput")
        self.lastNameInput.setGeometry(QRect(20, 120, 760, 30))
        self.emailInput = QLineEdit(SignUp)
        self.emailInput.setObjectName(u"emailInput")
        self.emailInput.setGeometry(QRect(20, 160, 760, 30))
        self.passwordInput = QLineEdit(SignUp)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setEchoMode(QLineEdit.Password)
        self.passwordInput.setGeometry(QRect(20, 200, 760, 30))
        self.carTypeInput = QLineEdit(SignUp)
        self.carTypeInput.setObjectName(u"carTypeInput")
        self.carTypeInput.setGeometry(QRect(20, 240, 760, 30))
        self.carModelInput = QLineEdit(SignUp)
        self.carModelInput.setObjectName(u"carModelInput")
        self.carModelInput.setGeometry(QRect(20, 280, 760, 30))
        self.registerButton = QPushButton(SignUp)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setGeometry(QRect(20, 320, 760, 30))
        self.backButton = QPushButton(SignUp)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(20, 360, 760, 30))

        self.retranslateUi(SignUp)

        QMetaObject.connectSlotsByName(SignUp)
    # setupUi

    def retranslateUi(self, SignUp):
        SignUp.setWindowTitle(QCoreApplication.translate("SignUp", u"Park & Spark - Parking System", None))
        self.titleLabel.setText(QCoreApplication.translate("SignUp", u"Sign Up", None))
        self.firstNameInput.setPlaceholderText(QCoreApplication.translate("SignUp", u"First Name", None))
        self.lastNameInput.setPlaceholderText(QCoreApplication.translate("SignUp", u"Last Name", None))
        self.emailInput.setPlaceholderText(QCoreApplication.translate("SignUp", u"Email Address", None))
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("SignUp", u"Password", None))
        self.carTypeInput.setPlaceholderText(QCoreApplication.translate("SignUp", u"Car Type", None))
        self.carModelInput.setPlaceholderText(QCoreApplication.translate("SignUp", u"Car Model", None))
        self.registerButton.setText(QCoreApplication.translate("SignUp", u"Register", None))
        self.backButton.setText(QCoreApplication.translate("SignUp", u"Back", None))
    # retranslateUi

