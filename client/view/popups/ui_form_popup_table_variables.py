# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_form_popup_table_variables.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import q_resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(340, 30)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(340, 30))
        Form.setMaximumSize(QSize(340, 30))
        Form.setStyleSheet(u"#Form {\n"
"    background-color: none;\n"
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
"\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEditArrayIndex = QLineEdit(Form)
        self.lineEditArrayIndex.setObjectName(u"lineEditArrayIndex")
        self.lineEditArrayIndex.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEditArrayIndex.sizePolicy().hasHeightForWidth())
        self.lineEditArrayIndex.setSizePolicy(sizePolicy1)
        self.lineEditArrayIndex.setMinimumSize(QSize(170, 30))
        self.lineEditArrayIndex.setMaximumSize(QSize(170, 30))
        self.lineEditArrayIndex.setStyleSheet(u"QLineEdit {\n"
"    color: #babbbd;\n"
"	background-color: white;\n"
"	border-left: 1px solid #BABBBD;\n"
"	border-top: 1px solid #BABBBD;\n"
"	border-bottom: 1px solid #BABBBD;\n"
"	border-radius: 0px;\n"
"	padding: 3px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    color: black;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    color: #aaaaaa;\n"
"	background-color: #babbbd;\n"
"}")

        self.horizontalLayout.addWidget(self.lineEditArrayIndex)

        self.pushButtonSetTrigger = QPushButton(Form)
        self.pushButtonSetTrigger.setObjectName(u"pushButtonSetTrigger")
        sizePolicy1.setHeightForWidth(self.pushButtonSetTrigger.sizePolicy().hasHeightForWidth())
        self.pushButtonSetTrigger.setSizePolicy(sizePolicy1)
        self.pushButtonSetTrigger.setMinimumSize(QSize(170, 30))
        self.pushButtonSetTrigger.setMaximumSize(QSize(340, 30))
        self.pushButtonSetTrigger.setStyleSheet(u"QPushButton {	\n"
"	background-color: white;	\n"
"	border: none; \n"
"	color: #212121;\n"
"	border-bottom: 1px solid #BABBBD;\n"
"	border-top: 1px solid #BABBBD;\n"
"	border-left: 1px solid #BABBBD;\n"
"	border-right: 1px solid #BABBBD;\n"
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

        self.horizontalLayout.addWidget(self.pushButtonSetTrigger)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lineEditArrayIndex.setText("")
        self.lineEditArrayIndex.setPlaceholderText(QCoreApplication.translate("Form", u"Index", None))
        self.pushButtonSetTrigger.setText(QCoreApplication.translate("Form", u"   Select as Trigger   ", None))
    # retranslateUi

