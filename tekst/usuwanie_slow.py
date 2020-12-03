#!/usr/bin/env python3

import re

unwanted_words = ['się ', ' się', 'i ', ' i', 'oraz ', ' oraz', 'nigdy ', ' nigdy', 'dlaczego ', ' dlaczego']

with open('sample_text_file.txt', 'r') as file:
    words = re.findall(r'\S+\s|\s\S+', file.read())

new_words = [word for word in words if word.lower() not in unwanted_words]

with open('sample_text_file_new.txt', 'w') as file:
    file.writelines(new_words)
    file.close()

