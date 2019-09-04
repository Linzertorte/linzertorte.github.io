#! coding:utf-8

def html(f_name,title,audio):
  f = open(f_name)  # 歌词文件
  o_name = f_name.split('.')[0]+'.html'
  o = open(o_name,'w')
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

  def to_second(ts):
    hms,ms = ts.split(',')
    h,m,s = hms.split(':')
    h,m,s = map(int,(h,m,s))
    return str(h*60*60+m*60+s)+'.'+ms


  o.write(header)
  lines = [line.rstrip() for line in f.readlines()]
  cnt = len(lines)
  j = 1
  for i in xrange(0,cnt,4):
    s,t = lines[i+1][:12], lines[i+1][-12:]
    s,t = to_second(s), to_second(t)
    lrc = lines[i+2]
    o.write('''            <tr data-start="%s" data-end="%s" id="p%d">
               <td>%s</td>
            </tr>
'''%(s,t,j,lrc))
    j += 1
  o.write(footer)
  o.close()


#html("2.srt","Lesson 2","2.mp3")
import sys
a,b,c = sys.argv[1],sys.argv[2],sys.argv[3]
html(a,b,c)
