#import numpy as np
import collections

#### PART 1
start = 265275
end = 781584

def countCombs(start, end):
	combs = 0
	for i in range(start, end+1):
		t = str(i)

		works = True
		if len(set(t)) == 1:
			#print(t)
			combs = combs + 1

		elif len(set(t)) < 6:
			for j in range(6-1):
				if t[j] > t[j+1]:
					works = False
					j = 6

			if works:
				#print(t)
				combs = combs + 1
	return(combs)

#c = countCombs(start, end)
#print(c)
#967 is too high
#960

#### PART 2

def countCombs2(start, end):
	combs = 0
	for i in range(start, end+1):
		t = str(i)
		ct = collections.Counter(t)

		existsDouble = False
		for s in t:
			if ct[s] == 2:
				existsDouble = True

		if existsDouble:
			works = True
			if (len(set(t)) > 1) and (len(set(t)) < 6):
				for j in range(6-1):
					if t[j] > t[j+1]:
						works = False
						j = 6

				if works:
					#print(t)
					combs = combs + 1
	return(combs)


start = 265275
end = 781584

c = countCombs2(start, end)
print(c)
#626