from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtGui import QMouseEvent, QPaintEvent
from PyQt6.QtWidgets import *
import shapefile


class Draw(QWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.q = QPointF(-10,-10)
        self.polygons = []
        self.results = []
        self.shapefile = None
        self.border = [0,0,10,10]
        self.missingFile = False

    def getData(self):
        
        #Find file (.shp)
        file = QFileDialog.getOpenFileName(self, "Open file", "", "Shapefile (*.shp)")
        path = file[0]

        #Fix if no file is chosen (phantom polygon procedure)
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
        
        #Phantom polygon definition
        if self.missingFile == True:
            self.polygons = []
            pol = QPolygonF([QPointF(0,0), QPointF(-10,0), QPointF(0,-10), QPointF(-10,-10)])
            self.polygons.append(pol)

        #Set the border window to view data
        else:
            self.polygons = [None] * len(self.shapefile)

            #Polygon scaling and creation
            for i in range(len(self.shapefile)):
                self.polygons[i] = QPolygonF()
                for j in self.shapefile[i].points:
                    x = int(((j[0] - self.border[0]) / (self.border[2] - self.border[0]) * w))
                    y = int((h - (j[1] - self.border[1]) / (self.border[3] - self.border[1]) * (h)))
                    point = QPointF(x,y)
                    self.polygons[i].append(point)
    
        
    def mousePressEvent(self, e: QMouseEvent):
        
        #Get coordinates of q
        x = e.position().x()
        y = e.position().y()
                  
        #Move q
        self.q.setX(x)
        self.q.setY(y)
            
        #Repaint screen
        self.repaint()
        
        
    def paintEvent(self, e: QPaintEvent):
                
        #Create new graphic object
        qp = QPainter(self)
        
        #Start drawing
        qp.begin(self)
        
        #Set graphical attributes (polygones)
        for i, polygon in enumerate(self.polygons):
            
            qp.setPen(QColor(204, 119, 34))
            qp.setBrush(QColor(230, 205, 0))

            if self.results and (self.results[i] == 1) or self.results and (self.results[i] == 2):
                qp.setPen(QColor(255, 0, 0))
                qp.setBrush(QColor(255, 102, 0))

            qp.drawPolygon(polygon)
        
        self.results = []
        
        #Set graphical attributes (point)
        qp.setBrush(Qt.GlobalColor.darkMagenta)
        
        #Draw point
        r = 6
        qp.drawEllipse(int(self.q.x()-r), int(self.q.y()-r), 2*r, 2*r)
        
        #End drawing
        qp.end()


    def setResult(self, result):
        
        #Add results to be visualised
        self.results.append(result)      
        
            
    def getQ(self):
        
        #Return analyzed point
        return self.q
    
    
    def getPolygons(self):
        
        #Return analyzed polygon
        return self.polygons
    
    
    def clearData(self):
        
        #Clear polygon
        self.polygons = []
        
        #Shift point
        self.q.setX(-100)
        self.q.setY(-100)
        
        #Repaint screen
        self.repaint()
        