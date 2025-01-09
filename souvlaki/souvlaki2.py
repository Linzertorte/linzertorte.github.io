f = open("sl.txt", "r")
txt = f.read().split("\n")
for i in range(0,len(txt), 7):
    head = txt[i].split(" ")
    print('%s\t%s'%(head[1]," ".join(head[2:])))