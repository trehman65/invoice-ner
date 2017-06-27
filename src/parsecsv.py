import csv
import os

#input:  CSV file
#output: Word1 label1
#....... Word2 label2
#....... Word3 label3



dirpath = "/Users/talha/Documents/Workspace/pricerightnlp/Data/pricerightdata/WBMasonData/A/"
outfilepath = "traindata.txt"
outfile = open(outfilepath,'w')


csvfilespath = [file for file in os.listdir(dirpath) if file.endswith('.csv')]

for infilename in csvfilespath:
	
	print "Processing ",infilename
	csvfile = open(dirpath+infilename)
	reader = csv.reader(csvfile)
	rows = list(reader)

	classes = [['ITEM','I-ITEM'], ['B-DES','I-DES'],['QTY','I-QTY'],['UM','I-UM'],['PRICE','I-PRICE']]

	for rowindex in range(1,len(rows)):
		
		row = rows[rowindex]
		for index in range(0, len(row)-1):

			row[index] = row[index].replace(" ",',')
			tokens = row[index].split(',')
			
			for tokenindex in range(0,len(tokens)):
				if (len(tokens[tokenindex])== 0):
					continue
				outfile.write(tokens[tokenindex])
				outfile.write(" ")	
				outfile.write(classes[index][tokenindex>0])
				outfile.write("\n")

outfile.close()
