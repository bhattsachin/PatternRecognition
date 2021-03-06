'''
Created on Apr 7, 2013

@author: bhatt
'''
import sys, math
import numpy
from adaboost.src import Classifier

class Adaboost(Classifier):
    def __init__(self, weak_classifier_type):
        Classifier.Classifier.__init__(self)
        self.WeakClassifierType = weak_classifier_type

    def train(self, T, k = 1):
        X = self.X
        Y = numpy.array(self.Y)
        N = len(self.Y)
        w = (1.0/N)*numpy.ones(N)
        self.weak_classifier_ensemble = []
        self.alpha = []
        for t in range(T):
            sys.stdout.write('.')
            weak_learner = self.WeakClassifierType()
            weak_learner.set_training_sample(X,Y)
            weak_learner.weights = w
            weak_learner.train()
            Y_pred = weak_learner.predict(X)
            # (Y=-1, Y_pred=1) False Positive
            # (Y=1, Y_pred=-1) Missing  should be assigned more weights
            #ww = numpy.log(k)*(numpy.exp( (Y-Y_pred)>1 ) - 1)/(numpy.exp(1)-1) + 1
            e = sum(0.5*w*abs((Y-Y_pred)))/sum(w)
            #e = sum(0.5*w*abs(Y-Y_pred))
            ee = (1-e)/(e*1.0)
            alpha = 0.5*math.log(ee+0.00001)
            w *= numpy.exp(-alpha*Y*Y_pred) #*ww) # increase weights for wrongly classified
            w /= sum(w)
            self.weak_classifier_ensemble.append(weak_learner)
            self.alpha.append(alpha)
        print "\n"
        self.T = T

    def predict(self,X):
        X = numpy.array(X)
        N, d = X.shape
        Y = numpy.zeros(N)
        for t in range(self.T):
            #sys.stdout.write('.')
            weak_learner = self.weak_classifier_ensemble[t]
            #print Y.shape, self.alpha[t], weak_learner.predict(X).shape
            Y += self.alpha[t]*weak_learner.predict(X)
        return Y

    def test_on_training_set(self, X, Y, T):
        self.set_training_sample(X,Y)
        self.train(T)
        o = self.predict(X)
        return o

    def measure_accuracy(self, Y, o, threshold=0):
        oo = o.copy()
        oo[numpy.where(o>threshold)[0]] = 1
        oo[numpy.where(o<threshold)[0]] = -1
        d = (oo - Y)
        return len(d[numpy.where(d==0)[0]])*1.0/len(Y)
        