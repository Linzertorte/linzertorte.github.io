with open("ru.txt") as f:
    out = open("1.txt","wb")
    lines = [line.strip() for line in f.readlines()]
    for line in lines:
        if line[0] in "0123456789" and '.' in line:
            continue
        if len(line) < 30:
            print line
