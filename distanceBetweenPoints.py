
# -*- coding: utf-8 -*-
"""
Created on Web Feb 16 12:54:24 2022

@author: Mohoshina Toma
"""


import random as r
import math as m


class Point():
    """
    A point in a 2D (xy) space
    properties:
        x: float, x-coordinate
        y: float, y-coordinate
    """


    def __init__(self, xy=None):
        """
        Constructor
        If xy is not provided, randomly generate xy coordiantes.
        Otherwise, xy can be assigned by a tuple (e.g., (2, 3))
        """

        
        # properties
        self.x = None
        self.y = None
        
        # assign values to x and y
        if xy is None:
            self.x= r.uniform(-1, 1)
            self.y= r.uniform(-1, 1)
         
        else:
            
            self.x= xy[0]
            self.y= xy[1]  
       

    def __repr__(self):
        """
        Allow the xy-coordinates to be printed when the point is called
        """
        return "Point: %.2f, %.2f" % (self.x, self.y)

    def distance(self,point):
        """
        input: a Point() object
        output: Euclidean distance between self point and the input point
        
        """
        originDistance= m.sqrt(((self.x - point.x)**2) + ((self.y - point.y) ** 2))
        return originDistance


    






