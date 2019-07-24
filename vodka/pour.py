# coding: utf-8
# python3
import pickle
import requests
from os import path

TOTAL = 257

def init_cnt():
  pickle.dump(1,open("cnt.p","wb"))

def get_cnt():
  return pickle.load(open("cnt.p","rb"))

def save_cnt(cnt):
  pickle.dump(cnt,open("cnt.p","wb"))

def file_exists(f):
  return path.exists(f)

def main():
  if not file_exists("cnt.p"):
    init_cnt()
  cnt = get_cnt()
  word_file = str(cnt)+".txt"
  url = "https://linzertorte.github.io/vodka/"+word_file
  r = requests.get(url)
  if r.status_code == 404:
    return
  print(r.text)
  cnt += 1
  if cnt > TOTAL:
    cnt = 1
  save_cnt(cnt)

if __name__ == '__main__':
  main()
