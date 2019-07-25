cnt = 0
with open("ru.txt") as f:
    out = open("1.txt","wb")
    lines = [line.strip() for line in f.readlines()]
    for line in lines:
        if line[0] in "0123456789" and '.' in line:
            cnt += 1
            out.close()
            out = open(str(cnt)+".txt","wb")
        out.write(line+'\n')
    out.close()
