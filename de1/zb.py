# coding:utf-8
LESSON = 14
CNT = 56
W_FILE = "14.txt"
JS_FILE = "de1_14.json"

head = '''<html>
   <head>
      <title>Russian Vocabulary</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
      <link rel="stylesheet" href="bootstrap.min.css">
      <script src="jquery.min.js"></script>
      <script src="popper.min.js"></script>
      <script src="bootstrap.min.js"></script>
      <script src="howler.core.min.js"></script>
      <script src="howler.min.js"></script>
      <style>
         body {
            padding-top: 2em;
            background-color: #F8F8F8;
         }
         table {
           table-layout: fixed;
           word-wrap: break-word;
         }
         tr {
            background-color: white;
         }
         td {
            word-break: break-all;
         }
      </style>
   </head>
   <body>
      <div class="container">
         <h3>第%d课</h3>
         <table class="table">
            <tbody>'''
tail1 = '''            </tbody>
         </table>
      </div>
   </body>
   <script>
      var sound = new Howl('''
tail2 = '''      );
      function m(p){
        sound.play(p);
      }
      $('table tr').each(function(a,b){
        $(b).click(function(){
          $('table tr').css('background','white');
          $(this).css('background','#E8E8E8');
        });
      });
   </script>
</html>'''

w = open(W_FILE, "r")
word = w.readlines()
word = "\n".join([x.rstrip() for x in word])
ac = [
('а!','а́'),
('е!','е́'),
('и!','и́'),
('о!','о́'),
('у!','у́'),
('ы!','ы́'),
('э!','э́'),
('ю!','ю́'),
('я!','я́'),
]
for t in ac:
  x,y = t
  word = word.replace(x,y)
words = word.split("\n")
print head%LESSON
for i in xrange(0,CNT):
    r,c = words[i].split('|')[0],words[i].split('|')[1]
    print '''               <tr onclick="m('untitled-%02d')">'''%(i+1)
    print '''                  <td>%s</td>'''%r
    print '''                  <td>%s</td>'''%c
    print '''               </tr>'''

print tail1
js = open(JS_FILE, "r")
for l in js.readlines():
    print ' '*8+l.rstrip()
print tail2
