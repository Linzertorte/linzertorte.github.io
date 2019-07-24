# coding:UTF-8

# simple program send weibo
#  |python3 vodka.py
import sys
from weibo import Weibo
text = ''
for line in sys.stdin:
  text += line
  if line=='\n':
    text+='\\n'
username = 'cpydvfuqwvslho-af61540@yahoo.com'
password = ''
wb = Weibo(username, password)
wb.add_new(text)
