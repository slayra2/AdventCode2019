import numpy as np
inputFile = '../resources/input02.txt'

#### PART 1

def readFile(f):
    array = []
    with open(inputFile, 'r') as f:
        for line in f:
            array = [int(x) for x in line.split(',')]

    return(array)

def decideF(opcode, pos1, pos2, array):
	if opcode == 1:
		value = array[pos1] + array[pos2]
	elif opcode == 2:
		value = array[pos1] * array[pos2]
	else:
		print('Error found, opcode = ' + str(opcode))

	return(value)

# arr = readFile(inputFile)
# arr[1] = 12
# arr[2] = 2
# #print(arr)
#
# for i in range(0,len(arr)-1,4):
#
# 	if arr[i] != 99:
# 		newVal = decideF(arr[i], arr[i+1], arr[i+2], arr)
# 		posF = arr[i+3]
# 		arr[posF] = newVal
# 	else:
# 		i = len(arr)
#
# print("Array final :")
# print(arr)
# print("Valor na posição zero:")
# print(arr[0])
#4570637

#### PART 2

def findAddress0(arr):

	for i in range(0, len(arr)-1, 4):
		if arr[i] != 99:
			newValue = decideF(arr[i], arr[i+1], arr[i+2], arr)
			posF = arr[i+3]
			arr[posF] = newValue
		else:
			i = len(arr)

	return(arr[0])


address0 = 19690720
nounVerb = []

for n in range(0, 100):
	for v in range(0, 100):
		array = readFile(inputFile)
		array[1] = n
		array[2] = v
		newVal = findAddress0(array)
		if newVal == address0:
			nounVerb = [n, v]
			print("noun + verb: " + str(n) + ' and ' + str(v))

print("final: " + str(100*nounVerb[0] + nounVerb[1]))
#5485

# array = readFile(inputFile)
# array[1] = 54
# array[2] = 85
# print(findAddress0(array))