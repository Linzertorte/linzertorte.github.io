# coding:utf-8

# audiosprite -o zb1_01 -f howler -e mp3 *.mp3

LESSON = 1
CNT = 52

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
tail = '''            </tbody>
         </table>
      </div>
   </body>
   <script>
      var sound = Howl(
      );
      function m(p) {
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
    print '''               <tr onclick="m('%03d')">'''%i
    print '''                  <td>%d</td>'''%i
    print '''                  <td>%d</td>'''%i
    print '''               </tr>'''
print tail
