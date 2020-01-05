inputFile = '../resources/input09.txt'

#### PART 1
def readFile(inputFile):
	array = []
	with open(inputFile, 'r') as f:
		for line in f:
			array.extend([int(x) for x in line.split(',')])

	return (array)

def getCodes(strI, i, relBase):
	global code

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

	if mode1 in [0, 2]:
		try:
			pos1 = code[i + 1]
		except:
			lenCode = len(code)-1
			code.extend([0] * (i + 1 - lenCode))

		if mode1 == 0:
			pos1 = code[i + 1]
		else:
			pos1 = relBase + code[i + 1]
	else:
		pos1 = i + 1

	if mode2 in [0, 2]:
		try:
			pos2 = code[i + 2]
		except:
			lenCode = len(code) - 1
			code.extend([0] * (i + 2 - lenCode))

		if mode2 == 0:
			pos2 = code[i + 2]
		else:
			pos2 = relBase + code[i + 2]
	else:
		pos2 = i + 2

	if mode3 in [0, 2]:
		try:
			pos3 = code[i + 3]
		except:
			lenCode = len(code) - 1
			code.extend([0] * (i + 3 - lenCode))

		if mode3 == 0:
			pos3 = code[i + 3]
		else:
			pos3 = relBase + code[i + 3]
	else:
		pos3 = i + 3

	#print('code length:' + str(len(code)))
	return(opcode, mode1, mode2, mode3, pos1, pos2, pos3)

def outputCode(inputCode):
	outputs = []
	global code

	relBase = 0
	i = 0
	while code[i] != 99:

		if len(str(code[i])) == 1:
			aux = '00' + str(code[i])
			opcode, mode1, mode2, mode3, pos1, pos2, pos3 = getCodes(aux, i, relBase)
		else:
			opcode, mode1, mode2, mode3, pos1, pos2, pos3 = getCodes(str(code[i]), i, relBase)

		if opcode in [1, 2]:

			if opcode == 1:
				code[pos3] = code[pos1] + code[pos2]
			else:
				code[pos3] = code[pos1] * code[pos2]
			#print('Position ' + str(pos3) + ' changed to ' + str(code[pos3]))
			i = i + 4

		elif opcode == 3:
			code[pos1] = inputCode
			i = i + 2

		elif opcode == 4:
			outputs.append(code[pos1])
			print('output: ' + str(code[pos1]))
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

		elif opcode == 9:
			relBase = relBase + code[pos1]
			#print('New relative base:' + str(relBase))
			i = i + 2
		#print(code)
	return (outputs)

code = readFile(inputFile)
#print(code)

#code = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
#code = [1102,34915192,34915192,7,4,7,99,0] #1219070632396864
#code = [104,1125899906842624,99]

inputCode = 1
outputs = outputCode(inputCode)

print(outputs)
#4634208483351283024 - too high