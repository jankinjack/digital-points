# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_form_com_settings.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QWidget)
import q_resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.WindowModal)
        MainWindow.resize(669, 314)
        MainWindow.setStyleSheet(u"QWidget {\n"
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget {\n"
"	border: 1px solid #495474;\n"
"}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frameTop = QFrame(self.centralwidget)
        self.frameTop.setObjectName(u"frameTop")
        self.frameTop.setMinimumSize(QSize(0, 50))
        self.frameTop.setMaximumSize(QSize(16777215, 50))
        self.frameTop.setStyleSheet(u"")
        self.frameTop.setFrameShape(QFrame.Shape.NoFrame)
        self.frameTop.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frameTop)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frameTop_1 = QFrame(self.frameTop)
        self.frameTop_1.setObjectName(u"frameTop_1")
        self.frameTop_1.setMinimumSize(QSize(0, 50))
        self.frameTop_1.setMaximumSize(QSize(16777215, 50))
        self.frameTop_1.setStyleSheet(u"#frameTop_1 {	\n"
"	background-color: #6272a4;\n"
"	border-left:1px solid #566490;\n"
"	border-right:1px solid #566490;\n"
"}")
        self.frameTop_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frameTop_1.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.frameTop_1)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer_12 = QSpacerItem(372, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_12, 0, 0, 1, 1)

        self.label_2 = QLabel(self.frameTop_1)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Droid Sans"])
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	color: #f8f8f2;\n"
"	font-size: 16px;\n"
"}")

        self.gridLayout_8.addWidget(self.label_2, 0, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(372, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_13, 0, 2, 1, 1)


        self.horizontalLayout_15.addWidget(self.frameTop_1)

        self.frameTop_2 = QFrame(self.frameTop)
        self.frameTop_2.setObjectName(u"frameTop_2")
        self.frameTop_2.setMinimumSize(QSize(50, 50))
        self.frameTop_2.setMaximumSize(QSize(16777215, 50))
        self.frameTop_2.setStyleSheet(u"#frameTop_2 {	\n"
"	background-color: #6272a4;\n"
"}")
        self.frameTop_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frameTop_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frameTop_2)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(5, 0, 5, 0)
        self.pushButtonCloseApp = QPushButton(self.frameTop_2)
        self.pushButtonCloseApp.setObjectName(u"pushButtonCloseApp")
        self.pushButtonCloseApp.setMinimumSize(QSize(28, 28))
        self.pushButtonCloseApp.setMaximumSize(QSize(28, 28))
        self.pushButtonCloseApp.setStyleSheet(u"QPushButton {	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none; \n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  #D21F3C;\n"
"	border-style: solid;\n"
"	border-radius: 4px;\n"
"	color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #B31431;\n"
"	border-style: solid;\n"
"	border-radius: 4px;\n"
"	color: white;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonCloseApp.setIcon(icon)

        self.horizontalLayout_13.addWidget(self.pushButtonCloseApp)


        self.horizontalLayout_15.addWidget(self.frameTop_2)


        self.gridLayout.addWidget(self.frameTop, 0, 0, 1, 1)

        self.frameContent = QFrame(self.centralwidget)
        self.frameContent.setObjectName(u"frameContent")
        self.frameContent.setStyleSheet(u"#frameContent {\n"
"	background-color: #f8f8f2;\n"
"	border-right: 1px solid #6272a4;\n"
"	border-bottom: 1px solid #6272a4;\n"
"	border-left: 1px solid #6272a4;\n"
"}")
        self.frameContent.setFrameShape(QFrame.Shape.NoFrame)
        self.frameContent.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frameContent)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(9)
        self.gridLayout_3.setVerticalSpacing(6)
        self.gridLayout_3.setContentsMargins(9, 8, 9, -1)
        self.label = QLabel(self.frameContent)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 20))
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"	margin-left: 5px;\n"
"}")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.frameContent)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(0, 20))
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"QLabel {\n"
"	margin-left: 5px;\n"
"}")

        self.gridLayout_3.addWidget(self.label_3, 0, 1, 1, 1)

        self.frameLine_1 = QFrame(self.frameContent)
        self.frameLine_1.setObjectName(u"frameLine_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frameLine_1.sizePolicy().hasHeightForWidth())
        self.frameLine_1.setSizePolicy(sizePolicy1)
        self.frameLine_1.setMinimumSize(QSize(0, 0))
        self.frameLine_1.setStyleSheet(u"#frameLine_1 {\n"
"	background: white;\n"
"	border: 0px solid #6272a4;\n"
"	border-radius: 7px;\n"
"}")
        self.frameLine_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLine_1.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frameLine_1)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 3, 0, 3)
        self.line_3 = QFrame(self.frameLine_1)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(0, 2))
        self.line_3.setMaximumSize(QSize(16777215, 2))
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 7, 0, 1, 1)

        self.line_2 = QFrame(self.frameLine_1)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(0, 2))
        self.line_2.setMaximumSize(QSize(16777215, 2))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 3, 0, 1, 1)

        self.line_4 = QFrame(self.frameLine_1)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMinimumSize(QSize(0, 2))
        self.line_4.setMaximumSize(QSize(16777215, 2))
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_4, 5, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, -1, 3, -1)
        self.label_20 = QLabel(self.frameLine_1)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_2.addWidget(self.label_20)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_16)

        self.comboBoxSerialBaudrate = QComboBox(self.frameLine_1)
        self.comboBoxSerialBaudrate.setObjectName(u"comboBoxSerialBaudrate")
        sizePolicy1.setHeightForWidth(self.comboBoxSerialBaudrate.sizePolicy().hasHeightForWidth())
        self.comboBoxSerialBaudrate.setSizePolicy(sizePolicy1)
        self.comboBoxSerialBaudrate.setMinimumSize(QSize(200, 30))
        self.comboBoxSerialBaudrate.setMaximumSize(QSize(200, 30))
        self.comboBoxSerialBaudrate.setStyleSheet(u"QComboBox{\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #6272a4;\n"
"	padding-left: 10px;\n"
"	height: 20px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"	border: 1px solid #7284b9;\n"
"}\n"
"\n"
"QComboBox:disabled{\n"
"	border: 1px solid #7d7d7d;\n"
"	color: #7d7d7d;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	background-color: white;\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 28px; \n"
"	border-left: 1px solid #6272a4;\n"
"	border-top-right-radius: 3px;\n"
"	background-image: url(:/icons/icons/icon_arrow_bottom.png);\n"
"	border-bottom-right-radius: 3px;\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"\n"
"QComboBox::drop-down:disabled {\n"
"	background-color: #aaaaaa;\n"
"	border-left-color: #aaaaaa;\n"
" }\n"
"\n"
"QComboBox::drop-down:hover {\n"
"	background-color: #d1eeff;\n"
" }\n"
"\n"
"QComboBox::drop-down:on {\n"
"	background-image: url(:/icons/icons/icon_arrow_top.png);\n"
" }\n"
"\n"
"QComboBox QAbstract"
                        "ItemView {\n"
"    background-color: white;\n"
"    selection-background-color: #adc9ff;\n"
"	selection-color: #212121;\n"
"	height: 20px;\n"
"    outline: 0;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.comboBoxSerialBaudrate)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.line = QFrame(self.frameLine_1)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 2))
        self.line.setMaximumSize(QSize(16777215, 2))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, -1, 3, -1)
        self.label_18 = QLabel(self.frameLine_1)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_5.addWidget(self.label_18)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_18)

        self.comboBoxSerialStopBits = QComboBox(self.frameLine_1)
        self.comboBoxSerialStopBits.setObjectName(u"comboBoxSerialStopBits")
        sizePolicy1.setHeightForWidth(self.comboBoxSerialStopBits.sizePolicy().hasHeightForWidth())
        self.comboBoxSerialStopBits.setSizePolicy(sizePolicy1)
        self.comboBoxSerialStopBits.setMinimumSize(QSize(200, 30))
        self.comboBoxSerialStopBits.setMaximumSize(QSize(200, 30))
        self.comboBoxSerialStopBits.setStyleSheet(u"QComboBox{\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #6272a4;\n"
"	padding-left: 10px;\n"
"	height: 20px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"	border: 1px solid #7284b9;\n"
"}\n"
"\n"
"QComboBox:disabled{\n"
"	border: 1px solid #7d7d7d;\n"
"	color: #7d7d7d;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	background-color: white;\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 28px; \n"
"	border-left: 1px solid #6272a4;\n"
"	border-top-right-radius: 3px;\n"
"	background-image: url(:/icons/icons/icon_arrow_bottom.png);\n"
"	border-bottom-right-radius: 3px;\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"\n"
"QComboBox::drop-down:disabled {\n"
"	background-color: #aaaaaa;\n"
"	border-left-color: #aaaaaa;\n"
" }\n"
"\n"
"QComboBox::drop-down:hover {\n"
"	background-color: #d1eeff;\n"
" }\n"
"\n"
"QComboBox::drop-down:on {\n"
"	background-image: url(:/icons/icons/icon_arrow_top.png);\n"
" }\n"
"\n"
"QComboBox QAbstract"
                        "ItemView {\n"
"    background-color: white;\n"
"    selection-background-color: #adc9ff;\n"
"	selection-color: #212121;\n"
"	height: 20px;\n"
"    outline: 0;\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.comboBoxSerialStopBits)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 8, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, -1, 3, -1)
        self.label_17 = QLabel(self.frameLine_1)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_3.addWidget(self.label_17)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_19)

        self.comboBoxSerialDataBits = QComboBox(self.frameLine_1)
        self.comboBoxSerialDataBits.setObjectName(u"comboBoxSerialDataBits")
        sizePolicy1.setHeightForWidth(self.comboBoxSerialDataBits.sizePolicy().hasHeightForWidth())
        self.comboBoxSerialDataBits.setSizePolicy(sizePolicy1)
        self.comboBoxSerialDataBits.setMinimumSize(QSize(200, 30))
        self.comboBoxSerialDataBits.setMaximumSize(QSize(200, 30))
        self.comboBoxSerialDataBits.setStyleSheet(u"QComboBox{\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #6272a4;\n"
"	padding-left: 10px;\n"
"	height: 20px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"	border: 1px solid #7284b9;\n"
"}\n"
"\n"
"QComboBox:disabled{\n"
"	border: 1px solid #7d7d7d;\n"
"	color: #7d7d7d;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	background-color: white;\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 28px; \n"
"	border-left: 1px solid #6272a4;\n"
"	border-top-right-radius: 3px;\n"
"	background-image: url(:/icons/icons/icon_arrow_bottom.png);\n"
"	border-bottom-right-radius: 3px;\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"\n"
"QComboBox::drop-down:disabled {\n"
"	background-color: #aaaaaa;\n"
"	border-left-color: #aaaaaa;\n"
" }\n"
"\n"
"QComboBox::drop-down:hover {\n"
"	background-color: #d1eeff;\n"
" }\n"
"\n"
"QComboBox::drop-down:on {\n"
"	background-image: url(:/icons/icons/icon_arrow_top.png);\n"
" }\n"
"\n"
"QComboBox QAbstract"
                        "ItemView {\n"
"    background-color: white;\n"
"    selection-background-color: #adc9ff;\n"
"	selection-color: #212121;\n"
"	height: 20px;\n"
"    outline: 0;\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.comboBoxSerialDataBits)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, -1, 3, -1)
        self.label_16 = QLabel(self.frameLine_1)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_4.addWidget(self.label_16)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_17)

        self.comboBoxSerialParity = QComboBox(self.frameLine_1)
        self.comboBoxSerialParity.setObjectName(u"comboBoxSerialParity")
        sizePolicy1.setHeightForWidth(self.comboBoxSerialParity.sizePolicy().hasHeightForWidth())
        self.comboBoxSerialParity.setSizePolicy(sizePolicy1)
        self.comboBoxSerialParity.setMinimumSize(QSize(200, 30))
        self.comboBoxSerialParity.setMaximumSize(QSize(200, 30))
        self.comboBoxSerialParity.setStyleSheet(u"QComboBox{\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #6272a4;\n"
"	padding-left: 10px;\n"
"	height: 20px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"	border: 1px solid #7284b9;\n"
"}\n"
"\n"
"QComboBox:disabled{\n"
"	border: 1px solid #7d7d7d;\n"
"	color: #7d7d7d;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	background-color: white;\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 28px; \n"
"	border-left: 1px solid #6272a4;\n"
"	border-top-right-radius: 3px;\n"
"	background-image: url(:/icons/icons/icon_arrow_bottom.png);\n"
"	border-bottom-right-radius: 3px;\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"\n"
"QComboBox::drop-down:disabled {\n"
"	background-color: #aaaaaa;\n"
"	border-left-color: #aaaaaa;\n"
" }\n"
"\n"
"QComboBox::drop-down:hover {\n"
"	background-color: #d1eeff;\n"
" }\n"
"\n"
"QComboBox::drop-down:on {\n"
"	background-image: url(:/icons/icons/icon_arrow_top.png);\n"
" }\n"
"\n"
"QComboBox QAbstract"
                        "ItemView {\n"
"    background-color: white;\n"
"    selection-background-color: #adc9ff;\n"
"	selection-color: #212121;\n"
"	height: 20px;\n"
"    outline: 0;\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.comboBoxSerialParity)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 6, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, -1, 3, -1)
        self.label_19 = QLabel(self.frameLine_1)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout.addWidget(self.label_19)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_20)

        self.comboBoxSerialPorts = QComboBox(self.frameLine_1)
        self.comboBoxSerialPorts.setObjectName(u"comboBoxSerialPorts")
        sizePolicy1.setHeightForWidth(self.comboBoxSerialPorts.sizePolicy().hasHeightForWidth())
        self.comboBoxSerialPorts.setSizePolicy(sizePolicy1)
        self.comboBoxSerialPorts.setMinimumSize(QSize(200, 30))
        self.comboBoxSerialPorts.setMaximumSize(QSize(200, 30))
        self.comboBoxSerialPorts.setStyleSheet(u"QComboBox{\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #6272a4;\n"
"	padding-left: 10px;\n"
"	height: 20px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"	border: 1px solid #7284b9;\n"
"}\n"
"\n"
"QComboBox:disabled{\n"
"	border: 1px solid #7d7d7d;\n"
"	color: #7d7d7d;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	background-color: white;\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 28px; \n"
"	border-left: 1px solid #6272a4;\n"
"	border-top-right-radius: 3px;\n"
"	background-image: url(:/icons/icons/icon_arrow_bottom.png);\n"
"	border-bottom-right-radius: 3px;\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"\n"
"QComboBox::drop-down:disabled {\n"
"	background-color: #aaaaaa;\n"
"	border-left-color: #aaaaaa;\n"
" }\n"
"\n"
"QComboBox::drop-down:hover {\n"
"	background-color: #d1eeff;\n"
" }\n"
"\n"
"QComboBox::drop-down:on {\n"
"	background-image: url(:/icons/icons/icon_arrow_top.png);\n"
" }\n"
"\n"
"QComboBox QAbstract"
                        "ItemView {\n"
"    background-color: white;\n"
"    selection-background-color: #adc9ff;\n"
"	selection-color: #212121;\n"
"	height: 20px;\n"
"    outline: 0;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.comboBoxSerialPorts)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 10, 0, 1, 1)

        self.line_9 = QFrame(self.frameLine_1)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_9, 9, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frameLine_1, 1, 0, 1, 1)

        self.frameLine_2 = QFrame(self.frameContent)
        self.frameLine_2.setObjectName(u"frameLine_2")
        sizePolicy1.setHeightForWidth(self.frameLine_2.sizePolicy().hasHeightForWidth())
        self.frameLine_2.setSizePolicy(sizePolicy1)
        self.frameLine_2.setMinimumSize(QSize(0, 0))
        self.frameLine_2.setStyleSheet(u"#frameLine_2 {\n"
"	background: white;\n"
"	border: 0px solid #6272a4;\n"
"	border-radius: 7px;\n"
"}")
        self.frameLine_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLine_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frameLine_2)
        self.gridLayout_4.setSpacing(3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 3, 0, 3)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(10, -1, 3, -1)
        self.label_22 = QLabel(self.frameLine_2)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_9.addWidget(self.label_22)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_23)

        self.comboBoxCANBusType = QComboBox(self.frameLine_2)
        self.comboBoxCANBusType.addItem("")
        self.comboBoxCANBusType.addItem("")
        self.comboBoxCANBusType.addItem("")
        self.comboBoxCANBusType.addItem("")
        self.comboBoxCANBusType.setObjectName(u"comboBoxCANBusType")
        sizePolicy1.setHeightForWidth(self.comboBoxCANBusType.sizePolicy().hasHeightForWidth())
        self.comboBoxCANBusType.setSizePolicy(sizePolicy1)
        self.comboBoxCANBusType.setMinimumSize(QSize(200, 30))
        self.comboBoxCANBusType.setMaximumSize(QSize(200, 30))
        self.comboBoxCANBusType.setStyleSheet(u"QComboBox{\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #6272a4;\n"
"	padding-left: 10px;\n"
"	height: 20px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"	border: 1px solid #7284b9;\n"
"}\n"
"\n"
"QComboBox:disabled{\n"
"	border: 1px solid #7d7d7d;\n"
"	color: #7d7d7d;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	background-color: white;\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 28px; \n"
"	border-left: 1px solid #6272a4;\n"
"	border-top-right-radius: 3px;\n"
"	background-image: url(:/icons/icons/icon_arrow_bottom.png);\n"
"	border-bottom-right-radius: 3px;\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"\n"
"QComboBox::drop-down:disabled {\n"
"	background-color: #aaaaaa;\n"
"	border-left-color: #aaaaaa;\n"
" }\n"
"\n"
"QComboBox::drop-down:hover {\n"
"	background-color: #d1eeff;\n"
" }\n"
"\n"
"QComboBox::drop-down:on {\n"
"	background-image: url(:/icons/icons/icon_arrow_top.png);\n"
" }\n"
"\n"
"QComboBox QAbstract"
                        "ItemView {\n"
"    background-color: white;\n"
"    selection-background-color: #adc9ff;\n"
"	selection-color: #212121;\n"
"	height: 20px;\n"
"    outline: 0;\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.comboBoxCANBusType)


        self.gridLayout_4.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)

        self.line_6 = QFrame(self.frameLine_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setMinimumSize(QSize(0, 2))
        self.line_6.setMaximumSize(QSize(16777215, 2))
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_6, 3, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(10, -1, 3, -1)
        self.label_23 = QLabel(self.frameLine_2)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_11.addWidget(self.label_23)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_25)

        self.checkBoxExtendedID = QCheckBox(self.frameLine_2)
        self.checkBoxExtendedID.setObjectName(u"checkBoxExtendedID")
        self.checkBoxExtendedID.setMinimumSize(QSize(0, 30))
        self.checkBoxExtendedID.setMaximumSize(QSize(30, 30))
        self.checkBoxExtendedID.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.checkBoxExtendedID.setStyleSheet(u"QCheckBox::indicator {\n"
"    border: 1px solid #6272a4;\n"
"	width: 20px;\n"
"	height: 20px;\n"
"	border-radius: 11px;\n"
"    background: white;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 1px solid #7284b9;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	background-image: url(:/icons/icons/icon_check.png);\n"
"	background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}")

        self.horizontalLayout_11.addWidget(self.checkBoxExtendedID)


        self.gridLayout_4.addLayout(self.horizontalLayout_11, 6, 0, 1, 1)

        self.line_5 = QFrame(self.frameLine_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setMinimumSize(QSize(0, 2))
        self.line_5.setMaximumSize(QSize(16777215, 2))
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_5, 1, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(10, -1, 3, -1)
        self.label_24 = QLabel(self.frameLine_2)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_10.addWidget(self.label_24)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_24)

        self.spinBoxCANID = QSpinBox(self.frameLine_2)
        self.spinBoxCANID.setObjectName(u"spinBoxCANID")
        sizePolicy1.setHeightForWidth(self.spinBoxCANID.sizePolicy().hasHeightForWidth())
        self.spinBoxCANID.setSizePolicy(sizePolicy1)
        self.spinBoxCANID.setMinimumSize(QSize(200, 30))
        self.spinBoxCANID.setMaximumSize(QSize(200, 30))
        self.spinBoxCANID.setStyleSheet(u"QSpinBox {\n"
"	color: black;\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #6272a4;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QSpinBox:disabled {\n"
"	color: #7d7d7d;\n"
"	border: 1px solid #7d7d7d;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"	width: 28px;\n"
"	height: 28px;\n"
"	subcontrol-position: left;\n"
"	border-top-left-radius: 3px;\n"
"	border-bottom-left-radius: 3px;\n"
"	background-image: url(:/icons/icons/icon_minus.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border-right: 1px solid #6272a4;\n"
"	border-top: 1px solid #6272a4;\n"
"	border-bottom: 1px solid #6272a4;\n"
"	margin-left: 1px;\n"
" }\n"
"\n"
"QSpinBox::up-button:hover,\n"
"QSpinBox::down-button:hover {\n"
"	background-color: #d1eeff;\n"
" }\n"
"\n"
"QSpinBox::up-button:pressed,\n"
"QSpinBox::down-button:pressed {\n"
"	background-color: #f8f8f2;\n"
"}\n"
"\n"
"QSpinBox::down-button:disabled {\n"
"	background-color: #aaaaaa;\n"
"	border-left-color: #aaaaaa;\n"
"	border-top: 1"
                        "px solid #aaaaaa;\n"
" }\n"
"\n"
"QSpinBox::up-button {\n"
"	width: 28px;\n"
"	height: 28px;\n"
"	subcontrol-position: right;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"	background-image: url(:/icons/icons/icon_plus.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border-left: 1px solid #6272a4;\n"
"	border-top: 1px solid #6272a4;\n"
"	border-bottom: 1px solid #6272a4;\n"
"	margin-right: 1px;\n"
" }\n"
"\n"
"QSpinBox::up-button:disabled {\n"
"	background-color: #aaaaaa;\n"
"	border-left-color: #aaaaaa;\n"
" }\n"
"")
        self.spinBoxCANID.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinBoxCANID.setMinimum(0)
        self.spinBoxCANID.setMaximum(536870911)
        self.spinBoxCANID.setValue(0)

        self.horizontalLayout_10.addWidget(self.spinBoxCANID)


        self.gridLayout_4.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 8, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, -1, 3, -1)
        self.label_21 = QLabel(self.frameLine_2)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_8.addWidget(self.label_21)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_22)

        self.spinBoxCANBitrate = QSpinBox(self.frameLine_2)
        self.spinBoxCANBitrate.setObjectName(u"spinBoxCANBitrate")
        sizePolicy1.setHeightForWidth(self.spinBoxCANBitrate.sizePolicy().hasHeightForWidth())
        self.spinBoxCANBitrate.setSizePolicy(sizePolicy1)
        self.spinBoxCANBitrate.setMinimumSize(QSize(200, 30))
        self.spinBoxCANBitrate.setMaximumSize(QSize(200, 30))
        self.spinBoxCANBitrate.setStyleSheet(u"QSpinBox {\n"
"	color: black;\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #6272a4;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QSpinBox:disabled {\n"
"	color: #7d7d7d;\n"
"	border: 1px solid #7d7d7d;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"	width: 28px;\n"
"	height: 28px;\n"
"	subcontrol-position: left;\n"
"	border-top-left-radius: 3px;\n"
"	border-bottom-left-radius: 3px;\n"
"	background-image: url(:/icons/icons/icon_minus.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border-right: 1px solid #6272a4;\n"
"	border-top: 1px solid #6272a4;\n"
"	border-bottom: 1px solid #6272a4;\n"
"	margin-left: 1px;\n"
" }\n"
"\n"
"QSpinBox::up-button:hover,\n"
"QSpinBox::down-button:hover {\n"
"	background-color: #d1eeff;\n"
" }\n"
"\n"
"QSpinBox::up-button:pressed,\n"
"QSpinBox::down-button:pressed {\n"
"	background-color: #f8f8f2;\n"
"}\n"
"\n"
"QSpinBox::down-button:disabled {\n"
"	background-color: #aaaaaa;\n"
"	border-left-color: #aaaaaa;\n"
"	border-top: 1"
                        "px solid #aaaaaa;\n"
" }\n"
"\n"
"QSpinBox::up-button {\n"
"	width: 28px;\n"
"	height: 28px;\n"
"	subcontrol-position: right;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"	background-image: url(:/icons/icons/icon_plus.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border-left: 1px solid #6272a4;\n"
"	border-top: 1px solid #6272a4;\n"
"	border-bottom: 1px solid #6272a4;\n"
"	margin-right: 1px;\n"
" }\n"
"\n"
"QSpinBox::up-button:disabled {\n"
"	background-color: #aaaaaa;\n"
"	border-left-color: #aaaaaa;\n"
" }\n"
"")
        self.spinBoxCANBitrate.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinBoxCANBitrate.setMinimum(1)
        self.spinBoxCANBitrate.setMaximum(1000000)

        self.horizontalLayout_8.addWidget(self.spinBoxCANBitrate)


        self.gridLayout_4.addLayout(self.horizontalLayout_8, 4, 0, 1, 1)

        self.line_7 = QFrame(self.frameLine_2)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setMinimumSize(QSize(0, 2))
        self.line_7.setMaximumSize(QSize(16777215, 2))
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_7, 5, 0, 1, 1)

        self.line_8 = QFrame(self.frameLine_2)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setMinimumSize(QSize(0, 2))
        self.line_8.setMaximumSize(QSize(16777215, 2))
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_8, 7, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frameLine_2, 1, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.gridLayout_5.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frameContent, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"COM Settings", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Interfaces Configuration", None))
        self.pushButtonCloseApp.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Serial Interface", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CAN Interface", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Baudrate [baud]", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Stop Bits", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Byte Size", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Parity", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"COM Port", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"CAN Bus Type", None))
        self.comboBoxCANBusType.setItemText(0, QCoreApplication.translate("MainWindow", u"robotell", None))
        self.comboBoxCANBusType.setItemText(1, QCoreApplication.translate("MainWindow", u"socketcan", None))
        self.comboBoxCANBusType.setItemText(2, QCoreApplication.translate("MainWindow", u"gs_usb", None))
        self.comboBoxCANBusType.setItemText(3, QCoreApplication.translate("MainWindow", u"canalyst_ii", None))

        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Extended ID", None))
        self.checkBoxExtendedID.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Bitrate [bit/s]", None))
    # retranslateUi

