# coding:utf-8
LESSON = 2
CNT = 57

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
tail = '''            </tbody>
         </table>
      </div>
   </body>
   <script>
      var sound = new Howl(
      );
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





word = '''как|[副]如何，怎样
лук|葱  
ко!мната|房间  
окно！|窗户  
кот|公猫  
молоко!|牛奶  
кто|[代]谁  
банк|银行
бу!ква|字母
мно!го|[副]很多  
ма!ло|[副]很少
когда!|[副]什么时候  
хо!лодно|[副]冷  
пло!хо|[副]不好，坏  
пого!да|天气  
бар|酒吧  
пар|蒸汽  
дар|礼物，恩赐
тар|塔尔琴（外高加索的一种民间拨弦乐器）
парк|公园  
ры!ба|鱼  
уро!к|课：功课  
брат|兄弟  
торт|蛋糕  
ка！рта|地图  
гру!ппа|一群；组  
у!тром|[副]（在）早晨  
клуб|俱乐部  
друг|朋友  
го!род|城市  
страна!|国家
звук|声音
за!втра|[副]明天
му!ха|苍蝇
сын|儿子
сок|果汁
суп|汤
сыр|奶酪
стол|桌子
стул|椅子
сло!во|单词
су!мка|书包
заво!д|工厂
расска!з|故事；短篇小说  
авто!бус|公共汽车
оно|[代]它
подру!га|女友  
соба!ка|狗  
зову!т(как зовут)|叫（叫什么名字）
мину!та|分钟（минуту是其第四格形式，意思是“请稍等”）
спаси!бо|[语气]谢谢
за!втрак|早饭
Ивано!в|伊万诺夫
Во!лга|伏尔加河
Москва!|莫斯科
Во!логда|沃洛格达市
Омск|鄂木斯克'''
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
    print '''               <tr onclick="m('%03d')">'''%(i+1)
    print '''                  <td>%s</td>'''%r
    print '''                  <td>%s</td>'''%c
    print '''               </tr>'''
print tail
