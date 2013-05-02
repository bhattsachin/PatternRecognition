'''
Created on Feb 14, 2013

@author: bhatt
'''

import numpy
import matplotlib.pyplot as plt


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
        w = self.batchPerceptron(fulldata, 0.01,inita )
        
        
        
        print "class1:" + str(fulldata)
        return w #weight vector
        
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
        return a
        
        
    
    def plotWVector(self,a,b=None,m=None):
        ''' In the current axes, plot the weight vector. 
         
            a is the weight vector, b is the bias term
            m is the margin
        '''
    
        # O is some arbitrary point on the line, say where x=0
        O = numpy.zeros(2) 
        if b is not None:
            O[1] = -b/a[1]
    
        an = a / numpy.linalg.norm(a)
        #V = O + 50*an
        #U = O + -50*an
    
        #plt.plot([O[0],U[0]],[O[1],U[1]],'b',linewidth=3.0)
        #plt.plot([O[0],V[0]],[O[1],V[1]],'r',linewidth=3.0)
    
        anr = numpy.asarray([an[1],-an[0]])
    
        A = O + 3*anr;
        B = O + -3*anr;
        plt.plot([A[0],B[0]],[A[1],B[1]],'k',linewidth=3.0)
    
        if m is not None and numpy.isscalar(m):
            Ob = O - m*an
            Ab = Ob + 50*anr;
            Bb = Ob + -50*anr;
            plt.plot([Ab[0],Bb[0]],[Ab[1],Bb[1]],'k-',linewidth=1.0)
    
            Ob = O + m*an
            Ab = Ob + 50*anr;
            Bb = Ob + -50*anr;
            plt.plot([Ab[0],Bb[0]],[Ab[1],Bb[1]],'k-',linewidth=1.0)

        
        
        
        
        
        