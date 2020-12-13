#!/usr/bin/env python3

import numpy as np


msize = np.random.randint(2,10)
matrix = np.random.randint(1000, size=(msize, msize))
mdet = np.linalg.det(matrix)

print(f"\nMacierz:\n{matrix}\n\nWyznacznik macierzy:\n{mdet}\n")

