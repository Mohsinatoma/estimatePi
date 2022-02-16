# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 17:51:35 2022

@author: Mohoshina Toma
"""

import distanceBetweenPoints
import numpy as np
import scipy.stats as st

def estimate_pi(n_points):
    """
    input: number of points to be generated
    output: estimated pi through the simulation
    
     Author's note:
        The center of the circle does not affect the original distance while estimating the value of
        pi using Monte Carlo Simulation. 
        Let's the center point is (2,3)
        then, when we generate random points using [-1,1], we have to add the value of the 
        center coordinates with the coordinates of randomly generated points.
        
        So, the formula of original distance will be:
            distance = ((randomly generated X-coordinate + X- coordinate of center)- X- coordinate of center)**2
                       +((randomly generated Y-coordinate + Y- coordinate of center)- Y- coordinate of center)**2
       
        finally, 
            distance = ((randomly generated X-coordinate)**2 +((randomly generated Y-coordinate)**2
    """

    insidePoint= 0
   # print(centeroftheCircle)
    
    
    for i in range(n_points):
        # assume the center of the circule (0,0)
        p1= distanceBetweenPoints.Point((0,0))
        #print(p1.__repr__());
        p2= distanceBetweenPoints.Point()
        #print(p2.__repr__());
        distance = p2.distance(p1)
        if distance<= 1.00:
           insidePoint+= 1     

    pi = 4* (insidePoint / n_points)
    return pi


# estimate pi for 100 iterations

def estimateConfidenceInterval(n_iter,totalSamplePoints):
    pi = np.zeros(int(n_iter))
    for i in range(int(n_iter)):
        pi[i] = estimate_pi(int(totalSamplePoints))
    t= st.norm.interval(alpha=0.95, loc=np.mean(pi), scale=st.sem(pi))
    print(t)



noofIter = input("Enter the number of iteration:\n") 
noofPoints = input("Enter the total sample size:\n") 
#centeroftheCircle = input("enter Center of the Circle:\n") 
#centeroftheCircle = tuple(int(x.strip()) for x in centeroftheCircle.split(','))
estimateConfidenceInterval(noofIter,noofPoints)
