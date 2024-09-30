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
    <br>
    <br>
  </div>
  <div id="entry">
    <span style="font-size:30px;cursor:pointer" id="hamburger">&#9776;</span>
    <h1>Larousse</h1>
    <input type="text" id="word" name="word"><button type="button" id="btn">Search</button>
    <div>
      <button type="button" id="prev">Prev</button>
      <button type="button" id="next">Next</button>
    </div>
    <div id="page"></div>
  </div>
</body>
<script src="script.js"></script>
</html>
'''
col = "https://www.collinsdictionary.com/us/dictionary/spanish-english/"
print(head)
print(title)
print(s)
for l in fileinput.input():
  l = l.rstrip()
  if l == "":
    continue
  print('      <li><a href="">%s</a></li>'%(l))

print(tail)
