#!/usr/bin/env python3

import os

number_of_files = sum(len(files) for root, dirs, files in os.walk(r'/dev'))

print (f"Ilosc plikow w katalogu /dev oraz jego podkatalogach (wylacznie pliki regularne): {number_of_files}")

