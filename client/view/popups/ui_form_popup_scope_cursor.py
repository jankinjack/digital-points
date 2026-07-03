# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_form_popup_scope_cursor.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QSizePolicy, QWidget)
import q_resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(206, 45)
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
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(3, 0, 0, 0)
        self.label = QLabel(self.frameContent)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEditXCursor1 = QLineEdit(self.frameContent)
        self.lineEditXCursor1.setObjectName(u"lineEditXCursor1")
        self.lineEditXCursor1.setStyleSheet(u"QLineEdit {\n"
"	color: #212121;\n"
"	background-color: white;\n"
"	border-top: 1px solid #6272a4;\n"
"	border-right: 1px solid #6272a4;\n"
"	border-left: 1px solid #6272a4;\n"
"	padding-left: 0px;\n"
"}")

        self.gridLayout.addWidget(self.lineEditXCursor1, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frameContent)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEditXCursor2 = QLineEdit(self.frameContent)
        self.lineEditXCursor2.setObjectName(u"lineEditXCursor2")
        self.lineEditXCursor2.setStyleSheet(u"QLineEdit {\n"
"	color: #212121;\n"
"	background-color: white;\n"
"	border-top: 1px solid #6272a4;\n"
"	border-bottom: 1px solid #6272a4;\n"
"	border-right: 1px solid #6272a4;\n"
"	border-left: 1px solid #6272a4;\n"
"	padding-left: 0px;\n"
"}")

        self.gridLayout.addWidget(self.lineEditXCursor2, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frameContent, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Cursor 1", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Cursor 2", None))
    # retranslateUi

