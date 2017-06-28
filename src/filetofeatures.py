import sys 
import re
import os

def isNumber(inputVal):
	try:
   		val = float(inputVal)
	except ValueError:
   		val = -1

	number = (1 if val>0 else 0)
	return number

def isAlphabet(inputVal):
	alpha = (1 if inputVal.isalpha() > 0 else 0)
	return alpha


file = open(sys.argv[1])

tokens = sys.argv[1].split('/')
outputfile = tokens[len(tokens)-1]
outputfile = outputfile.replace('.png','.feat')

testfile = open('/Users/talha/Documents/Workspace/pricerightnlp/src/'+outputfile,'w')

for line in file.readlines():

	line = line.replace('\r\n','')
	tokens = re.split(' |, |,',line)
	number = -1

	tokens = [token for token in tokens if len(token) != 0]

	for index in range(0,len(tokens)):

		token = tokens[index]
		
		try:
			nextToken = tokens[index+1]
		except:
			nextToken='null'

		try:
			prevToken = tokens[index-1]
		except:
			prevToken='null'

		testfile.write(token + " ")
		
		number = isNumber(token)
		testfile.write(str(number)+" ")

		alphabet = isAlphabet(token)
		testfile.write(str(number)+" ")

		number = isNumber(alphabet)
		testfile.write(str(number) + " ")

		number = isNumber(nextToken)
		testfile.write(str(number) + " ")

		testfile.write(str(len(token)) + " ")

		testfile.write(prevToken + " ")
		testfile.write(nextToken)


		testfile.write("\n")

	testfile.write("\n")

testfile.close()
