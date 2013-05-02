'''
Created on Apr 7, 2013

'''
import math
import numpy
import operator

from adaboost.src.Classifier import *

class DecisionStump(object):
    def __init__(self):
        Classifier.__init__(self)

    def train(self):
        X = self.X
        Y = self.Y
        w = self.weights
    
        feature_index, stump = self.train_decision_stump(X,Y,w)
        self.feature_index = feature_index
        self.stump = stump
    
    def predict(self,X):
        N, d = X.shape
        feature_index = self.feature_index
        threshold = self.stump.threshold
        s = self.stump.s
    
        Y = numpy.ones(N)
        Y[numpy.where(X[:,feature_index]<threshold)[0]] = -1 * s
        Y[numpy.where(X[:,feature_index]>=threshold)[0]] = 1 * s
        return Y
    
    
    class Stump:
        """1D stump"""
        def __init__(self, err, threshold, s):
            self.err = err
            self.threshold = threshold
            self.s = s
    
        def __cmp__(self, other):
            return cmp(self.err, other.err)
        
    
        def train_decision_stump(self,X,Y,w):
            stumps = [self.build_stump_1d(x,Y,w) for x in X.T]
            feature_index, best_stump = min(enumerate(stumps), key=operator.itemgetter(1))
            best_threshold = best_stump.threshold
            return feature_index, best_stump
    
    
        def build_stump_1d(self, x,y,w):
            sorted_xyw = numpy.array(sorted(zip(x,y,w), key=operator.itemgetter(0)))
            xsorted = sorted_xyw[:,0]
            wy = sorted_xyw[:,1]*sorted_xyw[:,2]
            score_left = numpy.cumsum(wy)
            score_right = numpy.cumsum(wy[::-1])
            score = -score_left[0:-1:1] + score_right[-1:0:-1]
            Idec = numpy.where(xsorted[:-1]<xsorted[1:])[0]
            if len(Idec)>0:  # determine the boundary
                ind, maxscore = max(zip(Idec,abs(score[Idec])),key=operator.itemgetter(1))
                err = 0.5-0.5*maxscore # compute weighted error
                threshold = (xsorted[ind] + xsorted[ind+1])/2 # threshold
                s = numpy.sign(score[ind]) # direction of -1 -> 1 change
            else:  # all identical; todo: add random noise?
                err = 0.5
                threshold = 0
                s = 1
            return self(err, threshold, s)
        