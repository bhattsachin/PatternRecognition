'''
Created on Feb 3, 2013

@author: bhatt
'''

import numpy

class GaussianBoundary(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def computePrior(self, data):
        ''' Assuming data is not more than 2 dimension
        '''
        return self.computeMean(data)
    
    def computeMean(self, data):
        [nrow, ncol] = data.shape
        result = numpy.zeros(ncol)
      
        for idx,row in enumerate(data):
            for idy, col in enumerate(row):
                result[idy] = result[idy] + row[idy]
                
        a = [b/nrow for b in result]
        return a
    
    
    def computeCovariance(self, data, first, second):
        ''' finds covariance in data for features indexed at first and second
        '''
        mean = self.computeMean(data);
        print "is this fine:" + str(mean)
        print str(mean[first])
        [nrow, ncol] = data.shape
        meanResult = numpy.array([[mean[first], mean[second]],[mean[first], mean[second]]])
        result = numpy.zeros((2, 2))
        
        for i in range(1):
            for j in range(1):
                sum = 0
                for idx, row in enumerate(data):
                    sum = sum + (row[first]-meanResult[i])*(row[second]-meanResult[j])
                
                result[i][j] = sum/(nrow-1)
                
        
        print "cov: " + str(result)
        
        
        