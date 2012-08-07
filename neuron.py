from __future__ import division
__author__ = "arunprasath shankar <axs918@case.edu>"
__date__ = "08/05/2012"

import random
from difflib import SequenceMatcher
results = open('/Users/arunprasathshankar/Desktop/out.txt','w')

class ANN(object):

    correct,wrong = 0,0
    output_list = []
    th,w1,w2 = [],[],[]

    def __init__(self):
        self.inputs = []
        self.weights = []
        self.output = 0.0
        self.threshold = random.uniform(0,1)

    def inputNeurons(self,inN):
        for i in inN:
            self.inputs = i
            ANN.inputWeights(self)
            ANN.computeSquash(self)
            ANN.output(self)

    def inputWeights(self):
        self.weights  = [random.uniform(0,1),random.uniform(0,1)]

    def computeSquash(self):
        self.squash = self.inputs[0] * self.weights[0] + self.inputs[1] * self.weights[1]

    def output(self):
        if self.squash > self.threshold:
            self.output = 1
        else:
            self.output = 0
        results.write('%d %d %d'% (self.inputs[0],self.inputs[1],self.output))
        self.output_list.append(self.output)

    def percentageMatch(self):
        #print NN.output_list
        correct_match = [0,0,0,1]
        match = SequenceMatcher(None,correct_match,ANN.output_list)
        if match.ratio() == 1:
            results.write("TRUE")
            self.correct += 1
            self.th.append(self.threshold)
            self.w1.append(self.weights[0])
            self.w2.append(self.weights[1])
        else:
            results.write("FALSE")
            self.wrong += 1

    def trueFalseCount(self):
        results.write('Correct => %d, Wrong => %d' %(self.correct,self.wrong))
        accuracy = self.correct/(self.correct + self.wrong)
        results.write('Accuracy = %f' % accuracy)
        #print self.th,self.w1,self.w2
        th,w1,w2 = 0,0,0
        for item in self.th:
            th += item
        for item in self.w1:
            w1 += item
        for item in self.w2:
            w2 += item

        thresholdFound = th/len(self.th)
        weight1 = w1/len(self.w1)
        weight2 = w2/len(self.w2)
        results.write('Trained Threshold = %f' % thresholdFound)
        results.write('Trained Weights = %f,%f' % (weight1,weight2))

if __name__ == '__main__':
    nn = ANN()
    inp = [[0,0],[0,1],[1,0],[1,1]]

    for i in range(1000000):
        nn.inputNeurons(inp)
        nn.percentageMatch()
        ANN.output_list = []
        results.write('-----')
    nn.trueFalseCount()








