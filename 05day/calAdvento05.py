inputFile = '../resources/input05.txt'

#### PART 1
def readFile(inputFile):
	array = []
	with open(inputFile, 'r') as f:
		for line in f:
			array.extend([int(x) for x in line.split(',')])

	return (array)

def returnValue12(opcode, pos1, pos2):
	if opcode == 1:
		value = code[pos1] + code[pos2]
	else:
		value = code[pos1] * code[pos2]

	return (value)

def outputCode(inputCode):
	outputs = []
	global code

	i = 0
	while i < len(code):
		# print(str(code[i]))

		if code[i] == 99:
			return (outputs)

		elif code[i] in [1, 2]:
			pos3 = code[i + 3]
			code[pos3] = returnValue12(code[i], code[i + 1], code[i + 2])
			i = i + 4

		elif code[i] == 3:
			pos1 = code[i + 1]
			code[pos1] = inputCode
			i = i + 2

		elif code[i] == 4:
			pos1 = code[i + 1]
			outputs.append(code[pos1])
			print('output: ' + str(code[pos1]))
			i = i + 2

		else:
			strI = str(code[i])
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
			# print('valor final 1: ' + str(code[pos1]))

			if opcode in [1, 2]:
				if mode2 == 0:
					pos2 = code[i + 2]
				else:
					pos2 = i + 2
				# print('valor final 2: ' + str(code[pos2]))

				if mode3 == 0:
					pos3 = code[i + 3]
				else:
					pos3 = i + 3

				if opcode == 1:
					code[pos3] = code[pos1] + code[pos2]
				else:
					code[pos3] = code[pos1] * code[pos2]
				# print('colocar na posicao ' + str(pos3) + ' o valor ' + str(code[pos3]))
				i = i + 4
			# print('i: ' + str(i))

			elif opcode == 3:
				code[pos1] = inputCode
				i = i + 2

			elif opcode == 4:
				outputs.append(code[pos1])
				print('output: ' + str(code[pos1]))
				i = i + 2


# code = readFile(inputFile)

# code = [1002, 4, 3, 4, 33]
# inputCode = 1
# arr = outputCode(inputCode)
# 16434972
# print(code)

#### PART 2

def getCodes(strI, i):

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

def outputCode(inputCode):
	outputs = []
	global code

	i = 0
	while code[i] != 99:
		#print(str(code[i]))

		if code[i] in [1, 2]:
			pos3 = code[i + 3]
			code[pos3] = returnValue12(code[i], code[i + 1], code[i + 2])
			i = i + 4

		elif code[i] == 3:
			pos1 = code[i + 1]
			code[pos1] = inputCode
			i = i + 2

		elif code[i] == 4:
			pos1 = code[i + 1]
			outputs.append(code[pos1])
			print('output: ' + str(code[pos1]))
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
			opcode, mode1, mode2, mode3, pos1, pos2, pos3 = getCodes(str(code[i]), i)

			if opcode in [1, 2]:
				if opcode == 1:
					code[pos3] = code[pos1] + code[pos2]
				else:
					code[pos3] = code[pos1] * code[pos2]
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
		#print(code)
	return (outputs)


code = readFile(inputFile)
#code = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
#		1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,
#		1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

#code = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
#code = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]

inputCode = 5
arr = outputCode(inputCode)
#5176287 is too low
#7273471 is too low
#16694270
print(arr)
