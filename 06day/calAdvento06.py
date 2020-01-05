inputFile = '../resources/input06.txt'

#### PART 1
def readFile(inputFile):

	with open(inputFile, 'r') as f:
		edges = []
		nodes = []
		for line in f:
			edges.append([str(x).replace('\n', '') for x in line.split(')')])
			nodes.extend([str(x).replace('\n', '') for x in line.split(')')])
	return (edges, set(nodes))

def findEdge(edges, n):

	i = 0
	while n not in edges[i][1]:
		i = i + 1

	return(edges[i])

#edges, nodes = readFile(inputFile)
#edges = [['COM', 'B'], ['B','C'], ['C','D'], ['D','E'],['E','F'],['B','G'],['G','H'],['D','I'],['E','J'],['J','K'],['K','L']]
#nodes = set(['COM','B','C','D','E','F','G','H','I','J','K','L'])

dicOrbits = {'COM': 0}

for node in nodes.difference(['COM']):
	auxOrbits = 1
	currEdge = findEdge(edges, node)

	while (currEdge[0] != 'COM') or (currEdge[0] not in dicOrbits.keys()):
		auxOrbits = auxOrbits + 1
		currEdge = findEdge(edges, currEdge[0])

	if currEdge[0] == 'COM':
		dicOrbits[node] = auxOrbits
	else:
		auxOrbits = auxOrbits + dicOrbits[currEdge[0]]

print(sum(dicOrbits.values()))
#144909

#### PART 2

edges, nodes = readFile(inputFile)
#edges = [['COM', 'B'], ['B','C'], ['C','D'], ['D','E'],['E','F'],['B','G'],['G','H'],['D','I'],['E','J'],['J','K'],['K','L'], ['K','YOU'], ['I', 'SAN']]

nodesDic = {}
for edge in edges:
	if edge[1] == 'YOU':
		nodesDic['YOU'] = edge

	if edge[1] == 'SAN':
		nodesDic['SAN'] = edge

dicOrbits = {}
for node in nodesDic.keys():
	auxArray = []
	currEdge = nodesDic[node]

	while currEdge[0] != 'COM':
		auxArray.append(currEdge[0])
		currEdge = findEdge(edges, currEdge[0])

	dicOrbits[node] = auxArray

p = 0
while dicOrbits['YOU'][p] not in dicOrbits['SAN']:
	p = p + 1

nOrbits = p + dicOrbits['SAN'].index(dicOrbits['YOU'][p])

print(nOrbits)
#259