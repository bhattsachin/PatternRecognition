'''
Created on Feb 3, 2013

@author: bhatt
'''
import unittest
import numpy
from array import array
from gaussianBoundary.src import GaussianBoundary



class TwoDimensional(unittest.TestCase):


    def testName(self):
        
        #class1 = numpy.zeros((6,2))
        class1 = numpy.array( [[0, 0], [0, 1], [2, 2], [3, 1], [3, 2], [3, 3]] )
        
        gauss = GaussianBoundary.GaussianBoundary()
        priorOfClass1 = gauss.computePrior(class1)
        print "class1: " + str(priorOfClass1)
        
        class2 = numpy.array( [[6, 9], [8, 9], [9, 8], [9, 9], [9, 10], [8, 11]] )
        
        priorOfClass2 = gauss.computePrior(class2)
        print "class2: " + str(priorOfClass2)
        
        pass
    
    def testCov(self):
        class1 = numpy.array( [[0, 0], [0, 1], [2, 2], [3, 1], [3, 2], [3, 3]] )
        
        gauss = GaussianBoundary.GaussianBoundary()
        covClass1 = gauss.computeCovariance(class1, 0, 1)
        print "class1 covariance : " + str(covClass1)
        
        
        
        pass
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'TwoDimensional.testName']
    unittest.main()