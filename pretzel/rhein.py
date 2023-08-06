# -*- coding: utf-8 -*-
CNT =  19
HEAD = '''<html>
   <head>
      <title>German Vocabulary</title>
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
          <table class="table">
            <tbody>      
 '''
print HEAD
print '         <h3>第%d课</h3>'%CNT
print '''<tr onclick="m('untitled-1')"><td>'''
i = 1
f = open("%d.txt"%CNT,"r")
for line in f.readlines():
    line = line.rstrip()
    if line == '==':
        i += 1
        print "</td></tr>"
        print
        print '''<tr onclick="m('untitled-%d')"><td>'''%i
    else:
        print line + "<br>"

MIDDLE = '''</td></tr>
            </tbody>
         </table>
      </div>
   </body>
   <script>
      var sound = new Howl(
        {
          "src": [
            "%d.webm"
          ],
          html5: true,
          "sprite": {
'''%CNT
print MIDDLE
f = open("%d.srt"%CNT,"r")
i = 1
for line in f.readlines():
    line = line.rstrip()
    if "-->" not in line:
        continue
    a,b = line.split(" --> ")
    #print a
    #print b
    h,m,s = a.split(":")
    s = int(s.split(",")[0])*1000+int(s.split(",")[1])
    h,m = int(h),int(m)
    a = 1000*(h*3600+m*60)+s
    #print a
    h,m,s = b.split(":")
    s = int(s.split(",")[0])*1000+int(s.split(",")[1])
    h,m = int(h),int(m)
    b = 1000*(h*3600+m*60)+s
    #print b
    print """            "untitled-%d": ["""%i
    i += 1
    print "              %d,"%a
    print "              %d"%(b-a)
    print "            ],"

TAIL = '''           
          }
        });
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
</html>
'''
print TAIL
