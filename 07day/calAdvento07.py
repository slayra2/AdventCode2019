inputFile = '../resources/input07.txt'

#### PART 1
def readFile(inputFile):
	array = []
	with open(inputFile, 'r') as f:
		for line in f:
			array.extend([int(x) for x in line.split(',')])

	return (array)

def getCodes(strI, i, codeGlobal):
	#print('string: ' + strI)
	code = codeGlobal.copy()
	opcode = int(strI[-2:])
	mode1 = int(strI[-3])

	if len(strI) > 3:
		mode2 = int(strI[-4])
	else:
		mode2 = 0

	if len(strI) > 4:
		mode3 = int(strI[-5])
	else:
		mode3 = 0

	if mode1 == 0:
		pos1 = code[i + 1]
	else:
		pos1 = i + 1

	if mode2 == 0:
		pos2 = code[i + 2]
	else:
		pos2 = i + 2

	if mode3 == 0:
		pos3 = code[i + 3]
	else:
		pos3 = i + 3

	return(opcode, mode1, mode2, mode3, pos1, pos2, pos3)

def outputCode(inputCode, phaseCode, codeGlobal):
	outputs = []
	code = codeGlobal.copy()

	firstInput = True
	i = 0
	while code[i] != 99:
		#print('opcode:' + str(code[i]))

		if code[i] in [1, 2]:
			pos1 = code[i + 1]
			pos2 = code[i + 2]
			pos3 = code[i + 3]

			if code[i] == 1:
				code[pos3] = code[pos1] + code[pos2]
			else:
				code[pos3] = code[pos1] * code[pos2]

			i = i + 4

		elif code[i] == 3:
			pos1 = code[i + 1]
			if firstInput:
				code[pos1] = phaseCode
				firstInput = False
			else:
				code[pos1] = inputCode
			i = i + 2

		elif code[i] == 4:
			pos1 = code[i + 1]
			outputs.append(code[pos1])
			#print('output: ' + str(code[pos1]))
			i = i + 2

		elif code[i] == 5:
			pos1 = code[i + 1]
			if code[pos1] != 0:
				pos2 = code[i + 2]
				i = code[pos2]
			else:
				i = i + 3

		elif code[i] == 6:
			pos1 = code[i + 1]
			if code[pos1] == 0:
				pos2 = code[i + 2]
				i = code[pos2]
			else:
				i = i + 3

		elif code[i] == 7:
			pos1 = code[i + 1]
			pos2 = code[i + 2]
			pos3 = code[i + 3]
			if code[pos1] < code[pos2]:
				code[pos3] = 1
			else:
				code[pos3] = 0
			i = i + 4

		elif code[i] == 8:
			pos1 = code[i + 1]
			pos2 = code[i + 2]
			pos3 = code[i + 3]

			if code[pos1] == code[pos2]:
				code[pos3] = 1
			else:
				code[pos3] = 0
			i = i + 4

		else:
			opcode, mode1, mode2, mode3, pos1, pos2, pos3 = getCodes(str(code[i]), i, code)

			if opcode in [1, 2]:
				if opcode == 1:
					code[pos3] = code[pos1] + code[pos2]
				else:
					code[pos3] = code[pos1] * code[pos2]
				#print('Position ' + str(pos3) + ' changed to ' + str(code[pos3]))
				i = i + 4

			elif opcode == 3:
				if firstInput:
					code[pos1] = phaseCode
					firstInput = False
				else:
					code[pos1] = inputCode
				i = i + 2

			elif opcode == 4:
				outputs.append(code[pos1])
				#print('output: ' + str(code[pos1]))
				i = i + 2

			elif opcode == 5:
				if code[pos1] != 0:
					i = code[pos2]
				else:
					i = i + 3

			elif opcode == 6:
				if code[pos1] == 0:
					i = code[pos2]
				else:
					i = i + 3

			elif opcode == 7:
				if code[pos1] < code[pos2]:
					code[pos3] = 1
				else:
					code[pos3] = 0
				i = i + 4

			elif opcode == 8:
				if code[pos1] == code[pos2]:
					code[pos3] = 1
				else:
					code[pos3] = 0
				i = i + 4
		#print(code)
	return (outputs)


code = readFile(inputFile)
#code = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
#code = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
#code = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

# numbers = [0, 1, 2, 3, 4]
# sequences = []
# for i in range(5):
# 	for j in set(numbers).difference([i]):
# 		for k in set(numbers).difference([i, j]):
# 			for l in set(numbers).difference([i, j, k]):
# 				for m in set(numbers).difference([i, j, k, l]):
# 					sequences.append([i,j,k,l,m])
#
# signals = []
# for sequence in sequences:
# 	inputCode = 0
#
# 	for n in sequence:
# 		output = outputCode(inputCode, n, code)
# 		inputCode = output[0]
# 		#print('New input code: ' + str(inputCode))
#
# 	signals.append(output[0])

#print(signals)
#print('highest signal: ' + str(max(signals)))
#43812

#### PART 2
def findSequences(numbers):
	sequences = []
	for i in range(min(numbers), max(numbers)+1):
		for j in set(numbers).difference([i]):
			for k in set(numbers).difference([i, j]):
				for l in set(numbers).difference([i, j, k]):
					for m in set(numbers).difference([i, j, k, l]):
						sequences.append([i, j, k, l, m])

	return(sequences)

def outputCode2(inputCode, codeAmp, currIndex, firstInput=False, phaseCode=0):

	i = currIndex
	outputs = [inputCode]
	code = codeAmp.copy()

	while code[i] != 99:
		#print('opcode:' + str(code[i]))

		if code[i] in [1, 2]:
			pos1 = code[i + 1]
			pos2 = code[i + 2]
			pos3 = code[i + 3]

			if code[i] == 1:
				code[pos3] = code[pos1] + code[pos2]
			else:
				code[pos3] = code[pos1] * code[pos2]

			i = i + 4

		elif code[i] == 3:
			pos1 = code[i + 1]
			if firstInput:
				code[pos1] = phaseCode
				firstInput = False
			else:
				#code[pos1] = output
				code[pos1] = inputCode
			i = i + 2

		elif code[i] == 4:
			pos1 = code[i + 1]
			outputs.append(code[pos1])
			#print('output: ' + str(code[pos1]))
			i = i + 2
			return(code, code[pos1], i)

		elif code[i] == 5:
			pos1 = code[i + 1]
			if code[pos1] != 0:
				pos2 = code[i + 2]
				i = code[pos2]
			else:
				i = i + 3

		elif code[i] == 6:
			pos1 = code[i + 1]
			if code[pos1] == 0:
				pos2 = code[i + 2]
				i = code[pos2]
			else:
				i = i + 3

		elif code[i] == 7:
			pos1 = code[i + 1]
			pos2 = code[i + 2]
			pos3 = code[i + 3]
			if code[pos1] < code[pos2]:
				code[pos3] = 1
			else:
				code[pos3] = 0
			i = i + 4

		elif code[i] == 8:
			pos1 = code[i + 1]
			pos2 = code[i + 2]
			pos3 = code[i + 3]

			if code[pos1] == code[pos2]:
				code[pos3] = 1
			else:
				code[pos3] = 0
			i = i + 4

		else:
			opcode, mode1, mode2, mode3, pos1, pos2, pos3 = getCodes(str(code[i]), i, code)

			if opcode in [1, 2]:
				if opcode == 1:
					code[pos3] = code[pos1] + code[pos2]
				else:
					code[pos3] = code[pos1] * code[pos2]
				#print('Position ' + str(pos3) + ' changed to ' + str(code[pos3]))
				i = i + 4

			elif opcode == 3:
				if firstInput:
					code[pos1] = phaseCode
					firstInput = False
				else:
					#code[pos1] = output
					code[pos1] = inputCode
				i = i + 2

			elif opcode == 4:
				#print('output: ' + str(code[pos1]))
				outputs.append(code[pos1])
				i = i + 2
				return(code, code[pos1], i)

			elif opcode == 5:
				if code[pos1] != 0:
					i = code[pos2]
					#print('new i=' + str(i))
				else:
					i = i + 3

			elif opcode == 6:
				if code[pos1] == 0:
					i = code[pos2]
				else:
					i = i + 3

			elif opcode == 7:
				if code[pos1] < code[pos2]:
					code[pos3] = 1
				else:
					code[pos3] = 0
				i = i + 4

			elif opcode == 8:
				if code[pos1] == code[pos2]:
					code[pos3] = 1
				else:
					code[pos3] = 0
				i = i + 4
		#print(code)
	#print(code[i])
	#print('Last output: ' + str(outputs[-1]))
	return(code, outputs[-1], 99)


codeO = readFile(inputFile)
sequences = findSequences([5, 6, 7, 8, 9])

#code = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
#sequences = [[9,8,7,6,5]]
#139629729

#code = [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54, -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4, 53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10]
#sequences = [[9, 7, 8, 5, 6]]
#18216

signal = 0

# per amplifier
for sequence in sequences:

	newIndex = 0
	currIndex = [0, 0, 0, 0, 0]
	codes = [codeO, codeO, codeO, codeO, codeO]
	currInput = 0
	loops = -1

	while newIndex != 99:
		loops = loops + 1

		for a in range(5):
			if newIndex != 99:
				#print('################## Amplifier ' + str(a))
				#print('Pointer for amplifiers: ' + str(currIndex))
				if loops < 1:
					#print('Phase code: ' + str(sequence[a]))
					newCode, newInput, newIndex = outputCode2(currInput, codes[a], currIndex[a], True, sequence[a])
				else:
					newCode, newInput, newIndex = outputCode2(currInput, codes[a], currIndex[a])

				currInput = newInput
				currIndex[a] = newIndex
				codes[a] = newCode
				#print('New output = ' + str(currInput) + ' and iterator changed to ' + str(newIndex))

	signal = max(signal, newInput)
	print('For sequence ' + str(sequence) + ' the best value was ' + str(currInput) + ' and the best overall is ' + str(signal))


print('highest signal: ' + str(signal))
#41095364 - low
59597414