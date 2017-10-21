<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>



任务app 我用的Remember the milk. 点击 [文章]

Remeber the milk 任务批量添加工具 [批量添加]

这里许多文章介绍了，有的同时也介绍了其他类似的app. Remember the milk可能中国境内没法用，可以试试其他的。实在不行就找张纸打勾。
再不会自杀..
{% highlight python %}
X = 48
def ok(i):
    return i>=1 and i<=X
def add(x):
    return ' %2d'%x if ok(x) else ''
intervals = [0,1,2,4]
#intervals = [0,1,2,4,7,15,0]
Y = max(intervals)
for i in xrange(1,X+1+Y):
    s =  '%02d:'%i
    for t in intervals:
        s += add(i-t)
    print s + ' #N1'
{% endhighlight %}


List总数: <input type="text" name="day" value="48" id="day"><br>
复习间隔: <input type="text" name="interval" value="0,1,2,4,7,15,0" id="interval"><br>
<input type="submit" value="Submit" id="submit">


<div id="plan">
</div>

<script>
function ok(x,day){
  return x>=1 && x<=day;
}
function format(x){
  if(x<10)
    return " "+x.toString();
    else 
  return x.toString();
}
function add(x,day){
  if(ok(x,day)){
    return " "+format(x);
  }else {
    return "";
  }
}
function task(day,interval){
  var X = day;
  var Y = Math.max.apply(null,interval);
  var s ="";
  for(var i=1;i<=X+Y;i++){
    s += format(i)+":";
    for(var t in interval){
      s+=add(i-interval[t],X);
    }
    s+=" #N1<br>\n"
  }
  return s;
  
};
    $("#submit").click(function(){
        var day = parseInt($("#day").val());
        var b = $("#interval").val();
        b = b.split(",");
        console.log(b);
        var interval = [];
        for(var x in b){
            interval.push(+b[x]);
        }
        var s= task(day,interval);        
        $("#plan").html(s);
        console.log(interval);
    });
</script>

[文章]: http://www.jianshu.com/search?q=Remember%20The%20Milk&page=1&type=note
[批量添加]: http://files.alnorth.com/rtm/index.html
