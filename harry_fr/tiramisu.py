import fileinput
import sys,os
i = 1
for line in fileinput.input():
    line = line.rstrip()
    print('HPfrb1ch13-%04d\t%s'%(i,line))
    i+=1  
