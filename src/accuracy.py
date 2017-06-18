#computes accuracy of the model 
import sys 

output = open('outputpr.txt')
lines = output.readlines()
total=0
correct = 0

for line in lines:
	tokens	= line.split()

	length = len(tokens) 

	if tokens[length-2] == tokens[length-1]:
		correct = correct + 1
	total=total+1


print correct
print total 