# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_form_popup_fft_range.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import q_resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(408, 30)
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
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))
        self.label.setStyleSheet(u"QLabel {\n"
"	color: #212121;\n"
"	background-color: white;\n"
"	border-top: 1px solid #BABBBD;\n"
"	border-left: 1px solid #BABBBD;\n"
"	border-bottom: 1px solid #BABBBD;\n"
"}")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEditXmin = QLineEdit(Form)
        self.lineEditXmin.setObjectName(u"lineEditXmin")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEditXmin.sizePolicy().hasHeightForWidth())
        self.lineEditXmin.setSizePolicy(sizePolicy1)
        self.lineEditXmin.setMinimumSize(QSize(100, 30))
        self.lineEditXmin.setMaximumSize(QSize(16777215, 30))
        self.lineEditXmin.setStyleSheet(u"QLineEdit {\n"
"    color: black;\n"
"	background-color: white;\n"
"	border-bottom: 1px solid #BABBBD;\n"
"	border-top: 1px solid #BABBBD;\n"
"	border-radius: 0px;\n"
"	padding: 3px;\n"
"}")

        self.gridLayout.addWidget(self.lineEditXmin, 0, 1, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 30))
        self.label_2.setStyleSheet(u"QLabel {\n"
"	color: #212121;\n"
"	background-color: white;\n"
"	border-top: 1px solid #BABBBD;\n"
"	border-left: 1px solid #BABBBD;\n"
"	border-bottom: 1px solid #BABBBD;\n"
"}")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.lineEditXmax = QLineEdit(Form)
        self.lineEditXmax.setObjectName(u"lineEditXmax")
        sizePolicy1.setHeightForWidth(self.lineEditXmax.sizePolicy().hasHeightForWidth())
        self.lineEditXmax.setSizePolicy(sizePolicy1)
        self.lineEditXmax.setMinimumSize(QSize(100, 30))
        self.lineEditXmax.setMaximumSize(QSize(16777215, 30))
        self.lineEditXmax.setStyleSheet(u"QLineEdit {\n"
"    color: black;\n"
"	background-color: white;\n"
"	border-bottom: 1px solid #BABBBD;\n"
"	border-top: 1px solid #BABBBD;\n"
"	border-radius: 0px;\n"
"	padding: 3px;\n"
"}")

        self.gridLayout.addWidget(self.lineEditXmax, 0, 3, 1, 1)

        self.pushButtonCompute = QPushButton(Form)
        self.pushButtonCompute.setObjectName(u"pushButtonCompute")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButtonCompute.sizePolicy().hasHeightForWidth())
        self.pushButtonCompute.setSizePolicy(sizePolicy2)
        self.pushButtonCompute.setMinimumSize(QSize(90, 30))
        self.pushButtonCompute.setStyleSheet(u"QPushButton {	\n"
"	background-color: white;	\n"
"	border: none; \n"
"	color: #212121;\n"
"	border: 1px solid #BABBBD;\n"
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

        self.gridLayout.addWidget(self.pushButtonCompute, 0, 4, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt;\">t</span><span style=\" font-size:14pt; vertical-align:sub;\">min</span><span style=\" font-size:11pt;\"> =</span></p></body></html>", None))
        self.lineEditXmin.setText("")
        self.lineEditXmin.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt;\">t</span><span style=\" font-size:14pt; vertical-align:sub;\">max</span><span style=\" font-size:11pt;\"> =</span></p></body></html>", None))
        self.lineEditXmax.setText("")
        self.lineEditXmax.setPlaceholderText("")
        self.pushButtonCompute.setText(QCoreApplication.translate("Form", u"Compute", None))
    # retranslateUi

