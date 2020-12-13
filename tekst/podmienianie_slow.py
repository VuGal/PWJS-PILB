#!/usr/bin/env python3

import re


words_replacement_dict = { 'i ' : 'oraz ', ' i' : ' oraz', 'oraz ' : 'i ', ' oraz' : ' i', 'nigdy ' : 'prawie nigdy ', ' nigdy' : ' prawie nigdy', 'dlaczego ' : 'czemu ', ' dlaczego' : ' czemu' }

with open('sample_text_file.txt', 'r') as file:
    words = re.findall(r'\S+\s|\s\S+', file.read())

words[:] = [words_replacement_dict[word] if word in words_replacement_dict else word for word in words]

with open('sample_text_file_new.txt', 'w') as file:
    file.writelines(words)
    file.close()

