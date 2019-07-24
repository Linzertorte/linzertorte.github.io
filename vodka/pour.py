# coding: utf-8
import pickle_jar
import requests

TOTAL = 257

def main():
  cnt = pickle_jar.get_cnt()
  word_file = str(cnt)+".txt"
  url = "https://linzertorte.github.io/vodka/"+word_file
  r = requests.get(url)
  if r.status_code == 404:
    return
  print(r.text)
  cnt += 1
  if cnt > TOTAL:
    cnt = 1
  pickle_jar.save_cnt(cnt)

if __name__ == '__main__':
  main()
