<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>



任务app 我用的Remember the milk. 点击 [文章]

这里许多文章介绍了，有的同时也介绍了其他类似的app. Remember the milk可能中国境内没法用，可以试试其他的。实在不行就找张纸打勾。
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



{% highlight python %}

{% endhighlight %}

<script>
    $("#submit").lick(function(){
        console.log($("#day").val());
    });
</script>

[文章]: http://www.jianshu.com/search?q=Remember%20The%20Milk&page=1&type=note
