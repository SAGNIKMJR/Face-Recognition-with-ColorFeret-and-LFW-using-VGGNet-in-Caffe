import os
from os import walk

f = []
g= []
arr = []
mypath = "/home/siddharth/colfer/images"

for (dirpath, dirnames, filenames) in walk(mypath):
	for name in filenames:
		f.append(os.path.join(dirpath, name))

filetrain = open("train.txt",'w')
k =0
j = f[0]

for i in f:

	if (i[31] != j[31]) | (i[32] != j[32]) | (i[33] != j[33]) | (i[34] != j[34]):
		k = k+1
	filetrain.write(i+" "+ str(k))
	filetrain.write("\n")
	j=i	
	

