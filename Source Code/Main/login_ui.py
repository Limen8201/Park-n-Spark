# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        if not LoginForm.objectName():
            LoginForm.setObjectName(u"LoginForm")
        LoginForm.resize(800, 600)
        self.label = QLabel(LoginForm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 20, 361, 41))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.emailInput = QLineEdit(LoginForm)
        self.emailInput.setObjectName(u"emailInput")
        self.emailInput.setGeometry(QRect(30, 120, 741, 51))
        self.passwordInput = QLineEdit(LoginForm)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setGeometry(QRect(30, 220, 741, 51))
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)
        self.loginButton = QPushButton(LoginForm)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(30, 490, 741, 31))
        self.backButton = QPushButton(LoginForm)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(30, 540, 741, 31))

        self.retranslateUi(LoginForm)

        QMetaObject.connectSlotsByName(LoginForm)
    # setupUi

    def retranslateUi(self, LoginForm):
        LoginForm.setWindowTitle(QCoreApplication.translate("LoginForm", u"Park & Spark - Login", None))
        self.label.setText(QCoreApplication.translate("LoginForm", u"Sign In", None))
        self.emailInput.setPlaceholderText(QCoreApplication.translate("LoginForm", u"Email Address", None))
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("LoginForm", u"Password", None))
        self.loginButton.setText(QCoreApplication.translate("LoginForm", u"Log In", None))
        self.backButton.setText(QCoreApplication.translate("LoginForm", u"Back", None))
    # retranslateUi

