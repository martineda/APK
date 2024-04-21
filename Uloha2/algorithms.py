from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import math as m
from numpy import *
from scipy.linalg import *

#Processing data
class Algorithms:
    
    def __init__(self):
        pass
    
    def getTwoLineAngle(self, p1: QPointF, p2: QPointF, p3: QPointF, p4: QPointF):
        
        #Get two line angle
        ux = p2.x() - p1.x()
        uy = p2.y() - p1.y()
        
        vx = p4.x() - p3.x()
        vy = p4.y() - p3.y()
        
        #Dot product
        dot = ux * vx + uy * vy
        
        #Norms 
        nu = (ux**2 + uy**2)**(1/2)
        nv = (vx**2 + vy**2)**(1/2)
        
        #Prevent division by zero error
        if nu == 0 or nv == 0:
            return 0
        
        #Correct interval        
        arg = dot/(nu*nv)
        
        return m.acos(max(min(arg, 1), -1))
    
    def cHull(self, pol: QPolygonF):
        
        #Construct Convex Hull (Jarvis)
        ch = QPolygonF()
        
        #Find first pivot
        q = min(pol, key = lambda k: k.y())
        
        #Find second pivot
        s = min(pol, key = lambda k: k.x())
        
        #Initialize last two points of CH
        qj = q
        qj1 = QPointF(s.x(), q.y()) #Zkusme bez závorek
        
        #Append pivot to CH
        ch.append(q) 
        
        #Find all points of CH
        while True:
            #Initialize angle and index
            omega_max = 0.0
            index_max = -1
            
            #Process all points
            for i in range(len(pol)):
                
                #Compute angle
                if qj != pol[i]:
                    omega = self.getTwoLineAngle(qj, qj1, qj, pol[i])
                    
                    #Update max
                    if omega > omega_max:
                        omega_max = omega
                        index_max = i
                    
            #Add vertex to CH            
            ch.append(pol[index_max])
            
            #Is CH already closed?
            if q == pol[index_max]:
                break
        
            #Update last segment
            qj1 = qj
            qj = pol[index_max]
            
        return ch
    
    def minmaxBox(self, pol:QPolygonF):
        
        #Find coordinates of min/max box
        x_min = min(pol, key = lambda k: k.x()).x()
        x_max = max(pol, key = lambda k: k.x()).x()
        y_min = min(pol, key = lambda k: k.y()).y()
        y_max = max(pol, key = lambda k: k.y()).y()

        v1 = QPointF(x_min, y_min)
        v2 = QPointF(x_max, y_min)
        v3 = QPointF(x_max, y_max)
        v4 = QPointF(x_min, y_max)
        box = QPolygonF([v1, v2, v3, v4])
        
        return box
    
    def rotate(self, pol: QPolygonF, sig:float):
        
        #Rotate polygon
        pol_r = QPolygonF()
        
        #Process all points
        for p in pol:
            
            #Rotate point
            x_r = p.x() * m.cos(sig) - m.sin(sig) * p.y()
            y_r = p.x() * m.sin(sig) + m.cos(sig) * p.y()
            
            #Add point to polygon
            p_r = QPointF(x_r, y_r)
            pol_r.append(p_r)
            
        return pol_r
    
    def getArea(self, pol : QPolygonF):
        
        #Return polygon area
        area = 0
        n = len(pol)  
          
        #Proccesing of vertexes
        for i in range(n):
            area = area + pol[i].x() * (pol[(i+1)%n].y() - pol[(i-1+n)%n].y())
            
        return abs(area)/2
    
    
    def resizeRectangle(self, rect: QPolygonF, build: QPolygonF):
        
        #Compute areas
        Ab = self.getArea(build)
        A = self.getArea(rect)

        # Compute ratio
        if A != 0:
            k = Ab / A

        #Problémové budovy (díry?)
        else:
            return None
        
        #Center of mass
        tx = (rect[0].x() + rect[1].x() + rect[2].x() + rect[3].x()) / 4
        ty = (rect[0].y() + rect[1].y() + rect[2].y() + rect[3].y()) / 4
        
        #Vectors 
        u1x = rect[0].x() - tx
        u1y = rect[0].y() - ty
        u2x = rect[1].x() - tx
        u2y = rect[1].y() - ty
        u3x = rect[2].x() - tx
        u3y = rect[2].y() - ty
        u4x = rect[3].x() - tx
        u4y = rect[3].y() - ty
        
        #New vertices
        v1x = tx + m.sqrt(k) * u1x
        v1y = ty + m.sqrt(k) * u1y
        v2x = tx + m.sqrt(k) * u2x
        v2y = ty + m.sqrt(k) * u2y
        v3x = tx + m.sqrt(k) * u3x
        v3y = ty + m.sqrt(k) * u3y
        v4x = tx + m.sqrt(k) * u4x
        v4y = ty + m.sqrt(k) * u4y
        
        v1 = QPointF(v1x, v1y)
        v2 = QPointF(v2x, v2y)
        v3 = QPointF(v3x, v3y)
        v4 = QPointF(v4x, v4y)
        
        #Add vertices to polygon
        rectR = QPolygonF([v1, v2, v3, v4])
        
        return rectR
    
    
    def mbr(self, pol : QPolygonF):  
    
        #Compute convex hull
        ch = self.cHull(pol)
        
        #Initialization
        mmb_min = self.minmaxBox(ch)
        area_min = self.getArea(mmb_min)
        sigma_min = 0
        
        #Process all segments of CH
        n = len(ch)
        for i in range(n):
            #Coordinate differences
            dx = ch[(i+1)%n].x() - ch[i].x()
            dy = ch[(i+1)%n].y() - ch[i].y()
            
            #Direction
            sigma = m.atan2(dy, dx)
            
            #Rotate convex hull by -sigma
            ch_rot = self.rotate(ch, -sigma)
            
            #Find mmb and its area
            mmb_rot = self.minmaxBox(ch_rot)
            area_rot = self.getArea(mmb_rot)
            
            #Is it a better approximation?
            if area_rot < area_min:
                mmb_min = mmb_rot
                area_min = area_rot
                sigma_min = sigma
        
        #Back rotation
        mmb_unrot = self.rotate(mmb_min, sigma_min)
        
        #Resize rectangle
        mmb_res = self.resizeRectangle(mmb_unrot, pol)
        if mmb_res == None:
            return None
        
        return mmb_res   


    def createERPCA(self, pol: QPolygonF):
        
        #Create enclosing rectangle using PCA
        x = []
        y = []
        
        #List coordinates of vertexes
        for i in pol:
            x.append(i.x())
            y.append(i.y())
            
        #Create array
        P = array([x, y])
        
        #Compute covariation matrix
        C = cov(P)
        
        #Singular value decomposition
        [U, S, V] = svd(C)
        
        #Compute sigma
        sigma = m.atan2(U[0][1], U[0][0])
        
        #Rotate polygon and get min/max box + rotate back
        pol_unrot = self.rotate(pol, -sigma)
        mmb = self.minmaxBox(pol_unrot)
        er = self.rotate(mmb, sigma)
        
        #Resize enclosing rectangle
        resized_er = self.resizeRectangle(er, pol)
        
        return resized_er
    
    def longestEdge(self, pol: QPolygonF):
        
        #Find longest edge
        edge_longest = 0
        n = len(pol)

        for i in range(n):
            #Calculate length of edge
            dx = pol[(i+1)%n].x() - pol[i].x()
            dy = pol[(i+1)%n].y() - pol[i].y()
            edge_length = m.sqrt(dx**2 + dy**2)
            
            #Update angle with longer edge
            if edge_length > edge_longest:
                edge_longest = edge_length
                sigma = m.atan2(dy, dx)
        
        #Rotate polygon and get min/max box + rotate back        
        pol_unrot = self.rotate(pol, -sigma)
        mmb = self.minmaxBox(pol_unrot)
        er = self.rotate(mmb, sigma)
        
        #Resize enclosing rectangle
        resized_er = self.resizeRectangle(er, pol)
        
        return resized_er
    
    def wallAverage(self, pol: QPolygonF):
        
        #Initiate angle
        dx_0 = pol[1].x() - pol[0].x()
        dy_0 = pol[1].x() - pol[0].x()
        sigma_0 = m.atan2(dy_0, dx_0)
        
        #Process all edges
        n = len(pol)
        r_average = 0
        
        for i in range(n):
            #Calculate angle (sigma)
            dx = pol[(i+1)%n].x() - pol[i].x()
            dy = pol[(i+1)%n].y() - pol[i].y()
            sigma = m.atan2(dy, dx)
            
            #Calcualte inner angle (omega)
            omega = abs(sigma - sigma_0)
                
            #Fragment
            k = 2*omega/pi
            
            #Oriented residue
            r = (omega - k)*pi/2
            
            #Get residue average
            r_average += r
        
        #Get average angle
        sigma_average = r_average/n + sigma_0
            
        #Rotate polygon and get min/max box + rotate back        
        pol_unrot = self.rotate(pol, -sigma_average)
        mmb = self.minmaxBox(pol_unrot)
        er = self.rotate(mmb, sigma_average)
        
        #Resize enclosing rectangle
        resized_er = self.resizeRectangle(er, pol)
        
        return resized_er
    
    def weightedBisector(self, pol: QPolygonF):
        
        #Construct convex hull
        ch = self.cHull(pol)
        
        #Exclude polygons with less than 4 vertexes
        if len(ch) < 5:
            return None
        
        #Initiate diagonals and its points
        diag_1 = 0
        start_1 = QPointF(ch[0].x(), ch[0].y())
        end_1 = QPointF(ch[1].x(), ch[1].y())
        
        diag_2 = 0
        start_2 = QPointF(ch[1].x(), ch[1].y())
        end_2 = QPointF(ch[2].x(), ch[2].y())
        
        #Loop through all points
        n = len(ch)
        for i in range(n):
            
            #Calculate edge between all points
            for j in range(n):
                
                #Exclude self
                if ch[i] == ch[j]:
                    continue
                
                #Prevent start_1 = end_1 and vice versa
                if ch[j] == start_1:
                    break
                
                #Calculate distance
                dx = ch[j].x() - ch[i].x()
                dy = ch[j].y() - ch[i].y()
                potential_diag = m.sqrt(dx**2 + dy**2)
            
                #Update longest diagonals
                if potential_diag > diag_1:
                    diag_2 = diag_1
                    start_2 = start_1
                    end_2 = end_1
                    diag_1 = potential_diag
                    start_1 = ch[i]
                    end_1 = ch[j]
                elif potential_diag > diag_2:
                    diag_2 = potential_diag
                    start_2 = ch[i]
                    end_2 = ch[j]
        
        #Compute angles            
        dx_1 = end_1.x() - start_1.x()
        dy_1 = end_1.y() - start_1.y()
            
        dx_2 = end_2.x() - start_2.x()
        dy_2 = end_2.y() - start_2.y()

        sigma_1 = m.atan2(dy_1, dx_1)
        sigma_2 = m.atan2(dy_2, dx_2)
        
        #Angle of diagonal axis
        sigma = (diag_1 * sigma_1 + diag_2 * sigma_2) / (diag_1 + diag_2)
        
        #Rotate polygon and get min/max box + rotate back        
        pol_unrot = self.rotate(pol, -sigma)
        mmb = self.minmaxBox(pol_unrot)
        er = self.rotate(mmb, sigma)
        
        #Resize enclosing rectangle
        resized_er = self.resizeRectangle(er, pol)
        
        return resized_er