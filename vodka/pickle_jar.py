# coding: utf-8
import pickle
from os import path

PICKLE_FILE = "cnt.p"

def init_cnt():
  pickle.dump(1,open(PICKLE_FILE,"wb"))

def get_cnt():
  if not path.exists(PICKLE_FILE):
    init_cnt()
  return pickle.load(open(PICKLE_FILE,"rb"))

def save_cnt(cnt):
  pickle.dump(cnt,open(PICKLE_FILE,"wb"))
