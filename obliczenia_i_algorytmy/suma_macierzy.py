#!/usr/bin/env python3

import numpy as np

#############################################################
# Po odkomentowaniu program wypisuje pelne postaci macierzy #
#############################################################
# import sys
# np.set_printoptions(threshold=sys.maxsize)
#############################################################


a = np.random.randint(1000, size=(128, 128))
b = np.random.randint(1000, size=(128, 128))

addition_result = np.add(a, b)

print(f"\nMacierz a:\n{a}\n\nMacierz b:\n{b}\n\nSuma macierzy:\n{addition_result}\n")

