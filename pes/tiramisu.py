import fileinput
import sys,os

bch = sys.argv[1][4:8]

i = 1

for line in fileinput.input():
    line = line.rstrip()
    w,s = line.split("|")[1].rstrip().lstrip(),line.split("|")[2].rstrip().lstrip()
    if "," in w:
        w = w.split(",")[1]
    print('soledad%s-%04d\t%s\t%s'%(bch,i,w,s))
    i+=1 
