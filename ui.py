# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1099, 868)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.leftMenu = QtWidgets.QGroupBox(self.splitter)
        self.leftMenu.setObjectName("leftMenu")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.leftMenu)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.leftMenuIn = QtWidgets.QGridLayout()
        self.leftMenuIn.setObjectName("leftMenuIn")
        self.addRelatLabel = QtWidgets.QLabel(self.leftMenu)
        self.addRelatLabel.setObjectName("addRelatLabel")
        self.leftMenuIn.addWidget(self.addRelatLabel, 0, 0, 1, 1)
        self.addNodeLabel = QtWidgets.QLabel(self.leftMenu)
        self.addNodeLabel.setObjectName("addNodeLabel")
        self.leftMenuIn.addWidget(self.addNodeLabel, 4, 0, 1, 1)
        self.nameButton = QtWidgets.QPushButton(self.leftMenu)
        self.nameButton.setObjectName("nameButton")
        self.leftMenuIn.addWidget(self.nameButton, 2, 1, 1, 1)
        self.weigth = QtWidgets.QDoubleSpinBox(self.leftMenu)
        self.weigth.setObjectName("weigth")
        self.leftMenuIn.addWidget(self.weigth, 3, 1, 1, 1)
        self.weigthLabel = QtWidgets.QLabel(self.leftMenu)
        self.weigthLabel.setObjectName("weigthLabel")
        self.leftMenuIn.addWidget(self.weigthLabel, 3, 0, 1, 1)
        self.pickColor = QtWidgets.QPushButton(self.leftMenu)
        self.pickColor.setObjectName("pickColor")
        self.leftMenuIn.addWidget(self.pickColor, 1, 1, 1, 1)
        self.pickColorLabel = QtWidgets.QLabel(self.leftMenu)
        self.pickColorLabel.setObjectName("pickColorLabel")
        self.leftMenuIn.addWidget(self.pickColorLabel, 1, 0, 1, 1)
        self.addRelat = QtWidgets.QPushButton(self.leftMenu)
        self.addRelat.setObjectName("addRelat")
        self.leftMenuIn.addWidget(self.addRelat, 0, 1, 1, 1)
        self.nameLine = QtWidgets.QLineEdit(self.leftMenu)
        self.nameLine.setObjectName("nameLine")
        self.leftMenuIn.addWidget(self.nameLine, 2, 0, 1, 1)
        self.addNode = QtWidgets.QPushButton(self.leftMenu)
        self.addNode.setObjectName("addNode")
        self.leftMenuIn.addWidget(self.addNode, 4, 1, 1, 1)
        self.gridLayout_4.addLayout(self.leftMenuIn, 0, 0, 1, 1)
        self.mapView = QtWidgets.QGraphicsView(self.splitter)
        self.mapView.setObjectName("mapView")
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1099, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionFullscreen = QtWidgets.QAction(MainWindow)
        self.actionFullscreen.setObjectName("actionFullscreen")
        self.actionOpen_Help = QtWidgets.QAction(MainWindow)
        self.actionOpen_Help.setObjectName("actionOpen_Help")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_as)
        self.menuView.addAction(self.actionFullscreen)
        self.menuHelp.addAction(self.actionOpen_Help)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addRelatLabel.setText(_translate("MainWindow", "Add Relationship:"))
        self.addNodeLabel.setText(_translate("MainWindow", "Add Node:"))
        self.nameButton.setText(_translate("MainWindow", "Name"))
        self.weigthLabel.setText(_translate("MainWindow", "Weigth:"))
        self.pickColor.setText(_translate("MainWindow", "Pick"))
        self.pickColorLabel.setText(_translate("MainWindow", "Pick color:"))
        self.addRelat.setText(_translate("MainWindow", "Add"))
        self.nameLine.setText(_translate("MainWindow", "Name"))
        self.addNode.setText(_translate("MainWindow", "Add"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionFullscreen.setText(_translate("MainWindow", "Fullscreen"))
        self.actionFullscreen.setShortcut(_translate("MainWindow", "F11"))
        self.actionOpen_Help.setText(_translate("MainWindow", "View Docs"))
        self.actionOpen_Help.setShortcut(_translate("MainWindow", "Ctrl+H"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
