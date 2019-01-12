import math
import random
import util_general as util

#Do linear regression with gradient descent for the data in matrix.
def linearRegression(matrix, batchSize):
 if len(matrix) % batchSize != 0:
  print('batchSize need to be alligned with the number of datapoints')
  return ()
 #I guess on values for the regressionline
 w0 = 0
 w1 = matrix[0][1] / matrix[0][0]
 stepSize = 0.1
 iterations = 100
 for i in range(0, iterations):
  for j in range(0, len(matrix), batchSize):
   sum = 0
   sum2 = 0
   for k in range(j, j + batchSize):
    sum += w0 + w1*matrix[k][0] - matrix[k][1]
    sum2 += matrix[k][0]*sum
   w0 -= stepSize*2*sum
   w1 -= stepSize*2*sum2
 return (w0, w1)

#Return a logisticFunction for the parameters given by the perceptronAlgorithm algorithm.
def logisticRegression(mx1, mx2, misclassified):
 v = perceptronAlgorithm(mx1, mx2, misclassified)
 def logisticFunction(xi):
  return 1/(1 + math.exp(-sum([a*b for a,b in zip(v,[1.0] + xi)])))
 return logisticFunction

#Returns weights for a binary classifier calculated by the perceptronAlgorithm,
#the condition for when to stop is when the number of misclassifications is lower
#than misclassified
def perceptronAlgorithm(mx1, mx2, misclassified):
  matrix = joinMatrix(mx1,mx2)
  w=[0,0,0]
  while errorsNum(w,matrix)>misclassified:
    random.shuffle(matrix)
    for j in range(0,len(matrix)):
      if util.vectorDotProduct(w,[1]+[matrix[j][0]]+[matrix[j][1]])<0:
        w[0] += matrix[j][2]
        w[1] += matrix[j][2]*matrix[j][0]
        w[2] += matrix[j][2]*matrix[j][1]
      else:
        w[0] += matrix[j][2] - 1
        w[1] += (matrix[j][2]-1)*matrix[j][0]
        w[2] += (matrix[j][2]-1)*matrix[j][1] 
  return w

#Get number of misclassifications.
def errorsNum(w,matrix):
  errors=0;
  for j in range(0,len(matrix)):
    if util.vectorDotProduct(w,[1]+[matrix[j][0]]+[matrix[j][1]])<0 and matrix[j][2]==1:
      errors += 1
    elif util.vectorDotProduct(w,[1]+[matrix[j][0]]+[matrix[j][1]]) >= 0 and matrix[j][2] == 0:
      errors += 1
  return errors
  
#Join two matrices and give rows that correspond to french a 1 and rows that 
#correspond to english a 0, it also scale each column in the range 0 to 1.
def joinMatrix(mx1,mx2):
  m=[]
  for i in range(0,len(mx1)):
    m.append(mx1[i]+[1])
  for j in range(0,len(mx2)):
    m.append(mx2[j]+[0])
  m = util.scaleMatrixToRange(m,0,1)
  return m




