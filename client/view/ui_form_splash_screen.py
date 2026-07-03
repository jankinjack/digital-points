# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_form_splash_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QMainWindow,
    QSizePolicy, QWidget)
import q_resources_rc

class Ui_Window_Main(object):
    def setupUi(self, Window_Main):
        if not Window_Main.objectName():
            Window_Main.setObjectName(u"Window_Main")
        Window_Main.resize(350, 170)
        Window_Main.setMinimumSize(QSize(350, 170))
        Window_Main.setMaximumSize(QSize(350, 200))
        Window_Main.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}")
        Window_Main.setDocumentMode(False)
        Window_Main.setDockNestingEnabled(False)
        self.centralwidget = QWidget(Window_Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(350, 170))
        self.widget.setMaximumSize(QSize(350, 170))
        self.widget.setStyleSheet(u"#widget {\n"
"	background: url(':/images/images/splash_screen.png')  no-repeat transparent;\n"
"}")

        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        Window_Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window_Main)

        QMetaObject.connectSlotsByName(Window_Main)
    # setupUi

    def retranslateUi(self, Window_Main):
        Window_Main.setWindowTitle(QCoreApplication.translate("Window_Main", u"Splash Screen", None))
    # retranslateUi

