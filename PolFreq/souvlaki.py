def is_english(word):
    c = word[0].lower()
    return (c>='a' and c<='z') or (c>='0' and c<='9')

f = open("sl.txt", "r")
txt = f.read().split("\n")
for i in range(0,len(txt), 7):
    head = txt[i].split(" ")
    j = 2
    if "się" in head[j]: j+=1
    #while not is_english(head[j]): j+=1
    print('frequent-polish-%04d,%s,"'%(int(head[0])," ".join(head[1:j])))
    print('<div class=""trans"">%s</div>'%" ".join(head[j:]))
    print(txt[i+1])
    print('<br>')
    print(txt[i+4].replace('"','""'))
    print('<div class=""trans"">%s</div>'%txt[i+5].replace('"','""'))
    print('"')
