import sys 
import os
import re
import pickle

#*****************************************************
# EXTRACT TONE DROP INFORMATION FROM THE ORIGIN DICT *
#*****************************************************
def dict_extraction():

	origin_dict_path = os.path.join('../', 'Dictionary/nhk_pronunciation.csv') 

	tone_drop_dict_path = os.path.join('../', 'Dictionary/')

	tone_drop_dict = dict()

	with open(origin_dict_path, 'r', encoding='utf8') as origin_dict:

		for line in origin_dict:

			add_stress = re.sub('<span class="overline">', '(\'', line) 

			add_R_parenthesis = re.sub('</span>', ')', add_stress) 

			add_down_arrow = add_R_parenthesis.replace(')&#42780', ')\'') 

			rm_R_parenthesis = add_down_arrow.replace(')', '')

			rm_L_parenthesis = rm_R_parenthesis.replace('(', '')

			rm_u176 = re.sub('&#176', '', rm_L_parenthesis) 

			rm_colon = re.sub(';', '', rm_u176) 

			#PROBLEM: How to separate nopron with '.'?
			rm_nopron = re.sub('<span class="nopron">', '', rm_colon) 

			rm_nasal = re.sub('<span class="nasal">', '', rm_nopron)
			rm_enter = re.sub('\n', '', rm_nasal)

			stress_cnt =0
			for item in rm_enter:
				if item == '\'':
					stress_cnt += 1

			if stress_cnt == 1:
				rm_enter += '\''

			words = rm_enter.split()

			if words[0] not in tone_drop_dict.keys():

				tone_drop_dict[words[0]] = words[2]

			else:
				pass

	with open(tone_drop_dict_path + 'tone_drop.dic', 'w') as new_dict:

		for key in tone_drop_dict.keys():
			new_dict.write(key + ' ' + tone_drop_dict[key]+'\n')

#****************************************************
#                    MAIN FUNCTION                  *
#****************************************************
if __name__ == "__main__":

	dict_extraction()

