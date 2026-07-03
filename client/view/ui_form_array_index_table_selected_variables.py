# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_form_array_index_table_selected_variables.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import q_resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(280, 30)
        Form.setStyleSheet(u"#Form {\n"
"    background-color: rgba(0,0,0,0)\n"
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
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEditArrayIndex = QLineEdit(Form)
        self.lineEditArrayIndex.setObjectName(u"lineEditArrayIndex")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditArrayIndex.sizePolicy().hasHeightForWidth())
        self.lineEditArrayIndex.setSizePolicy(sizePolicy)
        self.lineEditArrayIndex.setMinimumSize(QSize(200, 30))
        self.lineEditArrayIndex.setMaximumSize(QSize(16777215, 30))
        self.lineEditArrayIndex.setStyleSheet(u"QLineEdit {\n"
"    color: #babbbd;\n"
"	background-color: white;\n"
"	border-left: 1px solid #BABBBD;\n"
"	border-bottom: 1px solid #BABBBD;\n"
"	border-top: 1px solid #BABBBD;\n"
"	border-radius: 0px;\n"
"	padding: 3px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    color: black;\n"
"}")

        self.gridLayout.addWidget(self.lineEditArrayIndex, 0, 0, 1, 1)

        self.pushButtonAdd = QPushButton(Form)
        self.pushButtonAdd.setObjectName(u"pushButtonAdd")
        self.pushButtonAdd.setMinimumSize(QSize(80, 30))
        self.pushButtonAdd.setStyleSheet(u"QPushButton {	\n"
"	background-color: white;	\n"
"	border: none; \n"
"	color: #212121;\n"
"	border: 1px solid #BABBBD;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 1px solid #6272a4;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	color: #7d7d7d;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"}")

        self.gridLayout.addWidget(self.pushButtonAdd, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lineEditArrayIndex.setPlaceholderText(QCoreApplication.translate("Form", u"Array Index: x, y, z, ...", None))
        self.pushButtonAdd.setText(QCoreApplication.translate("Form", u"Add", None))
    # retranslateUi

