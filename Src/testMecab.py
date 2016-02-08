#coding:utf-8

import MeCab
import sys


mecab = MeCab.Tagger ("-Ochasen")

for line in sys.stdin:
    print(mecab.parse(line.strip()))
