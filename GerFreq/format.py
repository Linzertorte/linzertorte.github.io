def get_token(s):
    return s.split(" ")[0]
def p(bl):
    if len(bl)==0:
        return
    b = []
    for l in bl:
        if l!="":
            b.append(l)
    #print(b[0])
    #print(len(b))
    if b[4][0]!='-':
        b = b[0:3] +[b[3]+" "+b[4]] + b[5:]
    if len(b) > 5:
        b = b[0:4]+[b[4]+" "+b[5]]
    b = b[0:3]+[""]+b[3:]+[""]
    for l in b:
        print(l)
        #break    
f = open("souvlaki2.txt", "r")
block = []
txt = f.read().split("\n")
i = 0
while i < len(txt):
    if txt[i].strip().isdigit():
        pass
        #print(txt[i].strip())
    elif get_token(txt[i].strip()).isdigit():
        p(block)
        block = []
        block.append(txt[i].strip())
    else:
        block.append(txt[i].strip())
    i += 1
p(block)