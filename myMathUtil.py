import sys

L = 0
H = 1

class BinaryMovingAeverage:
    def __init__(self, numOfSample, initBinary):
        self.buffer = []
        self.numOfSample = numOfSample
        for i in range(numOfSample):
            self.buffer.append(initBinary)
    def update(self, newBinary):
        self.buffer.pop(0)
        self.buffer.append(newBinary)
        return self.evaluate()
    def evaluate(self):
        val = 0
        for i in range(self.numOfSample):
            val = val + self.buffer[i]
        return (self.numOfSample / 2) < val

#def errorExit(reason):
#    sys.exit(reason)
#
#def testBinaryMovingAeverage():
#    n = 19
#    bma = BinaryMovingAeverage(n, L)
#    for i in range(n):
#        if bma.update(H) != (H if n/2 <= i else L):
#            errorExit("Failed at " + str(i))
#
#testBinaryMovingAeverage()
#            
#    
#
