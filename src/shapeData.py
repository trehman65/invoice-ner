import nltk
import sys 

infilename = sys.argv[1]
outfilename = "formatedtrainingdata.txt"
outfile = open(outfilename,'w')

lines = []
tokens = []
with open(infilename) as data:
	lines = data.readlines()

for index in range(0,len(lines)):

	if len(lines[index]) < 3:
		continue
	
	line = lines[index]
	thisToken = line.split(" ")
	#print thisToken[1]
	thisToken[1]=thisToken[1].replace("\r\n","")
	captial = (1 if thisToken[0]==thisToken[0].capitalize() else 0)
	thisToken.append(captial)

	tokens.append(thisToken)

#[word,label,iscapital]

for index in range(1,len(tokens)-1):
	

	#word
	outfile.write(str(tokens[index][0]))
	outfile.write(" ")
	#thiscapital
	outfile.write(str(tokens[index][2]))
	outfile.write(" ")
	#prevcaptical
	outfile.write(str(tokens[index-1][2]))
	outfile.write(" ")
	#nextcaptical
	outfile.write(str(tokens[index+1][2]))
	outfile.write(" ")
	#prevword
	outfile.write(str(tokens[index-1][0]))
	outfile.write(" ")
	#nextlabel
	outfile.write(str(tokens[index+1][0]))
	outfile.write(" ")
	#annotation
	outfile.write(str(tokens[index][1]))
	outfile.write("\n")

outfile.close()



