import sys 
import os 


dirpath = sys.argv[1]


files = [f for f in os.listdir(dirpath) if f.endswith('.txt')]


for file in files:
	abspath = dirpath+file
	os.system('python filetofeatures.py '+abspath)