#!/usr/bin/env python3

import numpy as np


coeffs = ['a', 'b', 'c']

for coeff in coeffs:
  while True:
    print(f"\nPodaj wspolczynnik {coeff}: ")
    try:
      globals()[coeff] = input()
      globals()[coeff] = float(globals()[coeff])
      break
    except:
      print("\nWprowadzono nieprawidlowy wspolczynnik! Sprobuj jeszcze raz.\n")

roots = np.roots([a, b, c])

if (roots[0] == roots[1]):
    print(f"\n\nZnaleziono jedno miejsce zerowe:\n\nx0 = {roots[0]}\n")
else:
    print(f"\n\nZnaleziono dwa miejsca zerowe:\n\nx1 = {roots[0]}\nx2 = {roots[1]}\n")

