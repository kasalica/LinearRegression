import sys

#Read the data in the file filename and convert it to a matrix. Each set of features need to 
#be on a new line and the different features need to be separated by a tab. 
def convertDataFileToMatrix(filename):
 f = open(filename,'r')
 matrix = []
 for line in f:
  line = line.strip('\n')
  strlist = line.split('\t')
  matrix.append([float(str) for str in strlist])
 f.close()
 return matrix

#Scale a matrix to the range [min_r, max_r].
def scaleMatrixToRange(matrix, min_r, max_r):
 return [scaleListToRange(list, min_r, max_r, minOfEachColumn(matrix), maxOfEachColumn(matrix)) for list in matrix]

#Scale a list to the range [min_r, max_r].
def scaleListToRange(list, min_r, max_r, minimumvector, maximumvector):
 return [scaleToRange(list[i], min_r, max_r, minimumvector[i], maximumvector[i]) for i in range(0, len(list))]

#Scale a element to the range [min_r, max_r]
def scaleToRange(element, min_r, max_r, minimum, maximum):
 return (max_r - min_r)*(element - minimum)/(maximum - minimum) + min_r

#Return a vector with the max of each column 
def maxOfEachColumn(matrix):
 maxvector = [sys.float_info.min]*len(matrix[0])
 for vector in matrix:
  for i in range(0,len(vector)):  
   maxvector[i] = vector[i] if vector[i] > maxvector[i] else maxvector[i]
 return maxvector 

#Return a vector with the min of each column
def minOfEachColumn(matrix):
 minvector = [sys.float_info.max]*len(matrix[0])
 for vector in matrix:
  for i in range(0,len(vector)):  
   minvector[i] = vector[i] if vector[i] < minvector[i] else minvector[i]
 return minvector

#Return dot product of 2 vectors
def vectorDotProduct(v1,v2):
 return sum([a*b for a,b in zip(v1,v2)])

