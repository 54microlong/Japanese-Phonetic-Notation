#!/usr/bin/python
# -*- coding: utf-8 -*-

import CaboCha


def SentenceBunnsetu(input):
	c = CaboCha.Parser()
	print(c.parseToString(sentence))

	tree =  c.parse(input)
	output = ""
	# print(tree.toString(CaboCha.FORMAT_TREE))
	for i in range(tree.chunk_size()):
	    chunk = tree.chunk(i)
	    for j in range(chunk.token_pos,chunk.token_pos+chunk.token_size):
	        output += (tree.token(j).surface)
	    output+="/"
	output=output[:-1]
	return output

if __name__ == "__main__":
    sentence = "太郎はこの本を二郎を見た女性に渡した。"
    sentence = "私は大学生です"
    print(SentenceBunnsetu(sentence))
