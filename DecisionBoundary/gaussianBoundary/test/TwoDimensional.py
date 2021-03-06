'''
Created on Feb 3, 2013

@author: bhatt
'''
import unittest
import numpy
from array import array
from gaussianBoundary.src import GaussianBoundary
from pylab import *
import matplotlib.pyplot as plt




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
        covClass1 = gauss.computeCovariance(class1)
        print "class1 covariance : " + str(covClass1)
        
        class2 = numpy.array( [[6, 9], [8, 9], [9, 8], [9, 9], [9, 10], [8, 11]] )
        covClass2 = gauss.computeCovariance(class2)
        print "class2 covariance : " + str(covClass2)
        
        
        pass
    
    def testDiscriminant(self):
        class1 = numpy.array( [[0, 0], [0, 1], [2, 2], [3, 1], [3, 2], [3, 3]] )
        
        gauss = GaussianBoundary.GaussianBoundary()
        gauss.computeDiscriminat(class1)
        pass
    
    def testDecisionBoundary(self):
        class1 = numpy.array( [[0, 0], [0, 1], [2, 2], [3, 1], [3, 2], [3, 3]] )
        class2 = numpy.array( [[6, 9], [8, 9], [9, 8], [9, 9], [9, 10], [8, 11]] )
       
        
        gauss = GaussianBoundary.GaussianBoundary()
        
        g0 = gauss.computeDecisionBoundary(class1, class2)
        
        print "final:" + str(g0)
        plt.plot(g0)
        plt.show()
        
        
        pass
    
    def testMatplotlib(self):
        
        X = numpy.linspace(-numpy.pi, numpy.pi, 256,endpoint=True)
        C,S = numpy.cos(X), numpy.sin(X)
        
        plt.plot(X,C)
        plt.plot(X,S)
        
        #plt.show()
        
        
        pass
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'TwoDimensional.testName']
    unittest.main()