from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtGui import QMouseEvent, QPaintEvent
from PyQt6.QtWidgets import *
import shapefile

class Draw(QWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mbr = []
        self.buildings = []
        self.shapefile = None
        self.border = [0,0,10,10]
        self.missingFile = False
        
    def getData(self):
        
        #Find file (.shp)
        file = QFileDialog.getOpenFileName(self, "Open file", "", "Shapefile (*.shp)")
        path = file[0]

        #Fix if no file is chosen (phantom building procedure)
        if bool(file[0]) == False:
            self.missingFile = True
            return
        self.missingFile = False

        #Load the shapefile
        shp = shapefile.Reader(path)
        self.shapefile = shp.shapes()

        #Get border window
        x = []
        y = []
        for i in range(len(shp)):
            for j in self.shapefile[i].points:
                x.append(j[0])
                y.append(j[1])
        self.border = [min(x), min(y), max(x), max(y)]

    def setView(self, h, w):
        
        #Phantom building definition
        if self.missingFile == True:
            self.buildings = []
            pol = QPolygonF([QPointF(0,0), QPointF(-10,0), QPointF(0,-10), QPointF(-10,-10)])
            self.buildings.append(pol)

        #Set the border window to view data
        else:
            self.buildings = [None] * len(self.shapefile)

            #Building scaling and creation
            for i in range(len(self.shapefile)):
                self.buildings[i] = QPolygonF()
                for j in self.shapefile[i].points:
                    x = int(((j[0] - self.border[0]) / (self.border[2] - self.border[0]) * w))
                    y = int((h - (j[1] - self.border[1]) / (self.border[3] - self.border[1]) * (h)))
                    point = QPointF(x,y)
                    self.buildings[i].append(point)      
        
    def paintEvent(self, e: QPaintEvent):
        
        #Create new graphic object
        qp = QPainter(self)
        
        #Start drawing
        qp.begin(self)
        
        #Set graphical attributes (buildings)
        for i, building in enumerate(self.buildings):
            
            qp.setPen(QColor(204, 119, 34))
            qp.setBrush(QColor(230, 205, 0))
            qp.drawPolygon(building)
            
        for i, mbr in enumerate(self.mbr):
            
            qp.setPen(Qt.GlobalColor.black)
            qp.setBrush(Qt.GlobalColor.black)
            qp.drawPolygon(mbr)
            
        self.mbr = []
                     
        #End drawing
        qp.end()

    def getBuildings(self):
        return self.buildings
    
    def setMBR(self, pol: QPolygonF):
        self.mbr.append(pol)  
    
    def clearData(self):
        
        #Clear everythink from canvas
        self.buildings = []
        self.mbr = []
                
        #Repaint screen
        self.repaint()
        
    def clearResults(self):
        
        #Clear result of simplification
        self.mbr = []
        
        #Repain screen
        self.repaint()