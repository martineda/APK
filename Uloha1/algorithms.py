from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import math as m

class Algorithms:
    
    def __init__(self):
        pass
    
    def polygonFilter(self, q: QPointF, pol: QPolygonF):
        
        #Get min/max coordinates
        x_min = min(pol, key = lambda k: k.x()).x()
        x_max = max(pol, key = lambda k: k.x()).x()
        y_min = min(pol, key = lambda k: k.y()).y()
        y_max = max(pol, key = lambda k: k.y()).y()
        
        #Is q inside min/max box?
        if x_min <= q.x() <= x_max and y_min <= q.y() <= y_max:
            return 1    
        
        return 0

    
    def rayCrossing(self, q:QPointF, pol:QPolygonF):
        
        #Quick filter through min/max boxes
        mmb = self.polygonFilter(q, pol)
        if mmb == 0:
            return 0
        
        #Inicialize amount of intersections
        k_right = 0
        k_left = 0
        
        #Amount of vertices
        n = len(pol)
        
        #Process all segments
        for i in range(n):
            
            #Does point lie on vertex?
            if q.x() == pol[i].x() and q.y() == pol[i].y():
                return 2
            
            #Reduce coordinates
            xir = pol[i].x() - q.x()
            yir = pol[i].y() - q.y()
            
            xi1r = pol[(i+1)%n].x() - q.x()
            yi1r = pol[(i+1)%n].y() - q.y()
            
            #Suitable segment?
            if ((yi1r > 0) and (yir <= 0)) or ((yir > 0) and (yi1r <= 0)):
               
                #Compute intersection
                xm = (xi1r * yir - xir * yi1r)/(yi1r - yir)
               
                #Right half plane
                if xm > 0:       
                   k_right += 1  
                
                #Left half plane
                if xm < 0:
                    k_left += 1 
                   
        #Point q on edge
        if (k_right % 2) != (k_left % 2):
            return 2
        
        #Point q inside polygon?
        if k_right%2 == 1:
            return 1
        
        #Point q outside polygon
        return 0
    
    def windingNumber(self, q:QPointF, pol: QPolygonF):
        
        #Quick filter through min/max boxes
        mmb = self.polygonFilter(q, pol)
        if mmb == 0:
            return 0
        
        #Initialize total angle (omega) and tolerance (e)
        omega = 0
        e = 0.0000001
        
        #Amount of vertices 
        n = len(pol)
        
        for i in range(n):
            
            #Calculate vectors and determinant       
            u = pol[i].x() - q.x(), pol[i].y() - q.y()
            v = pol[(i+1)%n].x() - q.x(), pol[(i+1)%n].y() - q.y()
            
            det = u[0] * v[1] - u[1] * v[0]
            
            #Points in line, check if on edge/vertex
            if det ==0:
                x_min = min(pol[i].x(), pol[(i+1)%n].x())
                y_min = min(pol[i].y(), pol[(i+1)%n].y())
                x_max = max(pol[i].x(), pol[(i+1)%n].x())
                y_max = max(pol[i].y(), pol[(i+1)%n].y())
                if (x_min <= q.x() <= x_max) and (y_min <= q.y() <= y_max):
                    return 2
            
            #Calculate angle
            u_v_dot = u[0] * v[0] + u[1] * v[1]
            u_v_dis = m.sqrt(u[0]**2 + u[1]**2) * m.sqrt(v[0]**2 + v[1]**2)
            
            #Prevent division by zero, point on vertex
            if u_v_dis == 0:
                return 2
            
            w_raw = u_v_dot/u_v_dis
            
            #Acos is limited to <-1, 1>
            w_cor = min(max(-1, w_raw), 1)

            w = abs(m.acos(w_cor))
            
            #Add or subtract angle?
            if det > 0:
                omega += w
            if det < 0:
                omega -= w
                
        #Is point in or out?        
        if abs(abs(omega) - 2 * m.pi) < e:
            return 1
        
        return 0