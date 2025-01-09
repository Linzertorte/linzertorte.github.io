def is_english(word):
    c = word[0].lower()
    return c>='a' and c<='z'

f = open("sl.txt", "r")
txt = f.read().split("\n")
for i in range(0,len(txt), 7):
    head = txt[i].split(" ")
    j = 1
    while not is_english(head[j]): j+=1
    print('%s\t%s'%(" ".join(head[1:j])," ".join(head[j:])))