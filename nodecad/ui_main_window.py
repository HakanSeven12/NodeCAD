# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from pyqtribbon import RibbonBar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1368, 908)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionImport_Nodes = QAction(MainWindow)
        self.actionImport_Nodes.setObjectName(u"actionImport_Nodes")
        self.actionSave_Project = QAction(MainWindow)
        self.actionSave_Project.setObjectName(u"actionSave_Project")
        self.actionDesignDark_Std = QAction(MainWindow)
        self.actionDesignDark_Std.setObjectName(u"actionDesignDark_Std")
        self.actionDesignDark_Tron = QAction(MainWindow)
        self.actionDesignDark_Tron.setObjectName(u"actionDesignDark_Tron")
        self.actionEnableInfoMessages = QAction(MainWindow)
        self.actionEnableInfoMessages.setObjectName(u"actionEnableInfoMessages")
        self.actionDisableInfoMessages = QAction(MainWindow)
        self.actionDisableInfoMessages.setObjectName(u"actionDisableInfoMessages")
        self.actionSave_Pic_Viewport = QAction(MainWindow)
        self.actionSave_Pic_Viewport.setObjectName(u"actionSave_Pic_Viewport")
        self.actionSave_Pic_Whole_Scene_scaled = QAction(MainWindow)
        self.actionSave_Pic_Whole_Scene_scaled.setObjectName(u"actionSave_Pic_Whole_Scene_scaled")
        self.actionNew_Flow = QAction(MainWindow)
        self.actionNew_Flow.setObjectName(u"actionNew_Flow")
        self.actionRename_Flow = QAction(MainWindow)
        self.actionRename_Flow.setObjectName(u"actionRename_Flow")
        self.actionDelete_Flow = QAction(MainWindow)
        self.actionDelete_Flow.setObjectName(u"actionDelete_Flow")
        self.actionImport_Example_Nodes = QAction(MainWindow)
        self.actionImport_Example_Nodes.setObjectName(u"actionImport_Example_Nodes")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.gridLayout = QGridLayout(self.centralWidget)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_vertical_splitter = QSplitter(self.centralWidget)
        self.main_vertical_splitter.setObjectName(u"main_vertical_splitter")
        self.main_vertical_splitter.setOrientation(Qt.Vertical)
        self.main_horizontal_splitter = QSplitter(self.main_vertical_splitter)
        self.main_horizontal_splitter.setObjectName(u"main_horizontal_splitter")
        self.main_horizontal_splitter.setOrientation(Qt.Horizontal)
        self.splitter = QSplitter(self.main_horizontal_splitter)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.flows_groupBox = QGroupBox(self.splitter)
        self.flows_groupBox.setObjectName(u"flows_groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.flows_groupBox)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter.addWidget(self.flows_groupBox)
        self.nodes_groupBox = QGroupBox(self.splitter)
        self.nodes_groupBox.setObjectName(u"nodes_groupBox")
        self.verticalLayout = QVBoxLayout(self.nodes_groupBox)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter.addWidget(self.nodes_groupBox)
        self.main_horizontal_splitter.addWidget(self.splitter)
        self.flows_tab_widget = QTabWidget(self.main_horizontal_splitter)
        self.flows_tab_widget.setObjectName(u"flows_tab_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.flows_tab_widget.sizePolicy().hasHeightForWidth())
        self.flows_tab_widget.setSizePolicy(sizePolicy1)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.flows_tab_widget.addTab(self.tab, "")
        self.main_horizontal_splitter.addWidget(self.flows_tab_widget)
        self.main_vertical_splitter.addWidget(self.main_horizontal_splitter)
        self.console_placeholder_widget = QWidget(self.main_vertical_splitter)
        self.console_placeholder_widget.setObjectName(u"console_placeholder_widget")
        self.main_vertical_splitter.addWidget(self.console_placeholder_widget)
        self.gridLayout.addWidget(self.main_vertical_splitter, 0, 0, 1, 1)

        self.menuBar = RibbonBar(title="RibbonBar",maxRows=3, parent=MainWindow)

        self.menuFile = QMenu(self.menuBar)
        self.menuScripts = QMenu(self.menuFile)
        self.menuView = QMenu(self.menuBar)
        self.menuFlow_Design_Style = QMenu(self.menuView)
        self.menuSave_Picture = QMenu(self.menuView)
        self.menuDebugging = QMenu(self.menuBar)
        self.menuInfo_Messages = QMenu(self.menuDebugging)

        self.file = QToolButton(self.menuBar)
        self.file.setMenu(self.menuFile)
        self.file.setText("File")
        self.file.setPopupMode(QToolButton.InstantPopup)
        
        self.view = QToolButton(self.menuBar)
        self.view.setMenu(self.menuView)
        self.view.setText("View")
        self.view.setPopupMode(QToolButton.InstantPopup)
        
        self.debug = QToolButton(self.menuBar)
        self.debug.setMenu(self.menuDebugging)
        self.debug.setText("Options")
        self.debug.setPopupMode(QToolButton.InstantPopup)

        self.menuBar.addQuickAccessButton(self.file)
        self.menuBar.addQuickAccessButton(self.view)
        self.menuBar.addQuickAccessButton(self.debug)

        self.menuFile.addAction(self.actionImport_Nodes)
        self.menuFile.addAction(self.actionImport_Example_Nodes)
        self.menuFile.addAction(self.actionSave_Project)
        self.menuFile.addAction(self.menuScripts.menuAction())
        self.menuScripts.addAction(self.actionNew_Flow)
        self.menuScripts.addAction(self.actionRename_Flow)
        self.menuScripts.addAction(self.actionDelete_Flow)

        self.menuView.addSeparator()
        self.menuView.addAction(self.menuFlow_Design_Style.menuAction())
        self.menuView.addAction(self.menuSave_Picture.menuAction())
        self.menuSave_Picture.addAction(self.actionSave_Pic_Viewport)
        self.menuSave_Picture.addAction(self.actionSave_Pic_Whole_Scene_scaled)

        self.menuDebugging.addAction(self.menuInfo_Messages.menuAction())
        self.menuInfo_Messages.addAction(self.actionEnableInfoMessages)
        self.menuInfo_Messages.addAction(self.actionDisableInfoMessages)

        MainWindow.setCentralWidget(self.centralWidget)
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        # Categories
        category1 = self.menuBar.addCategory("Test")
        panel1 = category1.addPanel("Box")

        disp = panel1.addLargeButton("Display Box", QIcon("python.png"))
        disp.clicked.connect(self.displayBOX)

        eras = panel1.addLargeButton("Erase Box", QIcon("python.png"))
        eras.clicked.connect(self.eraseBOX)

        self.flows_tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def displayBOX(self):
        pass

    def eraseBOX(self):
        pass
