#coding:utf-8


import MeCab
import sys

from kana_to_romaji import kana_to_romaji
from Bunnsetu import SentenceBunnsetu

class Phonetic:

    
    #Mecab instance
    mecab = None
    
    ''' Initialize the mecab and kanaToRoma dictionary'''
    def __init__(self, dicUrl):
        Phonetic.mecab = MeCab.Tagger ("-Ochasen")
        self.kanaToRoma = kana_to_romaji()
        self.dropDic = {}
        #self.kanaToEng = kana_to_romaji("../Dictionary/kana_to_eng.dic")
        self.kanaToEng = kana_to_romaji(dicUrl)
        self.loadDropDic("../Dictionary/tone_drop.dic")

    def ParseMecab(self, japaneseString):
        return Phonetic.mecab.parse(japaneseString.strip())

    def KanaToRoma(self, kanaString):
        return self.kanaToRoma._convert_roma_to_kana(kanaString)

    ''' detecte the long vowel in japanese and transfer
        long vowel to english phonetic alphebate ':'  '''
    def LongVowelDetective(self, words):
        #traverse all the parts of the words
        # Long a: aa
        # Long e: ei ee
        # Long i: ii
        # Long o: oo ou
        # long u: uu
        longVowel = set(["aa","ei","ii","oo","uu","ou","ee","ɔɔ","ɔu"]) 
        
        tokens = words.split(".")
        if len(tokens) < 2:
            return words
        
        result = [tokens[0]]
        for i in range(1, len(tokens)):
            if tokens[i-1][-1] + tokens[i] in longVowel:
                #delete i element and change i-1 as long vowel
                result[-1] += ":"
                i += 1
            else:
                result.append(tokens[i])
        
        return ".".join(result).strip(".")

    def sokuonDetective(self, words):
        # k,s,t,p
        
        #print(words)
        sokuon = {"kk":"_k","ss":"_s","tt":"_t","pp":"_p"}
        tokens = words.split(".")

        
        for i in range(len(tokens)):
            for item in sokuon:
                if item in tokens[i]:
                    tokens[i] = tokens[i].replace(item, sokuon[item])
        
        return ".".join(tokens).strip(".")

    
    def sokuonDetectiveTest(self):
        
        input = ["sakka","gakko","hattatu","issyo"]
    
        result = self.sokuonDetective(".".join(input))
        
        print(result)

    def loadDropDic(self, dropDicSrc):
        
        for line in open(dropDicSrc, 'r'):
            items = line.strip().split(" ")
            if len(items) == 2:
                self.dropDic[items[0]] = items[1]

    def MatchDropDic(self, word):
        if word[0] in self.dropDic:
            word[1] = self.dropDic[word[0]]
        return(word)

    def detecHawithwa(self, segment):
        result = ""
        bunnsetu = segment.split("/")
        for i in range(len(bunnsetu)):
            tem = ""
            segs = bunnsetu[i].split(".")
            if segs[-1] == "ha":
                temp = ".".join(segs[:-1]) + ".wa."
            else:
                temp = ".".join(segs)
            result += temp + "/"
        
        return result.strip("/")

    def KanaToEnglish():
        pass


if __name__ == "__main__":

    phonetic = Phonetic(sys.argv[1])
    
    #phonetic.sokuonDetectiveTest()
    
    #test 
    #print(phonetic.detecHawithwa("wa.ta.si.ha/da.i.ga.ku.se:.de.su"))
    
    
    
    for line in sys.stdin:
        
        sentWithBun = SentenceBunnsetu(line.strip()) 
       
        result = []
        for bunnsetu in sentWithBun.split("/"):
            mecabResu = phonetic.ParseMecab(bunnsetu.strip())
            
            wordsNota = [tokens.split("\t")[:2] for tokens in mecabResu.split("\n")
                         if len(tokens.split("\t")) > 1]
            
            #wordsNota = [phonetic.MatchDropDic(tokens.split("\t")[:2]) for tokens in mecabResu.split("\n")
            #             if len(tokens.split("\t")) > 1]
            
            #wordsNota = []

            
            ####result = []
            ####for item in wordsNota:
            ####    temp = []
            ####    tokens = item[1].split("'")
            ####    if len(tokens) == 3:
            ####        for seg in tokens:
            ####            temp.append(phonetic.KanaToRoma(seg).strip("."))
            ####        temp[1] = "'" + temp[1] + "'"
            ####        result.append("".join(temp))
            ####    else:
            ####        #do not contain "'"
            ####        result.append(Phonetic.KanaToRoma(tokens))
            ####
            ####print("result is: ")
            ####print(result)
            #kana to roma
            # first split to multi segment and trasfer to roma representitively.
            
            [pairs.append(phonetic.KanaToRoma(pairs[1])) for pairs in wordsNota]
            
            [pairs.append(phonetic.sokuonDetective(phonetic.LongVowelDetective(pairs[-1]))) for pairs in wordsNota]
            #result.append(wordsNota)
            
            result.append(wordsNota)
        
        #last result
        
        #output the result
        resultStr = ""
        for res in result:
            temp = ""
            for item in res:
                temp += item[-1] + "."
            resultStr += temp.strip(".") + "/"
        
        #transfer ha and wa
        print(phonetic.detecHawithwa(resultStr.strip("/")))
        #long vowel and sokuo nn
        #for pairs in wordsNota:
        #    pairs.append(phonetic.LongVowelDetective(pairs[-1]))
        
        #detecte long vowel

        #detect soku vowel
        #for item in result:
        #    print(item)
        
        #print(type(mecabResu))
        #print(mecabResu)
        #phonetic.KanaToRoma()
