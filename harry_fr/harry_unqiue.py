import stanza
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup



b = [0,17,18,22,37]
b = [0,17,7,22,37]
uniq_words = {}



for j in range(1,3):
    for i in range(1,b[j]+1):
        with open ("goldb%dch%02d.txt"%(j,i)) as fin:
            print("chapter b%dch%02d..."%(j,i))
            fout = open("b%dch%02d.txt"%(j,i),"w")
            for line in fin.readlines():
                word = line.split("\t")[0].rstrip()
                if word == "":
                    continue
                if word in uniq_words:
                    print(word)
                if word not in uniq_words:
                    fout.write(line)
                    uniq_words[word] = 1
