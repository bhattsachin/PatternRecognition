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
            
            xValidateSize = int(row/5)
            XVALIDATE = numpy.zeros(shape=(xValidateSize, col))
            print str(row) + '  ' + str(col)
            X = numpy.zeros(shape=(row-xValidateSize, col-1))
            #X = rowelement[1:]
            #target matrix 
            T = numpy.zeros(shape=(row - xValidateSize,10))
            for i in range(len(rowelement)-1): 
            
                if i < (row - xValidateSize):
                    T[i][int(rowelement[i][0])] = 1.0
                    #T[i][rowelement[i][0]] = 1.0
                    X[i] = [int(k) for k in rowelement[i][1:]]
                
                else:
                    XVALIDATE[row-(i+1)] = [int(k) for k in rowelement[i]] #in reverse order
                
               
                #print T[i]
                #print X[1]
        return X, T, XVALIDATE
    
    """
        Compute pseudo inverse
    """
        
    def computeW(self, X, T):
        W = numpy.dot(numpy.linalg.pinv(X), T)
        return W
        
    def validate(self, XVALIDATE, W):
        rows = len(XVALIDATE)
        X = numpy.zeros(shape=(rows, len(XVALIDATE[0])-1))
        
        X = XVALIDATE[:,1:]
        Y = numpy.dot(X, W)
        Z = Y.argmax(axis=1)
        #print XVALIDATE[:,0]
        R = numpy.zeros(shape=(rows,1))
        for i in range(rows):
            if (int(XVALIDATE[i][0]) == Z[i]):
                R[i] = 1
            #R[i] = (
            #print str(int(XVALIDATE[i][0])) + " == " + str(Z[i])
        CORRECT = numpy.sum(R, axis=0)[0]
        print "success : " + str(CORRECT) +  "/" + str(rows) + " Rate:" + str((CORRECT/rows)*100) + "%"
    
        pass       
        
    def main():
        obj = LeastSquare.LeastSquare()
        X, T, XVALIDATE = obj.readFile('/home/ubuntu/Downloads/train.csv')
        print numpy.shape(XVALIDATE)
        W = obj.computeW(X,T)
        obj.validate(XVALIDATE, W)
        #sys.exit(main())
    
    if __name__ == '__main__':main()
       
    
    
