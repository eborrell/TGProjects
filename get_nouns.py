#!/usr/bin/python
# -*- encoding: utf-8 -*-



def is_noun(word_type):
    if word_type == 'noun':
        return True
    else:
        return False

def is_without_adj(ger):
    ger_words = ger.split(' ')
    if ger_words[0][0].isupper():
        return True
    else:
        return False

def get_noun(line):
    if len(line.split('\t')) == 3:
        ger, eng, word_type = line.split('\t')
        if is_noun(word_type) and is_without_adj(ger):
            ger_words = ger.split(' ')
            ger_noun = ""
            is_gender = False
            gender = ""
            for word in ger_words:
                if word[0] == '{' and word[-1] == '}':
                    is_gender = True
                if not is_gender:
                    ger_noun += word + ' '
                else:
                    gender = word[1:-1]
                    break
            #print(ger_noun, gender, eng)
            return ger_noun, gender, eng
        else:
            return []
    else: #let is ignore this case so far
        return []


import argparse
parser = argparse.ArgumentParser(description='Creates list of nouns.')
args = parser.parse_args()

#create f_nouns file
f_gender = open('gender.txt', 'w')
f_gender.close()
with open('gender.txt', 'a') as f_nouns:
    #read the cc file
    f_data = open('dict.cc_database.txt', 'r')
    data = f_data.read().split('\n')
    for line in data:
        if get_noun(line):
            ger_word, gender, eng_word = get_noun(line)
            f_nouns.write(ger_word + '\t' + gender + '\t' + eng_word + '\n')
    f_data.close()
f_gender.close()