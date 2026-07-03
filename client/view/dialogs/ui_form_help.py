# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_form_help.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QWidget)
import q_resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(830, 632)
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
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frameTop = QFrame(self.centralwidget)
        self.frameTop.setObjectName(u"frameTop")
        self.frameTop.setMinimumSize(QSize(0, 50))
        self.frameTop.setMaximumSize(QSize(16777215, 50))
        self.frameTop.setStyleSheet(u"#frameTop {\n"
"	border-bottom: 1px solid #566490\n"
"}")
        self.frameTop.setFrameShape(QFrame.NoFrame)
        self.frameTop.setFrameShadow(QFrame.Raised)
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
        self.frameTop_1.setFrameShape(QFrame.NoFrame)
        self.frameTop_1.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frameTop_1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_12 = QSpacerItem(372, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_12, 0, 0, 1, 1)

        self.label_4 = QLabel(self.frameTop_1)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamilies([u"Droid Sans"])
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"QLabel {\n"
"	color: #f8f8f2;\n"
"	font-size: 16px;\n"
"}")

        self.gridLayout_3.addWidget(self.label_4, 0, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(372, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_13, 0, 2, 1, 1)


        self.horizontalLayout_15.addWidget(self.frameTop_1)

        self.frameTop_2 = QFrame(self.frameTop)
        self.frameTop_2.setObjectName(u"frameTop_2")
        self.frameTop_2.setMinimumSize(QSize(50, 50))
        self.frameTop_2.setMaximumSize(QSize(16777215, 50))
        self.frameTop_2.setStyleSheet(u"#frameTop_2 {	\n"
"	background-color: #6272a4;\n"
"}")
        self.frameTop_2.setFrameShape(QFrame.NoFrame)
        self.frameTop_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frameTop_2)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(5, 0, 5, 0)
        self.pushButtonCloseApp = QPushButton(self.frameTop_2)
        self.pushButtonCloseApp.setObjectName(u"pushButtonCloseApp")
        self.pushButtonCloseApp.setMinimumSize(QSize(28, 28))
        self.pushButtonCloseApp.setMaximumSize(QSize(28, 16777215))
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


        self.gridLayout_2.addWidget(self.frameTop, 0, 0, 1, 1)

        self.frameContent = QFrame(self.centralwidget)
        self.frameContent.setObjectName(u"frameContent")
        self.frameContent.setStyleSheet(u"#frameContent {\n"
"	background-color: #f8f8f2;\n"
"}")
        self.frameContent.setFrameShape(QFrame.NoFrame)
        self.frameContent.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frameContent)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(9, 9, 9, -1)
        self.pushButtonExpressions = QPushButton(self.frameContent)
        self.pushButtonExpressions.setObjectName(u"pushButtonExpressions")
        self.pushButtonExpressions.setMinimumSize(QSize(0, 25))
        self.pushButtonExpressions.setMaximumSize(QSize(16777215, 25))
        self.pushButtonExpressions.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_4.addWidget(self.pushButtonExpressions, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(720, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.frame_1 = QFrame(self.frameContent)
        self.frame_1.setObjectName(u"frame_1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_1.sizePolicy().hasHeightForWidth())
        self.frame_1.setSizePolicy(sizePolicy)
        self.frame_1.setStyleSheet(u"#frame_1 {\n"
"	background: white;\n"
"	border: 0px solid #6272a4;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"}")
        self.frame_1.setFrameShape(QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_1)
        self.gridLayout_5.setSpacing(3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 3, 0, 3)
        self.scrollArea = QScrollArea(self.frame_1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 795, 1428))
        self.scrollAreaWidgetContents.setStyleSheet(u"#scrollAreaWidgetContents {\n"
"	background-color: white;\n"
"}")
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setMargin(10)
        self.label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_5.addWidget(self.scrollArea, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_1, 1, 0, 1, 2)


        self.gridLayout_6.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(3, -1, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.gridLayout_6.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frameContent, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Variables Selection", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.pushButtonCloseApp.setText("")
        self.pushButtonExpressions.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"x1, x2, x3, ... \u2013 \u043e\u0431\u043e\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445.\n"
"x \u2013 \u0430\u043b\u0438\u0430\u0441 \u0442\u0435\u043a\u0443\u0449\u0435\u0439 \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0439, \u0434\u043b\u044f \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0444\u043e\u0440\u043c\u0438\u0440\u0443\u0435\u0442\u0441\u044f \u0432\u044b\u0440\u0430\u0436\u0435\u043d\u0438\u0435.\n"
"t \u2013 \u0444\u0443\u043d\u043a\u0446\u0438\u044f \u0432\u0440\u0435\u043c\u0435\u043d\u0438.\n"
"\n"
"\u041f\u0440\u0438\u043c\u0435\u0440 \u0432\u044b\u0440\u0430\u0436\u0435\u043d\u0438\u0439:\n"
"    0.5 * x + 10 \u2013 \u0441\u0443\u043c\u043c\u0430 \u043a\u043e\u043d\u0441\u0442\u0430\u043d\u0442\u044b 10 \u0438 \u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u044f 'x' \u0441 \u043a\u043e\u043d\u0441\u0442\u0430\u043d\u0442\u043e\u0439 0,5\n"
"    sin(t) + x1^2 * x2 \u2013 \u0441\u0438\u043d\u0443\u0441"
                        " 't' \u043f\u043b\u044e\u0441 \u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u0435 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u0430 'x1' \u0438 'x'\n"
"\n"
"\u0412\u044b\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e:\n"
"    x\n"
"\n"
"\u0421\u043f\u0438\u0441\u043e\u043a \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u043c\u044b\u0445 \u0444\u0443\u043d\u043a\u0446\u0438\u0439:\n"
"    sin(x) \u2013 \u0441\u0438\u043d\u0443\u0441 'x'\n"
"    cos(x) \u2013 \u043a\u043e\u0441\u0438\u043d\u0443\u0441 'x'\n"
"    tan(x) \u2013 \u0442\u0430\u043d\u0433\u0435\u043d\u0441 'x'\n"
"    arcsin(x) \u2013 \u0430\u0440\u043a\u0441\u0438\u043d\u0443\u0441 'x'\n"
"    arccos(x) \u2013 \u0430\u0440\u043a\u043a\u043e\u0441\u0438\u043d\u0443\u0441 'x'\n"
"    arctan(x) \u2013 \u0430\u0440\u043a\u0442\u0430\u043d\u0433\u0435\u043d\u0441 'x'\n"
"    arctan2(x, y) \u2013 \u0430\u0440\u043a\u0442\u0430\u043d\u0433\u0435\u043d\u0441"
                        " \u043e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u044f y/x \u0441 \u0443\u0447\u0451\u0442\u043e\u043c \u043a\u0432\u0430\u0434\u0440\u0430\u043d\u0442\u0430\n"
"    degrees(x) \u2013 \u043f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0435 'x' \u043e\u0442 \u0440\u0430\u0434\u0438\u0430\u043d \u043a \u0433\u0440\u0430\u0434\u0443\u0441\u0430\u043c\n"
"    radians(x) \u2013 \u043f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0435 'x' \u043e\u0442 \u0433\u0440\u0430\u0434\u0443\u0441\u043e\u0432 \u043a \u0440\u0430\u0434\u0438\u0430\u043d\u0430\u043c\n"
"    deg2rad(x) \u2013 \u0442\u043e \u0436\u0435, \u0447\u0442\u043e \u0438 radians(x)\n"
"    rad2deg(x) \u2013 \u0442\u043e \u0436\u0435, \u0447\u0442\u043e \u0438 degrees(x)\n"
"    sinh(x) \u2013 \u0433\u0438\u043f\u0435\u0440\u0431\u043e\u043b\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0441\u0438\u043d\u0443\u0441 'x'\n"
"    cosh(x) \u2013 \u0433\u0438\u043f\u0435\u0440\u0431\u043e\u043b\u0438\u0447"
                        "\u0435\u0441\u043a\u0438\u0439 \u043a\u043e\u0441\u0438\u043d\u0443\u0441 'x'\n"
"    tanh(x) \u2013 \u0433\u0438\u043f\u0435\u0440\u0431\u043e\u043b\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0442\u0430\u043d\u0433\u0435\u043d\u0441 'x'\n"
"    arcsinh(x) \u2013 \u0433\u0438\u043f\u0435\u0440\u0431\u043e\u043b\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0430\u0440\u043a\u0441\u0438\u043d\u0443\u0441 'x'\n"
"    arccosh(x) \u2013 \u0433\u0438\u043f\u0435\u0440\u0431\u043e\u043b\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0430\u0440\u043a\u043a\u043e\u0441\u0438\u043d\u0443\u0441 'x'\n"
"    arctanh(x) \u2013 \u0433\u0438\u043f\u0435\u0440\u0431\u043e\u043b\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0430\u0440\u043a\u0442\u0430\u043d\u0433\u0435\u043d\u0441 'x'\n"
"    round(x, n) \u2013 \u043e\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 'x' \u0434\u043e \u0431\u043b\u0438\u0436\u0430\u0439\u0448\u0435\u0433\u043e \u0447\u0438\u0441\u043b\u0430 \u0441 'n' \u0446\u0438\u0444\u0440 \u043f\u043e\u0441\u043b"
                        "\u0435 \u0434\u0435\u0441\u044f\u0442\u0438\u0447\u043d\u043e\u0439 \u0437\u0430\u043f\u044f\u0442\u043e\u0439\n"
"    fix(x) \u2013 \u043e\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 'x' \u0434\u043e \u0431\u043b\u0438\u0436\u0430\u0439\u0448\u0435\u0433\u043e \u0446\u0435\u043b\u043e\u0433\u043e \u0447\u0438\u0441\u043b\u0430 \u0432 \u0441\u0442\u043e\u0440\u043e\u043d\u0443 0\n"
"    floor(x) \u2013 \u043e\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 'x' \u0434\u043e \u043d\u0430\u0438\u0431\u043e\u043b\u044c\u0448\u0435\u0433\u043e \u0446\u0435\u043b\u043e\u0433\u043e, \u043c\u0435\u043d\u044c\u0448\u0435\u0433\u043e \u0438\u043b\u0438 \u0440\u0430\u0432\u043d\u043e\u0433\u043e 'x'\n"
"    ceil(x) \u2013 \u043e\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 'x' \u0434\u043e \u043d\u0430\u0438\u043c\u0435\u043d\u044c\u0448\u0435\u0433\u043e \u0446\u0435\u043b\u043e\u0433\u043e, \u0431\u043e\u043b\u044c\u0448\u0435\u0433\u043e \u0438\u043b\u0438 \u0440\u0430\u0432\u043d\u043e\u0433\u043e"
                        " 'x'\n"
"    trunc(x) \u2013 \u0442\u043e \u0436\u0435, \u0447\u0442\u043e \u0438 fix(x)\n"
"    cumprod(x) \u2013 \u043d\u0430\u043a\u0430\u043f\u043b\u0438\u0432\u0430\u0435\u043c\u043e\u0435 \u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u0435 'x'\n"
"    cumsum(x) \u2013 \u043d\u0430\u043a\u0430\u043f\u043b\u0438\u0432\u0430\u0435\u043c\u0430\u044f \u0441\u0443\u043c\u043c\u0430 'x'\n"
"    gradient(x) \u2013 \u0433\u0440\u0430\u0434\u0438\u0435\u043d\u0442 'x'\n"
"    exp(x) \u2013 \u044d\u043a\u0441\u043f\u043e\u043d\u0435\u043d\u0442\u0430 'x'\n"
"    log(x) \u2013 \u043d\u0430\u0442\u0443\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u043b\u043e\u0433\u0430\u0440\u0438\u0444\u043c 'x'\n"
"    log10(x) \u2013 \u0434\u0435\u0441\u044f\u0442\u0438\u0447\u043d\u044b\u0439 \u043b\u043e\u0433\u0430\u0440\u0438\u0444\u043c 'x'\n"
"    log2(x) \u2013 \u0434\u0432\u043e\u0438\u0447\u043d\u044b\u0439 \u043b\u043e\u0433\u0430\u0440\u0438\u0444\u043c 'x'\n"
"    i0(x) \u2013 \u043c\u043e\u0434\u0438"
                        "\u0444\u0438\u0446\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u0430\u044f \u0444\u0443\u043d\u043a\u0446\u0438\u044f \u0411\u0435\u0441\u0441\u0435\u043b\u044f 1-\u0433\u043e \u0440\u043e\u0434\u0430 0-\u0433\u043e \u043f\u043e\u0440\u044f\u0434\u043a\u0430 'x'\n"
"    sinc(x) \u2013 \u043d\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u043a\u0430\u0440\u0434\u0438\u043d\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u0438\u043d\u0443\u0441 'x'\n"
"    mod(x1, x2) \u2013 \u043e\u0441\u0442\u0430\u0442\u043e\u043a \u043e\u0442 \u0434\u0435\u043b\u0435\u043d\u0438\u044f 'x1' \u043d\u0430 'x2'\n"
"    remainder(x1, x2) \u2013 \u0442\u043e \u0436\u0435, \u0447\u0442\u043e \u0438 mod(x1, x2)\n"
"    maximum(x1, x2) \u2013 \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 'x1' \u0438 'x2'\n"
"    minimum(x1, x2) \u2013 \u043c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u0437\u043d"
                        "\u0430\u0447\u0435\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 'x1' \u0438 'x2'\n"
"    clip(x, u, l) \u2013 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u043c\u0435\u0436\u0434\u0443 \u0432\u0435\u0440\u0445\u043d\u0438\u043c 'u' \u0438 \u043d\u0438\u0436\u043d\u0438\u043c 'l' \u0443\u0440\u043e\u0432\u043d\u044f\u043c\u0438\n"
"    sqrt(x) \u2013 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u043d\u044b\u0439 \u043a\u043e\u0440\u0435\u043d\u044c 'x'\n"
"    cbrt(x) \u2013 \u043a\u0443\u0431\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043a\u043e\u0440\u0435\u043d\u044c 'x'\n"
"    square(x) \u2013 \u043a\u0432\u0430\u0434\u0440\u0430\u0442 'x' (\u0442\u043e \u0436\u0435, \u0447\u0442\u043e \u0438 x**2 \u0438\u043b\u0438 x^2)\n"
"    absolute(x) \u2013 \u0430\u0431\u0441\u043e\u043b\u044e\u0442\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 'x'\n"
"    abs(x) \u2013 \u0442\u043e \u0436\u0435, \u0447\u0442\u043e \u0438"
                        " absolute(x)\n"
"    sign(x) \u2013 \u0444\u0443\u043d\u043a\u0446\u0438\u044f \u0437\u043d\u0430\u043a\u0430 'x'\n"
"    heaviside(x) \u2013 \u0444\u0443\u043d\u043a\u0446\u0438\u044f \u0425\u0435\u0432\u0438\u0441\u0430\u0439\u0434\u0430 'x'\n"
"    median_f(x, w) \u2013 \u043c\u0435\u0434\u0438\u0430\u043d\u043d\u044b\u0439 \u0444\u0438\u043b\u044c\u0442\u0440 'x' \u043f\u043e\u0440\u044f\u0434\u043a\u0430 'w'\n"
"    l_f(x, w) \u2013 \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440 L \u0434\u043b\u044f 'x' \u0438\u0437 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0430 LULU \u0444\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u0438 \u043f\u043e\u0440\u044f\u0434\u043a\u0430 'w'\n"
"    u_f(x, w) \u2013 \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440 U \u0434\u043b\u044f 'x' \u0438\u0437 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0430 LULU \u0444\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u0438 \u043f\u043e\u0440\u044f\u0434\u043a\u0430 'w'\n"
"    lu_f(x, w) \u2013 \u043e\u043f\u0435\u0440"
                        "\u0430\u0442\u043e\u0440 LU \u0434\u043b\u044f 'x' \u0438\u0437 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0430 LULU \u0444\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u0438 \u043f\u043e\u0440\u044f\u0434\u043a\u0430 'w'\n"
"    ul_f(x, w) \u2013 \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440 UL \u0434\u043b\u044f 'x' \u0438\u0437 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0430 LULU \u0444\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u0438 \u043f\u043e\u0440\u044f\u0434\u043a\u0430 'w'\n"
"    lulu_f(x, w) \u2013 LULU \u0444\u0438\u043b\u044c\u0442\u0440 'x' \u043f\u043e\u0440\u044f\u0434\u043a\u0430 'w'\n"
"    ulul_f(x, w) \u2013 ULUL \u0444\u0438\u043b\u044c\u0442\u0440 'x' \u043f\u043e\u0440\u044f\u0434\u043a\u0430 'w'\n"
"    ma_f(x, w) \u2013 \u0444\u0438\u043b\u044c\u0442\u0440 \u0441\u043a\u043e\u043b\u044c\u0437\u044f\u0449\u0435\u0433\u043e \u0441\u0440\u0435\u0434\u043d\u0435\u0433\u043e 'x' \u043f\u043e\u0440\u044f\u0434\u043a\u0430 'w'\n"
"", None))
    # retranslateUi

