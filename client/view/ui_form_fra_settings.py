# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_form_fra_settings.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from pyqtgraph import GraphicsLayoutWidget
import q_resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.WindowModal)
        MainWindow.resize(945, 900)
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
        self.centralwidget.setStyleSheet(u"")
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
        self.verticalLayout_3 = QVBoxLayout(self.frameContent)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 6, -1, -1)
        self.horizontalSpacer_2 = QSpacerItem(13, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)

        self.frame = QFrame(self.frameContent)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"#frame {\n"
"	background: white;\n"
"	border: 0px solid #6272a4;\n"
"	border-radius: 7px;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))
        self.label.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.label)

        self.lineEditFmin = QLineEdit(self.frame)
        self.lineEditFmin.setObjectName(u"lineEditFmin")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEditFmin.sizePolicy().hasHeightForWidth())
        self.lineEditFmin.setSizePolicy(sizePolicy1)
        self.lineEditFmin.setMinimumSize(QSize(50, 30))
        self.lineEditFmin.setMaximumSize(QSize(16777215, 30))
        self.lineEditFmin.setStyleSheet(u"QLineEdit {\n"
"	color: #212121;\n"
"	background-color: white;\n"
"	border-left: 1px solid #6272a4;\n"
"	border-top: 1px solid #6272a4;\n"
"	border-bottom: 1px solid #6272a4;\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"	padding-left: 3px;\n"
"}")

        self.horizontalLayout.addWidget(self.lineEditFmin)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setMaximumSize(QSize(16777215, 30))
        self.label_4.setStyleSheet(u"QLabel {\n"
"	color: #212121;\n"
"	background-color: white;\n"
"	border-right: 1px solid #6272a4;\n"
"	border-top: 1px solid #6272a4;\n"
"	border-bottom: 1px solid #6272a4;\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}")

        self.horizontalLayout.addWidget(self.label_4)


        self.horizontalLayout_8.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setMaximumSize(QSize(16777215, 30))
        self.label_3.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEditFmax = QLineEdit(self.frame)
        self.lineEditFmax.setObjectName(u"lineEditFmax")
        sizePolicy1.setHeightForWidth(self.lineEditFmax.sizePolicy().hasHeightForWidth())
        self.lineEditFmax.setSizePolicy(sizePolicy1)
        self.lineEditFmax.setMinimumSize(QSize(50, 30))
        self.lineEditFmax.setMaximumSize(QSize(16777215, 30))
        self.lineEditFmax.setStyleSheet(u"QLineEdit {\n"
"	color: #212121;\n"
"	background-color: white;\n"
"	border-left: 1px solid #6272a4;\n"
"	border-top: 1px solid #6272a4;\n"
"	border-bottom: 1px solid #6272a4;\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"	padding-left: 3px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.lineEditFmax)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(0, 30))
        self.label_5.setMaximumSize(QSize(16777215, 30))
        self.label_5.setStyleSheet(u"QLabel {\n"
"	color: #212121;\n"
"	background-color: white;\n"
"	border-right: 1px solid #6272a4;\n"
"	border-top: 1px solid #6272a4;\n"
"	border-bottom: 1px solid #6272a4;\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.label_5)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setMaximumSize(QSize(40, 30))
        self.label_8.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.lineEditNfreq = QLineEdit(self.frame)
        self.lineEditNfreq.setObjectName(u"lineEditNfreq")
        sizePolicy1.setHeightForWidth(self.lineEditNfreq.sizePolicy().hasHeightForWidth())
        self.lineEditNfreq.setSizePolicy(sizePolicy1)
        self.lineEditNfreq.setMinimumSize(QSize(50, 30))
        self.lineEditNfreq.setMaximumSize(QSize(16777215, 30))
        self.lineEditNfreq.setStyleSheet(u"QLineEdit {\n"
"	color: #212121;\n"
"	background-color: white;\n"
"	border: 1px solid #6272a4;\n"
"	border-radius: 5px;\n"
"	padding-left: 3px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.lineEditNfreq)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_5)

        self.comboBoxFreqDistrib = QComboBox(self.frame)
        self.comboBoxFreqDistrib.addItem("")
        self.comboBoxFreqDistrib.addItem("")
        self.comboBoxFreqDistrib.setObjectName(u"comboBoxFreqDistrib")
        self.comboBoxFreqDistrib.setMinimumSize(QSize(0, 30))
        self.comboBoxFreqDistrib.setMaximumSize(QSize(16777215, 30))
        self.comboBoxFreqDistrib.setStyleSheet(u"QComboBox{\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #6272a4;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
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
""
                        "\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white;\n"
"    selection-background-color: #adc9ff;\n"
"	selection-color: #212121;\n"
"	height: 20px;\n"
"    outline: 0;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_8.addWidget(self.comboBoxFreqDistrib)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(0, 30))
        self.label_6.setMaximumSize(QSize(16777215, 30))
        self.label_6.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.lineEditAmplitude = QLineEdit(self.frame)
        self.lineEditAmplitude.setObjectName(u"lineEditAmplitude")
        sizePolicy1.setHeightForWidth(self.lineEditAmplitude.sizePolicy().hasHeightForWidth())
        self.lineEditAmplitude.setSizePolicy(sizePolicy1)
        self.lineEditAmplitude.setMinimumSize(QSize(50, 30))
        self.lineEditAmplitude.setMaximumSize(QSize(16777215, 30))
        self.lineEditAmplitude.setStyleSheet(u"QLineEdit {\n"
"	color: #212121;\n"
"	background-color: white;\n"
"	border: 1px solid #6272a4;\n"
"	border-radius: 5px;\n"
"	padding-left: 3px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.lineEditAmplitude)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_2)

        self.comboBoxAverageType = QComboBox(self.frame)
        self.comboBoxAverageType.addItem("")
        self.comboBoxAverageType.addItem("")
        self.comboBoxAverageType.setObjectName(u"comboBoxAverageType")
        self.comboBoxAverageType.setMinimumSize(QSize(220, 30))
        self.comboBoxAverageType.setMaximumSize(QSize(16777215, 30))
        self.comboBoxAverageType.setStyleSheet(u"QComboBox{\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #6272a4;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
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
""
                        "\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white;\n"
"    selection-background-color: #adc9ff;\n"
"	selection-color: #212121;\n"
"	height: 20px;\n"
"    outline: 0;\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.comboBoxAverageType)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 30))
        self.label_9.setMaximumSize(QSize(16777215, 30))
        self.label_9.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.lineEditRepeat = QLineEdit(self.frame)
        self.lineEditRepeat.setObjectName(u"lineEditRepeat")
        self.lineEditRepeat.setMinimumSize(QSize(50, 30))
        self.lineEditRepeat.setMaximumSize(QSize(16777215, 30))
        self.lineEditRepeat.setStyleSheet(u"QLineEdit {\n"
"	color: #212121;\n"
"	background-color: white;\n"
"	border: 1px solid #6272a4;\n"
"	border-radius: 5px;\n"
"	padding-left: 3px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.lineEditRepeat)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_4)

        self.comboBoxExcitationType = QComboBox(self.frame)
        self.comboBoxExcitationType.addItem("")
        self.comboBoxExcitationType.addItem("")
        self.comboBoxExcitationType.setObjectName(u"comboBoxExcitationType")
        self.comboBoxExcitationType.setMinimumSize(QSize(0, 30))
        self.comboBoxExcitationType.setMaximumSize(QSize(16777215, 30))
        self.comboBoxExcitationType.setStyleSheet(u"QComboBox{\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #6272a4;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
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
""
                        "\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white;\n"
"    selection-background-color: #adc9ff;\n"
"	selection-color: #212121;\n"
"	height: 20px;\n"
"    outline: 0;\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.comboBoxExcitationType)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_10.addWidget(self.frame)

        self.horizontalSpacer_3 = QSpacerItem(13, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer = QSpacerItem(1, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.graphFRAConfig = GraphicsLayoutWidget(self.frameContent)
        self.graphFRAConfig.setObjectName(u"graphFRAConfig")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.graphFRAConfig.sizePolicy().hasHeightForWidth())
        self.graphFRAConfig.setSizePolicy(sizePolicy3)
        self.graphFRAConfig.setMinimumSize(QSize(0, 200))

        self.verticalLayout.addWidget(self.graphFRAConfig)

        self.graphFRAExcitation = GraphicsLayoutWidget(self.frameContent)
        self.graphFRAExcitation.setObjectName(u"graphFRAExcitation")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.graphFRAExcitation.sizePolicy().hasHeightForWidth())
        self.graphFRAExcitation.setSizePolicy(sizePolicy4)
        self.graphFRAExcitation.setMinimumSize(QSize(0, 200))

        self.verticalLayout.addWidget(self.graphFRAExcitation)


        self.horizontalLayout_7.addLayout(self.verticalLayout)

        self.horizontalSpacer_4 = QSpacerItem(1, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(3, -1, 0, -1)
        self.pushButtonUpdateFRAExcitation = QPushButton(self.frameContent)
        self.pushButtonUpdateFRAExcitation.setObjectName(u"pushButtonUpdateFRAExcitation")
        self.pushButtonUpdateFRAExcitation.setMinimumSize(QSize(0, 25))
        self.pushButtonUpdateFRAExcitation.setMaximumSize(QSize(16777215, 25))
        self.pushButtonUpdateFRAExcitation.setStyleSheet(u"QPushButton {\n"
"	background-color: #6272a4;	\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"	border: 1px solid #6272a4;\n"
"    color: #f8f8f2;\n"
"	padding-left: 8px;\n"
"	padding-right: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7284b9;\n"
"	border-style: solid;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #566490;\n"
"	border-style: solid;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #aaaaaa;\n"
"	border: 2px solid #aaaaaa;\n"
"}")

        self.horizontalLayout_6.addWidget(self.pushButtonUpdateFRAExcitation)

        self.progressBarExcitationSynhesis = QProgressBar(self.frameContent)
        self.progressBarExcitationSynhesis.setObjectName(u"progressBarExcitationSynhesis")
        self.progressBarExcitationSynhesis.setMinimumSize(QSize(0, 22))
        self.progressBarExcitationSynhesis.setMaximumSize(QSize(16777215, 22))
        self.progressBarExcitationSynhesis.setStyleSheet(u"QProgressBar\n"
"{\n"
"	border: 1px solid #6272a4;\n"
"	border-radius: 5px;\n"
"	color: black;\n"
"}\n"
"QProgressBar::chunk \n"
"{\n"
"	background-color: #7284b9;\n"
"	border-radius: 4px;\n"
"}    ")
        self.progressBarExcitationSynhesis.setValue(0)
        self.progressBarExcitationSynhesis.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.progressBarExcitationSynhesis)

        self.pushButtonEnableFRAConfigCursors = QPushButton(self.frameContent)
        self.pushButtonEnableFRAConfigCursors.setObjectName(u"pushButtonEnableFRAConfigCursors")
        self.pushButtonEnableFRAConfigCursors.setEnabled(True)
        self.pushButtonEnableFRAConfigCursors.setMinimumSize(QSize(0, 25))
        self.pushButtonEnableFRAConfigCursors.setMaximumSize(QSize(16777215, 25))
        self.pushButtonEnableFRAConfigCursors.setStyleSheet(u"QPushButton {\n"
"	background-color: #6272a4;	\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"	border: 1px solid #6272a4;\n"
"    color: #f8f8f2;\n"
"	padding-left: 8px;\n"
"	padding-right: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7284b9;\n"
"	border-style: solid;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #566490;\n"
"	border-style: solid;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #aaaaaa;\n"
"	border: 2px solid #aaaaaa;\n"
"}")
        self.pushButtonEnableFRAConfigCursors.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.pushButtonEnableFRAConfigCursors)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.gridLayout.addWidget(self.frameContent, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FRA Settings", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"FRA Configuration", None))
        self.pushButtonCloseApp.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">f</span><span style=\" font-size:12pt; vertical-align:sub;\">min</span><span style=\" font-size:12pt;\"> = </span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"(Hz)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">f</span><span style=\" font-size:12pt; vertical-align:sub;\">max</span><span style=\" font-size:12pt;\"> = </span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"(Hz)", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">N</span><span style=\" font-size:12pt; vertical-align:sub;\">f</span><span style=\" font-size:12pt;\"> = </span></p></body></html>", None))
        self.comboBoxFreqDistrib.setItemText(0, QCoreApplication.translate("MainWindow", u"h=1 Frequency Distribution", None))
        self.comboBoxFreqDistrib.setItemText(1, QCoreApplication.translate("MainWindow", u"h=var Frequency Distribution", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"A = ", None))
        self.comboBoxAverageType.setItemText(0, QCoreApplication.translate("MainWindow", u"Vector Averaging", None))
        self.comboBoxAverageType.setItemText(1, QCoreApplication.translate("MainWindow", u"Exponential Averaging", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">N</span><span style=\" font-size:12pt; vertical-align:sub;\">repeat</span><span style=\" font-size:12pt;\"> = </span></p></body></html>", None))
        self.comboBoxExcitationType.setItemText(0, QCoreApplication.translate("MainWindow", u"Single-Sine Excitation", None))
        self.comboBoxExcitationType.setItemText(1, QCoreApplication.translate("MainWindow", u"Multi-Sine Excitation", None))

        self.pushButtonUpdateFRAExcitation.setText(QCoreApplication.translate("MainWindow", u"Synthesize Excitation Signal", None))
        self.pushButtonEnableFRAConfigCursors.setText(QCoreApplication.translate("MainWindow", u"Cursors", None))
    # retranslateUi

