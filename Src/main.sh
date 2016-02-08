#!/bin/sh

awk -F '\t' '{print $3}' ../Test/Japanese.words.testSet | python3 PhoneticForJapanese.py $1 > result_for_word
paste ../Test/Japanese.words.testSet result_for_word > ../Test/Japanese.words.testSet.result
rm result_for_word

awk -F '\t' '{print $3}' ../Test/Japanese.sentences.testSet| python3 PhoneticForJapanese.py $1 > result_for_word
paste ../Test/Japanese.sentences.testSet result_for_word > ../Test/Japanese.sentences.testSet.result
rm result_for_word
