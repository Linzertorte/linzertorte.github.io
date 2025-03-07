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
    <li></li>
    <li></li>
    </ul>
  </div>
  <span style="font-size:30px;cursor:pointer" id="hamburger">&#9776;</span>
  <div id="entry">
    <div id="sent">
    Sentence
    </div>
    <div id="dict-entry"></div>
    <div>
      <h1>Básico</h1>
      <input type="text" id="word" name="word"><button type="button" id="btn">Search</button>
      <div>
        <button type="button" id="prev">Prev</button>
        <button type="button" id="next">Next</button>
        <span id="page_num"></span>
      </div>
      <div id="page"></div>
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
  word = l.split("|")[1].rstrip()
  if "," in word:
    h,w = word.split(",")[0],word.split(",")[1]
    print('      <li><a href="%s" data-sent="%s">%s</a></li>'%(h,l.split("|")[2],w))
  else:
    print('      <li><a href="" data-sent="%s">%s</a></li>'%(l.split("|")[2],word))

print(tail)
