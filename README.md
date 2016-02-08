Definition of the japanese phonetic system.
besides the normal word pronounction, we also need to solve the problems of belows:
The Suprasegmentals of Japanese:
1. " Primary stress
2. ː long vowel　「ojiisan、obaasan、seppuku」
3. ꜜ　tone drops:　「kaꜜki (oyster), kakiꜜ (fence)」
4. .　Syllabification 「mo.e, a.ni.me, sai.kin」



Environment:

1. How to use python mecab tools.
https://github.com/SamuraiT/mecab-python
Installation
pip install mecab-python3
Before installing mecabpython3, make sure you have installed mecab already.

example of installtion. Assume you are using Debian-based linux.

sudo apt-get install libmecab-dev
sudo apt-get install mecab mecab-ipadic-utf8
pip install mecab-python3


How to use?
see 'test.py' as a sample program.

Simple example

import MeCab
mecab = MeCab.Tagger ("-Ochasen")
print(mecab.parse("pythonが大好きです"))

Japanese　IPA
Consonants:
|---|---|---|---|---|
| ア:ɑ/ɑ:| イ:i/i: | ウ:u(ʊ)/u:  | エ:e/e:  | オ:ɔ(ɒ)/ɔ: |
| カ:ka  | キ:ki   | ク:ku       | ケ:ke    | コ:kɔ  |
| サ:sa  | シ:ʃ(machine) | ス:s(sprint)  | セ:se(set)  | ソ:sɔ(soda)  |
| タ:ta  | チ:tʃi(chink)  | ツ:tsu(tsunami)  | テ:te(table)  | ト:tɔ(tall)  |
| ナ:na(banana)  | ニ:ni(nip)  | ヌ:nu(snoopy) | ネ:  | ノ:nɔ(noddy) |
| ハ:ha(harvest) | ヒ:hi(hippo)  | フ:fu  | ヘ:he(head)  | ホ:hɔ() |
| マ:ma(master)  | ミ:mi(mini)  | ム:mu()  | メ:me (meadow)  | モ:mɔ(morning)
| ヤ:ya/jʌ(jump) |     | ユ:yu:(you)  |      | ヨ:jɔ:(your)  |
| ラ:la(large)  | リ:li(family)  | ル:lu(Lucy)  | レ:le(leg)  | ロ:lɔ  |
| ワ:  | ヰ:  |      | ヱ:  | ヲ:  |
| ン:en  | ゛:  | ゜:  |      |      |

CaboCha
1.requirement
   GCC
   CRF++
   Mecab
2. Install CaboCHa
  homepage http://taku910.github.io/cabocha/
  ./configure --with-charset=UTF8 --with-posset=IPA
  make
  make install

3. install interface for python
   go to CaboCha-6.9.0/python
   python setup.py build
   python setup.py install
4. python3 version
   https://github.com/morishin/cabocha-python3
   python3 setup.py build
   python3 setup.py install
5. Useful Link
   ERRORS when installing Cabocha http://kumagonjp2.blog.fc2.com/blog-entry-82.html
                         http://d.hatena.ne.jp/Syo-Takasaki/20090528/1243484754
   
   ERRORS when Running .py "No libcabocha.o"
   copy licabocha.so from /usr/local/lib to usr/lib
