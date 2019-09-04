import os
for i in xrange(1,13):
    cmd = 'python bubugao.py %d.srt "Lesson %02d" %d.mp3>%d.html'%(i,i,i,i)
    print cmd
    os.system(cmd)
