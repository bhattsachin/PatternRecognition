'''
Created on Apr 7, 2013

@author: bhatt
'''
import unittest
import random
import numpy


class Test(unittest.TestCase):


    def testName(self):
        pass
    
    
    
    def shuffle(self,ary):
        a = len(ary)
        b = a-1
        for d in range(b,0,-1):
            e = random.randint(0,d)
            if e == d:
                continue
            ary[d],ary[e] = ary[e],ary[d]
        return ary

    def test_build_stump_1d(self):
        x = [0, 1, 2, 4]
        y = [-1, -1, 1, 1]
        w = [0.25, 0.25, 0.25, 0.25]
        stump = DecisionStump.build_stump_1d(x, y, w)
        assert(stump.threshold == 1.5)
        assert(stump.s == 1)
        assert(stump.err == 0)
        x = [0, 1, 2, 4]
        y = [1, 1, -1, -1]
        stump = decisionStump.build_stump_1d(x, y, w)
        assert(stump.threshold == 1.5)
        assert(stump.s == -1)
        assert(stump.err == 0)

    def test_build_stump_1d_shuffle(self):
        N = 100
        x = numpy.random.rand(N)
        y = numpy.random.rand(N)
        y[numpy.where(y < 0.5)] = -1
        y[numpy.where(y > 0.5)] = 1
        w = numpy.ones(N)/N
        stump = DecisionStump.build_stump_1d(x, y, w)
        ind = self.shuffle(range(0, N))
        stump_shuffled = decisionStump.build_stump_1d(x[ind], y[ind], w[ind])
        assert(stump == stump_shuffled)
        ind = self.shuffle(range(0, N))
        yy = y.copy()
        for i in range(N):
            yy[i] = -y[ind[i]]
        stump_shuffled = decisionStump.build_stump_1d(x[ind], yy, w[ind])
        assert(stump.err == stump_shuffled.err)
        assert(stump.threshold == stump_shuffled.threshold)
        assert(stump.s == -1.0*stump_shuffled.s)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()