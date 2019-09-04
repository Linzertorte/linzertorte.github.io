import os
for i in xrange(1,9):
    cmd = 'python bubugao.py %d.srt "Lesson %d" %d.mp3>%d.html'%(i,i,i,i)
    print cmd
    os.system(cmd)
