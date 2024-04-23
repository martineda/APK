from PyQt6 import QtCore, QtGui, QtWidgets
from algorithms import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1108, 794)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayoSut")
        self.Canvas = Draw(parent=self.centralwidget)
        self.Canvas.setObjectName("Canvas")
        self.horizontalLayout.addWidget(self.Canvas)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1108, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSimplify = QtWidgets.QMenu(parent=self.menubar)
        self.menuSimplify.setObjectName("menuSimplify")
        self.menuView = QtWidgets.QMenu(parent=self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionMinimum_Bounding_Rectangle = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons\maer.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionMinimum_Bounding_Rectangle.setIcon(icon)
        self.actionMinimum_Bounding_Rectangle.setObjectName("actionMinimum_Bounding_Rectangle")
        self.actionPCA = QtGui.QAction(parent=MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons\pca.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionPCA.setIcon(icon1)
        self.actionPCA.setObjectName("actionPCA")
        self.actionClear_results = QtGui.QAction(parent=MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons\clear_ch.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClear_results.setIcon(icon2)
        self.actionClear_results.setObjectName("actionClear_results")
        self.actionClear_all = QtGui.QAction(parent=MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons\clear_er.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClear_all.setIcon(icon3)
        self.actionClear_all.setObjectName("actionClear_all")
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons\open_file.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionOpen.setIcon(icon4)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtGui.QAction(parent=MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons\exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClose.setIcon(icon5)
        self.actionClose.setObjectName("actionClose")
        self.actionLongestEdge = QtGui.QAction(parent=MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons\maer.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionLongestEdge.setIcon(icon6)
        self.actionLongestEdge.setObjectName("actionLongestEdge")
        self.actionLongestEdge = QtGui.QAction(parent=MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons\longestedge.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionLongestEdge.setIcon(icon7)
        self.actionLongestEdge.setObjectName("actionLongestEdge")
        self.actionWallAverage = QtGui.QAction(parent=MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons\wa.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionWallAverage.setIcon(icon8)
        self.actionWallAverage.setObjectName("actionWallAverage")
        self.actionWeightedBisector = QtGui.QAction(parent=MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons\weightedbisector.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionWeightedBisector.setIcon(icon9)
        self.actionWeightedBisector.setObjectName("actionWallAverage")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuSimplify.addAction(self.actionMinimum_Bounding_Rectangle)
        self.menuSimplify.addAction(self.actionPCA)
        self.menuSimplify.addAction(self.actionLongestEdge)
        self.menuSimplify.addAction(self.actionWallAverage)
        self.menuSimplify.addAction(self.actionWeightedBisector)
        self.menuView.addAction(self.actionClear_results)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionClear_all)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSimplify.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionMinimum_Bounding_Rectangle)
        self.toolBar.addAction(self.actionPCA)
        self.toolBar.addAction(self.actionLongestEdge)
        self.toolBar.addAction(self.actionWallAverage)
        self.toolBar.addAction(self.actionWeightedBisector)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClear_results)
        self.toolBar.addAction(self.actionClear_all)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClose)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.retranslateUi(MainWindow)
        self.actionClear_all.triggered.connect(self.clearAllClick)
        self.actionClear_results.triggered.connect(self.clearClick)
        self.actionClose.triggered.connect(MainWindow.close)
        self.actionOpen.triggered.connect(self.openClick)
        self.actionMinimum_Bounding_Rectangle.triggered.connect(self.maerClick)
        self.actionPCA.triggered.connect(self.pcaClick)
        self.actionLongestEdge.triggered.connect(self.longestEdgeClick)
        self.actionWallAverage.triggered.connect(self.wallAverageClick)
        self.actionWeightedBisector.triggered.connect(self.weightedBisectorClick)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def clearAllClick(self):
        self.Canvas.clearData()
    
    def clearClick(self):
        self.Canvas.clearResults()
    
    def openClick(self):
        
        #Get canvas parameters
        h = self.Canvas.frameSize().height()
        w = self.Canvas.frameSize().width()
        
        #Open and view data
        self.Canvas.getData()
        self.Canvas.setView(h, w)
    
    def pcaClick(self):
        
        #Get buildings
        polygons = self.Canvas.getBuildings()
        
        #Simplify buildings
        a = Algorithms()
        evaluation = 0
        n = len(polygons)
        for pol in polygons:
            pca = a.createERPCA(pol)
            
            #Don't accept poorly simplified buildings and errors
            if pca is not None:
                evaluation += 1
                self.Canvas.setMBR(pca) 
        
        #Get result for PCA
        print(f'PCA accuracy score: {100 * evaluation / n} %')
        
        #Repaint screen
        self.Canvas.repaint()
    
    def maerClick(self):
        
        #Get buildings
        polygons = self.Canvas.getBuildings()
        
        #Simplify buildings
        a = Algorithms()
        evaluation = 0
        n = len(polygons)
        for pol in polygons:
            maer = a.mbr(pol)
            
            #Don't accept poorly simplified buildings and errors
            if maer is not None:
                evaluation += 1
                self.Canvas.setMBR(maer) 
        
        #Get result for MAER
        print(f'MAER accuracy score: {100 * evaluation / n} %')
                   
        #Repaint screen
        self.Canvas.repaint()
    
    def longestEdgeClick(self):
        
        #Get buildings
        polygons = self.Canvas.getBuildings()
        
        #Simplify buildings
        a = Algorithms()
        evaluation = 0
        n = len(polygons)
        for pol in polygons:
            le = a.longestEdge(pol)
            
            #Don't accept poorly simplified buildings and errors
            if le is not None:
                evaluation += 1
            self.Canvas.setMBR(le)
            
        #Get result for Longest Edge
        print(f'Longest Edge accuracy score: {100 * evaluation / n} %')
        
        #Repaint screen    
        self.Canvas.repaint()
    
    def wallAverageClick(self):
        
        #Get buildings
        polygons = self.Canvas.getBuildings()
        
        #Simplify buildings
        a = Algorithms()
        evaluation = 0
        n = len(polygons)
        for pol in polygons:
            wa = a.wallAverage(pol)
            
            #Don't accept poorly simplified buildings and errors
            if wa is not None:
                evaluation += 1
            self.Canvas.setMBR(wa)

        #Get result for Wall Average
        print(f'Wall Average accuracy score: {100 * evaluation / n} %')
                
        #Repaint screen    
        self.Canvas.repaint()
    
    def weightedBisectorClick(self):

        #Get buildings
        polygons = self.Canvas.getBuildings()
        
        #Simplify buildings
        a = Algorithms()
        evaluation = 0
        n = len(polygons)
        for pol in polygons:
            wb = a.weightedBisector(pol)
            
            #Don't accept poorly simplified buildings and errors
            if wb is not None:
                evaluation += 1
                self.Canvas.setMBR(wb) 

        #Get result for Weighted Bisector
        print(f'Weighted Bisector accuracy score: {100 * evaluation / n} %')
                
        #Repaint screen    
        self.Canvas.repaint()
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SimplifyBuildings"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSimplify.setTitle(_translate("MainWindow", "Simplify"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionMinimum_Bounding_Rectangle.setText(_translate("MainWindow", "Minimum Bounding Rectangle"))
        self.actionPCA.setText(_translate("MainWindow", "PCA"))
        self.actionClear_results.setText(_translate("MainWindow", "Clear results"))
        self.actionClear_all.setText(_translate("MainWindow", "Clear all"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionClose.setText(_translate("MainWindow", "Exit"))
        self.actionLongestEdge.setText(_translate("MainWindow", "Longest Edge"))
        self.actionWallAverage.setText(_translate("MainWindow", "Wall Average"))
        self.actionWeightedBisector.setText(_translate("MainWindow", "Weighted Bisector"))
        
from draw import Draw


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
