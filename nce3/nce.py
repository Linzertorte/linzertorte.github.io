#! coding:utf-8

import sys
fname = sys.argv[1]
audio = sys.argv[2]
title = sys.argv[3]

f = open(fname)

#将srt文件与音频文件与这个srt.py放在同一文件夹下
#运行python srt.py > 9.html
#用浏览器打开9.html就行了
#9.srt是用aegisub软件制作的





#============ 以下不要动
header = '''<html lang="en">
  <head>
    <title></title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
    <link rel="stylesheet" href="bootstrap.css">
    <link rel="stylesheet" href="bubugao.css">
    <script src="jquery.js"></script>
    <script src="bootstrap.js"></script>
  </head>
  <body>
    <div class="container">
      <h3>%s</h3>
      <div class="slidecontainer">
        <input type="range" min="1" max="20" value="3" class="slider" id="myRange">
      </div>
      <div>
        Repeat <span id="demo"> times.</span>
      </div>
      <audio id="audio-player" src="%s" controls="controls"></audio>
      <div class="slidecontainer">
        <input type="range" min="10" max="30" value="10" class="slider" id="rate">
      </div>
      <div>
        Speed x<span id="trate"></span>
      </div>
      <div>
        <input type="checkbox" id="nob">
        <label for="nob">Autoplay</label>
      </div>
      <table class="table">
         <tbody>
'''%(title,audio)

footer = '''        </tbody>
      </table>
    </div>
  </body>
  <script src="bubugao.js"></script>
</html>
'''



'''
'00:00:01,860' - > '1.860'
'''
def to_second(ts):
    hms,ms = ts.split('.')
    h,m,s = hms.split(':')
    h,m,s = map(int,(h,m,s))
    return str(h*60*60+m*60+s)+'.'+ms


print header

import json
lines = [line.rstrip() for line in f.readlines()][2:]
cnt = len(lines)
j = 1
for i in xrange(0,cnt,4):
    s,t = lines[i+1][:12], lines[i+1][-12:]
    s,t = to_second(s), to_second(t)
    lrc = json.loads(lines[i+2])['en']
    if i==0: lrc = lrc[4:-1]
    else: lrc = lrc[:-2]
    print '''            <tr data-start="%s" data-end="%s" id="p%d">
               <td>%s</td>
            </tr>'''%(s,t,j,lrc)
    j += 1
print footer
