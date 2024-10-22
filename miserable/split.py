import fileinput
i = 0
j = 1
f = open("%03d.txt"%j,"a")
for line in fileinput.input():
    f.write(line)
    i = i + 1
    if i == 30:
        i = 0
        j = j + 1
        f.close()
        f = open("%03d.txt"%j,"a")
f.close()