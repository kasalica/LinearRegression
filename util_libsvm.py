#Use a matrix of values to create a LibSVM encoded string with the specific label.
def encodeToLibSVM(matrix,label):
 string = ''
 for instance in matrix:
  string += label
  for i in range(0, len(instance)):
   string += ' ' + str(i + 1) + ':' + str(instance[i])
  string += '\n'
 return string

#Decode a file encoded in LibSVM. return a dictionaire with a matrix for each
#label.
def decodeLibSVM(filename):
 f = open(filename, 'r')
 dict = {}
 for line in f:
  line = line.strip('\n')
  featurelist = line.split(' ')
  label = featurelist.pop(0)
  if label not in dict:
   dict[label] = []
  temp = [0]*len(featurelist)
  for feature in featurelist:
   pair = feature.split(':')
   temp[int(pair[0]) - 1] = float(pair[1])
  dict[label].append(temp)
 f.close()
 return dict


