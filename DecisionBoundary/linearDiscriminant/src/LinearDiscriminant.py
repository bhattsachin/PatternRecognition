'''
Created on Feb 14, 2013

@author: bhatt
'''

import numpy

class LinearDiscriminant(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def classify(self, class1, class2):
        ''' Two class classifier
        '''
        class1 = self.augment(class1)
        class2 = self.augment(class2)
        
        negate = class2*-1
        
        fulldata = numpy.concatenate((class1, negate))
        inita = numpy.array( [[0, -0.5, 0.5]])
        self.batchPerceptron(fulldata, 0.01,inita )
        
        
        
        print "class1:" + str(fulldata)
        
    def augment(self, data):
        [nrow, ncol] = data.shape
        tmp = numpy.ones((nrow, 1), int)
        #add regularization term
        data = numpy.concatenate((tmp, data), axis=1)
        return data
    
    
    def batchPerceptron(self, data, scale, inita):
        [nrow, ncol] = data.shape
       
        
        a = inita
        b = 1
        
        while b==1:
            print "a:" + str(a)
            print "data:" + str(data)
            gx = numpy.dot(data, numpy.transpose(a))
            misclassify = numpy.zeros( (1, ncol) )
            b=0
            print "gx:" + str(gx)
            for idx, row in enumerate(gx):
                if row[0] <= 0: #as this is single dimensional
                    misclassify = misclassify + data[idx]
                    b=1
            
            a = a + scale*misclassify
            print "misclassify: " + str(misclassify)
        
            
        
        print "gx: " + str(a)
        
        
        
        
        
        