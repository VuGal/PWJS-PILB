#!/usr/bin/env python3

import numpy as np


a = np.random.randint(1000, size=(8, 8))
b = np.random.randint(1000, size=(8, 8))

multiplication_result = np.matmul(a, b)

print(f"\nMacierz a:\n{a}\n\nMacierz b:\n{b}\n\nIloczyn macierzy:\n{multiplication_result}\n")


