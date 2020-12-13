#!/usr/bin/env python3

import os


print("\nStruktura plikow rozpoczynajaca sie od obecnego katalogu roboczego:\n") 

for root, dirs, files in os.walk(r'.'):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))

print()

