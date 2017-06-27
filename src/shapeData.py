import nltk
from nltk import word_tokenize,pos_tag
import sys 



def isNumber(inputVal):
	try:
   		val = float(inputVal)
	except ValueError:
   		val = -1

	number = (1 if val>0 else 0)
	return number



infilename = sys.argv[1]
outfilename = "prtest.txt"
outfile = open(outfilename,'w')

lines = []
tokens = []
with open(infilename) as data:
	lines = data.readlines()

for index in range(0,len(lines)):

	line = lines[index]

	thisToken = line.split(" ")
	
	try:
   		val = float(thisToken[0])
	except ValueError:
   		val = -1


   	isNumber = (1 if val>0 else 0)

	thisToken[1]=thisToken[1].replace("\n","")
	thisToken.append(isNumber)
	tokens.append(thisToken)
	
#[word,label]

for index in range(1,len(tokens)-1):
	
	#word
	outfile.write(str(tokens[index][0]))
	outfile.write(" ")

	#isnumber
	outfile.write(str(tokens[index][2]))
	outfile.write(" ")
	
	#prevnumber
	outfile.write(str(tokens[index-1][2]))
	outfile.write(" ")
	
	#nextnumber
	outfile.write(str(tokens[index+1][2]))
	outfile.write(" ")

	#lenght of string
	outfile.write(str(len(tokens[index][0])))
	outfile.write(" ")

	#prevword
	outfile.write(str(tokens[index-1][0]))
	outfile.write(" ")

	#nextword
	outfile.write(str(tokens[index+1][0]))
	outfile.write(" ")

	#annotation
	outfile.write(str(tokens[index][1]))
	outfile.write("\n")

outfile.close()



