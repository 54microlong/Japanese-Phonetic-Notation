#encoding:utf-8

import sys


class kana_to_romaji():
    'convert kana to romaji'
    
    _kana_to_romaji = {}
    def __init__(self, dic_path="../Dictionary/kana_to_romaji.dic"):
        for line in open(dic_path):
            (key,value) = line.strip().split(" ") 
            kana_to_romaji._kana_to_romaji[key] = value 
       

    def _convert_roma_to_kana(self, roma_str):
        #Forward Maximum(4) Matching method
        suplited_words = []
        MAX_LENGTH = 4
        roma_len = roma_str.__len__()
        start_point = 0
        end_point = min(MAX_LENGTH, roma_len) 
        while(start_point < roma_len):
            while(end_point >= start_point):
                sub_roma = roma_str[start_point : end_point]
                if sub_roma in kana_to_romaji._kana_to_romaji:
                    suplited_words.append(kana_to_romaji._kana_to_romaji[sub_roma])
                    suplited_words.append(".")
                    break
                else:
                    end_point -= 1
            else:
                #can not find matched item in the dictionary
                return "".join(suplited_words) + roma_str[start_point:]
            forward_len = sub_roma.__len__() 
            start_point += forward_len 
            end_point = start_point + MAX_LENGTH \
            if start_point + MAX_LENGTH < roma_len else roma_len  
            
        return "".join(suplited_words)

    def _convert_roma_to_English(self, roma_str):
        #Forward Maximum(4) Matching method
        suplited_words = []
        MAX_LENGTH = 4
        roma_len = roma_str.__len__()
        start_point = 0
        end_point = min(MAX_LENGTH, roma_len) 
        while(start_point < roma_len):
            while(end_point >= start_point):
                sub_roma = roma_str[start_point : end_point]
                if sub_roma in kana_to_romaji._kana_to_romaji:
                    suplited_words.append(kana_to_romaji._kana_to_romaji[sub_roma])
                    suplited_words.append(".")
                    break
                else:
                    end_point -= 1
            else:
                #can not find matched item in the dictionary
                return "".join(suplited_words) + roma_str[start_point:]
            forward_len = sub_roma.__len__() 
            start_point += forward_len 
            end_point = start_point + MAX_LENGTH \
            if start_point + MAX_LENGTH < roma_len else roma_len  
            
        return "".join(suplited_words)

    def _test_dic(self, roma_str):
        return kana_to_romaji._kana_to_romaji[roma_str]

    def _test_(self):
        a = kana_to_romaji()
        print(a._test_dic("no"))
        print(a._test_dic("a"))
        print(a._test_dic("hi"))
        print(a._test_dic("to"))
        print(a._convert_roma_to_kana("anohhuto")) 
    
    def _instant_test_(self):
        for line in sys.stdin:
            sys.stdout.write(self._convert_roma_to_kana(roma_str) + "\n")
            sys.stdout.flush()
if __name__ == "__main__":
    a = kana_to_romaji()
    #a._test_()
    a._instant_test_()
