import numpy as np

inputFile = '../resources/input03.txt'


#### PART 1

def readFile(f):
	array = []
	with open(inputFile, 'r') as f:
		first = 0
		for line in f:
			if first == 0:
				line1 = [x for x in line.split(',')]
				first = 1
			else:
				line2 = [x for x in line.split(',')]

	return (line1, line2)


def initiateBoard(boardSize):
	board = np.zeros([boardSize, boardSize])
	stationPos = [int(boardSize / 2), int(boardSize / 2)]

	board[stationPos[0], stationPos[1]] = 1

	return (stationPos, board)


def calcNew(currPos, dir, steps):
	newPos = currPos.copy()
	if dir == 'R':
		newPos[0] = currPos[0] + steps
		currPos[0] = currPos[0] + 1
	elif dir == 'L':
		newPos[0] = currPos[0] - steps
		currPos[0] = currPos[0] - 1
	elif dir == 'U':
		newPos[1] = currPos[1] - steps
		currPos[1] = currPos[1] - 1
	else:
		newPos[1] = currPos[1] + steps
		currPos[1] = currPos[1] + 1

	return (currPos, newPos)


def drawBoard(dir, c, n, firstWire):
	if dir in ['R', 'D']:
		if firstWire:
			board[c[1]:(n[1] + 1), c[0]:(n[0] + 1)] = 1
		else:
			aux = board[c[1]:(n[1] + 1), c[0]:(n[0] + 1)]
			board[c[1]:(n[1] + 1), c[0]:(n[0] + 1)] = np.where(aux == 1, 3, 2)
	else:

		if firstWire:
			board[n[1]:(c[1] + 1), n[0]:(c[0] + 1)] = 1
		else:
			aux = board[n[1]:(c[1] + 1), n[0]:(c[0] + 1)]
			board[n[1]:(c[1] + 1), n[0]:(c[0] + 1)] = np.where(aux == 1, 3, 2)


def drawWire(wire, initialPos, firstWire):
	global board
	currPos = initialPos.copy()

	for instr in wire:
		dir = instr[0]
		steps = int(instr[1:])
		currPost, newPos = calcNew(currPos, dir, steps)
		# print(str(currPos) + ' -> ' + str(newPos) + ' for dir: ' + str(dir) + ', steps:' + str(steps))

		drawBoard(dir, currPos, newPos, firstWire)
		currPos = newPos.copy()


def calcMinDist(arr1, arr2, board, stationPos, minDist):
	# draw both wires
	drawWire(arr1, stationPos, True)
	drawWire(arr2, stationPos, False)

	a, b = np.where(board == 3)

	for i in range(0, len(a)):
		currD = abs(a[i] - stationPos[0]) + abs(b[i] - stationPos[1])
		if currD < minDist:
			minDist = currD

	return (minDist)


# arr1, arr2 = readFile(inputFile)
# print(arr1)
# print(arr2)
# arr1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
# arr2 = ['U62','R66','U55','R34','D71','R55','D58','R83']

# arr1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
# arr2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']

# arr1 = ['R8','U5','L5','D3']
# arr2 = ['U7','R6','D4','L4']

# size = 20000
# stationPos, board = initiateBoard(size)
# d = calcMinDist(arr1, arr2, board, stationPos, size)
# print('The minimum distance is ' + str(d))
# 462 is too low
# 2193

#### PART 2

def calcNew2(currPos, dir, steps):
	newPos = currPos.copy()
	if dir == 'R':
		newPos[0] = currPos[0] + steps
	elif dir == 'L':
		newPos[0] = currPos[0] - steps
	elif dir == 'U':
		newPos[1] = currPos[1] - steps
	else:
		newPos[1] = currPos[1] + steps

	return (newPos)

def isBetween(c, n, i):
	if (abs(i[0] - c[0]) <= abs(n[0] - c[0])) and (abs(i[1] - c[1]) <= abs(n[1] - c[1])):
		return(True)
	else:
		return(False)

def countSteps(wire, initialPos, inters):
	global board

	currPos = initialPos.copy()
	sumSteps = 0
	#print('inters:' + str(inters))

	for instr in wire:
		dir = instr[0]
		steps = int(instr[1:])
		newPos = calcNew2(currPos, dir, steps)

		#stop as soon as the intersection is found
		#print('positions: ' + str(currPos) + ' -> ' + str(newPos))
		if isBetween(currPos, newPos, inters):
			aux1 = abs(inters[0] - currPos[0])
			aux2 = abs(inters[1] - currPos[1])
			sumSteps = sumSteps + aux1 + aux2
			#print('Sum steps to intersection: ' + str(sumSteps))
			return(sumSteps)
		else:
			sumSteps = sumSteps + steps
			#print('increasing: ' + str(sumSteps))

		currPos = newPos.copy()

arr1, arr2 = readFile(inputFile)

#arr1 = ['R8', 'U5', 'L5', 'D3']
#arr2 = ['U7', 'R6', 'D4', 'L4']

#arr1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
#arr2 = ['U62','R66','U55','R34','D71','R55','D58','R83']

#arr1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
#arr2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']

size = 20000
stationPos, board = initiateBoard(size)

# draw both wires
drawWire(arr1, stationPos, True)
drawWire(arr2, stationPos, False)

# check intersection coordinates
a, b = np.where(board == 3)

distSum = []
for i in range(0, len(a)):
	dist1 = countSteps(arr1, stationPos, [b[i], a[i]])
	dist2 = countSteps(arr2, stationPos, [b[i], a[i]])
	distSum.append(dist1 + dist2)

print(distSum)
print('Minimum step-distance is ' + str(np.array(distSum).min()))
#63526