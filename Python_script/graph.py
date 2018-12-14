import sys
from tabulate import tabulate

# COMMAND: python graph.py 'InputPositions' 'resultT2'
# INPUT: Pathway to text based files.
# OUTPUT: Table and bar chart

def main():
	f = open(sys.argv[1])
	countArr = []
	absPos = []
	absPosStr = ''
	freq = []
	ID = []
	comboArr = []
	comboArrStr = []
	check = 0
	numPos = 0
	sumCount = 0
	line = f.readline()
	if "\t" not in line:
		tmpRead = line.split(' ')
	else:
		tmpRead = line.split('\t')
	while line:
		absPos.append(tmpRead[0])
		if check != 1:
			absPosStr = absPosStr + tmpRead[0]
			check = 1
		else:
			absPosStr = absPosStr + '\t' + tmpRead[0]
		line = f.readline()
		if "\t" not in line:
			tmpRead = line.split(' ')
		else:
			tmpRead = line.split('\t')

	f.close()

	f = open(sys.argv[2])
	line = f.readline()
	if "\t" not in line:
		tmpRead = line.split(' ')
	else:
		tmpRead = line.split('\t')
	while line:
		countArr.append(tmpRead[0])
		freq.append(float(tmpRead[0]))
		tmpRead = tmpRead[1:]
		#tmpRead.pop(0)
		if check != 0:
			numPos = len(tmpRead)
			check = 0
		tmpStr = ''
		for x in tmpRead:
			comboArr.append(x)
			if tmpStr == '':
				tmpStr = tmpStr + x
			else:
				tmpStr = tmpStr + '\t' + x
		comboArrStr.append(tmpStr)
		line = f.readline()
		if "\t" not in line:
			tmpRead = line.split(' ')
		else:
			tmpRead = line.split('\t')

	f.close()

	for i in range(len(countArr)):
		ID.append(i+1)
		sumCount = sumCount + freq[i]

	for i in range(len(freq)):
		freq[i] = freq[i] / float(sumCount)
	

	t = PrettyTable(['ID', 'Count', 'Frequency',absPosStr,])
	for i in range(len(comboArrStr)):
		t.add_row([ID[i], countArr[i],freq[i],comboArrStr[i]])
	print t
	#print(countArr)
	#print(absPos)
	#print(absPosStr)
	#print(freq)
	#print(ID)
	#print(comboArr)
	#print(comboArrStr)
	#print(check)
	#print(numPos)
	#print(sumCount)
	return
main()
