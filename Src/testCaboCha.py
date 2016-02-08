#!/usr/bin/python
# -*- coding: utf-8 -*-

import CaboCha
import sys


while(1):
	c = CaboCha.Parser()

	#sentence = "太郎はこの本を二郎を見た女性に渡した。"
	sentence = sys.stdin.readline()

	tree =  c.parse(sentence)
	
	print tree.toString(CaboCha.FORMAT_TREE)
	for i in range(tree.chunk_size()):
	    chunk = tree.chunk(i)
	    print 'chunk'+str(i)
	    for j in range(chunk.token_pos,chunk.token_pos+chunk.token_size):
	        print tree.token(j).surface,
	    print
