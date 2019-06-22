# coding:utf-8
LESSON = 12
CNT = 99
JS_FILE = "hd1_12.json"

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

print head%LESSON
for i in xrange(1,CNT+1):
    r,c = str(i),str(i)
    print '''               <tr onclick="m('%02d')">'''%(i)
    print '''                  <td>%s</td>'''%r
    print '''                  <td>%s</td>'''%c
    print '''               </tr>'''

print tail1
js = open(JS_FILE, "r")
for l in js.readlines():
    print ' '*8+l.rstrip()
print tail2
