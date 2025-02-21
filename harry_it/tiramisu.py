import fileinput
import sys,os

bch = sys.argv[1][4:10]

i = 1

for line in fileinput.input():
    line = line.rstrip()
    w,s = line.split("\t")[1].rstrip(),line.split("\t")[2].rstrip()
    if "|" in w:
        w = w.split("|")[1]
    line = "\t".join(line.split("\t")[1:])
    print('HPit%s-%04d\t%s\t%s'%(bch,i,w,s))
    i+=1 
