import spacy
word = "uniquech01.txt"
text = "ch01.txt"

nlp = spacy.load("es_core_news_lg")


words = []
lines = []
with open(word, "r") as f:
    for line in f.readlines():
        line = line.rstrip()
        lines.append(line)
        words.append(line.split("|")[0].rstrip())
n = len(words)
cur = 0
with open(text,"r") as f:
    doc = nlp(f.read())
    for token in doc:
        token_w = token.text
        if token_w.startswith('-¿'):
            token_w = token_w[2:]
        if token_w.startswith('-¡'):
            token_w = token_w[2:]
        if token_w.startswith('-'):
            token_w = token_w[1:]
        if token_w.endswith('-'):
            token_w = token_w[:-1]
        if token_w == words[cur]:
            print(lines[cur]+"|"+token.sent.text.replace("\n", " "))
            cur += 1
            if cur == n:
                break
