import util_libsvm as libsvm
import learning_algorithms as learn
import util_general as util

matrix1 = util.convertDataFileToMatrix('frenchdata')
matrix2 = util.convertDataFileToMatrix('englishdata')

svmString1 = libsvm.encodeToLibSVM(matrix1, '+1')
svmString2 = libsvm.encodeToLibSVM(matrix2, '-1')
print('\n')
print('frenchdata and englishdata is encoded to libsvm and written to the file "data_in_libsvm"')

f = open('data_in_libsvm','w')
f.write(svmString1)
f.write(svmString2)
f.close()

dict = libsvm.decodeLibSVM('data_in_libsvm')
matrix1 = dict['+1']
matrix2 = dict['-1']

scaledMatrix = learn.joinMatrix(matrix1,matrix2)
regressionLine1 = learn.linearRegression(scaledMatrix[0:15], 1)
regressionLine2 = learn.linearRegression(scaledMatrix[15:30], 1)

print('\n')
print('RegressionLine for french:')
print('y = ' + str(regressionLine1[1]) + 'x + ' + str(regressionLine1[0]))
print('RegressionLine for english:')
print('y = ' + str(regressionLine2[1]) + 'x + ' + str(regressionLine2[0]))

misses = input('Type number of acceptable misclassifications:')
print('\n')
print('Weights after the perceptron-algorithm has iterated until misclassifications of the dataset is less than or equal to ' + misses + '.')
w = learn.perceptronAlgorithm(matrix1, matrix2, int(misses))
print('w0 = ' + str(w[0]) + ', w1 = ' + str(w[1]) + ', w2 = ' + str(w[2]))

logisticFunction = learn.logisticRegression(matrix1, matrix2, int(misses))
print('\n')
print('Print probabilities of being french for each instance of data, calculated by logistic regression. 1-15 is french.')
i = 1
for instance in learn.joinMatrix(matrix1, matrix2):
 print('Line ' + str(i) + ' ' + str(logisticFunction(instance)))
 i += 1

input("prompt: ")


