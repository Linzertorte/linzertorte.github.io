#! coding:utf-8

f = open('33.srt')  # 歌词文件
title = '11 Text 2'  # title
audio = "33.mp3"  #音频文件名 可以是mp3格式，我这里是m4a

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
    hms,ms = ts.split(',')
    h,m,s = hms.split(':')
    h,m,s = map(int,(h,m,s))
    return str(h*60*60+m*60+s)+'.'+ms


print header


lines = [line.rstrip() for line in f.readlines()]
cnt = len(lines)
j = 1
for i in xrange(0,cnt,4):
    s,t = lines[i+1][:12], lines[i+1][-12:]
    s,t = to_second(s), to_second(t)
    print '''            <tr data-start="%s" data-end="%s" id="p%d">
               <td>%d</td>
               <td>%d</td>
            </tr>'''%(s,t,j,j,j)
    j += 1
print footer
