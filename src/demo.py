import sys
import os

def isNumber(inputVal):
	try:
   		val = float(inputVal)
	except ValueError:
   		val = -1

	number = (1 if val>0 else 0)
	return number



testfile = open('/Users/talha/Documents/Workspace/currentworkspace/pricerightnlp/CRF++-0.58/test.txt','w')
tokens = sys.argv[1].split()
number = -1

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

	number = isNumber(prevToken)
	testfile.write(str(number) + " ")

	number = isNumber(nextToken)
	testfile.write(str(number) + " ")

	testfile.write(str(len(token)) + " ")

	testfile.write(prevToken + " ")
	testfile.write(nextToken)


	testfile.write("\n")


testfile.close()



