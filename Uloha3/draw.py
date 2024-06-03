from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from qpoint3df import *
from edge import *
from random import *
from triangle import *
from math import *
import csv

class Draw(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.points = []
        self.dt = []
        self.contours = []
        self.boldContours = []
        self.dtm_slope = []
        self.dtm_aspect = []
        self.viewDT = True
        self.viewContourLines = True
        self.viewSlope = True
        self.viewAspect = True

    def getData(self, w, h):
        #Find file
        file = QFileDialog.getOpenFileName(self, "Open file", "", "*.txt")
        path = file[0]
    
        #Fix if no file is chosen (return empty list)
        if bool(file[0]) == False:
            self.points = []
            return self.points
        
        #Lists of coords
        points_x = []
        points_y = []
        points_z = []
        
        #Reader
        with open(path, "r") as f:
            for row in csv.reader(f, delimiter=" "):
                #Create separate columns
                points_x.append(float(row[0]))
                points_y.append(float(row[1]))
                points_z.append(float(row[2]))

        #Min/Max box for view
        minmaxBox = [min(points_x), min(points_y), max(points_x), max(points_y)]

        #Fit data into the window
        for i in range(len(points_x)):
            x = int(((points_x[i] - minmaxBox[0]) / (minmaxBox[2] - minmaxBox[0]) * w))
            y = int((h - (points_y[i] - minmaxBox[1]) / (minmaxBox[3] - minmaxBox[1]) * (h)))
            p = QPoint3DF(x, y, points_z[i])
            self.points.append(p)

    def aspectColor(self, aspect):
        #North
        if (aspect >= 11*pi/8) and (aspect < 13*pi/8):
            return QColor(0, 129, 16)

        #Northeast
        elif (aspect >= 13*pi/8) and (aspect < 15*pi/8):
            return QColor(102, 226, 117)

        #East
        elif ((aspect >= 0) and (aspect < pi/8)) or ((aspect >= 15*pi/8) and (aspect < 2*pi)):
            return QColor(95, 189, 206)

        #Southeast
        elif (aspect >= pi/8) and (aspect < 3*pi/8):
            return QColor(4, 133, 157)

        #South
        elif (aspect >= 3*pi/8) and (aspect < 5*pi/8):
            return QColor(1, 86, 102)

        #Southwest
        elif (aspect >= 5*pi/8) and (aspect < 7*pi/8):
            return QColor(166, 81, 0)

        #West
        elif (aspect >= 7*pi/8) and (aspect < 9*pi/8):
            return QColor(255, 183, 115)

        #Northwest
        elif (aspect >= 9*pi/8) and (aspect < 11*pi/8):
            return QColor(0, 198, 24)

        else:
            return QColor(255, 255, 255)
        
    def paintEvent(self,  e:QPaintEvent):
        #Draw situation
        
        #Create new object
        qp = QPainter(self)

        #Start drawing
        qp.begin(self)
        
        if self.viewSlope:
            #Set graphic attributes
            qp.setPen(Qt.GlobalColor.gray)
      
            #Draw slope
            for t in self.dtm_slope:
                #Get slope
                slope = t.getSlope()
            
                #Convert slope to color
                mju = 2*255/pi
                col = int(255 - mju*slope)
                color = QColor(col, col, col)
                qp.setBrush(color)
            
                #Draw triangle
                qp.drawPolygon(t.getVertices())
                
        if self.viewAspect:
            #Draw aspect
             for t in self.dtm_aspect:
                 aspect = t.getAspect()
                 color = self.aspectColor(aspect)
                 qp.setBrush(color)
                 
                 #Draw triangle
                 qp.drawPolygon(t.getVertices())
                
        #Draw DT
        if self.viewDT:     
            #Set graphic attributes
            qp.setPen(Qt.GlobalColor.green)
            qp.setBrush(Qt.GlobalColor.transparent)
            
            #Draw triangulation
            for e in self.dt:
                qp.drawLine(int(e.getStart().x()), int(e.getStart().y()), int(e.getEnd().x()), int(e.getEnd().y()))

        if self.viewContourLines:
            #Set graphic attributes
            qp.setPen(QColor(165, 42, 42))
            qp.setBrush(Qt.GlobalColor.yellow)
        
            #Draw contour lines
            for e in self.contours:
               qp.drawLine(int(e.getStart().x()), int(e.getStart().y()), int(e.getEnd().x()), int(e.getEnd().y()))
            
            #Set graphic attributes
            qp.setPen(QPen(QColor(165, 42, 42),2))
            qp.setBrush(Qt.GlobalColor.yellow)
            
            #Draw bold contour lines
            for e in self.boldContours:
                qp.drawLine(int(e.getStart().x()), int(e.getStart().y()), int(e.getEnd().x()), int(e.getEnd().y()))

        #Set graphic attributes
        qp.setPen(Qt.GlobalColor.gray)
        qp.setBrush(Qt.GlobalColor.yellow)    
            
        #Draw points
        r = 4
        for p in self.points:
            qp.drawEllipse(int(p.x()-r), int(p.y()-r), 2*r, 2*r)
       
        #End drawing
        qp.end()
        
    
    def getPoints(self):
        # Return points
        return self.points
    
    def getDT(self):
        #Return DT
        return self.dt
    
    def clearAll(self):
        #Clear points
        self.points.clear()
        
        #Clear results
        self.clearResults()
        
        #Repaint screen
        self.repaint()
        
        
    def clearResults(self):
        #Clear DT
        self.dt.clear()
        
        #Clear contours
        self.contours.clear()
        self.boldContours.clear()

        #Clear slope
        self.dtm_slope.clear()
        
        #Clear aspect
        self.dtm_aspect.clear()
        
        #Repaint screen
        self.repaint()      
    
    
    def setDT(self, dt: list[Edge]):
        self.dt = dt
        
    def setContours(self, contours: list[Edge], bold_contours: list[Edge]):
        self.contours = contours
        self.boldContours = bold_contours
        
    def setDTMAspect(self, dtm_aspect: list[Triangle]):
        self.dtm_aspect = dtm_aspect    
        
    def setDTMSlope(self, dtm_slope: list[Triangle]):
        self.dtm_slope = dtm_slope
    
    def setViewDT(self, viewDT):
        self.viewDT = viewDT
        
    def setViewContourLines(self, viewContourLines):
        self.viewContourLines = viewContourLines
        
    def setViewSlope(self, viewSlope):
        self.viewSlope = viewSlope
        
    def setViewAspect(self, viewAspect):
        self.viewAspect = viewAspect