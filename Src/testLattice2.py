#!/usr/bin/python
# -*- coding: utf-8 -*-

import MeCab
import sys
import string

sentence = "太郎はこの本を二郎を見た女性に渡した。"

try:
    
    print MeCab.VERSION
    model = MeCab.Model(" ".join(sys.argv))
    tagger = model.createTagger()
    
    # print tagger.parse(sentence)
    
    # n = tagger.parseToNode(sentence)
    
    # while n:
    #     print n.surface, "\t", n.feature, "\t", n.cost
    #     n = n.next
    # print "EOS"
    
    lattice = MeCab.Lattice()
    lattice.set_sentence(sentence)
    lattice.set_request_type(0)
    print lattice.request_type()
    tagger.parse(lattice)
    len = lattice.size()
    for i in range(len + 1):
        b = lattice.begin_nodes(i)
        while b:
            print "B[%d] %s\t%s" % (i, b.surface, b.feature)
            b = b.bnext
        e = lattice.end_nodes(i)
        while e:
            print "E[%d] %s\t%s" % (i, e.surface, e.feature)
            e = e.bnext
    print "EOS"
    
    lattice.set_sentence(sentence)
    lattice.set_request_type(MeCab.MECAB_NBEST)
    tagger.parse(lattice)
    for i in range(10):
        lattice.next()
        print lattice.toString()
    
    d = model.dictionary_info()
    while d:
        print "filename: %s" % d.filename
        print "charset: %s" %  d.charset
        print "size: %d" %  d.size
        print "type: %d" %  d.type
        print "lsize: %d" %  d.lsize
        print "rsize: %d" %  d.rsize
        print "version: %d" %  d.version
        d = d.next

except RuntimeError, e:
    print "RuntimeError:", e