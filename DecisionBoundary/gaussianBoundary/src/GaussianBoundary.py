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
        [nrow, ncol] = data.shape
        result = numpy.zeros(ncol)
      
        for idx,row in enumerate(data):
            for idy, col in enumerate(row):
                result[idy] = result[idy] + row[idy]
                
        a = [b/nrow for b in result]
        return a