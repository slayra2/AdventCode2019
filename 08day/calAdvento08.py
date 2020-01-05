from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

inputFile = '../resources/input08.txt'

#### PART 1
def readFile(inputFile):
	with open(inputFile, 'r') as f:
		code = f.readline()
	return (code)

imageCode = readFile(inputFile)
#imageCode = '123456789012'

w = 25
h = 6

layers = []
while len(imageCode) > 0:
	layer = []
	for j in range(h):
		layer.extend([imageCode[:w]])
		imageCode = imageCode[w:]

	layers.append(layer)

minZeros = -1
mult = 0

for l in layers:
	countDic = Counter()

	for j in range(h):
		countDic = countDic + Counter(l[j])

	#print('minZeros: ' + str(minZeros) + ' currZeros: ' + str(countDic['0']))
	if (minZeros == -1) or (minZeros > countDic['0']):
		minZeros = countDic['0']
		mult = countDic['1']*countDic['2']
		print('layer ' + str(l) + ' has ' + str(minZeros) + ' zeros and multiplication = ' + str(mult))
#2500

#### PART 2

def createLayers(imageCode, w, h):
	layers = []

	while len(imageCode) > 0:
		layer = []
		for j in range(h):
			layer.extend([imageCode[:w]])
			imageCode = imageCode[w:]

		layers.append(layer)

	return(layers)

imageCode = readFile(inputFile)
w = 25
h = 6

#imageCode = '0222112222120000'
#w = 2
#h = 2

layers = createLayers(imageCode, w, h)

#0 is black, 1 is white, and 2 is transparent

currLayer = layers[0]
for layer in layers[1:]:
	for j in range(h):
		s = ''
		for i in range(w):
			if currLayer[j][i:(i+1)] == '2':
				s = s + layer[j][i:(i+1)]
			else:
				s = s + currLayer[j][i:(i+1)]
		currLayer[j] = s

image = np.zeros([h,w])
for j in range(h):
	#print('j = ' + str(j))
	for i in range(w):
		#print('i = ' + str(i))
		if currLayer[j][i:(i+1)] == '1':
			image[j,i] = 1

cmap = ListedColormap(['w', 'r'])
plt.matshow(image, cmap=cmap)
#CYUAH