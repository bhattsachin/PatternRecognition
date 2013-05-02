'''
Created on Feb 14, 2013

@author: bhatt
'''
import unittest
from linearDiscriminant.src import LinearDiscriminant
import numpy
import matplotlib.pyplot as plt


class Test(unittest.TestCase):


    def testLDTest(self):
        
        ld = LinearDiscriminant.LinearDiscriminant()
        
        
        
        class1 = numpy.array( [[1, 0.75], [0, 0.5], [0, 1]] )
        class2 = numpy.array( [[-1, -1], [0.5, -0.25], [0, -0.5]] )
        
        
        ld.classify(class1, class2)
        
        
        pass
    
    def testPlot(self):
        
        ld = LinearDiscriminant.LinearDiscriminant()
        
        class1 = numpy.array( [[1, 0.75], [0, 0.5], [0, 1]] )
        class2 = numpy.array( [[-1, -1], [0.5, -0.25], [0, -0.5]] )
        plt.plot(class1[:,0], class1[:,1], 'ro')
        plt.plot(class2[:,0], class2[:,1], 'bx')
        
        plt.axis([-2, 2, -2, 2])
        
        w = ld.classify(class1, class2)
        ld.plotWVector(w[0,1:3], w[0,0])
        plt.show()
        pass
    
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLDTest']
    unittest.main()