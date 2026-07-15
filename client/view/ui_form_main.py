# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_form_main.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QAbstractSpinBox, QApplication,
    QCheckBox, QComboBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from pyqtgraph import GraphicsLayoutWidget
import q_resources_rc

class Ui_Window_Main(object):
    def setupUi(self, Window_Main):
        if not Window_Main.objectName():
            Window_Main.setObjectName(u"Window_Main")
        Window_Main.resize(1252, 772)
        Window_Main.setMinimumSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u":/images/images/logo_small_circle.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Window_Main.setWindowIcon(icon)
        Window_Main.setStyleSheet(u"#Window_Main {\n"
"	background-color: #f8f8f2;\n"
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
        Window_Main.setDocumentMode(False)
        Window_Main.setDockNestingEnabled(False)
        self.centralwidget = QWidget(Window_Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"#centralwidget {\n"
"	border-right: 1px solid #6272a4;\n"
"	padding-right: 0px;\n"
"}")
        self.gridLayout_9 = QGridLayout(self.centralwidget)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frameMain = QFrame(self.centralwidget)
        self.frameMain.setObjectName(u"frameMain")
        self.frameMain.setStyleSheet(u"#frameMain {\n"
"	border-right: 1px solid #6272a4;\n"
"	padding-right: 0px;\n"
"}")
        self.frameMain.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frameMain.setFrameShape(QFrame.Shape.NoFrame)
        self.frameMain.setFrameShadow(QFrame.Shadow.Raised)
        self.frameMain.setLineWidth(0)
        self.gridLayout = QGridLayout(self.frameMain)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frameContent = QFrame(self.frameMain)
        self.frameContent.setObjectName(u"frameContent")
        self.frameContent.setStyleSheet(u"#frameContent {\n"
"	border-right: 5px solid #566490;\n"
"}")
        self.frameContent.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frameContent.setFrameShape(QFrame.Shape.NoFrame)
        self.frameContent.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frameContent)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frameContent)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.pageWords = QWidget()
        self.pageWords.setObjectName(u"pageWords")
        self.comboBox = QComboBox(self.pageWords)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 20, 241, 37))
        self.stackedWidget.addWidget(self.pageWords)
        self.pageScope = QWidget()
        self.pageScope.setObjectName(u"pageScope")
        self.pageScope.setStyleSheet(u"#pageScope {\n"
"	background-color: #f8f8f2;\n"
"}")
        self.gridLayout_6 = QGridLayout(self.pageScope)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frameScope = QFrame(self.pageScope)
        self.frameScope.setObjectName(u"frameScope")
        self.frameScope.setStyleSheet(u"")
        self.frameScope.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frameScope.setFrameShape(QFrame.Shape.NoFrame)
        self.frameScope.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_11 = QGridLayout(self.frameScope)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.graphScope = GraphicsLayoutWidget(self.frameScope)
        self.graphScope.setObjectName(u"graphScope")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphScope.sizePolicy().hasHeightForWidth())
        self.graphScope.setSizePolicy(sizePolicy)
        self.graphScope.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout_11.addWidget(self.graphScope, 0, 0, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(3)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(3, -1, 3, -1)
        self.pushButtonOpenVarViewer = QPushButton(self.frameScope)
        self.pushButtonOpenVarViewer.setObjectName(u"pushButtonOpenVarViewer")
        self.pushButtonOpenVarViewer.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButtonOpenVarViewer.sizePolicy().hasHeightForWidth())
        self.pushButtonOpenVarViewer.setSizePolicy(sizePolicy1)
        self.pushButtonOpenVarViewer.setMinimumSize(QSize(0, 25))
        self.pushButtonOpenVarViewer.setMaximumSize(QSize(16777215, 25))
        self.pushButtonOpenVarViewer.setStyleSheet(u"QPushButton {\n"
"	background-color: #6272a4;	\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"    color: #f8f8f2;\n"
"	padding-left: 8px;\n"
"	padding-right: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7284b9;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #566490;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #aaaaaa;\n"
"}")
        self.pushButtonOpenVarViewer.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.pushButtonOpenVarViewer.setCheckable(False)

        self.horizontalLayout_19.addWidget(self.pushButtonOpenVarViewer)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_3)

        self.pushButtonScopeClearImport = QPushButton(self.frameScope)
        self.pushButtonScopeClearImport.setObjectName(u"pushButtonScopeClearImport")
        self.pushButtonScopeClearImport.setMinimumSize(QSize(0, 25))
        self.pushButtonScopeClearImport.setMaximumSize(QSize(16777215, 25))
        self.pushButtonScopeClearImport.setStyleSheet(u"QPushButton {\n"
"	background-color: #6272a4;	\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"    color: #f8f8f2;\n"
"	padding-left: 8px;\n"
"	padding-right: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7284b9;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #566490;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #aaaaaa;\n"
"}")
        self.pushButtonScopeClearImport.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_19.addWidget(self.pushButtonScopeClearImport)

        self.pushButtonEnableScopeCursors = QPushButton(self.frameScope)
        self.pushButtonEnableScopeCursors.setObjectName(u"pushButtonEnableScopeCursors")
        self.pushButtonEnableScopeCursors.setMinimumSize(QSize(0, 25))
        self.pushButtonEnableScopeCursors.setMaximumSize(QSize(16777215, 25))
        self.pushButtonEnableScopeCursors.setStyleSheet(u"QPushButton {\n"
"	background-color: #6272a4;	\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"    color: #f8f8f2;\n"
"	padding-left: 8px;\n"
"	padding-right: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7284b9;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #566490;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #aaaaaa;\n"
"}")
        self.pushButtonEnableScopeCursors.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.pushButtonEnableScopeCursors.setCheckable(True)

        self.horizontalLayout_19.addWidget(self.pushButtonEnableScopeCursors)


        self.gridLayout_11.addLayout(self.horizontalLayout_19, 1, 0, 1, 1)

        self.tableWidgetNumbers = QTableWidget(self.frameScope)
        if (self.tableWidgetNumbers.columnCount() < 9):
            self.tableWidgetNumbers.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidgetNumbers.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidgetNumbers.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidgetNumbers.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidgetNumbers.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidgetNumbers.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidgetNumbers.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidgetNumbers.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidgetNumbers.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidgetNumbers.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidgetNumbers.setObjectName(u"tableWidgetNumbers")
        sizePolicy.setHeightForWidth(self.tableWidgetNumbers.sizePolicy().hasHeightForWidth())
        self.tableWidgetNumbers.setSizePolicy(sizePolicy)
        self.tableWidgetNumbers.setMinimumSize(QSize(0, 129))
        self.tableWidgetNumbers.setMaximumSize(QSize(16777215, 129))
        self.tableWidgetNumbers.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.tableWidgetNumbers.setStyleSheet(u"QTableWidget {\n"
"	font-family: Droid Sans Mono;\n"
"	background-color: white;\n"
"	border-radius: 0px;\n"
"	border-top: 1px solid #6272a4;\n"
"	padding-top: 0px;\n"
"	padding-bottom: 1px;\n"
"	gridline-color: #D6CFC7; \n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"	background-color: white;\n"
"	color: #212121;\n"
"	border-style: none;\n"
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
        self.tableWidgetNumbers.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.tableWidgetNumbers.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidgetNumbers.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableWidgetNumbers.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableWidgetNumbers.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidgetNumbers.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidgetNumbers.setProperty(u"showDropIndicator", False)
        self.tableWidgetNumbers.setDragDropOverwriteMode(False)
        self.tableWidgetNumbers.setAlternatingRowColors(False)
        self.tableWidgetNumbers.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tableWidgetNumbers.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidgetNumbers.setShowGrid(True)
        self.tableWidgetNumbers.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidgetNumbers.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidgetNumbers.horizontalHeader().setHighlightSections(True)
        self.tableWidgetNumbers.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetNumbers.verticalHeader().setVisible(False)
        self.tableWidgetNumbers.verticalHeader().setMinimumSectionSize(25)
        self.tableWidgetNumbers.verticalHeader().setDefaultSectionSize(25)
        self.tableWidgetNumbers.verticalHeader().setHighlightSections(True)
        self.tableWidgetNumbers.verticalHeader().setStretchLastSection(True)

        self.gridLayout_11.addWidget(self.tableWidgetNumbers, 2, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frameScope, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.pageScope)
        self.pageSettings = QWidget()
        self.pageSettings.setObjectName(u"pageSettings")
        self.gridLayout_7 = QGridLayout(self.pageSettings)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frameSettings = QFrame(self.pageSettings)
        self.frameSettings.setObjectName(u"frameSettings")
        self.frameSettings.setStyleSheet(u"")
        self.frameSettings.setFrameShape(QFrame.Shape.NoFrame)
        self.frameSettings.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_12 = QGridLayout(self.frameSettings)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frameSettings)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1179, 1082))
        self.scrollAreaWidgetContents.setStyleSheet(u"#scrollAreaWidgetContents {\n"
"	background-color: #f8f8f2;\n"
"}")
        self.gridLayout_21 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setHorizontalSpacing(9)
        self.gridLayout_21.setVerticalSpacing(3)
        self.gridLayout_21.setContentsMargins(9, 3, 9, 9)
        self.labelFRA = QLabel(self.scrollAreaWidgetContents)
        self.labelFRA.setObjectName(u"labelFRA")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelFRA.sizePolicy().hasHeightForWidth())
        self.labelFRA.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamilies([u"Droid Sans"])
        font.setBold(True)
        self.labelFRA.setFont(font)
        self.labelFRA.setStyleSheet(u"QLabel {\n"
"	margin-top: 5px;\n"
"	margin-left: 5px;\n"
"}")

        self.gridLayout_21.addWidget(self.labelFRA, 8, 0, 1, 1)

        self.frameLineGraphsMeas = QFrame(self.scrollAreaWidgetContents)
        self.frameLineGraphsMeas.setObjectName(u"frameLineGraphsMeas")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frameLineGraphsMeas.sizePolicy().hasHeightForWidth())
        self.frameLineGraphsMeas.setSizePolicy(sizePolicy3)
        self.frameLineGraphsMeas.setMinimumSize(QSize(520, 0))
        self.frameLineGraphsMeas.setMaximumSize(QSize(520, 16777215))
        self.frameLineGraphsMeas.setStyleSheet(u"#frameLineGraphsMeas {\n"
"	background: white;\n"
"	border: 0px solid #6272a4;\n"
"	border-radius: 7px;\n"
"}")
        self.frameLineGraphsMeas.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLineGraphsMeas.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frameLineGraphsMeas)
        self.gridLayout_4.setSpacing(3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 3, 0, 3)
        self.line_2 = QFrame(self.frameLineGraphsMeas)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(0, 2))
        self.line_2.setMaximumSize(QSize(16777215, 2))
        self.line_2.setStyleSheet(u"")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_2, 1, 0, 1, 1)

        self.line_12 = QFrame(self.frameLineGraphsMeas)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_12, 3, 0, 1, 1)

        self.widget_2 = QWidget(self.frameLineGraphsMeas)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_12.setSpacing(3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(10, 0, 3, 0)
        self.labelGraphVisibility = QLabel(self.widget_2)
        self.labelGraphVisibility.setObjectName(u"labelGraphVisibility")
        self.labelGraphVisibility.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_12.addWidget(self.labelGraphVisibility)

        self.horizontalSpacer = QSpacerItem(26, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)

        self.comboBoxGraphVisibility = QComboBox(self.widget_2)
        self.comboBoxGraphVisibility.addItem("")
        self.comboBoxGraphVisibility.addItem("")
        self.comboBoxGraphVisibility.addItem("")
        self.comboBoxGraphVisibility.setObjectName(u"comboBoxGraphVisibility")
        self.comboBoxGraphVisibility.setMinimumSize(QSize(220, 30))
        self.comboBoxGraphVisibility.setMaximumSize(QSize(220, 30))
        self.comboBoxGraphVisibility.setStyleSheet(u"QComboBox{\n"
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
        self.comboBoxGraphVisibility.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_12.addWidget(self.comboBoxGraphVisibility)


        self.gridLayout_4.addWidget(self.widget_2, 2, 0, 1, 1)

        self.widgetLayoutMode = QWidget(self.frameLineGraphsMeas)
        self.widgetLayoutMode.setObjectName(u"widgetLayoutMode")
        self.widgetLayoutMode.setStyleSheet(u"")
        self.horizontalLayoutMode = QHBoxLayout(self.widgetLayoutMode)
        self.horizontalLayoutMode.setSpacing(3)
        self.horizontalLayoutMode.setObjectName(u"horizontalLayoutMode")
        self.horizontalLayoutMode.setContentsMargins(10, 0, 3, 0)
        self.labelMode = QLabel(self.widgetLayoutMode)
        self.labelMode.setObjectName(u"labelMode")
        self.labelMode.setMinimumSize(QSize(250, 0))
        self.labelMode.setStyleSheet(u"QLabel {\n"
"	color: black;\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"	color: #7d7d7d;\n"
"}")
        self.labelMode.setWordWrap(True)

        self.horizontalLayoutMode.addWidget(self.labelMode)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutMode.addItem(self.horizontalSpacer_14)

        self.comboBoxMode = QComboBox(self.widgetLayoutMode)
        self.comboBoxMode.addItem("")
        self.comboBoxMode.addItem("")
        self.comboBoxMode.addItem("")
        self.comboBoxMode.setObjectName(u"comboBoxMode")
        self.comboBoxMode.setEnabled(True)
        self.comboBoxMode.setMinimumSize(QSize(220, 30))
        self.comboBoxMode.setMaximumSize(QSize(16777215, 30))
        self.comboBoxMode.setStyleSheet(u"QComboBox{\n"
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
        self.comboBoxMode.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.comboBoxMode.setEditable(False)
        self.comboBoxMode.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)

        self.horizontalLayoutMode.addWidget(self.comboBoxMode)


        self.gridLayout_4.addWidget(self.widgetLayoutMode, 0, 0, 1, 1)

        self.widgetLayoutMeas = QFrame(self.frameLineGraphsMeas)
        self.widgetLayoutMeas.setObjectName(u"widgetLayoutMeas")
        self.widgetLayoutMeas.setFrameShape(QFrame.Shape.StyledPanel)
        self.widgetLayoutMeas.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.widgetLayoutMeas)
        self.horizontalLayout_17.setSpacing(3)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(10, 0, 3, 0)
        self.labelCursorsMeas = QLabel(self.widgetLayoutMeas)
        self.labelCursorsMeas.setObjectName(u"labelCursorsMeas")
        self.labelCursorsMeas.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_17.addWidget(self.labelCursorsMeas)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_6)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setHorizontalSpacing(5)
        self.gridLayout_16.setVerticalSpacing(2)
        self.checkBoxMeasRMS = QCheckBox(self.widgetLayoutMeas)
        self.checkBoxMeasRMS.setObjectName(u"checkBoxMeasRMS")
        self.checkBoxMeasRMS.setStyleSheet(u"QCheckBox::indicator {\n"
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

        self.gridLayout_16.addWidget(self.checkBoxMeasRMS, 0, 1, 1, 1)

        self.checkBoxMeasDelta = QCheckBox(self.widgetLayoutMeas)
        self.checkBoxMeasDelta.setObjectName(u"checkBoxMeasDelta")
        sizePolicy1.setHeightForWidth(self.checkBoxMeasDelta.sizePolicy().hasHeightForWidth())
        self.checkBoxMeasDelta.setSizePolicy(sizePolicy1)
        self.checkBoxMeasDelta.setStyleSheet(u"QCheckBox::indicator {\n"
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

        self.gridLayout_16.addWidget(self.checkBoxMeasDelta, 0, 0, 1, 1)

        self.checkBoxMeasMean = QCheckBox(self.widgetLayoutMeas)
        self.checkBoxMeasMean.setObjectName(u"checkBoxMeasMean")
        self.checkBoxMeasMean.setStyleSheet(u"QCheckBox::indicator {\n"
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

        self.gridLayout_16.addWidget(self.checkBoxMeasMean, 2, 0, 1, 1)

        self.checkBoxMeasCF = QCheckBox(self.widgetLayoutMeas)
        self.checkBoxMeasCF.setObjectName(u"checkBoxMeasCF")
        self.checkBoxMeasCF.setStyleSheet(u"QCheckBox::indicator {\n"
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

        self.gridLayout_16.addWidget(self.checkBoxMeasCF, 2, 1, 1, 1)

        self.checkBoxMeasMin = QCheckBox(self.widgetLayoutMeas)
        self.checkBoxMeasMin.setObjectName(u"checkBoxMeasMin")
        self.checkBoxMeasMin.setStyleSheet(u"QCheckBox::indicator {\n"
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

        self.gridLayout_16.addWidget(self.checkBoxMeasMin, 1, 0, 1, 1)

        self.checkBoxMeasMax = QCheckBox(self.widgetLayoutMeas)
        self.checkBoxMeasMax.setObjectName(u"checkBoxMeasMax")
        self.checkBoxMeasMax.setStyleSheet(u"QCheckBox::indicator {\n"
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
"}\n"
"")

        self.gridLayout_16.addWidget(self.checkBoxMeasMax, 1, 1, 1, 1)


        self.horizontalLayout_17.addLayout(self.gridLayout_16)


        self.gridLayout_4.addWidget(self.widgetLayoutMeas, 4, 0, 1, 1)


        self.gridLayout_21.addWidget(self.frameLineGraphsMeas, 3, 0, 1, 1)

        self.labelUpdate = QLabel(self.scrollAreaWidgetContents)
        self.labelUpdate.setObjectName(u"labelUpdate")
        self.labelUpdate.setFont(font)
        self.labelUpdate.setStyleSheet(u"QLabel {\n"
"	margin-top: 5px;\n"
"	margin-left: 5px;\n"
"}")

        self.gridLayout_21.addWidget(self.labelUpdate, 10, 0, 1, 1)

        self.frameLineCom = QFrame(self.scrollAreaWidgetContents)
        self.frameLineCom.setObjectName(u"frameLineCom")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frameLineCom.sizePolicy().hasHeightForWidth())
        self.frameLineCom.setSizePolicy(sizePolicy4)
        self.frameLineCom.setMinimumSize(QSize(520, 0))
        self.frameLineCom.setMaximumSize(QSize(520, 16777215))
        self.frameLineCom.setStyleSheet(u"#frameLineCom {\n"
"	background: white;\n"
"	border: 0px solid #6272a4;\n"
"	border-radius: 7px;\n"
"}")
        self.frameLineCom.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLineCom.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_17 = QGridLayout(self.frameLineCom)
        self.gridLayout_17.setSpacing(3)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 3, 0, 3)
        self.widgetLayoutSaveSelection = QWidget(self.frameLineCom)
        self.widgetLayoutSaveSelection.setObjectName(u"widgetLayoutSaveSelection")
        self.horizontalLayout_21 = QHBoxLayout(self.widgetLayoutSaveSelection)
        self.horizontalLayout_21.setSpacing(3)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(10, 0, 3, 0)
        self.labelSaveSelection = QLabel(self.widgetLayoutSaveSelection)
        self.labelSaveSelection.setObjectName(u"labelSaveSelection")
        self.labelSaveSelection.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_21.addWidget(self.labelSaveSelection)

        self.horizontalSpacer_7 = QSpacerItem(310, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_7)

        self.checkBoxSaveSelection = QCheckBox(self.widgetLayoutSaveSelection)
        self.checkBoxSaveSelection.setObjectName(u"checkBoxSaveSelection")
        self.checkBoxSaveSelection.setMinimumSize(QSize(0, 25))
        self.checkBoxSaveSelection.setMaximumSize(QSize(16777215, 30))
        self.checkBoxSaveSelection.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.checkBoxSaveSelection.setStyleSheet(u"QCheckBox::indicator {\n"
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

        self.horizontalLayout_21.addWidget(self.checkBoxSaveSelection)


        self.gridLayout_17.addWidget(self.widgetLayoutSaveSelection, 4, 0, 1, 1)

        self.widgetLayoutCom = QWidget(self.frameLineCom)
        self.widgetLayoutCom.setObjectName(u"widgetLayoutCom")
        self.horizontalLayoutCom = QHBoxLayout(self.widgetLayoutCom)
        self.horizontalLayoutCom.setSpacing(3)
        self.horizontalLayoutCom.setObjectName(u"horizontalLayoutCom")
        self.horizontalLayoutCom.setContentsMargins(10, 0, 3, 0)
        self.labelComInterface = QLabel(self.widgetLayoutCom)
        self.labelComInterface.setObjectName(u"labelComInterface")
        self.labelComInterface.setEnabled(True)
        self.labelComInterface.setMinimumSize(QSize(250, 0))
        self.labelComInterface.setStyleSheet(u"QLabel {\n"
"	color: black;\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"	color: #7d7d7d;\n"
"}")
        self.labelComInterface.setWordWrap(True)

        self.horizontalLayoutCom.addWidget(self.labelComInterface)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutCom.addItem(self.horizontalSpacer_23)

        self.widgetLayoutComButtons = QWidget(self.widgetLayoutCom)
        self.widgetLayoutComButtons.setObjectName(u"widgetLayoutComButtons")
        self.widgetLayoutComButtons.setEnabled(True)
        self.horizontalLayoutComButtons = QHBoxLayout(self.widgetLayoutComButtons)
        self.horizontalLayoutComButtons.setSpacing(0)
        self.horizontalLayoutComButtons.setObjectName(u"horizontalLayoutComButtons")
        self.horizontalLayoutComButtons.setContentsMargins(0, 0, 0, 0)
        self.pushButtonSetSerial = QPushButton(self.widgetLayoutComButtons)
        self.pushButtonSetSerial.setObjectName(u"pushButtonSetSerial")
        self.pushButtonSetSerial.setEnabled(True)
        self.pushButtonSetSerial.setMinimumSize(QSize(0, 30))
        self.pushButtonSetSerial.setMaximumSize(QSize(87, 40))
        self.pushButtonSetSerial.setStyleSheet(u"QPushButton {\n"
"	background-color: #6272a4;	\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"	border-right: 1px solid #7284b9;\n"
"    color: #f8f8f2;\n"
"	padding-left: 6px;\n"
"	padding-right: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7284b9;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: #566490;\n"
"	color: #f8f8f2;\n"
"}")
        self.pushButtonSetSerial.setCheckable(True)
        self.pushButtonSetSerial.setChecked(True)

        self.horizontalLayoutComButtons.addWidget(self.pushButtonSetSerial)

        self.pushButtonSetCAN = QPushButton(self.widgetLayoutComButtons)
        self.pushButtonSetCAN.setObjectName(u"pushButtonSetCAN")
        self.pushButtonSetCAN.setEnabled(True)
        self.pushButtonSetCAN.setMinimumSize(QSize(0, 40))
        self.pushButtonSetCAN.setMaximumSize(QSize(88, 40))
        self.pushButtonSetCAN.setStyleSheet(u"QPushButton {\n"
"	background-color: #6272a4;	\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"    color: #f8f8f2;\n"
"	padding-left: 6px;\n"
"	padding-right: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7284b9;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: #566490;\n"
"	color: #f8f8f2;\n"
"}")
        self.pushButtonSetCAN.setCheckable(True)

        self.horizontalLayoutComButtons.addWidget(self.pushButtonSetCAN)


        self.horizontalLayoutCom.addWidget(self.widgetLayoutComButtons)

        self.pushButtonConfigureInterface = QPushButton(self.widgetLayoutCom)
        self.pushButtonConfigureInterface.setObjectName(u"pushButtonConfigureInterface")
        self.pushButtonConfigureInterface.setEnabled(True)
        self.pushButtonConfigureInterface.setMinimumSize(QSize(40, 40))
        self.pushButtonConfigureInterface.setMaximumSize(QSize(40, 40))
        self.pushButtonConfigureInterface.setStyleSheet(u"QPushButton {\n"
"	background-color: #6272a4;	\n"
"	border-radius: 5px;\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7284b9;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #566490;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #aaaaaa;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/icon_network_settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonConfigureInterface.setIcon(icon1)
        self.pushButtonConfigureInterface.setIconSize(QSize(30, 30))

        self.horizontalLayoutCom.addWidget(self.pushButtonConfigureInterface)


        self.gridLayout_17.addWidget(self.widgetLayoutCom, 0, 0, 1, 1)

        self.widgetLayoutNodeAddr = QWidget(self.frameLineCom)
        self.widgetLayoutNodeAddr.setObjectName(u"widgetLayoutNodeAddr")
        self.horizontalLayoutNodeAddr = QHBoxLayout(self.widgetLayoutNodeAddr)
        self.horizontalLayoutNodeAddr.setSpacing(3)
        self.horizontalLayoutNodeAddr.setObjectName(u"horizontalLayoutNodeAddr")
        self.horizontalLayoutNodeAddr.setContentsMargins(10, 0, 3, 0)
        self.labelNodeAddress = QLabel(self.widgetLayoutNodeAddr)
        self.labelNodeAddress.setObjectName(u"labelNodeAddress")
        self.labelNodeAddress.setMinimumSize(QSize(250, 0))
        self.labelNodeAddress.setStyleSheet(u"QLabel {\n"
"	color: black;\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"	color: #7d7d7d;\n"
"}")
        self.labelNodeAddress.setWordWrap(True)

        self.horizontalLayoutNodeAddr.addWidget(self.labelNodeAddress)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutNodeAddr.addItem(self.horizontalSpacer_24)

        self.spinBoxNodeAddr = QSpinBox(self.widgetLayoutNodeAddr)
        self.spinBoxNodeAddr.setObjectName(u"spinBoxNodeAddr")
        self.spinBoxNodeAddr.setEnabled(True)
        self.spinBoxNodeAddr.setMinimumSize(QSize(220, 30))
        self.spinBoxNodeAddr.setMaximumSize(QSize(220, 30))
        self.spinBoxNodeAddr.setStyleSheet(u"QSpinBox {\n"
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
        self.spinBoxNodeAddr.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.spinBoxNodeAddr.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinBoxNodeAddr.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.spinBoxNodeAddr.setMaximum(255)

        self.horizontalLayoutNodeAddr.addWidget(self.spinBoxNodeAddr)


        self.gridLayout_17.addWidget(self.widgetLayoutNodeAddr, 2, 0, 1, 1)

        self.line_13 = QFrame(self.frameLineCom)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setMinimumSize(QSize(0, 2))
        self.line_13.setMaximumSize(QSize(16777215, 2))
        self.line_13.setFrameShape(QFrame.Shape.HLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_17.addWidget(self.line_13, 3, 0, 1, 1)

        self.line_1 = QFrame(self.frameLineCom)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setMinimumSize(QSize(0, 2))
        self.line_1.setMaximumSize(QSize(16777215, 2))
        self.line_1.setFrameShape(QFrame.Shape.HLine)
        self.line_1.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_17.addWidget(self.line_1, 1, 0, 1, 1)


        self.gridLayout_21.addWidget(self.frameLineCom, 1, 0, 1, 1)

        self.frameLineSystem = QFrame(self.scrollAreaWidgetContents)
        self.frameLineSystem.setObjectName(u"frameLineSystem")
        sizePolicy3.setHeightForWidth(self.frameLineSystem.sizePolicy().hasHeightForWidth())
        self.frameLineSystem.setSizePolicy(sizePolicy3)
        self.frameLineSystem.setMinimumSize(QSize(520, 0))
        self.frameLineSystem.setStyleSheet(u"#frameLineSystem {\n"
"	background: white;\n"
"	border: 0px solid #6272a4;\n"
"	border-radius: 7px;\n"
"}")
        self.frameLineSystem.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLineSystem.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_19 = QGridLayout(self.frameLineSystem)
        self.gridLayout_19.setSpacing(3)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 3, 0, 3)
        self.widgetLayoutSystem = QWidget(self.frameLineSystem)
        self.widgetLayoutSystem.setObjectName(u"widgetLayoutSystem")
        self.horizontalLayout = QHBoxLayout(self.widgetLayoutSystem)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 3, 0)
        self.labelLanguage = QLabel(self.widgetLayoutSystem)
        self.labelLanguage.setObjectName(u"labelLanguage")
        self.labelLanguage.setMinimumSize(QSize(190, 0))
        self.labelLanguage.setStyleSheet(u"QLabel {\n"
"	color: black;\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"	color: #7d7d7d;\n"
"}")
        self.labelLanguage.setWordWrap(True)

        self.horizontalLayout.addWidget(self.labelLanguage)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_30)

        self.comboBoxLanguage = QComboBox(self.widgetLayoutSystem)
        self.comboBoxLanguage.addItem("")
        self.comboBoxLanguage.addItem("")
        self.comboBoxLanguage.setObjectName(u"comboBoxLanguage")
        self.comboBoxLanguage.setEnabled(True)
        self.comboBoxLanguage.setMinimumSize(QSize(220, 30))
        self.comboBoxLanguage.setMaximumSize(QSize(16777215, 30))
        self.comboBoxLanguage.setStyleSheet(u"QComboBox{\n"
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

        self.horizontalLayout.addWidget(self.comboBoxLanguage)


        self.gridLayout_19.addWidget(self.widgetLayoutSystem, 0, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(3, -1, 3, 0)
        self.pushButtonSaveSettings = QPushButton(self.frameLineSystem)
        self.pushButtonSaveSettings.setObjectName(u"pushButtonSaveSettings")
        self.pushButtonSaveSettings.setMinimumSize(QSize(0, 40))
        self.pushButtonSaveSettings.setMaximumSize(QSize(16777215, 40))
        self.pushButtonSaveSettings.setStyleSheet(u"QPushButton {\n"
"	background-color: #6272a4;	\n"
"	border-radius: 5px;\n"
"    color: #f8f8f2;\n"
"	padding-left: 6px;\n"
"	padding-right: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7284b9;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #566490;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #aaaaaa;\n"
"}")

        self.horizontalLayout_11.addWidget(self.pushButtonSaveSettings)

        self.pushButtonLoadSettings = QPushButton(self.frameLineSystem)
        self.pushButtonLoadSettings.setObjectName(u"pushButtonLoadSettings")
        self.pushButtonLoadSettings.setMinimumSize(QSize(0, 40))
        self.pushButtonLoadSettings.setMaximumSize(QSize(16777215, 40))
        self.pushButtonLoadSettings.setStyleSheet(u"QPushButton {\n"
"	background-color: #6272a4;	\n"
"	border-radius: 5px;\n"
"    color: #f8f8f2;\n"
"	padding-left: 6px;\n"
"	padding-right: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7284b9;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #566490;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #aaaaaa;\n"
"}")

        self.horizontalLayout_11.addWidget(self.pushButtonLoadSettings)


        self.gridLayout_19.addLayout(self.horizontalLayout_11, 2, 0, 1, 1)

        self.line_3 = QFrame(self.frameLineSystem)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(0, 2))
        self.line_3.setMaximumSize(QSize(16777215, 2))
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_19.addWidget(self.line_3, 1, 0, 1, 1)


        self.gridLayout_21.addWidget(self.frameLineSystem, 13, 0, 1, 1)

        self.labelRTM = QLabel(self.scrollAreaWidgetContents)
        self.labelRTM.setObjectName(u"labelRTM")
        self.labelRTM.setFont(font)
        self.labelRTM.setStyleSheet(u"QLabel {\n"
"	margin-top: 5px;\n"
"	margin-left: 5px;\n"
"}")

        self.gridLayout_21.addWidget(self.labelRTM, 4, 0, 1, 1)

        self.labelTrigger = QLabel(self.scrollAreaWidgetContents)
        self.labelTrigger.setObjectName(u"labelTrigger")
        sizePolicy2.setHeightForWidth(self.labelTrigger.sizePolicy().hasHeightForWidth())
        self.labelTrigger.setSizePolicy(sizePolicy2)
        self.labelTrigger.setFont(font)
        self.labelTrigger.setStyleSheet(u"QLabel {\n"
"	margin-top: 5px;\n"
"	margin-left: 5px;\n"
"}")

        self.gridLayout_21.addWidget(self.labelTrigger, 6, 0, 1, 1)

        self.labelSystem = QLabel(self.scrollAreaWidgetContents)
        self.labelSystem.setObjectName(u"labelSystem")
        self.labelSystem.setFont(font)
        self.labelSystem.setStyleSheet(u"QLabel {\n"
"	margin-top: 5px;\n"
"	margin-left: 5px;\n"
"}")

        self.gridLayout_21.addWidget(self.labelSystem, 12, 0, 1, 1)

        self.labelGraphsMeas = QLabel(self.scrollAreaWidgetContents)
        self.labelGraphsMeas.setObjectName(u"labelGraphsMeas")
        sizePolicy2.setHeightForWidth(self.labelGraphsMeas.sizePolicy().hasHeightForWidth())
        self.labelGraphsMeas.setSizePolicy(sizePolicy2)
        self.labelGraphsMeas.setFont(font)
        self.labelGraphsMeas.setStyleSheet(u"QLabel {\n"
"	margin-top: 5px;\n"
"	margin-left: 5px;\n"
"}")

        self.gridLayout_21.addWidget(self.labelGraphsMeas, 2, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frameLineVariables = QFrame(self.scrollAreaWidgetContents)
        self.frameLineVariables.setObjectName(u"frameLineVariables")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(10)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frameLineVariables.sizePolicy().hasHeightForWidth())
        self.frameLineVariables.setSizePolicy(sizePolicy5)
        self.frameLineVariables.setMinimumSize(QSize(300, 0))
        self.frameLineVariables.setStyleSheet(u"#frameLineVariables {\n"
"	background: white;\n"
"	border: 0px solid #6272a4;\n"
"	border-radius: 7px;\n"
"}")
        self.frameLineVariables.setFrameShape(QFrame.Shape.NoFrame)
        self.frameLineVariables.setFrameShadow(QFrame.Shadow.Raised)
        self.frameLineVariables.setLineWidth(0)
        self.verticalLayout_8 = QVBoxLayout(self.frameLineVariables)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 3, 0, 3)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(7, -1, 3, 3)
        self.label_19 = QLabel(self.frameLineVariables)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"QLabel {\n"
"	margin-right: 3px;\n"
"}")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_19)

        self.progressBarOpenELF = QProgressBar(self.frameLineVariables)
        self.progressBarOpenELF.setObjectName(u"progressBarOpenELF")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.progressBarOpenELF.sizePolicy().hasHeightForWidth())
        self.progressBarOpenELF.setSizePolicy(sizePolicy6)
        self.progressBarOpenELF.setMinimumSize(QSize(150, 40))
        self.progressBarOpenELF.setMaximumSize(QSize(16777215, 40))
        self.progressBarOpenELF.setStyleSheet(u"QProgressBar\n"
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
        self.progressBarOpenELF.setValue(0)
        self.progressBarOpenELF.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_14.addWidget(self.progressBarOpenELF)

        self.pushButtonOpenELF = QPushButton(self.frameLineVariables)
        self.pushButtonOpenELF.setObjectName(u"pushButtonOpenELF")
        sizePolicy1.setHeightForWidth(self.pushButtonOpenELF.sizePolicy().hasHeightForWidth())
        self.pushButtonOpenELF.setSizePolicy(sizePolicy1)
        self.pushButtonOpenELF.setMinimumSize(QSize(0, 40))
        self.pushButtonOpenELF.setMaximumSize(QSize(16777215, 40))
        self.pushButtonOpenELF.setStyleSheet(u"QPushButton {\n"
"	background-color: #6272a4;	\n"
"	border-radius: 5px;\n"
"    color: #f8f8f2;\n"
"	padding-left: 6px;\n"
"	padding-right: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7284b9;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #566490;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #aaaaaa;\n"
"}")
        self.pushButtonOpenELF.setText(u"(None)")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/icon_folder.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonOpenELF.setIcon(icon2)
        self.pushButtonOpenELF.setIconSize(QSize(25, 25))

        self.horizontalLayout_14.addWidget(self.pushButtonOpenELF)

        self.pushButtonUpdateELF = QPushButton(self.frameLineVariables)
        self.pushButtonUpdateELF.setObjectName(u"pushButtonUpdateELF")
        self.pushButtonUpdateELF.setMinimumSize(QSize(0, 0))
        self.pushButtonUpdateELF.setMaximumSize(QSize(16777215, 40))
        self.pushButtonUpdateELF.setStyleSheet(u"QPushButton {\n"
"	background-color: #6272a4;	\n"
"	border-radius: 5px;\n"
"    color: #f8f8f2;\n"
"	padding-left: 6px;\n"
"	padding-right: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7284b9;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #566490;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #aaaaaa;\n"
"}")

        self.horizontalLayout_14.addWidget(self.pushButtonUpdateELF)


        self.verticalLayout_8.addLayout(self.horizontalLayout_14)

        self.line = QFrame(self.frameLineVariables)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(7, 1, 3, 3)
        self.label_6 = QLabel(self.frameLineVariables)
        self.label_6.setObjectName(u"label_6")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy7)
        self.label_6.setMinimumSize(QSize(0, 40))
        self.label_6.setMaximumSize(QSize(16777215, 40))
        self.label_6.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.label_6)

        self.labelTriggerName = QLabel(self.frameLineVariables)
        self.labelTriggerName.setObjectName(u"labelTriggerName")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.labelTriggerName.sizePolicy().hasHeightForWidth())
        self.labelTriggerName.setSizePolicy(sizePolicy8)
        self.labelTriggerName.setMinimumSize(QSize(0, 40))
        self.labelTriggerName.setMaximumSize(QSize(16777215, 40))
        self.labelTriggerName.setWordWrap(True)

        self.horizontalLayout_10.addWidget(self.labelTriggerName)

        self.pushButtonRemoveTrigger = QPushButton(self.frameLineVariables)
        self.pushButtonRemoveTrigger.setObjectName(u"pushButtonRemoveTrigger")
        self.pushButtonRemoveTrigger.setMinimumSize(QSize(0, 0))
        self.pushButtonRemoveTrigger.setMaximumSize(QSize(16777215, 40))
        self.pushButtonRemoveTrigger.setStyleSheet(u"QPushButton {\n"
"	background-color: #6272a4;	\n"
"	border-radius: 5px;\n"
"    color: #f8f8f2;\n"
"	padding-left: 6px;\n"
"	padding-right: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7284b9;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #566490;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #aaaaaa;\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButtonRemoveTrigger)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.lineEditSearchVariable = QLineEdit(self.frameLineVariables)
        self.lineEditSearchVariable.setObjectName(u"lineEditSearchVariable")
        sizePolicy8.setHeightForWidth(self.lineEditSearchVariable.sizePolicy().hasHeightForWidth())
        self.lineEditSearchVariable.setSizePolicy(sizePolicy8)
        self.lineEditSearchVariable.setMinimumSize(QSize(0, 23))
        self.lineEditSearchVariable.setMaximumSize(QSize(16777215, 23))
        self.lineEditSearchVariable.setStyleSheet(u"QLineEdit {\n"
"    color: #babbbd;\n"
"	background-color: white;\n"
"	/*border-bottom: 1px solid #6272a4;*/\n"
"	border-top: 1px solid #6272a4;\n"
"	padding-top: 3px;\n"
"	padding-bottom: -2px;\n"
"	padding-left: 4px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    color: black;\n"
"}")

        self.verticalLayout_8.addWidget(self.lineEditSearchVariable)

        self.tableWidgetVariables = QTableWidget(self.frameLineVariables)
        if (self.tableWidgetVariables.columnCount() < 3):
            self.tableWidgetVariables.setColumnCount(3)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidgetVariables.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidgetVariables.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidgetVariables.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        self.tableWidgetVariables.setObjectName(u"tableWidgetVariables")
        sizePolicy.setHeightForWidth(self.tableWidgetVariables.sizePolicy().hasHeightForWidth())
        self.tableWidgetVariables.setSizePolicy(sizePolicy)
        self.tableWidgetVariables.setMinimumSize(QSize(0, 0))
        self.tableWidgetVariables.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tableWidgetVariables.setStyleSheet(u"QTableWidget {\n"
"	font-family: Droid Sans Mono;\n"
"	background-color: white;\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"	border: none;\n"
"	padding-top: 3px;\n"
"	gridline-color: #D6CFC7; \n"
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
"	padding-top: 2px;\n"
"	padding-bottom: 3px;\n"
"	height: 20px;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"	/*border-bottom: 1px dashed #6272a4;*/\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"	color: #212121;\n"
"	background:#adc9ff;\n"
"}")
        self.tableWidgetVariables.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidgetVariables.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.EditKeyPressed)
        self.tableWidgetVariables.setProperty(u"showDropIndicator", False)
        self.tableWidgetVariables.setDragDropOverwriteMode(False)
        self.tableWidgetVariables.setAlternatingRowColors(False)
        self.tableWidgetVariables.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidgetVariables.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidgetVariables.setShowGrid(True)
        self.tableWidgetVariables.horizontalHeader().setHighlightSections(False)
        self.tableWidgetVariables.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetVariables.verticalHeader().setVisible(False)
        self.tableWidgetVariables.verticalHeader().setMinimumSectionSize(25)
        self.tableWidgetVariables.verticalHeader().setDefaultSectionSize(26)
        self.tableWidgetVariables.verticalHeader().setHighlightSections(False)

        self.verticalLayout_8.addWidget(self.tableWidgetVariables)


        self.verticalLayout_3.addWidget(self.frameLineVariables)


        self.gridLayout_21.addLayout(self.verticalLayout_3, 0, 1, 15, 1)

        self.frameLineUpdate = QFrame(self.scrollAreaWidgetContents)
        self.frameLineUpdate.setObjectName(u"frameLineUpdate")
        sizePolicy3.setHeightForWidth(self.frameLineUpdate.sizePolicy().hasHeightForWidth())
        self.frameLineUpdate.setSizePolicy(sizePolicy3)
        self.frameLineUpdate.setMinimumSize(QSize(520, 0))
        self.frameLineUpdate.setStyleSheet(u"#frameLineUpdate {\n"
"	background: white;\n"
"	border: 0px solid #6272a4;\n"
"	border-radius: 7px;\n"
"}")
        self.frameLineUpdate.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLineUpdate.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_23 = QGridLayout(self.frameLineUpdate)
        self.gridLayout_23.setSpacing(3)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 3, 0, 3)
        self.widgetLayoutUpdate = QWidget(self.frameLineUpdate)
        self.widgetLayoutUpdate.setObjectName(u"widgetLayoutUpdate")
        self.horizontalLayout_5 = QHBoxLayout(self.widgetLayoutUpdate)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 0, 3, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelCurrentVersionText = QLabel(self.widgetLayoutUpdate)
        self.labelCurrentVersionText.setObjectName(u"labelCurrentVersionText")
        sizePolicy2.setHeightForWidth(self.labelCurrentVersionText.sizePolicy().hasHeightForWidth())
        self.labelCurrentVersionText.setSizePolicy(sizePolicy2)
        self.labelCurrentVersionText.setMinimumSize(QSize(0, 19))
        self.labelCurrentVersionText.setMaximumSize(QSize(16777215, 19))
        self.labelCurrentVersionText.setStyleSheet(u"QLabel {\n"
"	color: black;\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"	color: #7d7d7d;\n"
"}")
        self.labelCurrentVersionText.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.labelCurrentVersionText)

        self.labelCurrentVersion = QLabel(self.widgetLayoutUpdate)
        self.labelCurrentVersion.setObjectName(u"labelCurrentVersion")
        sizePolicy8.setHeightForWidth(self.labelCurrentVersion.sizePolicy().hasHeightForWidth())
        self.labelCurrentVersion.setSizePolicy(sizePolicy8)
        self.labelCurrentVersion.setMinimumSize(QSize(0, 19))
        self.labelCurrentVersion.setMaximumSize(QSize(16777215, 19))
        self.labelCurrentVersion.setStyleSheet(u"QLabel {\n"
"	color: black;\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"	color: #7d7d7d;\n"
"}")
        self.labelCurrentVersion.setText(u" -")

        self.horizontalLayout_2.addWidget(self.labelCurrentVersion)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labelAvailableVersionText = QLabel(self.widgetLayoutUpdate)
        self.labelAvailableVersionText.setObjectName(u"labelAvailableVersionText")
        sizePolicy2.setHeightForWidth(self.labelAvailableVersionText.sizePolicy().hasHeightForWidth())
        self.labelAvailableVersionText.setSizePolicy(sizePolicy2)
        self.labelAvailableVersionText.setMinimumSize(QSize(0, 19))
        self.labelAvailableVersionText.setMaximumSize(QSize(16777215, 19))
        self.labelAvailableVersionText.setStyleSheet(u"QLabel {\n"
"	color: black;\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"	color: #7d7d7d;\n"
"}")
        self.labelAvailableVersionText.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.labelAvailableVersionText)

        self.labelAvailableVersion = QLabel(self.widgetLayoutUpdate)
        self.labelAvailableVersion.setObjectName(u"labelAvailableVersion")
        sizePolicy8.setHeightForWidth(self.labelAvailableVersion.sizePolicy().hasHeightForWidth())
        self.labelAvailableVersion.setSizePolicy(sizePolicy8)
        self.labelAvailableVersion.setMinimumSize(QSize(0, 19))
        self.labelAvailableVersion.setMaximumSize(QSize(16777215, 19))
        self.labelAvailableVersion.setStyleSheet(u"QLabel {\n"
"	color: black;\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"	color: #7d7d7d;\n"
"}")
        self.labelAvailableVersion.setText(u" -")

        self.horizontalLayout_4.addWidget(self.labelAvailableVersion)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_27)

        self.pushButtonCheckUpdates = QPushButton(self.widgetLayoutUpdate)
        self.pushButtonCheckUpdates.setObjectName(u"pushButtonCheckUpdates")
        self.pushButtonCheckUpdates.setMinimumSize(QSize(0, 40))
        self.pushButtonCheckUpdates.setMaximumSize(QSize(16777215, 40))
        self.pushButtonCheckUpdates.setStyleSheet(u"QPushButton {\n"
"	background-color: #6272a4;	\n"
"	border-radius: 5px;\n"
"    color: #f8f8f2;\n"
"	padding-left: 6px;\n"
"	padding-right: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7284b9;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #566490;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #aaaaaa;\n"
"}")

        self.horizontalLayout_5.addWidget(self.pushButtonCheckUpdates)

        self.pushButtonDownload = QPushButton(self.widgetLayoutUpdate)
        self.pushButtonDownload.setObjectName(u"pushButtonDownload")
        self.pushButtonDownload.setEnabled(True)
        self.pushButtonDownload.setMinimumSize(QSize(0, 40))
        self.pushButtonDownload.setMaximumSize(QSize(16777215, 40))
        self.pushButtonDownload.setStyleSheet(u"QPushButton {\n"
"	background-color: #6272a4;	\n"
"	border-radius: 5px;\n"
"    color: #f8f8f2;\n"
"	padding-left: 6px;\n"
"	padding-right: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7284b9;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #566490;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #aaaaaa;\n"
"}")

        self.horizontalLayout_5.addWidget(self.pushButtonDownload)


        self.gridLayout_23.addWidget(self.widgetLayoutUpdate, 0, 0, 1, 1)


        self.gridLayout_21.addWidget(self.frameLineUpdate, 11, 0, 1, 1)

        self.frameLineFRA = QFrame(self.scrollAreaWidgetContents)
        self.frameLineFRA.setObjectName(u"frameLineFRA")
        sizePolicy3.setHeightForWidth(self.frameLineFRA.sizePolicy().hasHeightForWidth())
        self.frameLineFRA.setSizePolicy(sizePolicy3)
        self.frameLineFRA.setMinimumSize(QSize(520, 0))
        self.frameLineFRA.setStyleSheet(u"#frameLineFRA {\n"
"	background: white;\n"
"	border: 0px solid #6272a4;\n"
"	border-radius: 7px;\n"
"}")
        self.frameLineFRA.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLineFRA.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_20 = QGridLayout(self.frameLineFRA)
        self.gridLayout_20.setSpacing(3)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 3, 0, 3)
        self.widgetLayoutFRAConfig = QWidget(self.frameLineFRA)
        self.widgetLayoutFRAConfig.setObjectName(u"widgetLayoutFRAConfig")
        self.horizontalLayoutFRAConfig = QHBoxLayout(self.widgetLayoutFRAConfig)
        self.horizontalLayoutFRAConfig.setSpacing(3)
        self.horizontalLayoutFRAConfig.setObjectName(u"horizontalLayoutFRAConfig")
        self.horizontalLayoutFRAConfig.setContentsMargins(10, 0, 3, 0)
        self.labelFRAConfig = QLabel(self.widgetLayoutFRAConfig)
        self.labelFRAConfig.setObjectName(u"labelFRAConfig")
        self.labelFRAConfig.setEnabled(True)
        self.labelFRAConfig.setMinimumSize(QSize(250, 0))
        self.labelFRAConfig.setStyleSheet(u"QLabel {\n"
"	color: black;\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"	color: #7d7d7d;\n"
"}")
        self.labelFRAConfig.setWordWrap(True)

        self.horizontalLayoutFRAConfig.addWidget(self.labelFRAConfig)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutFRAConfig.addItem(self.horizontalSpacer_29)

        self.pushButtonConfigureFRA = QPushButton(self.widgetLayoutFRAConfig)
        self.pushButtonConfigureFRA.setObjectName(u"pushButtonConfigureFRA")
        self.pushButtonConfigureFRA.setMinimumSize(QSize(0, 40))
        self.pushButtonConfigureFRA.setMaximumSize(QSize(16777215, 40))
        self.pushButtonConfigureFRA.setStyleSheet(u"QPushButton {\n"
"	background-color: #6272a4;	\n"
"	border-radius: 5px;\n"
"    color: #f8f8f2;\n"
"	padding-left: 6px;\n"
"	padding-right: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7284b9;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #566490;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #aaaaaa;\n"
"}")
        self.pushButtonConfigureFRA.setIconSize(QSize(30, 30))

        self.horizontalLayoutFRAConfig.addWidget(self.pushButtonConfigureFRA)


        self.gridLayout_20.addWidget(self.widgetLayoutFRAConfig, 0, 0, 1, 1)


        self.gridLayout_21.addWidget(self.frameLineFRA, 9, 0, 1, 1)

        self.frameLineRTM = QFrame(self.scrollAreaWidgetContents)
        self.frameLineRTM.setObjectName(u"frameLineRTM")
        self.frameLineRTM.setMinimumSize(QSize(520, 0))
        self.frameLineRTM.setMaximumSize(QSize(520, 16777215))
        self.frameLineRTM.setStyleSheet(u"#frameLineRTM {\n"
"	background: white;\n"
"	border: 0px solid #6272a4;\n"
"	border-radius: 7px;\n"
"}")
        self.frameLineRTM.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLineRTM.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_26 = QGridLayout(self.frameLineRTM)
        self.gridLayout_26.setSpacing(3)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 3, 0, 3)
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setSpacing(3)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(10, -1, 3, -1)
        self.label_25 = QLabel(self.frameLineRTM)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"QLabel {\n"
"	color: black;\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"	color: #7d7d7d;\n"
"}")

        self.horizontalLayout_28.addWidget(self.label_25)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_9)

        self.spinBoxDumpSize = QSpinBox(self.frameLineRTM)
        self.spinBoxDumpSize.setObjectName(u"spinBoxDumpSize")
        self.spinBoxDumpSize.setMinimumSize(QSize(220, 30))
        self.spinBoxDumpSize.setMaximumSize(QSize(220, 30))
        self.spinBoxDumpSize.setStyleSheet(u"QSpinBox {\n"
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
        self.spinBoxDumpSize.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinBoxDumpSize.setMaximum(1048576)
        self.spinBoxDumpSize.setSingleStep(1)

        self.horizontalLayout_28.addWidget(self.spinBoxDumpSize)


        self.gridLayout_26.addLayout(self.horizontalLayout_28, 0, 0, 1, 1)


        self.gridLayout_21.addWidget(self.frameLineRTM, 5, 0, 1, 1)

        self.labelCom = QLabel(self.scrollAreaWidgetContents)
        self.labelCom.setObjectName(u"labelCom")
        sizePolicy2.setHeightForWidth(self.labelCom.sizePolicy().hasHeightForWidth())
        self.labelCom.setSizePolicy(sizePolicy2)
        self.labelCom.setFont(font)
        self.labelCom.setStyleSheet(u"QLabel {\n"
"	margin-top: 5px;\n"
"	margin-left: 5px;\n"
"}")

        self.gridLayout_21.addWidget(self.labelCom, 0, 0, 1, 1)

        self.frameLineTrigger = QFrame(self.scrollAreaWidgetContents)
        self.frameLineTrigger.setObjectName(u"frameLineTrigger")
        sizePolicy3.setHeightForWidth(self.frameLineTrigger.sizePolicy().hasHeightForWidth())
        self.frameLineTrigger.setSizePolicy(sizePolicy3)
        self.frameLineTrigger.setMinimumSize(QSize(520, 0))
        self.frameLineTrigger.setMaximumSize(QSize(520, 16777215))
        self.frameLineTrigger.setStyleSheet(u"#frameLineTrigger {\n"
"	background: white;\n"
"	border: 0px solid #6272a4;\n"
"	border-radius: 7px;\n"
"}")
        self.frameLineTrigger.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLineTrigger.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_15 = QGridLayout(self.frameLineTrigger)
        self.gridLayout_15.setSpacing(3)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 3, 0, 3)
        self.line_5 = QFrame(self.frameLineTrigger)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setEnabled(True)
        self.line_5.setMinimumSize(QSize(0, 2))
        self.line_5.setMaximumSize(QSize(16777215, 2))
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_5.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout_15.addWidget(self.line_5, 3, 0, 1, 1)

        self.widgetLayoutEdgeType = QWidget(self.frameLineTrigger)
        self.widgetLayoutEdgeType.setObjectName(u"widgetLayoutEdgeType")
        self.horizontalLayoutEdgeType = QHBoxLayout(self.widgetLayoutEdgeType)
        self.horizontalLayoutEdgeType.setSpacing(3)
        self.horizontalLayoutEdgeType.setObjectName(u"horizontalLayoutEdgeType")
        self.horizontalLayoutEdgeType.setContentsMargins(10, 0, 3, 0)
        self.labelEdgeType = QLabel(self.widgetLayoutEdgeType)
        self.labelEdgeType.setObjectName(u"labelEdgeType")
        self.labelEdgeType.setMinimumSize(QSize(250, 0))
        self.labelEdgeType.setStyleSheet(u"QLabel {\n"
"	color: black;\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"	color: #7d7d7d;\n"
"}")
        self.labelEdgeType.setWordWrap(True)

        self.horizontalLayoutEdgeType.addWidget(self.labelEdgeType)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutEdgeType.addItem(self.horizontalSpacer_17)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButtonLeadEdge = QPushButton(self.widgetLayoutEdgeType)
        self.pushButtonLeadEdge.setObjectName(u"pushButtonLeadEdge")
        self.pushButtonLeadEdge.setEnabled(True)
        self.pushButtonLeadEdge.setMinimumSize(QSize(40, 40))
        self.pushButtonLeadEdge.setMaximumSize(QSize(40, 40))
        self.pushButtonLeadEdge.setStyleSheet(u"QPushButton {\n"
"	background-color: #6272a4;	\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"	border-right: 1px solid #7284b9;\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7284b9;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: #566490;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #aaaaaa;\n"
"	color: #7d7d7d;\n"
"	border-right: 1px solid #7d7d7d;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/icon_leading_edge.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonLeadEdge.setIcon(icon3)
        self.pushButtonLeadEdge.setIconSize(QSize(30, 30))
        self.pushButtonLeadEdge.setCheckable(True)
        self.pushButtonLeadEdge.setChecked(True)

        self.horizontalLayout_3.addWidget(self.pushButtonLeadEdge)

        self.pushButtonTrailEdge = QPushButton(self.widgetLayoutEdgeType)
        self.pushButtonTrailEdge.setObjectName(u"pushButtonTrailEdge")
        self.pushButtonTrailEdge.setEnabled(True)
        self.pushButtonTrailEdge.setMinimumSize(QSize(40, 40))
        self.pushButtonTrailEdge.setMaximumSize(QSize(40, 40))
        self.pushButtonTrailEdge.setStyleSheet(u"QPushButton {\n"
"	background-color: #6272a4;	\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border-right: 1px solid #7284b9;\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7284b9;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: #566490;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #aaaaaa;\n"
"	color: #7d7d7d;border-right: 1px solid #7d7d7d;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/icon_trailing_edge.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonTrailEdge.setIcon(icon4)
        self.pushButtonTrailEdge.setIconSize(QSize(30, 30))
        self.pushButtonTrailEdge.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.pushButtonTrailEdge)

        self.pushButtonAlterEdge = QPushButton(self.widgetLayoutEdgeType)
        self.pushButtonAlterEdge.setObjectName(u"pushButtonAlterEdge")
        self.pushButtonAlterEdge.setEnabled(True)
        self.pushButtonAlterEdge.setMinimumSize(QSize(40, 40))
        self.pushButtonAlterEdge.setMaximumSize(QSize(40, 40))
        self.pushButtonAlterEdge.setStyleSheet(u"QPushButton {\n"
"	background-color: #6272a4;	\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7284b9;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: #566490;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #aaaaaa;\n"
"	color: #7d7d7d;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/icon_alter_edge.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonAlterEdge.setIcon(icon5)
        self.pushButtonAlterEdge.setIconSize(QSize(30, 30))
        self.pushButtonAlterEdge.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.pushButtonAlterEdge)


        self.horizontalLayoutEdgeType.addLayout(self.horizontalLayout_3)


        self.gridLayout_15.addWidget(self.widgetLayoutEdgeType, 2, 0, 1, 1)

        self.line_7 = QFrame(self.frameLineTrigger)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setMinimumSize(QSize(0, 2))
        self.line_7.setMaximumSize(QSize(16777215, 2))
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_15.addWidget(self.line_7, 7, 0, 1, 1)

        self.widgetLayoutTriggerCount = QWidget(self.frameLineTrigger)
        self.widgetLayoutTriggerCount.setObjectName(u"widgetLayoutTriggerCount")
        self.horizontalLayoutTriggerCount = QHBoxLayout(self.widgetLayoutTriggerCount)
        self.horizontalLayoutTriggerCount.setSpacing(3)
        self.horizontalLayoutTriggerCount.setObjectName(u"horizontalLayoutTriggerCount")
        self.horizontalLayoutTriggerCount.setContentsMargins(10, 0, 3, 0)
        self.labelTriggerCount = QLabel(self.widgetLayoutTriggerCount)
        self.labelTriggerCount.setObjectName(u"labelTriggerCount")
        self.labelTriggerCount.setMinimumSize(QSize(250, 0))
        self.labelTriggerCount.setStyleSheet(u"QLabel {\n"
"	color: black;\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"	color: #7d7d7d;\n"
"}")
        self.labelTriggerCount.setWordWrap(True)

        self.horizontalLayoutTriggerCount.addWidget(self.labelTriggerCount)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutTriggerCount.addItem(self.horizontalSpacer_21)

        self.spinBoxTriggerCount = QSpinBox(self.widgetLayoutTriggerCount)
        self.spinBoxTriggerCount.setObjectName(u"spinBoxTriggerCount")
        self.spinBoxTriggerCount.setEnabled(True)
        self.spinBoxTriggerCount.setMinimumSize(QSize(220, 30))
        self.spinBoxTriggerCount.setMaximumSize(QSize(220, 30))
        self.spinBoxTriggerCount.setStyleSheet(u"QSpinBox {\n"
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
        self.spinBoxTriggerCount.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.spinBoxTriggerCount.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinBoxTriggerCount.setMinimum(1)
        self.spinBoxTriggerCount.setMaximum(255)

        self.horizontalLayoutTriggerCount.addWidget(self.spinBoxTriggerCount)


        self.gridLayout_15.addWidget(self.widgetLayoutTriggerCount, 14, 0, 1, 1)

        self.line_11 = QFrame(self.frameLineTrigger)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setMinimumSize(QSize(0, 2))
        self.line_11.setMaximumSize(QSize(16777215, 2))
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_15.addWidget(self.line_11, 11, 0, 1, 1)

        self.line_10 = QFrame(self.frameLineTrigger)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setMinimumSize(QSize(0, 2))
        self.line_10.setMaximumSize(QSize(16777215, 2))
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_15.addWidget(self.line_10, 15, 0, 1, 1)

        self.widgetLayoutTriggerLevel = QWidget(self.frameLineTrigger)
        self.widgetLayoutTriggerLevel.setObjectName(u"widgetLayoutTriggerLevel")
        self.horizontalLayoutTriggerLevel = QHBoxLayout(self.widgetLayoutTriggerLevel)
        self.horizontalLayoutTriggerLevel.setSpacing(3)
        self.horizontalLayoutTriggerLevel.setObjectName(u"horizontalLayoutTriggerLevel")
        self.horizontalLayoutTriggerLevel.setContentsMargins(10, 0, 3, 0)
        self.labelTriggerLevel = QLabel(self.widgetLayoutTriggerLevel)
        self.labelTriggerLevel.setObjectName(u"labelTriggerLevel")
        self.labelTriggerLevel.setMinimumSize(QSize(250, 0))
        self.labelTriggerLevel.setStyleSheet(u"QLabel {\n"
"	color: black;\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"	color: #7d7d7d;\n"
"}")
        self.labelTriggerLevel.setWordWrap(True)

        self.horizontalLayoutTriggerLevel.addWidget(self.labelTriggerLevel)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutTriggerLevel.addItem(self.horizontalSpacer_18)

        self.doubleSpinBoxTriggerLevel = QDoubleSpinBox(self.widgetLayoutTriggerLevel)
        self.doubleSpinBoxTriggerLevel.setObjectName(u"doubleSpinBoxTriggerLevel")
        self.doubleSpinBoxTriggerLevel.setEnabled(True)
        self.doubleSpinBoxTriggerLevel.setMinimumSize(QSize(220, 30))
        self.doubleSpinBoxTriggerLevel.setMaximumSize(QSize(220, 30))
        self.doubleSpinBoxTriggerLevel.setStyleSheet(u"QDoubleSpinBox {\n"
"	color: black;\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #6272a4;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QDoubleSpinBox:disabled {\n"
"	color: #7d7d7d;\n"
"	border: 1px solid #7d7d7d;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button {\n"
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
"QDoubleSpinBox::up-button:hover,\n"
"QDoubleSpinBox::down-button:hover {\n"
"	background-color: #d1eeff;\n"
" }\n"
"\n"
"QDoubleSpinBox::up-button:pressed,\n"
"QDoubleSpinBox::down-button:pressed {\n"
"	background-color: #f8f8f2;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:disabled {\n"
"	background-color: #aaaaaa;\n"
""
                        "	border-left-color: #aaaaaa;\n"
"	border-top: 1px solid #aaaaaa;\n"
" }\n"
"\n"
"QDoubleSpinBox::up-button {\n"
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
"QDoubleSpinBox::up-button:disabled {\n"
"	background-color: #aaaaaa;\n"
"	border-left-color: #aaaaaa;\n"
" }\n"
"")
        self.doubleSpinBoxTriggerLevel.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.doubleSpinBoxTriggerLevel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.doubleSpinBoxTriggerLevel.setDecimals(6)
        self.doubleSpinBoxTriggerLevel.setMinimum(-100000000000000000000.000000000000000)
        self.doubleSpinBoxTriggerLevel.setMaximum(100000000000000000000.000000000000000)
        self.doubleSpinBoxTriggerLevel.setSingleStep(0.100000000000000)
        self.doubleSpinBoxTriggerLevel.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.horizontalLayoutTriggerLevel.addWidget(self.doubleSpinBoxTriggerLevel)


        self.gridLayout_15.addWidget(self.widgetLayoutTriggerLevel, 6, 0, 1, 1)

        self.widgetLayoutSettlingTime = QWidget(self.frameLineTrigger)
        self.widgetLayoutSettlingTime.setObjectName(u"widgetLayoutSettlingTime")
        self.horizontalLayoutSettlingTime = QHBoxLayout(self.widgetLayoutSettlingTime)
        self.horizontalLayoutSettlingTime.setSpacing(3)
        self.horizontalLayoutSettlingTime.setObjectName(u"horizontalLayoutSettlingTime")
        self.horizontalLayoutSettlingTime.setContentsMargins(10, 0, 3, 0)
        self.labelSettlingTime = QLabel(self.widgetLayoutSettlingTime)
        self.labelSettlingTime.setObjectName(u"labelSettlingTime")
        self.labelSettlingTime.setEnabled(True)
        self.labelSettlingTime.setMinimumSize(QSize(250, 0))
        self.labelSettlingTime.setStyleSheet(u"QLabel {\n"
"	color: black;\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"	color: #7d7d7d;\n"
"}")
        self.labelSettlingTime.setWordWrap(True)

        self.horizontalLayoutSettlingTime.addWidget(self.labelSettlingTime)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutSettlingTime.addItem(self.horizontalSpacer_22)

        self.doubleSpinBoxSettlingTime = QDoubleSpinBox(self.widgetLayoutSettlingTime)
        self.doubleSpinBoxSettlingTime.setObjectName(u"doubleSpinBoxSettlingTime")
        self.doubleSpinBoxSettlingTime.setEnabled(True)
        self.doubleSpinBoxSettlingTime.setMinimumSize(QSize(220, 30))
        self.doubleSpinBoxSettlingTime.setMaximumSize(QSize(220, 30))
        self.doubleSpinBoxSettlingTime.setStyleSheet(u"QDoubleSpinBox {\n"
"	color: black;\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #6272a4;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"QDoubleSpinBox:disabled {\n"
"	color: #7d7d7d;\n"
"	border: 1px solid #7d7d7d;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button {\n"
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
"QDoubleSpinBox::up-button:hover,\n"
"QDoubleSpinBox::down-button:hover {\n"
"	background-color: #d1eeff;\n"
" }\n"
"\n"
"QDoubleSpinBox::up-button:pressed,\n"
"QDoubleSpinBox::down-button:pressed {\n"
"	background-color: #f8f8f2;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:disabled {\n"
"	background-color: #aaaaaa;\n"
""
                        "	border-left-color: #aaaaaa;\n"
"	border-top: 1px solid #aaaaaa;\n"
" }\n"
"\n"
"QDoubleSpinBox::up-button {\n"
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
"QDoubleSpinBox::up-button:disabled {\n"
"	background-color: #aaaaaa;\n"
"	border-left-color: #aaaaaa;\n"
" }\n"
"")
        self.doubleSpinBoxSettlingTime.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.doubleSpinBoxSettlingTime.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.doubleSpinBoxSettlingTime.setDecimals(6)
        self.doubleSpinBoxSettlingTime.setMaximum(1000000000000000013287555072.000000000000000)
        self.doubleSpinBoxSettlingTime.setSingleStep(0.010000000000000)
        self.doubleSpinBoxSettlingTime.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.horizontalLayoutSettlingTime.addWidget(self.doubleSpinBoxSettlingTime)


        self.gridLayout_15.addWidget(self.widgetLayoutSettlingTime, 16, 0, 1, 1)

        self.widgetLayoutOneShotMode = QWidget(self.frameLineTrigger)
        self.widgetLayoutOneShotMode.setObjectName(u"widgetLayoutOneShotMode")
        self.horizontalLayoutOneShotMode = QHBoxLayout(self.widgetLayoutOneShotMode)
        self.horizontalLayoutOneShotMode.setSpacing(3)
        self.horizontalLayoutOneShotMode.setObjectName(u"horizontalLayoutOneShotMode")
        self.horizontalLayoutOneShotMode.setContentsMargins(10, 0, 3, 0)
        self.labelOneShotMode = QLabel(self.widgetLayoutOneShotMode)
        self.labelOneShotMode.setObjectName(u"labelOneShotMode")
        self.labelOneShotMode.setMinimumSize(QSize(250, 0))
        self.labelOneShotMode.setStyleSheet(u"QLabel {\n"
"	color: black;\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"	color: #7d7d7d;\n"
"}")
        self.labelOneShotMode.setWordWrap(True)

        self.horizontalLayoutOneShotMode.addWidget(self.labelOneShotMode)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutOneShotMode.addItem(self.horizontalSpacer_26)

        self.checkBoxOneShotMode = QCheckBox(self.widgetLayoutOneShotMode)
        self.checkBoxOneShotMode.setObjectName(u"checkBoxOneShotMode")
        self.checkBoxOneShotMode.setMinimumSize(QSize(0, 25))
        self.checkBoxOneShotMode.setMaximumSize(QSize(16777215, 30))
        self.checkBoxOneShotMode.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.checkBoxOneShotMode.setStyleSheet(u"QCheckBox::indicator {\n"
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

        self.horizontalLayoutOneShotMode.addWidget(self.checkBoxOneShotMode)


        self.gridLayout_15.addWidget(self.widgetLayoutOneShotMode, 4, 0, 1, 1)

        self.line_4 = QFrame(self.frameLineTrigger)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMinimumSize(QSize(0, 2))
        self.line_4.setMaximumSize(QSize(16777215, 2))
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_15.addWidget(self.line_4, 1, 0, 1, 1)

        self.widgetLayoutPreTrigger = QWidget(self.frameLineTrigger)
        self.widgetLayoutPreTrigger.setObjectName(u"widgetLayoutPreTrigger")
        self.horizontalLayout_6 = QHBoxLayout(self.widgetLayoutPreTrigger)
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 0, 3, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.labelPreTrigger = QLabel(self.widgetLayoutPreTrigger)
        self.labelPreTrigger.setObjectName(u"labelPreTrigger")
        self.labelPreTrigger.setMinimumSize(QSize(250, 20))
        self.labelPreTrigger.setMaximumSize(QSize(16777215, 20))
        self.labelPreTrigger.setStyleSheet(u"QLabel {\n"
"	color: black;\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"	color: #7d7d7d;\n"
"}")
        self.labelPreTrigger.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.labelPreTrigger)

        self.labelPreTriggerTime = QLabel(self.widgetLayoutPreTrigger)
        self.labelPreTriggerTime.setObjectName(u"labelPreTriggerTime")
        self.labelPreTriggerTime.setMinimumSize(QSize(250, 20))
        self.labelPreTriggerTime.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.labelPreTriggerTime)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_19)

        self.spinBoxPreTrigger = QSpinBox(self.widgetLayoutPreTrigger)
        self.spinBoxPreTrigger.setObjectName(u"spinBoxPreTrigger")
        self.spinBoxPreTrigger.setMinimumSize(QSize(220, 30))
        self.spinBoxPreTrigger.setMaximumSize(QSize(220, 30))
        self.spinBoxPreTrigger.setStyleSheet(u"QSpinBox {\n"
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
        self.spinBoxPreTrigger.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.spinBoxPreTrigger.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinBoxPreTrigger.setMaximum(999999999)

        self.horizontalLayout_6.addWidget(self.spinBoxPreTrigger)


        self.gridLayout_15.addWidget(self.widgetLayoutPreTrigger, 8, 0, 1, 1)

        self.widgetLayoutSampleCount = QWidget(self.frameLineTrigger)
        self.widgetLayoutSampleCount.setObjectName(u"widgetLayoutSampleCount")
        self.horizontalLayoutSampleCount = QHBoxLayout(self.widgetLayoutSampleCount)
        self.horizontalLayoutSampleCount.setSpacing(3)
        self.horizontalLayoutSampleCount.setObjectName(u"horizontalLayoutSampleCount")
        self.horizontalLayoutSampleCount.setContentsMargins(10, 0, 3, 0)
        self.labelSampleCount = QLabel(self.widgetLayoutSampleCount)
        self.labelSampleCount.setObjectName(u"labelSampleCount")
        self.labelSampleCount.setMinimumSize(QSize(250, 0))
        self.labelSampleCount.setStyleSheet(u"QLabel {\n"
"	color: black;\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"	color: #7d7d7d;\n"
"}")
        self.labelSampleCount.setWordWrap(True)

        self.horizontalLayoutSampleCount.addWidget(self.labelSampleCount)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutSampleCount.addItem(self.horizontalSpacer_28)

        self.spinBoxSampleCount = QSpinBox(self.widgetLayoutSampleCount)
        self.spinBoxSampleCount.setObjectName(u"spinBoxSampleCount")
        self.spinBoxSampleCount.setMinimumSize(QSize(220, 30))
        self.spinBoxSampleCount.setMaximumSize(QSize(220, 30))
        self.spinBoxSampleCount.setStyleSheet(u"QSpinBox {\n"
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
        self.spinBoxSampleCount.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.spinBoxSampleCount.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinBoxSampleCount.setMinimum(1)
        self.spinBoxSampleCount.setMaximum(255)

        self.horizontalLayoutSampleCount.addWidget(self.spinBoxSampleCount)


        self.gridLayout_15.addWidget(self.widgetLayoutSampleCount, 0, 0, 1, 1)

        self.widgetLayoutPostTrigger = QWidget(self.frameLineTrigger)
        self.widgetLayoutPostTrigger.setObjectName(u"widgetLayoutPostTrigger")
        self.widgetLayoutPostTrigger.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_7 = QHBoxLayout(self.widgetLayoutPostTrigger)
        self.horizontalLayout_7.setSpacing(3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 3, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.labelPostTrigger = QLabel(self.widgetLayoutPostTrigger)
        self.labelPostTrigger.setObjectName(u"labelPostTrigger")
        sizePolicy7.setHeightForWidth(self.labelPostTrigger.sizePolicy().hasHeightForWidth())
        self.labelPostTrigger.setSizePolicy(sizePolicy7)
        self.labelPostTrigger.setMinimumSize(QSize(250, 20))
        self.labelPostTrigger.setMaximumSize(QSize(16777215, 20))
        self.labelPostTrigger.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.labelPostTrigger)

        self.labelPostTriggerTime = QLabel(self.widgetLayoutPostTrigger)
        self.labelPostTriggerTime.setObjectName(u"labelPostTriggerTime")
        self.labelPostTriggerTime.setMinimumSize(QSize(250, 20))
        self.labelPostTriggerTime.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_5.addWidget(self.labelPostTriggerTime)


        self.horizontalLayout_7.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_2 = QSpacerItem(136, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.spinBoxPostTrigger = QSpinBox(self.widgetLayoutPostTrigger)
        self.spinBoxPostTrigger.setObjectName(u"spinBoxPostTrigger")
        self.spinBoxPostTrigger.setMinimumSize(QSize(220, 30))
        self.spinBoxPostTrigger.setMaximumSize(QSize(220, 30))
        self.spinBoxPostTrigger.setStyleSheet(u"QSpinBox {\n"
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
        self.spinBoxPostTrigger.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.spinBoxPostTrigger.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinBoxPostTrigger.setMinimum(1)
        self.spinBoxPostTrigger.setMaximum(99999999)

        self.horizontalLayout_7.addWidget(self.spinBoxPostTrigger)


        self.gridLayout_15.addWidget(self.widgetLayoutPostTrigger, 10, 0, 1, 1)

        self.line_6 = QFrame(self.frameLineTrigger)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setMinimumSize(QSize(0, 2))
        self.line_6.setMaximumSize(QSize(16777215, 2))
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_15.addWidget(self.line_6, 5, 0, 1, 1)

        self.line_8 = QFrame(self.frameLineTrigger)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setMinimumSize(QSize(0, 2))
        self.line_8.setMaximumSize(QSize(16777215, 2))
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_15.addWidget(self.line_8, 9, 0, 1, 1)


        self.gridLayout_21.addWidget(self.frameLineTrigger, 7, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_21.addItem(self.verticalSpacer_2, 14, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_12.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frameSettings, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.pageSettings)
        self.pageFRA = QWidget()
        self.pageFRA.setObjectName(u"pageFRA")
        self.pageFRA.setStyleSheet(u"#pageFRA {\n"
"	background-color: #f8f8f2;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.pageFRA)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.pageFRA)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_10 = QGridLayout(self.frame)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.graphFRA = GraphicsLayoutWidget(self.frame)
        self.graphFRA.setObjectName(u"graphFRA")
        sizePolicy.setHeightForWidth(self.graphFRA.sizePolicy().hasHeightForWidth())
        self.graphFRA.setSizePolicy(sizePolicy)
        self.graphFRA.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout_10.addWidget(self.graphFRA, 0, 0, 1, 1)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, -1, 3, -1)
        self.horizontalSpacer_4 = QSpacerItem(859, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_4)

        self.pushButtonEnableFRACursors = QPushButton(self.frame)
        self.pushButtonEnableFRACursors.setObjectName(u"pushButtonEnableFRACursors")
        self.pushButtonEnableFRACursors.setMinimumSize(QSize(0, 25))
        self.pushButtonEnableFRACursors.setMaximumSize(QSize(16777215, 25))
        self.pushButtonEnableFRACursors.setStyleSheet(u"QPushButton {\n"
"	background-color: #6272a4;	\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"    color: #f8f8f2;\n"
"	padding-left: 8px;\n"
"	padding-right: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7284b9;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #566490;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #aaaaaa;\n"
"}")
        self.pushButtonEnableFRACursors.setCheckable(True)

        self.horizontalLayout_20.addWidget(self.pushButtonEnableFRACursors)


        self.gridLayout_10.addLayout(self.horizontalLayout_20, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.pageFRA)
        self.pageLog = QWidget()
        self.pageLog.setObjectName(u"pageLog")
        self.pageLog.setStyleSheet(u"#pageLog {\n"
"	background-color: #f8f8f2;\n"
"}")
        self.gridLayout_14 = QGridLayout(self.pageLog)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.pageLog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_2)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(9, 9, 9, 9)
        self.tableWidgetLog = QTableWidget(self.frame_2)
        if (self.tableWidgetLog.columnCount() < 3):
            self.tableWidgetLog.setColumnCount(3)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidgetLog.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidgetLog.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
        self.tableWidgetLog.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        self.tableWidgetLog.setObjectName(u"tableWidgetLog")
        self.tableWidgetLog.setStyleSheet(u"QTableWidget {\n"
"	background-color: white;\n"
"	border-radius: 7px;\n"
"	border: 0px solid #6272a4;\n"
"	padding-top: 3px;\n"
"	gridline-color: #D6CFC7; \n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"	background-color: white;\n"
"	color: #212121;\n"
"	border-style: none;\n"
"	border-bottom: 1px solid #6272a4;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	padding-top: 0px;\n"
"	padding-bottom: 3px;\n"
"	height: 20px;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"	/*border-bottom: 1px dashed #6272a4;*/\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"	color: #212121;\n"
"	background:#adc9ff;\n"
"}")
        self.tableWidgetLog.setFrameShape(QFrame.Shape.StyledPanel)
        self.tableWidgetLog.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidgetLog.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidgetLog.setProperty(u"showDropIndicator", False)
        self.tableWidgetLog.setDragDropOverwriteMode(False)
        self.tableWidgetLog.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tableWidgetLog.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidgetLog.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.tableWidgetLog.setShowGrid(True)
        self.tableWidgetLog.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetLog.verticalHeader().setVisible(False)
        self.tableWidgetLog.verticalHeader().setMinimumSectionSize(25)
        self.tableWidgetLog.verticalHeader().setDefaultSectionSize(26)

        self.gridLayout_13.addWidget(self.tableWidgetLog, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.frame_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.pageLog)
        self.pageMath = QWidget()
        self.pageMath.setObjectName(u"pageMath")
        self.pageMath.setStyleSheet(u"#pageMath {\n"
"	background-color: #f8f8f2;\n"
"}")
        self.gridLayout_25 = QGridLayout(self.pageMath)
        self.gridLayout_25.setSpacing(9)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(-1, -1, 0, 0)
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.frameControlParameters = QFrame(self.pageMath)
        self.frameControlParameters.setObjectName(u"frameControlParameters")
        self.frameControlParameters.setStyleSheet(u"#frameControlParameters {\n"
"	background: white;\n"
"	border: 0px solid #6272a4;\n"
"	border-radius: 7px;\n"
"}")
        self.frameControlParameters.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameControlParameters.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_24 = QGridLayout(self.frameControlParameters)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_13 = QLabel(self.frameControlParameters)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 30))
        self.label_13.setMaximumSize(QSize(16777215, 30))
        self.label_13.setStyleSheet(u"QLabel {\n"
"	margin-right:2px;\n"
"}")

        self.horizontalLayout_8.addWidget(self.label_13)

        self.lineEditKCorrection = QLineEdit(self.frameControlParameters)
        self.lineEditKCorrection.setObjectName(u"lineEditKCorrection")
        self.lineEditKCorrection.setMinimumSize(QSize(50, 30))
        self.lineEditKCorrection.setMaximumSize(QSize(16777215, 30))
        self.lineEditKCorrection.setStyleSheet(u"QLineEdit {\n"
"	color: #212121;\n"
"	background-color: white;\n"
"	border-left: 1px solid #6272a4;\n"
"	border-top: 1px solid #6272a4;\n"
"	border-bottom: 1px solid #6272a4;\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"	padding-left: 3px;\n"
"}")

        self.horizontalLayout_8.addWidget(self.lineEditKCorrection)

        self.label_21 = QLabel(self.frameControlParameters)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"QLabel {\n"
"	color: #212121;\n"
"	background-color: white;\n"
"	border-right: 1px solid #6272a4;\n"
"	border-top: 1px solid #6272a4;\n"
"	border-bottom: 1px solid #6272a4;\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}")

        self.horizontalLayout_8.addWidget(self.label_21)


        self.gridLayout_24.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_17 = QLabel(self.frameControlParameters)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 30))
        self.label_17.setMaximumSize(QSize(16777215, 30))
        self.label_17.setStyleSheet(u"QLabel {\n"
"	margin-right:2px;\n"
"}")

        self.horizontalLayout_23.addWidget(self.label_17)

        self.lineEditPhiCorrection = QLineEdit(self.frameControlParameters)
        self.lineEditPhiCorrection.setObjectName(u"lineEditPhiCorrection")
        self.lineEditPhiCorrection.setMinimumSize(QSize(50, 30))
        self.lineEditPhiCorrection.setMaximumSize(QSize(16777215, 30))
        self.lineEditPhiCorrection.setStyleSheet(u"QLineEdit {\n"
"	color: #212121;\n"
"	background-color: white;\n"
"	border-left: 1px solid #6272a4;\n"
"	border-top: 1px solid #6272a4;\n"
"	border-bottom: 1px solid #6272a4;\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"	padding-left: 3px;\n"
"}")

        self.horizontalLayout_23.addWidget(self.lineEditPhiCorrection)

        self.label_20 = QLabel(self.frameControlParameters)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"QLabel {\n"
"	color: #212121;\n"
"	background-color: white;\n"
"	border-right: 1px solid #6272a4;\n"
"	border-top: 1px solid #6272a4;\n"
"	border-bottom: 1px solid #6272a4;\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}")

        self.horizontalLayout_23.addWidget(self.label_20)


        self.gridLayout_24.addLayout(self.horizontalLayout_23, 0, 1, 1, 1)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_3 = QLabel(self.frameControlParameters)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setMaximumSize(QSize(16777215, 30))
        self.label_3.setStyleSheet(u"QLabel {\n"
"	margin-right:2px;\n"
"}")

        self.horizontalLayout_24.addWidget(self.label_3)

        self.lineEditSamplingFrequency = QLineEdit(self.frameControlParameters)
        self.lineEditSamplingFrequency.setObjectName(u"lineEditSamplingFrequency")
        self.lineEditSamplingFrequency.setMinimumSize(QSize(50, 30))
        self.lineEditSamplingFrequency.setMaximumSize(QSize(16777215, 30))
        self.lineEditSamplingFrequency.setStyleSheet(u"QLineEdit {\n"
"	color: #212121;\n"
"	background-color: white;\n"
"	border-left: 1px solid #6272a4;\n"
"	border-top: 1px solid #6272a4;\n"
"	border-bottom: 1px solid #6272a4;\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"	padding-left: 3px;\n"
"}")

        self.horizontalLayout_24.addWidget(self.lineEditSamplingFrequency)

        self.label_8 = QLabel(self.frameControlParameters)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setMaximumSize(QSize(16777215, 30))
        self.label_8.setStyleSheet(u"QLabel {\n"
"	color: #212121;\n"
"	background-color: white;\n"
"	border-right: 1px solid #6272a4;\n"
"	border-top: 1px solid #6272a4;\n"
"	border-bottom: 1px solid #6272a4;\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}")

        self.horizontalLayout_24.addWidget(self.label_8)


        self.gridLayout_24.addLayout(self.horizontalLayout_24, 0, 2, 1, 1)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_5 = QLabel(self.frameControlParameters)
        self.label_5.setObjectName(u"label_5")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy9)
        self.label_5.setMinimumSize(QSize(0, 30))
        self.label_5.setMaximumSize(QSize(16777215, 30))
        self.label_5.setStyleSheet(u"QLabel {\n"
"	margin-right:2px;\n"
"}")

        self.horizontalLayout_25.addWidget(self.label_5)

        self.lineEditCrossFrequency = QLineEdit(self.frameControlParameters)
        self.lineEditCrossFrequency.setObjectName(u"lineEditCrossFrequency")
        self.lineEditCrossFrequency.setMinimumSize(QSize(50, 30))
        self.lineEditCrossFrequency.setMaximumSize(QSize(16777215, 30))
        self.lineEditCrossFrequency.setStyleSheet(u"QLineEdit {\n"
"	color: #212121;\n"
"	background-color: white;\n"
"	border-left: 1px solid #6272a4;\n"
"	border-top: 1px solid #6272a4;\n"
"	border-bottom: 1px solid #6272a4;\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"	padding-left: 3px;\n"
"}")

        self.horizontalLayout_25.addWidget(self.lineEditCrossFrequency)

        self.label_9 = QLabel(self.frameControlParameters)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 30))
        self.label_9.setMaximumSize(QSize(16777215, 30))
        self.label_9.setStyleSheet(u"QLabel {\n"
"	color: #212121;\n"
"	background-color: white;\n"
"	border-right: 1px solid #6272a4;\n"
"	border-top: 1px solid #6272a4;\n"
"	border-bottom: 1px solid #6272a4;\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}")

        self.horizontalLayout_25.addWidget(self.label_9)


        self.gridLayout_24.addLayout(self.horizontalLayout_25, 0, 3, 1, 1)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_7 = QLabel(self.frameControlParameters)
        self.label_7.setObjectName(u"label_7")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy10)
        self.label_7.setMinimumSize(QSize(0, 30))
        self.label_7.setMaximumSize(QSize(16777215, 30))
        self.label_7.setStyleSheet(u"QLabel {\n"
"	margin-right:2px;\n"
"}")

        self.horizontalLayout_26.addWidget(self.label_7)

        self.lineEditPhaseMargin = QLineEdit(self.frameControlParameters)
        self.lineEditPhaseMargin.setObjectName(u"lineEditPhaseMargin")
        self.lineEditPhaseMargin.setMinimumSize(QSize(50, 30))
        self.lineEditPhaseMargin.setMaximumSize(QSize(16777215, 30))
        self.lineEditPhaseMargin.setStyleSheet(u"QLineEdit {\n"
"	color: #212121;\n"
"	background-color: white;\n"
"	border-left: 1px solid #6272a4;\n"
"	border-top: 1px solid #6272a4;\n"
"	border-bottom: 1px solid #6272a4;\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"	padding-left: 3px;\n"
"}")

        self.horizontalLayout_26.addWidget(self.lineEditPhaseMargin)

        self.label_10 = QLabel(self.frameControlParameters)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 30))
        self.label_10.setMaximumSize(QSize(16777215, 30))
        self.label_10.setStyleSheet(u"QLabel {\n"
"	color: #212121;\n"
"	background-color: white;\n"
"	border-right: 1px solid #6272a4;\n"
"	border-top: 1px solid #6272a4;\n"
"	border-bottom: 1px solid #6272a4;\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}")

        self.horizontalLayout_26.addWidget(self.label_10)


        self.gridLayout_24.addLayout(self.horizontalLayout_26, 0, 4, 1, 1)

        self.pushButtonMathSynthesize = QPushButton(self.frameControlParameters)
        self.pushButtonMathSynthesize.setObjectName(u"pushButtonMathSynthesize")
        sizePolicy7.setHeightForWidth(self.pushButtonMathSynthesize.sizePolicy().hasHeightForWidth())
        self.pushButtonMathSynthesize.setSizePolicy(sizePolicy7)
        self.pushButtonMathSynthesize.setMinimumSize(QSize(0, 30))
        self.pushButtonMathSynthesize.setMaximumSize(QSize(16777215, 30))
        self.pushButtonMathSynthesize.setStyleSheet(u"QPushButton {\n"
"	background-color: #6272a4;	\n"
"	border-radius: 5px;\n"
"    color: #f8f8f2;\n"
"	padding-left: 6px;\n"
"	padding-right: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7284b9;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #566490;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #aaaaaa;\n"
"}")

        self.gridLayout_24.addWidget(self.pushButtonMathSynthesize, 0, 5, 1, 1)


        self.horizontalLayout_27.addWidget(self.frameControlParameters)

        self.horizontalSpacer_10 = QSpacerItem(9, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_10)


        self.gridLayout_25.addLayout(self.horizontalLayout_27, 0, 0, 1, 2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, -1, 9)
        self.frameControlSynthesis = QFrame(self.pageMath)
        self.frameControlSynthesis.setObjectName(u"frameControlSynthesis")
        sizePolicy2.setHeightForWidth(self.frameControlSynthesis.sizePolicy().hasHeightForWidth())
        self.frameControlSynthesis.setSizePolicy(sizePolicy2)
        self.frameControlSynthesis.setStyleSheet(u"#frameControlSynthesis {\n"
"	background: white;\n"
"	border: 0px solid #6272a4;\n"
"	border-radius: 7px;\n"
"}")
        self.frameControlSynthesis.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameControlSynthesis.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_22 = QGridLayout(self.frameControlSynthesis)
        self.gridLayout_22.setSpacing(3)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(3, 3, 3, 0)
        self.label_11 = QLabel(self.frameControlSynthesis)
        self.label_11.setObjectName(u"label_11")
        sizePolicy10.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy10)
        self.label_11.setMinimumSize(QSize(0, 30))
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_11.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_22.addWidget(self.label_11, 4, 0, 1, 2)

        self.labelControllerEquation = QLabel(self.frameControlSynthesis)
        self.labelControllerEquation.setObjectName(u"labelControllerEquation")
        self.labelControllerEquation.setStyleSheet(u"QLabel {\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}")
        self.labelControllerEquation.setPixmap(QPixmap(u":/images/images/pid_equation.svg"))
        self.labelControllerEquation.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelControllerEquation.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_22.addWidget(self.labelControllerEquation, 1, 0, 1, 2)

        self.comboBoxControllerType = QComboBox(self.frameControlSynthesis)
        self.comboBoxControllerType.addItem("")
        self.comboBoxControllerType.setObjectName(u"comboBoxControllerType")
        self.comboBoxControllerType.setMinimumSize(QSize(0, 30))
        self.comboBoxControllerType.setMaximumSize(QSize(16777215, 30))
        self.comboBoxControllerType.setStyleSheet(u"QComboBox{\n"
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

        self.gridLayout_22.addWidget(self.comboBoxControllerType, 0, 0, 1, 2)

        self.labelControllerFilterEquation = QLabel(self.frameControlSynthesis)
        self.labelControllerFilterEquation.setObjectName(u"labelControllerFilterEquation")
        self.labelControllerFilterEquation.setStyleSheet(u"QLabel {\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}")
        self.labelControllerFilterEquation.setPixmap(QPixmap(u":/images/images/pid_filter_equation.svg"))
        self.labelControllerFilterEquation.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelControllerFilterEquation.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_22.addWidget(self.labelControllerFilterEquation, 2, 0, 1, 1)

        self.labelPIDParams = QLabel(self.frameControlSynthesis)
        self.labelPIDParams.setObjectName(u"labelPIDParams")
        sizePolicy.setHeightForWidth(self.labelPIDParams.sizePolicy().hasHeightForWidth())
        self.labelPIDParams.setSizePolicy(sizePolicy)
        self.labelPIDParams.setMinimumSize(QSize(0, 30))
        self.labelPIDParams.setStyleSheet(u"QLabel {\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}")
        self.labelPIDParams.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.labelPIDParams.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_22.addWidget(self.labelPIDParams, 5, 0, 1, 1)

        self.line_9 = QFrame(self.frameControlSynthesis)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_22.addWidget(self.line_9, 3, 0, 1, 2)


        self.verticalLayout_7.addWidget(self.frameControlSynthesis)


        self.gridLayout_25.addLayout(self.verticalLayout_7, 1, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.graphMath = GraphicsLayoutWidget(self.pageMath)
        self.graphMath.setObjectName(u"graphMath")
        sizePolicy.setHeightForWidth(self.graphMath.sizePolicy().hasHeightForWidth())
        self.graphMath.setSizePolicy(sizePolicy)
        self.graphMath.setMinimumSize(QSize(100, 100))

        self.verticalLayout_6.addWidget(self.graphMath)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(3)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(3, -1, 3, -1)
        self.horizontalSpacer_5 = QSpacerItem(877, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_5)

        self.pushButtonEnableMathCursors = QPushButton(self.pageMath)
        self.pushButtonEnableMathCursors.setObjectName(u"pushButtonEnableMathCursors")
        self.pushButtonEnableMathCursors.setMinimumSize(QSize(0, 25))
        self.pushButtonEnableMathCursors.setMaximumSize(QSize(16777215, 25))
        self.pushButtonEnableMathCursors.setStyleSheet(u"QPushButton {\n"
"	background-color: #6272a4;	\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"    color: #f8f8f2;\n"
"	padding-left: 8px;\n"
"	padding-right: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7284b9;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #566490;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #aaaaaa;\n"
"}")
        self.pushButtonEnableMathCursors.setCheckable(True)

        self.horizontalLayout_18.addWidget(self.pushButtonEnableMathCursors)


        self.verticalLayout_6.addLayout(self.horizontalLayout_18)


        self.gridLayout_25.addLayout(self.verticalLayout_6, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.pageMath)

        self.gridLayout_5.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frameContent, 1, 1, 1, 1)

        self.frameBottom = QFrame(self.frameMain)
        self.frameBottom.setObjectName(u"frameBottom")
        self.frameBottom.setMinimumSize(QSize(0, 22))
        self.frameBottom.setMaximumSize(QSize(16777215, 22))
        self.frameBottom.setStyleSheet(u"#frameBottom {\n"
"	background-color: #495474;\n"
"}")
        self.frameBottom.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frameBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.frameBottom.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutBottomFrame = QHBoxLayout(self.frameBottom)
        self.horizontalLayoutBottomFrame.setSpacing(0)
        self.horizontalLayoutBottomFrame.setObjectName(u"horizontalLayoutBottomFrame")
        self.horizontalLayoutBottomFrame.setContentsMargins(0, 0, 0, 0)
        self.labelNodeStatus = QLabel(self.frameBottom)
        self.labelNodeStatus.setObjectName(u"labelNodeStatus")
        self.labelNodeStatus.setStyleSheet(u"QLabel {\n"
"	font-size: 12px;\n"
"	color: #f8f8f2;\n"
"	padding-left: 5px;\n"
"	padding-bottom: 2px;\n"
"}")
        self.labelNodeStatus.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayoutBottomFrame.addWidget(self.labelNodeStatus)

        self.label_4 = QLabel(self.frameBottom)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel {\n"
"	font-size: 12px;\n"
"	color: #f8f8f2;\n"
"	padding-bottom: 2px;\n"
"}")
        self.label_4.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayoutBottomFrame.addWidget(self.label_4)

        self.labelStatus = QLabel(self.frameBottom)
        self.labelStatus.setObjectName(u"labelStatus")
        sizePolicy3.setHeightForWidth(self.labelStatus.sizePolicy().hasHeightForWidth())
        self.labelStatus.setSizePolicy(sizePolicy3)
        self.labelStatus.setMaximumSize(QSize(16777215, 16))
        self.labelStatus.setStyleSheet(u"QLabel {\n"
"	font-size: 12px;\n"
"	color: #f8f8f2;\n"
"	padding-bottom: 2px;\n"
"}")
        self.labelStatus.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayoutBottomFrame.addWidget(self.labelStatus)

        self.label_15 = QLabel(self.frameBottom)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"QLabel {\n"
"	font-size: 12px;\n"
"	color: #f8f8f2;\n"
"	padding-bottom: 2px;\n"
"}")
        self.label_15.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayoutBottomFrame.addWidget(self.label_15)

        self.label = QLabel(self.frameBottom)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {\n"
"	font-size: 12px;\n"
"	color: #f8f8f2;\n"
"	padding-bottom: 2px;\n"
"}")
        self.label.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayoutBottomFrame.addWidget(self.label)

        self.labelProgress = QLabel(self.frameBottom)
        self.labelProgress.setObjectName(u"labelProgress")
        self.labelProgress.setStyleSheet(u"QLabel {\n"
"	font-size: 12px;\n"
"	color: #f8f8f2;\n"
"	padding-bottom: 2px;\n"
"}")
        self.labelProgress.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayoutBottomFrame.addWidget(self.labelProgress)

        self.label_16 = QLabel(self.frameBottom)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"QLabel {\n"
"	font-size: 12px;\n"
"	color: #f8f8f2;\n"
"	padding-bottom: 2px;\n"
"}")
        self.label_16.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayoutBottomFrame.addWidget(self.label_16)

        self.labelLog = QLabel(self.frameBottom)
        self.labelLog.setObjectName(u"labelLog")
        sizePolicy8.setHeightForWidth(self.labelLog.sizePolicy().hasHeightForWidth())
        self.labelLog.setSizePolicy(sizePolicy8)
        self.labelLog.setStyleSheet(u"QLabel {\n"
"	font-size: 12px;\n"
"	color: #f8f8f2;\n"
"	padding-bottom: 2px;\n"
"}")
        self.labelLog.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayoutBottomFrame.addWidget(self.labelLog)

        self.label_26 = QLabel(self.frameBottom)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"QLabel {\n"
"	font-size: 12px;\n"
"	color: #f8f8f2;\n"
"	padding-bottom: 2px;\n"
"}")

        self.horizontalLayoutBottomFrame.addWidget(self.label_26)

        self.labelModeStatus = QLabel(self.frameBottom)
        self.labelModeStatus.setObjectName(u"labelModeStatus")
        self.labelModeStatus.setStyleSheet(u"QLabel {\n"
"	font-size: 12px;\n"
"	color: #f8f8f2;\n"
"	padding-bottom: 2px;\n"
"}")

        self.horizontalLayoutBottomFrame.addWidget(self.labelModeStatus)

        self.labelVersion = QLabel(self.frameBottom)
        self.labelVersion.setObjectName(u"labelVersion")
        sizePolicy3.setHeightForWidth(self.labelVersion.sizePolicy().hasHeightForWidth())
        self.labelVersion.setSizePolicy(sizePolicy3)
        self.labelVersion.setMaximumSize(QSize(16777215, 16))
        self.labelVersion.setStyleSheet(u"QLabel {\n"
"	font-size: 12px;\n"
"	color: #f8f8f2;\n"
"	padding-bottom: 2px;\n"
"}")
        self.labelVersion.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.labelVersion.setText(u"| v0.0.0")
        self.labelVersion.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayoutBottomFrame.addWidget(self.labelVersion)


        self.gridLayout.addWidget(self.frameBottom, 2, 1, 1, 1)

        self.frameTop = QFrame(self.frameMain)
        self.frameTop.setObjectName(u"frameTop")
        self.frameTop.setMinimumSize(QSize(0, 50))
        self.frameTop.setMaximumSize(QSize(16777215, 50))
        self.frameTop.setStyleSheet(u"#frameTop {\n"
"	border-bottom: 1px solid #566490;\n"
"}")
        self.frameTop.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frameTop.setFrameShape(QFrame.Shape.NoFrame)
        self.frameTop.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frameTop)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frameTop_3 = QFrame(self.frameTop)
        self.frameTop_3.setObjectName(u"frameTop_3")
        self.frameTop_3.setMinimumSize(QSize(0, 50))
        self.frameTop_3.setMaximumSize(QSize(16777215, 50))
        self.frameTop_3.setStyleSheet(u"#frameTop_3 {	\n"
"	background-color: #6272a4;\n"
"}")
        self.frameTop_3.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frameTop_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frameTop_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frameTop_3)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(5, 0, 5, 0)
        self.pushButtonConnect = QPushButton(self.frameTop_3)
        self.pushButtonConnect.setObjectName(u"pushButtonConnect")
        self.pushButtonConnect.setMinimumSize(QSize(150, 0))
        self.pushButtonConnect.setMaximumSize(QSize(99999, 40))
        self.pushButtonConnect.setStyleSheet(u"QPushButton {	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none; \n"
"	border-radius: 5px;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7284b9;\n"
"	border-style: solid;\n"
"	border-radius: 4px;\n"
"	color: white;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: #566490;\n"
"	border-style: solid;\n"
"	border-radius: 4px;\n"
"	color: white;\n"
"}")
        self.pushButtonConnect.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/icon_plug.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonConnect.setIcon(icon6)
        self.pushButtonConnect.setIconSize(QSize(30, 30))
        self.pushButtonConnect.setCheckable(True)

        self.horizontalLayout_16.addWidget(self.pushButtonConnect)


        self.horizontalLayout_15.addWidget(self.frameTop_3)

        self.frameTop_1 = QFrame(self.frameTop)
        self.frameTop_1.setObjectName(u"frameTop_1")
        self.frameTop_1.setMinimumSize(QSize(0, 50))
        self.frameTop_1.setMaximumSize(QSize(16777215, 50))
        self.frameTop_1.setStyleSheet(u"#frameTop_1 {	\n"
"	background-color: #6272a4;\n"
"	border-left:1px solid #566490;\n"
"	border-right:1px solid #566490;\n"
"}")
        self.frameTop_1.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frameTop_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frameTop_1.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.frameTop_1)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(5)
        self.gridLayout_8.setVerticalSpacing(0)
        self.gridLayout_8.setContentsMargins(0, 0, 5, 0)
        self.label_12 = QLabel(self.frameTop_1)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(25, 25))
        self.label_12.setMaximumSize(QSize(25, 25))
        self.label_12.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.label_12.setPixmap(QPixmap(u":/images/images/logo_small.png"))
        self.label_12.setScaledContents(True)

        self.gridLayout_8.addWidget(self.label_12, 0, 3, 1, 1)

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
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/icon_help.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonHelp.setIcon(icon7)
        self.pushButtonHelp.setIconSize(QSize(20, 20))

        self.gridLayout_8.addWidget(self.pushButtonHelp, 0, 6, 1, 1)

        self.label_2 = QLabel(self.frameTop_1)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Tilda Sans VF"])
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	font-family: Tilda Sans VF;\n"
"	color: #f8f8f2;\n"
"	font-size: 22px;\n"
"}")
        self.label_2.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout_8.addWidget(self.label_2, 0, 4, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(372, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_13, 0, 5, 1, 1)

        self.checkBoxIPC = QCheckBox(self.frameTop_1)
        self.checkBoxIPC.setObjectName(u"checkBoxIPC")
        self.checkBoxIPC.setStyleSheet(u"QCheckBox {\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
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
"}\n"
"")

        self.gridLayout_8.addWidget(self.checkBoxIPC, 0, 1, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(372, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_12, 0, 2, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_8, 0, 0, 1, 1)


        self.horizontalLayout_15.addWidget(self.frameTop_1)

        self.frameTop_2 = QFrame(self.frameTop)
        self.frameTop_2.setObjectName(u"frameTop_2")
        self.frameTop_2.setMinimumSize(QSize(0, 50))
        self.frameTop_2.setMaximumSize(QSize(16777215, 50))
        self.frameTop_2.setStyleSheet(u"#frameTop_2 {	\n"
"	background-color: #6272a4;\n"
"}")
        self.frameTop_2.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frameTop_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frameTop_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frameTop_2)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(5, 0, 5, 0)
        self.pushButtonMinimizeApp = QPushButton(self.frameTop_2)
        self.pushButtonMinimizeApp.setObjectName(u"pushButtonMinimizeApp")
        self.pushButtonMinimizeApp.setMinimumSize(QSize(28, 0))
        self.pushButtonMinimizeApp.setMaximumSize(QSize(28, 28))
        self.pushButtonMinimizeApp.setStyleSheet(u"QPushButton {	\n"
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
        self.pushButtonMinimizeApp.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/icon_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonMinimizeApp.setIcon(icon8)
        self.pushButtonMinimizeApp.setIconSize(QSize(28, 28))

        self.horizontalLayout_13.addWidget(self.pushButtonMinimizeApp)

        self.pushButtonMaximizeApp = QPushButton(self.frameTop_2)
        self.pushButtonMaximizeApp.setObjectName(u"pushButtonMaximizeApp")
        self.pushButtonMaximizeApp.setMinimumSize(QSize(28, 0))
        self.pushButtonMaximizeApp.setMaximumSize(QSize(28, 28))
        self.pushButtonMaximizeApp.setStyleSheet(u"QPushButton {	\n"
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
        self.pushButtonMaximizeApp.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/icon_maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonMaximizeApp.setIcon(icon9)
        self.pushButtonMaximizeApp.setIconSize(QSize(28, 28))

        self.horizontalLayout_13.addWidget(self.pushButtonMaximizeApp)

        self.pushButtonCloseApp = QPushButton(self.frameTop_2)
        self.pushButtonCloseApp.setObjectName(u"pushButtonCloseApp")
        self.pushButtonCloseApp.setMinimumSize(QSize(28, 0))
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
"	color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #B31431;\n"
"	border-style: solid;\n"
"	color: white;\n"
"}")
        self.pushButtonCloseApp.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonCloseApp.setIcon(icon10)

        self.horizontalLayout_13.addWidget(self.pushButtonCloseApp)


        self.horizontalLayout_15.addWidget(self.frameTop_2)


        self.gridLayout.addWidget(self.frameTop, 0, 0, 1, 2)

        self.frameLeft = QFrame(self.frameMain)
        self.frameLeft.setObjectName(u"frameLeft")
        self.frameLeft.setMinimumSize(QSize(55, 0))
        self.frameLeft.setMaximumSize(QSize(55, 16777215))
        self.frameLeft.setStyleSheet(u"#frameLeft {	\n"
"	background-color: #6272a4;\n"
"	border-top: 1px solid #566490;\n"
"}")
        self.frameLeft.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frameLeft.setFrameShape(QFrame.Shape.NoFrame)
        self.frameLeft.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frameLeft)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.pushButtonOpenScope = QPushButton(self.frameLeft)
        self.pushButtonOpenScope.setObjectName(u"pushButtonOpenScope")
        sizePolicy9.setHeightForWidth(self.pushButtonOpenScope.sizePolicy().hasHeightForWidth())
        self.pushButtonOpenScope.setSizePolicy(sizePolicy9)
        self.pushButtonOpenScope.setMinimumSize(QSize(45, 45))
        self.pushButtonOpenScope.setMaximumSize(QSize(45, 45))
        self.pushButtonOpenScope.setStyleSheet(u"QPushButton {	\n"
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
"QPushButton:checked {\n"
"	background-color: #566490;\n"
"	border-style: solid;\n"
"	color: white;\n"
"}")
        self.pushButtonOpenScope.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/icon_line_chart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonOpenScope.setIcon(icon11)
        self.pushButtonOpenScope.setIconSize(QSize(30, 30))
        self.pushButtonOpenScope.setCheckable(True)
        self.pushButtonOpenScope.setChecked(True)

        self.verticalLayout.addWidget(self.pushButtonOpenScope)

        self.pushButtonOpenScopeFRA = QPushButton(self.frameLeft)
        self.pushButtonOpenScopeFRA.setObjectName(u"pushButtonOpenScopeFRA")
        self.pushButtonOpenScopeFRA.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.pushButtonOpenScopeFRA.sizePolicy().hasHeightForWidth())
        self.pushButtonOpenScopeFRA.setSizePolicy(sizePolicy9)
        self.pushButtonOpenScopeFRA.setMinimumSize(QSize(45, 45))
        self.pushButtonOpenScopeFRA.setMaximumSize(QSize(45, 45))
        self.pushButtonOpenScopeFRA.setStyleSheet(u"QPushButton {	\n"
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
"QPushButton:checked {\n"
"	background-color: #566490;\n"
"	border-style: solid;\n"
"	color: white;\n"
"}")
        self.pushButtonOpenScopeFRA.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/icon_fra.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonOpenScopeFRA.setIcon(icon12)
        self.pushButtonOpenScopeFRA.setIconSize(QSize(35, 35))
        self.pushButtonOpenScopeFRA.setCheckable(True)

        self.verticalLayout.addWidget(self.pushButtonOpenScopeFRA)

        self.pushButtonOpenMath = QPushButton(self.frameLeft)
        self.pushButtonOpenMath.setObjectName(u"pushButtonOpenMath")
        sizePolicy9.setHeightForWidth(self.pushButtonOpenMath.sizePolicy().hasHeightForWidth())
        self.pushButtonOpenMath.setSizePolicy(sizePolicy9)
        self.pushButtonOpenMath.setMinimumSize(QSize(45, 45))
        self.pushButtonOpenMath.setMaximumSize(QSize(45, 45))
        self.pushButtonOpenMath.setStyleSheet(u"QPushButton {	\n"
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
"QPushButton:checked {\n"
"	background-color: #566490;\n"
"	border-style: solid;\n"
"	color: white;\n"
"}")
        self.pushButtonOpenMath.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/icon_math.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonOpenMath.setIcon(icon13)
        self.pushButtonOpenMath.setIconSize(QSize(35, 35))
        self.pushButtonOpenMath.setCheckable(True)

        self.verticalLayout.addWidget(self.pushButtonOpenMath)

        self.verticalSpacer = QSpacerItem(20, 464, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButtonOpenLog = QPushButton(self.frameLeft)
        self.pushButtonOpenLog.setObjectName(u"pushButtonOpenLog")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy11.setHorizontalStretch(115)
        sizePolicy11.setVerticalStretch(45)
        sizePolicy11.setHeightForWidth(self.pushButtonOpenLog.sizePolicy().hasHeightForWidth())
        self.pushButtonOpenLog.setSizePolicy(sizePolicy11)
        self.pushButtonOpenLog.setMinimumSize(QSize(45, 45))
        self.pushButtonOpenLog.setMaximumSize(QSize(45, 45))
        self.pushButtonOpenLog.setStyleSheet(u"QPushButton {	\n"
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
"QPushButton:checked {\n"
"	background-color: #566490;\n"
"	border-style: solid;\n"
"	color: white;\n"
"}")
        self.pushButtonOpenLog.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/icon_log.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonOpenLog.setIcon(icon14)
        self.pushButtonOpenLog.setIconSize(QSize(25, 25))
        self.pushButtonOpenLog.setCheckable(True)

        self.verticalLayout.addWidget(self.pushButtonOpenLog)

        self.pushButtonOpenSettings = QPushButton(self.frameLeft)
        self.pushButtonOpenSettings.setObjectName(u"pushButtonOpenSettings")
        sizePolicy9.setHeightForWidth(self.pushButtonOpenSettings.sizePolicy().hasHeightForWidth())
        self.pushButtonOpenSettings.setSizePolicy(sizePolicy9)
        self.pushButtonOpenSettings.setMinimumSize(QSize(45, 45))
        self.pushButtonOpenSettings.setMaximumSize(QSize(45, 45))
        self.pushButtonOpenSettings.setStyleSheet(u"QPushButton {	\n"
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
"QPushButton:checked {\n"
"	background-color: #566490;\n"
"	border-style: solid;\n"
"	color: white;\n"
"}")
        self.pushButtonOpenSettings.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/icon_settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonOpenSettings.setIcon(icon15)
        self.pushButtonOpenSettings.setIconSize(QSize(25, 25))
        self.pushButtonOpenSettings.setCheckable(True)
        self.pushButtonOpenSettings.setChecked(False)

        self.verticalLayout.addWidget(self.pushButtonOpenSettings)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 2, 2)


        self.gridLayout.addWidget(self.frameLeft, 1, 0, 2, 1)


        self.gridLayout_9.addWidget(self.frameMain, 0, 0, 1, 1)

        Window_Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window_Main)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Window_Main)
    # setupUi

    def retranslateUi(self, Window_Main):
        Window_Main.setWindowTitle(QCoreApplication.translate("Window_Main", u"Digital Points", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Window_Main", u"  Connect", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Window_Main", u"  Start", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Window_Main", u"  Disconnect", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Window_Main", u"  Stop", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Window_Main", u"Connected", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Window_Main", u"Started", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Window_Main", u"Disconnected", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Window_Main", u"Stopped", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("Window_Main", u"Select a file to open", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("Window_Main", u"Select a folder to save to", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("Window_Main", u"Amplitudes of Pertubations", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("Window_Main", u"Estimation Periods", None))
        self.comboBox.setItemText(12, QCoreApplication.translate("Window_Main", u"Frequency (Hz)", None))
        self.comboBox.setItemText(13, QCoreApplication.translate("Window_Main", u"Linked", None))
        self.comboBox.setItemText(14, QCoreApplication.translate("Window_Main", u"Unlinked", None))
        self.comboBox.setItemText(15, QCoreApplication.translate("Window_Main", u"Started", None))
        self.comboBox.setItemText(16, QCoreApplication.translate("Window_Main", u"Waiting for the trigger", None))
        self.comboBox.setItemText(17, QCoreApplication.translate("Window_Main", u"Reading the buffer", None))
        self.comboBox.setItemText(18, QCoreApplication.translate("Window_Main", u"There is no license for updating", None))

        self.pushButtonOpenVarViewer.setText(QCoreApplication.translate("Window_Main", u"Variable Viewer \u2191", None))
        self.pushButtonScopeClearImport.setText(QCoreApplication.translate("Window_Main", u"Clear Import", None))
        self.pushButtonEnableScopeCursors.setText(QCoreApplication.translate("Window_Main", u"Cursors", None))
        ___qtablewidgetitem = self.tableWidgetNumbers.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Window_Main", u"Name", None))
        ___qtablewidgetitem1 = self.tableWidgetNumbers.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Window_Main", u"Type", None))
        ___qtablewidgetitem2 = self.tableWidgetNumbers.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Window_Main", u"Address (hex)", None))
        ___qtablewidgetitem3 = self.tableWidgetNumbers.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Window_Main", u"Value (dec)", None))
        ___qtablewidgetitem4 = self.tableWidgetNumbers.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Window_Main", u"Value (hex)", None))
        ___qtablewidgetitem5 = self.tableWidgetNumbers.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Window_Main", u"Value (bin)", None))
        ___qtablewidgetitem6 = self.tableWidgetNumbers.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Window_Main", u"Min", None))
        ___qtablewidgetitem7 = self.tableWidgetNumbers.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Window_Main", u"Max", None))
        ___qtablewidgetitem8 = self.tableWidgetNumbers.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Window_Main", u"Write", None))
        self.labelFRA.setText(QCoreApplication.translate("Window_Main", u"Frequency Response Analyzer (FRA)", None))
        self.labelGraphVisibility.setText(QCoreApplication.translate("Window_Main", u"Visibility of Scope Graphs", None))
        self.comboBoxGraphVisibility.setItemText(0, QCoreApplication.translate("Window_Main", u"Both Graphs", None))
        self.comboBoxGraphVisibility.setItemText(1, QCoreApplication.translate("Window_Main", u"Only Graph 1", None))
        self.comboBoxGraphVisibility.setItemText(2, QCoreApplication.translate("Window_Main", u"Only Graph 2", None))

        self.labelMode.setText(QCoreApplication.translate("Window_Main", u"Mode", None))
        self.comboBoxMode.setItemText(0, QCoreApplication.translate("Window_Main", u"Real-Time Mode", None))
        self.comboBoxMode.setItemText(1, QCoreApplication.translate("Window_Main", u"Triggered Mode", None))
        self.comboBoxMode.setItemText(2, QCoreApplication.translate("Window_Main", u"FRA Mode", None))

        self.labelCursorsMeas.setText(QCoreApplication.translate("Window_Main", u"Cursor measurements", None))
        self.checkBoxMeasRMS.setText(QCoreApplication.translate("Window_Main", u"RMS", None))
        self.checkBoxMeasDelta.setText(QCoreApplication.translate("Window_Main", u"Delta", None))
        self.checkBoxMeasMean.setText(QCoreApplication.translate("Window_Main", u"Mean", None))
        self.checkBoxMeasCF.setText(QCoreApplication.translate("Window_Main", u"Crest factor", None))
        self.checkBoxMeasMin.setText(QCoreApplication.translate("Window_Main", u"Min", None))
        self.checkBoxMeasMax.setText(QCoreApplication.translate("Window_Main", u"Max", None))
        self.labelUpdate.setText(QCoreApplication.translate("Window_Main", u"Update", None))
        self.labelSaveSelection.setText(QCoreApplication.translate("Window_Main", u"Save Selected Variables", None))
        self.checkBoxSaveSelection.setText("")
        self.labelComInterface.setText(QCoreApplication.translate("Window_Main", u"Communication Interface", None))
        self.pushButtonSetSerial.setText(QCoreApplication.translate("Window_Main", u"  Serial  ", None))
        self.pushButtonSetCAN.setText(QCoreApplication.translate("Window_Main", u"CAN", None))
        self.pushButtonConfigureInterface.setText("")
        self.labelNodeAddress.setText(QCoreApplication.translate("Window_Main", u"Address of Node", None))
        self.labelLanguage.setText(QCoreApplication.translate("Window_Main", u"Language", None))
        self.comboBoxLanguage.setItemText(0, QCoreApplication.translate("Window_Main", u"Russian (\u0420\u0443\u0441\u0441\u043a\u0438\u0439)", None))
        self.comboBoxLanguage.setItemText(1, QCoreApplication.translate("Window_Main", u"English (\u0410\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439)", None))

        self.pushButtonSaveSettings.setText(QCoreApplication.translate("Window_Main", u"Save Settings to File", None))
        self.pushButtonLoadSettings.setText(QCoreApplication.translate("Window_Main", u"Load Settings from File", None))
        self.labelRTM.setText(QCoreApplication.translate("Window_Main", u"Real-Time Mode (RTM)", None))
        self.labelTrigger.setText(QCoreApplication.translate("Window_Main", u"Trigger", None))
        self.labelSystem.setText(QCoreApplication.translate("Window_Main", u"System Settings", None))
        self.labelGraphsMeas.setText(QCoreApplication.translate("Window_Main", u"Modes and Graphs", None))
        self.label_19.setText(QCoreApplication.translate("Window_Main", u"Open ELF File", None))
        self.pushButtonUpdateELF.setText(QCoreApplication.translate("Window_Main", u"Update", None))
        self.label_6.setText(QCoreApplication.translate("Window_Main", u"Trigger:", None))
        self.labelTriggerName.setText("")
        self.pushButtonRemoveTrigger.setText(QCoreApplication.translate("Window_Main", u"Remove Trigger", None))
        self.lineEditSearchVariable.setPlaceholderText(QCoreApplication.translate("Window_Main", u"Search for a variable...", None))
        ___qtablewidgetitem9 = self.tableWidgetVariables.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Window_Main", u"Name", None))
        ___qtablewidgetitem10 = self.tableWidgetVariables.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Window_Main", u"Type", None))
        ___qtablewidgetitem11 = self.tableWidgetVariables.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Window_Main", u"Address (hex)", None))
        self.labelCurrentVersionText.setText(QCoreApplication.translate("Window_Main", u"Current Version: ", None))
        self.labelAvailableVersionText.setText(QCoreApplication.translate("Window_Main", u"Available Version: ", None))
        self.pushButtonCheckUpdates.setText(QCoreApplication.translate("Window_Main", u"Check for Updates", None))
        self.pushButtonDownload.setText(QCoreApplication.translate("Window_Main", u"Update", None))
        self.labelFRAConfig.setText(QCoreApplication.translate("Window_Main", u"FRA Config", None))
        self.pushButtonConfigureFRA.setText(QCoreApplication.translate("Window_Main", u"Open", None))
        self.label_25.setText(QCoreApplication.translate("Window_Main", u"Dump Size", None))
        self.spinBoxDumpSize.setSuffix(QCoreApplication.translate("Window_Main", u" MiB", None))
        self.labelCom.setText(QCoreApplication.translate("Window_Main", u"Communication", None))
        self.labelEdgeType.setText(QCoreApplication.translate("Window_Main", u"Type of Edge", None))
        self.pushButtonLeadEdge.setText("")
        self.pushButtonTrailEdge.setText("")
        self.pushButtonAlterEdge.setText("")
        self.labelTriggerCount.setText(QCoreApplication.translate("Window_Main", u"Trigger Divider", None))
        self.labelTriggerLevel.setText(QCoreApplication.translate("Window_Main", u"Trigger Level", None))
        self.labelSettlingTime.setText(QCoreApplication.translate("Window_Main", u"Settling Time", None))
        self.doubleSpinBoxSettlingTime.setSuffix(QCoreApplication.translate("Window_Main", u" s", None))
        self.labelOneShotMode.setText(QCoreApplication.translate("Window_Main", u"One-Shot Mode", None))
        self.checkBoxOneShotMode.setText("")
        self.labelPreTrigger.setText(QCoreApplication.translate("Window_Main", u"Pre-Trigger Samples", None))
        self.labelPreTriggerTime.setText(QCoreApplication.translate("Window_Main", u"-", None))
        self.spinBoxPreTrigger.setSuffix(QCoreApplication.translate("Window_Main", u" sample", None))
        self.spinBoxPreTrigger.setPrefix("")
        self.labelSampleCount.setText(QCoreApplication.translate("Window_Main", u"Sample Divider", None))
        self.labelPostTrigger.setText(QCoreApplication.translate("Window_Main", u"Post-Trigger Samples", None))
        self.labelPostTriggerTime.setText(QCoreApplication.translate("Window_Main", u"-", None))
        self.spinBoxPostTrigger.setSuffix(QCoreApplication.translate("Window_Main", u" sample", None))
        self.pushButtonEnableFRACursors.setText(QCoreApplication.translate("Window_Main", u"Cursors", None))
        ___qtablewidgetitem12 = self.tableWidgetLog.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Window_Main", u"Timestamp", None))
        ___qtablewidgetitem13 = self.tableWidgetLog.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Window_Main", u"Type", None))
        ___qtablewidgetitem14 = self.tableWidgetLog.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Window_Main", u"Message", None))
        self.label_13.setText(QCoreApplication.translate("Window_Main", u"<html><head/><body><p><span style=\" font-size:12pt;\">k</span><span style=\" font-size:12pt; vertical-align:sub;\">corr</span><span style=\" font-size:12pt;\"> =</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("Window_Main", u"(dB)", None))
        self.label_17.setText(QCoreApplication.translate("Window_Main", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u03c6</span><span style=\" font-size:12pt; vertical-align:sub;\">corr</span><span style=\" font-size:12pt;\"> = </span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("Window_Main", u"(deg)", None))
        self.label_3.setText(QCoreApplication.translate("Window_Main", u"<html><head/><body><p><span style=\" font-size:12pt;\">f</span><span style=\" font-size:12pt; vertical-align:sub;\">s</span><span style=\" font-size:12pt;\"> = </span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Window_Main", u"(Hz)", None))
        self.label_5.setText(QCoreApplication.translate("Window_Main", u"<html><head/><body><p><span style=\" font-size:12pt;\">f</span><span style=\" font-size:12pt; vertical-align:sub;\">c</span><span style=\" font-size:12pt;\"> = </span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Window_Main", u"(Hz)", None))
        self.label_7.setText(QCoreApplication.translate("Window_Main", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u03c6</span><span style=\" font-size:12pt; vertical-align:sub;\">m</span><span style=\" font-size:12pt;\"> = </span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Window_Main", u"(deg)", None))
        self.pushButtonMathSynthesize.setText(QCoreApplication.translate("Window_Main", u"Synthesize", None))
        self.label_11.setText(QCoreApplication.translate("Window_Main", u"Controller parameters", None))
        self.labelControllerEquation.setText("")
        self.comboBoxControllerType.setItemText(0, QCoreApplication.translate("Window_Main", u"PID", None))

        self.labelControllerFilterEquation.setText("")
        self.labelPIDParams.setText(QCoreApplication.translate("Window_Main", u"-", None))
        self.pushButtonEnableMathCursors.setText(QCoreApplication.translate("Window_Main", u"Cursors", None))
        self.labelNodeStatus.setText(QCoreApplication.translate("Window_Main", u"Unlinked", None))
        self.label_4.setText(QCoreApplication.translate("Window_Main", u"|", None))
        self.labelStatus.setText(QCoreApplication.translate("Window_Main", u"Disconnected", None))
        self.label_15.setText(QCoreApplication.translate("Window_Main", u"|", None))
        self.label.setText(QCoreApplication.translate("Window_Main", u"Status:", None))
        self.labelProgress.setText(QCoreApplication.translate("Window_Main", u"-", None))
        self.label_16.setText(QCoreApplication.translate("Window_Main", u"|", None))
        self.labelLog.setText("")
        self.label_26.setText(QCoreApplication.translate("Window_Main", u"|", None))
        self.labelModeStatus.setText(QCoreApplication.translate("Window_Main", u"Real-Time Mode", None))
#if QT_CONFIG(tooltip)
        self.pushButtonConnect.setToolTip(QCoreApplication.translate("Window_Main", u"Connect", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonConnect.setText(QCoreApplication.translate("Window_Main", u"  Start", None))
        self.label_12.setText("")
        self.pushButtonHelp.setText("")
        self.label_2.setText(QCoreApplication.translate("Window_Main", u"Digital Points", None))
        self.checkBoxIPC.setText(QCoreApplication.translate("Window_Main", u"IPC", None))
#if QT_CONFIG(tooltip)
        self.pushButtonMinimizeApp.setToolTip(QCoreApplication.translate("Window_Main", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonMinimizeApp.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonMaximizeApp.setToolTip(QCoreApplication.translate("Window_Main", u"Maximize/Restore", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonMaximizeApp.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonCloseApp.setToolTip(QCoreApplication.translate("Window_Main", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonCloseApp.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonOpenScope.setToolTip(QCoreApplication.translate("Window_Main", u"Scope", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButtonOpenScope.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.pushButtonOpenScope.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.pushButtonOpenScope.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonOpenScopeFRA.setToolTip(QCoreApplication.translate("Window_Main", u"FRA", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonOpenScopeFRA.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonOpenMath.setToolTip(QCoreApplication.translate("Window_Main", u"<html><head/><body><p>Math</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonOpenMath.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonOpenLog.setToolTip(QCoreApplication.translate("Window_Main", u"Log", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonOpenLog.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonOpenSettings.setToolTip(QCoreApplication.translate("Window_Main", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonOpenSettings.setText("")
    # retranslateUi

