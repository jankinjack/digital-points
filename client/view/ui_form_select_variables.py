# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_form_select_variables.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import q_resources_rc

class Ui_Window_Main(object):
    def setupUi(self, Window_Main):
        if not Window_Main.objectName():
            Window_Main.setObjectName(u"Window_Main")
        Window_Main.resize(789, 521)
        Window_Main.setStyleSheet(u"QWidget {\n"
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
        self.centralwidget = QWidget(Window_Main)
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
        self.gridLayout_3 = QGridLayout(self.frameTop_1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(5)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 5, 0)
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

        self.horizontalSpacer_12 = QSpacerItem(372, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_12, 0, 0, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(372, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_13, 0, 2, 1, 1)

        self.pushButtonHelp = QPushButton(self.frameTop_1)
        self.pushButtonHelp.setObjectName(u"pushButtonHelp")
        self.pushButtonHelp.setMinimumSize(QSize(28, 28))
        self.pushButtonHelp.setMaximumSize(QSize(28, 28))
        self.pushButtonHelp.setStyleSheet(u"QPushButton {	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none; \n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7284b9;\n"
"	border-style: solid;\n"
"	color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #566490;\n"
"	border-style: solid;\n"
"	color: white;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/icon_help.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonHelp.setIcon(icon)
        self.pushButtonHelp.setIconSize(QSize(20, 20))

        self.gridLayout_3.addWidget(self.pushButtonHelp, 0, 3, 1, 1)


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
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonCloseApp.setIcon(icon1)

        self.horizontalLayout_13.addWidget(self.pushButtonCloseApp)


        self.horizontalLayout_15.addWidget(self.frameTop_2)


        self.gridLayout_2.addWidget(self.frameTop, 0, 0, 1, 1)

        self.frameContent = QFrame(self.centralwidget)
        self.frameContent.setObjectName(u"frameContent")
        self.frameContent.setStyleSheet(u"#frameContent {\n"
"	background-color: #f8f8f2;\n"
"	border-left: 1px solid #6272a4;\n"
"	border-bottom: 1px solid #6272a4;\n"
"	border-right: 1px solid #6272a4;\n"
"}")
        self.frameContent.setFrameShape(QFrame.Shape.NoFrame)
        self.frameContent.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frameContent)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setSpacing(9)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(9, 9, 9, 0)
        self.frameLine_1 = QFrame(self.frameContent)
        self.frameLine_1.setObjectName(u"frameLine_1")
        self.frameLine_1.setStyleSheet(u"#frameLine_1 {\n"
"	background: white;\n"
"	border: 0px solid #6272a4;\n"
"	border-radius: 7px;\n"
"}")
        self.frameLine_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLine_1.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frameLine_1)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(0)
        self.gridLayout_5.setVerticalSpacing(3)
        self.gridLayout_5.setContentsMargins(0, 3, 0, 3)
        self.label_3 = QLabel(self.frameLine_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEditSearchVariable = QLineEdit(self.frameLine_1)
        self.lineEditSearchVariable.setObjectName(u"lineEditSearchVariable")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSearchVariable.sizePolicy().hasHeightForWidth())
        self.lineEditSearchVariable.setSizePolicy(sizePolicy)
        self.lineEditSearchVariable.setMinimumSize(QSize(0, 23))
        self.lineEditSearchVariable.setMaximumSize(QSize(16777215, 23))
        self.lineEditSearchVariable.setStyleSheet(u"QLineEdit {\n"
"    color: #babbbd;\n"
"	background-color: white;\n"
"	/*border-bottom: 1px solid #6272a4;*/\n"
"	border-top: 1px solid #6272a4;\n"
"	padding-top: 3px;\n"
"	padding-bottom: -2px;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    color: black;\n"
"}")
        self.lineEditSearchVariable.setFrame(True)

        self.verticalLayout.addWidget(self.lineEditSearchVariable)

        self.tableWidgetVariables = QTableWidget(self.frameLine_1)
        if (self.tableWidgetVariables.columnCount() < 3):
            self.tableWidgetVariables.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidgetVariables.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidgetVariables.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidgetVariables.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidgetVariables.setObjectName(u"tableWidgetVariables")
        self.tableWidgetVariables.setMinimumSize(QSize(320, 0))
        self.tableWidgetVariables.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tableWidgetVariables.setStyleSheet(u"QTableWidget {\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"	border: none;\n"
"	padding-top: 3px;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"	background-color: white;\n"
"	color: #212121;\n"
"	border-style: none;\n"
"	border-top: 1px solid #6272a4;\n"
"	border-bottom: 1px solid #6272a4;\n"
"	padding-left: 7px;\n"
"	padding-right: 5px;\n"
"	padding-top: 3px;\n"
"	padding-bottom: 3px;\n"
"	height: 20px;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"	color: #212121;\n"
"	background:#adc9ff;\n"
"}")
        self.tableWidgetVariables.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidgetVariables.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidgetVariables.setProperty(u"showDropIndicator", False)
        self.tableWidgetVariables.setDragEnabled(True)
        self.tableWidgetVariables.setDragDropOverwriteMode(False)
        self.tableWidgetVariables.setDragDropMode(QAbstractItemView.DragDropMode.DragOnly)
        self.tableWidgetVariables.setAlternatingRowColors(False)
        self.tableWidgetVariables.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidgetVariables.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidgetVariables.setShowGrid(True)
        self.tableWidgetVariables.horizontalHeader().setVisible(True)
        self.tableWidgetVariables.horizontalHeader().setHighlightSections(False)
        self.tableWidgetVariables.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetVariables.verticalHeader().setVisible(False)
        self.tableWidgetVariables.verticalHeader().setDefaultSectionSize(26)
        self.tableWidgetVariables.verticalHeader().setHighlightSections(False)

        self.verticalLayout.addWidget(self.tableWidgetVariables)


        self.gridLayout_5.addLayout(self.verticalLayout, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frameLine_1, 0, 0, 2, 1)

        self.frameLineGraph1 = QFrame(self.frameContent)
        self.frameLineGraph1.setObjectName(u"frameLineGraph1")
        self.frameLineGraph1.setStyleSheet(u"#frameLineGraph1 {\n"
"	background: white;\n"
"	border: 0px solid #6272a4;\n"
"	border-radius: 7px;\n"
"}")
        self.frameLineGraph1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLineGraph1.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frameLineGraph1)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 3, 0, 3)
        self.label_2 = QLabel(self.frameLineGraph1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 20))
        self.label_2.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setFamilies([u"Droid Sans"])
        font1.setBold(True)
        font1.setItalic(False)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)

        self.tableWidgetVariableSelected_1 = QTableWidget(self.frameLineGraph1)
        if (self.tableWidgetVariableSelected_1.columnCount() < 4):
            self.tableWidgetVariableSelected_1.setColumnCount(4)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidgetVariableSelected_1.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidgetVariableSelected_1.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidgetVariableSelected_1.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidgetVariableSelected_1.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        self.tableWidgetVariableSelected_1.setObjectName(u"tableWidgetVariableSelected_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidgetVariableSelected_1.sizePolicy().hasHeightForWidth())
        self.tableWidgetVariableSelected_1.setSizePolicy(sizePolicy1)
        self.tableWidgetVariableSelected_1.setMinimumSize(QSize(320, 0))
        self.tableWidgetVariableSelected_1.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tableWidgetVariableSelected_1.setStyleSheet(u"QTableWidget {\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"	border: none;\n"
"	padding-top: 3px;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"	background-color: white;\n"
"	color: #212121;\n"
"	border-style: none;\n"
"	border-top: 1px solid #6272a4;\n"
"	border-bottom: 1px solid #6272a4;\n"
"	padding-left: 7px;\n"
"	padding-right: 5px;\n"
"	padding-top: 3px;\n"
"	padding-bottom: 3px;\n"
"	height: 20px;\n"
"}\n"
"\n"
"QHeaderView\n"
"{\n"
"	background-color: white;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: white;\n"
"	border-top: 1px solid #6272a4;\n"
"	border-bottom: 1px solid #6272a4;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"	color: #212121;\n"
"	background:#adc9ff;\n"
"}")
        self.tableWidgetVariableSelected_1.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidgetVariableSelected_1.setFrameShadow(QFrame.Shadow.Sunken)
        self.tableWidgetVariableSelected_1.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidgetVariableSelected_1.setProperty(u"showDropIndicator", False)
        self.tableWidgetVariableSelected_1.setDragEnabled(False)
        self.tableWidgetVariableSelected_1.setDragDropOverwriteMode(False)
        self.tableWidgetVariableSelected_1.setDragDropMode(QAbstractItemView.DragDropMode.DropOnly)
        self.tableWidgetVariableSelected_1.setDefaultDropAction(Qt.DropAction.IgnoreAction)
        self.tableWidgetVariableSelected_1.setAlternatingRowColors(False)
        self.tableWidgetVariableSelected_1.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidgetVariableSelected_1.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidgetVariableSelected_1.setShowGrid(True)
        self.tableWidgetVariableSelected_1.horizontalHeader().setHighlightSections(False)
        self.tableWidgetVariableSelected_1.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetVariableSelected_1.verticalHeader().setVisible(True)
        self.tableWidgetVariableSelected_1.verticalHeader().setHighlightSections(False)

        self.gridLayout_4.addWidget(self.tableWidgetVariableSelected_1, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frameLineGraph1, 0, 1, 1, 1)

        self.frameLineGraph2 = QFrame(self.frameContent)
        self.frameLineGraph2.setObjectName(u"frameLineGraph2")
        self.frameLineGraph2.setStyleSheet(u"#frameLineGraph2 {\n"
"	background: white;\n"
"	border: 0px solid #6272a4;\n"
"	border-radius: 7px;\n"
"}")
        self.frameLineGraph2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLineGraph2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frameLineGraph2)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 3, 0, 3)
        self.label = QLabel(self.frameLineGraph2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 20))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.tableWidgetVariableSelected_2 = QTableWidget(self.frameLineGraph2)
        if (self.tableWidgetVariableSelected_2.columnCount() < 4):
            self.tableWidgetVariableSelected_2.setColumnCount(4)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidgetVariableSelected_2.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidgetVariableSelected_2.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidgetVariableSelected_2.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidgetVariableSelected_2.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        self.tableWidgetVariableSelected_2.setObjectName(u"tableWidgetVariableSelected_2")
        sizePolicy1.setHeightForWidth(self.tableWidgetVariableSelected_2.sizePolicy().hasHeightForWidth())
        self.tableWidgetVariableSelected_2.setSizePolicy(sizePolicy1)
        self.tableWidgetVariableSelected_2.setMinimumSize(QSize(320, 0))
        self.tableWidgetVariableSelected_2.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tableWidgetVariableSelected_2.setStyleSheet(u"QTableWidget {\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"	border: none;\n"
"	padding-top: 3px;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"	background-color: white;\n"
"	color: #212121;\n"
"	border-style: none;\n"
"	border-top: 1px solid #6272a4;\n"
"	border-bottom: 1px solid #6272a4;\n"
"	padding-left: 7px;\n"
"	padding-right: 5px;\n"
"	padding-top: 3px;\n"
"	padding-bottom: 3px;\n"
"	height: 20px;\n"
"}\n"
"\n"
"QHeaderView\n"
"{\n"
"	background-color: white;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: white;\n"
"	border-top: 1px solid #6272a4;\n"
"	border-bottom: 1px solid #6272a4;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"	color: #212121;\n"
"	background:#adc9ff;\n"
"}")
        self.tableWidgetVariableSelected_2.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidgetVariableSelected_2.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidgetVariableSelected_2.setProperty(u"showDropIndicator", False)
        self.tableWidgetVariableSelected_2.setDragEnabled(False)
        self.tableWidgetVariableSelected_2.setDragDropOverwriteMode(False)
        self.tableWidgetVariableSelected_2.setDragDropMode(QAbstractItemView.DragDropMode.DropOnly)
        self.tableWidgetVariableSelected_2.setDefaultDropAction(Qt.DropAction.IgnoreAction)
        self.tableWidgetVariableSelected_2.setAlternatingRowColors(False)
        self.tableWidgetVariableSelected_2.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidgetVariableSelected_2.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidgetVariableSelected_2.setShowGrid(True)
        self.tableWidgetVariableSelected_2.horizontalHeader().setVisible(True)
        self.tableWidgetVariableSelected_2.horizontalHeader().setHighlightSections(False)
        self.tableWidgetVariableSelected_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetVariableSelected_2.verticalHeader().setVisible(True)
        self.tableWidgetVariableSelected_2.verticalHeader().setHighlightSections(False)

        self.gridLayout.addWidget(self.tableWidgetVariableSelected_2, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frameLineGraph2, 1, 1, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, -1, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_7.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frameContent, 1, 0, 1, 1)

        Window_Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window_Main)

        QMetaObject.connectSlotsByName(Window_Main)
    # setupUi

    def retranslateUi(self, Window_Main):
        Window_Main.setWindowTitle(QCoreApplication.translate("Window_Main", u"Variables Selection", None))
        self.label_4.setText(QCoreApplication.translate("Window_Main", u"Variables Selection", None))
        self.pushButtonHelp.setText("")
        self.pushButtonCloseApp.setText("")
        self.label_3.setText(QCoreApplication.translate("Window_Main", u"List of Available Variables", None))
        self.lineEditSearchVariable.setText("")
        self.lineEditSearchVariable.setPlaceholderText(QCoreApplication.translate("Window_Main", u"Search for a variable...", None))
        ___qtablewidgetitem = self.tableWidgetVariables.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Window_Main", u"Name", None))
        ___qtablewidgetitem1 = self.tableWidgetVariables.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Window_Main", u"Type", None))
        ___qtablewidgetitem2 = self.tableWidgetVariables.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Window_Main", u"Address (hex)", None))
        self.label_2.setText(QCoreApplication.translate("Window_Main", u"Graph 1 (X for FRA)", None))
        ___qtablewidgetitem3 = self.tableWidgetVariableSelected_1.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Window_Main", u"Name", None))
        ___qtablewidgetitem4 = self.tableWidgetVariableSelected_1.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Window_Main", u"Type", None))
        ___qtablewidgetitem5 = self.tableWidgetVariableSelected_1.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Window_Main", u"Address (hex)", None))
        ___qtablewidgetitem6 = self.tableWidgetVariableSelected_1.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Window_Main", u"Expression", None))
        self.label.setText(QCoreApplication.translate("Window_Main", u"Graph 2 (Y for FRA)", None))
        ___qtablewidgetitem7 = self.tableWidgetVariableSelected_2.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Window_Main", u"Name", None))
        ___qtablewidgetitem8 = self.tableWidgetVariableSelected_2.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Window_Main", u"Type", None))
        ___qtablewidgetitem9 = self.tableWidgetVariableSelected_2.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Window_Main", u"Address (hex)", None))
        ___qtablewidgetitem10 = self.tableWidgetVariableSelected_2.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Window_Main", u"Expression", None))
    # retranslateUi

