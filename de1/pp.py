# coding:utf-8
W_FILE = "18.txt"
w = open(W_FILE, "r")
word = w.readlines()
word = "\n".join([x.rstrip() for x in word])
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
for w in words:
    print w
