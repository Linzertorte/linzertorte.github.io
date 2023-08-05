# -*- coding: utf-8 -*-

import fileinput
import os
i = 1
for l in fileinput.input():
  l = l.rstrip()
  if l == "":
    continue
  l = l.replace('é','e')
  l = l.replace('à','a')
  l = l.replace('è','e')
  l = l.replace('ù','u')
  l = l.replace('ç','c')
  l = l.replace('â','a')
  l = l.replace('ê','e')
  l = l.replace('î','i')
  l = l.replace('ô','o')
  l = l.replace('û','u')
  l = l.replace('ë','e')
  l = l.replace('ï','i')
  l = l.replace('ü','u')
  l = l.replace("'","-")
  print 'clear'
  print 'echo '+str(i)
  i += 1
  cmd = "ruby cambridge.rb "+l + "|python trim.py"
  print cmd
  print 'read'
