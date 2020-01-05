import numpy as np

inputFile = '../resources/input01.txt'

#### PART 1

def readFile(f):
    array = []
    with open(inputFile, 'r') as f:
        for line in f:
            array.append(int(line))

    return(array)

def findSum(array):
    arr = np.floor(np.array(array)/3)-2
    return(arr.sum())

mass = readFile(inputFile)
print(findSum(mass))
#3412207

#### PART 2
def measureFuel(sumF, fuel):

    global arraySum

    fuel2 = np.floor(np.array(fuel)/3)-2
    if fuel2 > 0:
        measureFuel(sumF+fuel2, fuel2)
    else:
        #print('fuel:' + str(fuel))
        #print('Added sum:' + str(sumF))
        arraySum.append(sumF)

arraySum = []
for m in mass:
    #print(m)
    measureFuel(0, m)

#print(arraySum)
print(np.array(arraySum).sum())
#8527643 - too high
#5115436