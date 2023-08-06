# -*- coding: utf-8 -*-

import fileinput
from termcolor import colored
red = False
print
print
print
print
for l in fileinput.input():
  l = l.lstrip().rstrip()
  if l == "" or l == "Add to word list":
    continue
  if "●" in l:
    print colored("    "+l,"red",attrs=['bold'])
    red = True
    continue
  if red:
    print colored("    "+l,"green")
    red = False
    continue
  print "    "+l
print
print
