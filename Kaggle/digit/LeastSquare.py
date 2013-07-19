import LeastSquare
import csv
import numpy


class LeastSquare(object):

    def __init__(self):
        pass
        
    def readFile(self, filename):
        with open( filename ) as infile:
            readfile = csv.reader(infile)
            #ignore the header
            next(readfile, None)
            rowelement = list(readfile)
            row = len(rowelement)
            col = len(rowelement[0])
            print str(row) + '  ' + str(col)
            X = numpy.zeros(shape=(row, col))
            X = rowelement[1:]
            #target matrix 
            T = numpy.zeros(shape=(row,10))
            for i in range(len(rowelement)-1): 
                T[i][int(rowelement[i][0])] = 1.0
                #T[i][rowelement[i][0]] = 1.0
                X[i] = [int(k) for k in rowelement[i][1:]]
                #print T[i]
                #print X[1]
        return X, T
    
    """
        Compute pseudo inverse
    """
        
    def computeW(self, X, T):
        W = numpy.dot(numpy.transpose(X), X)
        W = W.I
        print W
        pass        
        
    def main():
        print "all is ok till here"
        obj = LeastSquare.LeastSquare()
        X, T = obj.readFile('/home/ubuntu/Downloads/smalltrain.csv')
        obj.computeW(X,T)
        #sys.exit(main())
    
    if __name__ == '__main__':main()
       
    
    
