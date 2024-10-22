# -*- coding: utf-8 -*-
import spacy
nlp = spacy.load('fr_core_news_lg')
f = open("1.txt")
doc = nlp("\n".join(f.readlines()))

#token.lemma_

for token in doc:
    if token.is_space:
        print("<br><br>")
    else:
        print('<a href="%s">%s</a>'%(token.lemma_,token))