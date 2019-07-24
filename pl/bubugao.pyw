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
    <script src="jquery.js"></script>
    <script src="bootstrap.js"></script>
    <style>
      body {
      padding-top: 2em;
      }
      .speaking {
      color:#30DFF3;
      font-weight: bold;
      }
      .slidecontainer {
      width: 100%%;
      }
      tr {
         background-color: white;
      }
      .slider {
      -webkit-appearance: none;
      width: 100%%;
      height: 1em;
      border-radius: 0.5em;
      background: #d3d3d3;
      outline: none;
      opacity: 0.7;
      -webkit-transition: .2s;
      transition: opacity .2s;
      }
      .slider:hover {
      opacity: 1;
      }
      .slider::-webkit-slider-thumb {
      -webkit-appearance: none;
      appearance: none;
      width: 2em;
      height: 2em;
      border-radius: 50%%;
      background: #30DFF3;
      cursor: pointer;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h3>%s</h3>
      <div class="slidecontainer">
        <input type="range" min="1" max="20" value="1" class="slider" id="myRange">
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
  <script>
  $( document ).ready(function() {
    var player = document.getElementById('audio-player');
    var slider = document.getElementById("myRange");
    var output = document.getElementById("demo");
    var nob = document.getElementById("nob");
    var on = true;
    var total = $('tr').length;
    output.innerHTML = slider.value;
    slider.oninput = function() {
        output.innerHTML = this.value;
    }
    $('tr').click(function() {
        play(player, this.id)
    });
    function play(player, id) {
        var tr = $('#'+id);
        $('table tr').css('background','white');
        tr.css('background','#E8E8E8');
        var start = tr.attr('data-start');
        var end = tr.attr('data-end');
        player.currentTime = start;
        player.play();
        player.ontimeupdate = function () {
          if(player.currentTime >= end) {
            player.pause();
          }
        };
    }
    function replay(p_no, cnt) {
        if(!on) return;
        if(cnt > slider.value) cnt = 1, p_no ++;
        if(p_no > total) p_no = 1;
        tr = $('#p'+p_no);
        var start = tr.attr('data-start');
        var end = tr.attr('data-end');
        player.currentTime = start;
        player.play();
        player.ontimeupdate = function() {
          if(player.currentTime >= end) {
            player.pause();
            replay(p_no, cnt+1);
          }
        };
    }
    $('#nob').change(function() {
        if (nob.checked) {
            on = true;
            replay(1,1);
        } else {
            on = false;
        }
    });
    });
  </script>
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
    o.write('''            <tr data-start="%s" data-end="%s" id="p%d">
               <td>%d</td>
               <td>%d</td>
            </tr>
'''%(s,t,j,j,j))
    j += 1
  o.write(footer)
  o.close()


from Tkinter import *
class App(Frame):
    def createWidgets(self):
        self.l1 = Label(self, text="srt文件名(例1.srt)").grid(row=1)
        self.e1 = Entry(self)
        self.e1.grid(row=1,column=1)
        self.sname = StringVar()
        self.l2 = Label(self, text="音频文件名(例1.mp3)").grid(row=2)
        self.e2 = Entry(self)
        self.e2.grid(row=2,column=1)
        self.aname = StringVar()
        self.l3 = Label(self, text="标题(例 延世1-1)").grid(row=0)
        self.e3 = Entry(self)
        self.e3.grid(row=0,column=1)
        self.title = StringVar()
        self.e1["textvariable"] = self.sname
        self.e2["textvariable"] = self.aname
        self.e3["textvariable"] = self.title

        self.b = Button(self)
        self.b['text'] = '生成网页'
        self.b.grid(row=3,column=1)
        self.b["command"] = self.say_hi
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def say_hi(self):
        f_name = self.sname.get().encode("utf-8")
        audio = self.aname.get().encode("utf-8")
        title = self.title.get().encode("utf-8")
        html(f_name,title,audio)

root = Tk()
root.title("bubugao")
app = App(master=root)
app.mainloop()
