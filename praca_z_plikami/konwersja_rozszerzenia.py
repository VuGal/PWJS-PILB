#!/usr/bin/env python3

from PIL import Image
import glob


print("\nRozpoczeto konwersje plikow .jpg znajdujacych sie w biezacym katalogu (bez podkatalogow) na pliki .png ...\n") 

filenames = sorted(glob.glob('*.jpg'))

for filename in filenames:
    im = Image.open(filename)
    converted_filename = f"{filename[:-4]}.png"
    im.save(converted_filename)
    print(f"{filename}  -->  {converted_filename}")

print()

