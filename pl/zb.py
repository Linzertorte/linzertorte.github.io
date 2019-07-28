# coding:utf-8
import sys
L = int(sys.argv[1])
JS_FILE = 'pl_%03d.json'%L
head = '''<html>
   <head>
      <title>Assimil Polish</title>
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
         <h3>Lesson %d</h3>
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

print head%L
with open("%d.txt"%L) as f:
    for line in f.readlines():
        line = line.rstrip()
        print '''               <tr onclick="m('%s')">'''%(line)
        print '''                  <td>%s</td>'''%line
        print '''               </tr>'''
print tail1
js = open(JS_FILE, "r")
for l in js.readlines():
    print ' '*8+l.rstrip()
print tail2
