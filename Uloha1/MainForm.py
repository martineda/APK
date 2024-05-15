from PyQt6 import QtCore, QtGui, QtWidgets
from draw import Draw
from algorithms import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1095, 708)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Canvas = Draw(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Canvas.sizePolicy().hasHeightForWidth())
        self.Canvas.setSizePolicy(sizePolicy)
        self.Canvas.setObjectName("Canvas")
        self.horizontalLayout.addWidget(self.Canvas)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1095, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuInput = QtWidgets.QMenu(parent=self.menubar)
        self.menuInput.setObjectName("menuInput")
        self.menuAnalyze = QtWidgets.QMenu(parent=self.menubar)
        self.menuAnalyze.setObjectName("menuAnalyze")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/open_file.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setObjectName("actionExit")
        self.actionClear = QtGui.QAction(parent=MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/clear_all.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClear.setIcon(icon2)
        self.actionClear.setObjectName("actionClear")
        self.actionRay_Crossing_Algorithm = QtGui.QAction(parent=MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/ray.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionRay_Crossing_Algorithm.setIcon(icon3)
        self.actionRay_Crossing_Algorithm.setObjectName("actionRay_Crossing_Algorithm")
        self.actionWinding_Number_Algorithm = QtGui.QAction(parent=MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/winding.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionWinding_Number_Algorithm.setIcon(icon4)
        self.actionWinding_Number_Algorithm.setObjectName("actionWinding_Number_Algorithm")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuInput.addAction(self.actionClear)
        self.menuAnalyze.addAction(self.actionRay_Crossing_Algorithm)
        self.menuAnalyze.addAction(self.actionWinding_Number_Algorithm)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInput.menuAction())
        self.menubar.addAction(self.menuAnalyze.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRay_Crossing_Algorithm)
        self.toolBar.addAction(self.actionWinding_Number_Algorithm)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClear)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        
        self.actionOpen.triggered.connect(self.openClick)
        self.actionClear.triggered.connect(self.clearClick)
        self.actionRay_Crossing_Algorithm.triggered.connect(self.rayCrossingClick)
        self.actionWinding_Number_Algorithm.triggered.connect(self.windingNumberClick)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
    def openClick(self):
        
        #Get canvas parameters
        h = self.Canvas.frameSize().height()
        w = self.Canvas.frameSize().width()
        
        #Open and view data
        self.Canvas.getData()
        self.Canvas.setView(h, w)
     
        
    def clearClick(self):

        #Clear data
        self.Canvas.clearData()
        
        
    def rayCrossingClick(self):
        
        #Get data
        q = self.Canvas.getQ()
        pol = self.Canvas.getPolygons()

        #Run analysis
        a = Algorithms()
        for i in pol:
            result = a.rayCrossing(q, i)
            self.Canvas.setResult(result)
        self.Canvas.repaint()
        
        
    def windingNumberClick(self):
        
        #Get data
        q = self.Canvas.getQ()
        pol = self.Canvas.getPolygons()
        
        #Run analysis
        a = Algorithms()
        for i in pol:
            result = a.windingNumber(q, i)
            self.Canvas.setResult(result)
        self.Canvas.repaint()
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Point and polygon position"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuInput.setTitle(_translate("MainWindow", "Input"))
        self.menuAnalyze.setTitle(_translate("MainWindow", "Analyze"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setToolTip(_translate("MainWindow", "Open file"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setToolTip(_translate("MainWindow", "Close application"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionClear.setToolTip(_translate("MainWindow", "Clear data"))
        self.actionRay_Crossing_Algorithm.setText(_translate("MainWindow", "Ray Crossing Algorithm"))
        self.actionWinding_Number_Algorithm.setText(_translate("MainWindow", "Winding Number Algorithm"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
