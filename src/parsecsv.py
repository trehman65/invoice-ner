import csv
import os


#input:  CSV file
#output: Word1 label1
#....... Word2 label2
#....... Word3 label3



dirpath = "/Users/talha/Documents/Workspace/pricerightnlp/Data/pricerightdata/WBMasonData/E/"
outfilepath = "traindataE.txt"
outfile = open(outfilepath,'w')


csvfilespath = [file for file in os.listdir(dirpath) if file.endswith('.csv')]

for infilename in csvfilespath:

	wordlabelpairs=[]
	
	print "Processing ",infilename
	csvfile = open(dirpath+infilename)
	reader = csv.reader(csvfile)
	rows = list(reader)

	classes = [['ITEM','I-ITEM'], ['B-DES','I-DES'],['QTY','I-QTY'],['QTY','I-QTY'],['UM','I-UM'],['PRICE','I-PRICE'],['PRICE','I-PRICE']]

	for rowindex in range(1,len(rows)):
		
		row = rows[rowindex]
		for index in range(0, len(row)):

			row[index] = row[index].replace(" ",',')
			cells = row[index].split(',')

			#token contains each cell
			for cellindex in range(0,len(cells)):
				
				if (len(cells[cellindex]) == 0):
					continue

				word = cells[cellindex]
				label = classes[index][cellindex>0]
				wordlabelpairs.append([word,label])

	# print wordlabelpairs
				outfile.write(cells[cellindex])
				outfile.write(" ")	
				outfile.write(classes[index][cellindex>0])
				outfile.write("\n")
		outfile.write(". PERIOD")
		outfile.write("\n")


outfile.close()
