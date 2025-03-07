

ch_cnt = 1
uniq_words = {}

for i in range(1,ch_cnt+1):
    with open("rawch%02d.txt"%i) as fin:
        print("chapter ch%02d"%i)
        fout = open("uniquech%02d.txt"%i,"w")
        for line in fin.readlines():
            word = line.split("|")[1].rstrip()
            if word == "":
                continue
            if word in uniq_words:
                print(word)
            if word not in uniq_words:
                fout.write(line)
                uniq_words[word] = 1
