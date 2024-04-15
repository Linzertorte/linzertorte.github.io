# -*- coding: utf-8 -*-

import fileinput
import urllib
import sys

head = '''
<!DOCTYPE html>
<html>
<head>
'''
title = "<title>%s</title>"%sys.argv[1].split(".")[0]
s = '''
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
  <div id="words">
    <ul>
'''
tail = '''
    </ul>
  </div>
  <div id="entry">
  </div>
</body>
<script>
  $("a").on("click", function(e) {
      e.preventDefault();
      $("a").removeClass("current");
      $(this).addClass("current");
      $.get($(this).attr("href"),function(data,s) {
        var h = $(data).find("div.dictionary").find("div.cB-def").html();
        $("#entry").html(h);
      });
  });
</script>
</html>
'''
col = "https://www.collinsdictionary.com/us/dictionary/spanish-english/"
print head
print title
print s
for l in fileinput.input():
  l = l.rstrip()
  if l == "":
    continue
  print '      <li><a href="%s">%s</a></li>'%(col+urllib.quote(l),l)

print tail
