# coding:utf-8
import os
for i in xrange(1,101):
    cmd = 'python zb.py %d > %d.html'%(i,i)
    os.system(cmd)
