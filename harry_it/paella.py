# -*- coding: utf-8 -*-

import fileinput
import urllib
import sys

head = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
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
  <span style="font-size:30px;cursor:pointer" id="hamburger">&#9776;</span>
  <div id="entry">
    <div id="sent">
    Sentence
    </div>
    <div id="dict-entry">
    </div>
  </div>
</body>
<script src="script.js"></script>
</html>
'''
print(head)
print(title)
print(s)
for l in fileinput.input():
  l = l.rstrip()
  if l == "":
    continue
  print('      <li><a href="" data-sent="%s">%s</a></li>'%(l.split("\t")[1],l.split("\t")[0].rstrip()))

print(tail)
