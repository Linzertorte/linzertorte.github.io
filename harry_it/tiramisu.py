import fileinput
import sys,os

bch = sys.argv[1][4:10]

i = 1

for line in fileinput.input():
    line = line.rstrip()
    print('HPfr%s-%04d\t%s'%(bch,i,line))
    i+=1  
