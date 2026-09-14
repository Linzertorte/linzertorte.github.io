# coding:utf-8
import os
for i in xrange(1,78):
    cmd = 'python2 zb.py %d > %d.html'%(i,i)
    os.system(cmd)
