'''
Created on Feb 3, 2013

@author: bhatt
'''

import numpy
import math
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
    
    
    def computeCovariance(self, data):
        ''' finds covariance in data
        '''
        mean = self.computeMean(data)
        #print str(mean[first])
        [nrow, ncol] = data.shape
        #meanResult = numpy.array([[mean[first], mean[second]],[mean[first], mean[second]]])
        result = numpy.zeros((ncol, ncol))
        
        for i in range(ncol):
            for j in range(ncol):
                sum = 0
                for idx, row in enumerate(data):
                    sum = sum + (row[i]-mean[i])*(row[j]-mean[j])
                
                result[i][j] = sum/(nrow-1)
                
        return result;
    
    
    def computeDecisionBoundary(self, data1, data2):
        '''
        '''
        g1 = self.computeDiscriminat(data1)
        g2 = self.computeDiscriminat(data2)
        g0 = numpy.subtract(g1, g2)
        return g0
        
    def computeDiscriminat(self, data):
        ''' assuming data is gaussian
        '''
        mean = self.computeMean(data)
        cov = self.computeCovariance(data)
        [nrow, ncol] = data.shape
        
        subs = numpy.subtract(data, mean)
        
        icov = numpy.linalg.inv(cov)
        prod1 = numpy.dot(subs, icov)
        
        prod2 = numpy.dot(prod1, subs.conj().T)
        #pi component
        pivalue = (ncol/2)*numpy.log(2*math.pi)
        #determinant part
        detvalue = (0.5)*numpy.log(numpy.linalg.det(cov))
        discrimin = numpy.subtract(numpy.subtract(prod2, pivalue), detvalue)
        
        return discrimin
        
        
        
        
        
        