# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_form_popup_fra_scope.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QPushButton,
    QSizePolicy, QWidget)
import q_resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 30)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"#Form {\n"
"    background:  transparent;\n"
"}\n"
"\n"
"QWidget {\n"
"	font-family: Droid Sans;\n"
"	font-size: 15px;\n"
"    color: #212121;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"	font-family: Open Sans;\n"
"	font-size: 15px;\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frameContent = QFrame(Form)
        self.frameContent.setObjectName(u"frameContent")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frameContent.sizePolicy().hasHeightForWidth())
        self.frameContent.setSizePolicy(sizePolicy1)
        self.frameContent.setMinimumSize(QSize(0, 0))
        self.frameContent.setStyleSheet(u"#frameContent {\n"
"	background: white;\n"
"}")
        self.frameContent.setFrameShape(QFrame.NoFrame)
        self.frameContent.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frameContent)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButtonExportPng = QPushButton(self.frameContent)
        self.pushButtonExportPng.setObjectName(u"pushButtonExportPng")
        sizePolicy1.setHeightForWidth(self.pushButtonExportPng.sizePolicy().hasHeightForWidth())
        self.pushButtonExportPng.setSizePolicy(sizePolicy1)
        self.pushButtonExportPng.setMinimumSize(QSize(150, 30))
        self.pushButtonExportPng.setMaximumSize(QSize(150, 30))
        self.pushButtonExportPng.setStyleSheet(u"QPushButton {	\n"
"	background-color: white;	\n"
"	border: none; \n"
"	color: #212121;\n"
"	border-bottom: 1px solid #BABBBD;\n"
"	border-left: 1px solid #BABBBD;\n"
"	border-right: 1px solid #BABBBD;\n"
"	border-top: 1px solid #BABBBD;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #dfe2ec;\n"
"	border-style: solid;\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #bec5da;\n"
"	border-style: solid;\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #aaaaaa;\n"
"	border: 1px solid #aaaaaa;\n"
"}")

        self.gridLayout.addWidget(self.pushButtonExportPng, 0, 1, 1, 1)

        self.pushButtonExportCsv = QPushButton(self.frameContent)
        self.pushButtonExportCsv.setObjectName(u"pushButtonExportCsv")
        sizePolicy1.setHeightForWidth(self.pushButtonExportCsv.sizePolicy().hasHeightForWidth())
        self.pushButtonExportCsv.setSizePolicy(sizePolicy1)
        self.pushButtonExportCsv.setMinimumSize(QSize(150, 30))
        self.pushButtonExportCsv.setMaximumSize(QSize(150, 30))
        self.pushButtonExportCsv.setStyleSheet(u"QPushButton {	\n"
"	background-color: white;	\n"
"	border: none; \n"
"	color: #212121;\n"
"	border-bottom: 1px solid #BABBBD;\n"
"	border-left: 1px solid #BABBBD;\n"
"	border-top: 1px solid #BABBBD;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #dfe2ec;\n"
"	border-style: solid;\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #bec5da;\n"
"	border-style: solid;\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #aaaaaa;\n"
"	border: 1px solid #aaaaaa;\n"
"}")

        self.gridLayout.addWidget(self.pushButtonExportCsv, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frameContent, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButtonExportPng.setText(QCoreApplication.translate("Form", u"Export PNG", None))
        self.pushButtonExportCsv.setText(QCoreApplication.translate("Form", u"Export CSV", None))
    # retranslateUi

