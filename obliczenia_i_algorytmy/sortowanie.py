#!/usr/bin/env python3

# Uzyto sortowania przez wstawianie ze wzgledu na efektywnosc przy niewielkiej liczbie elementow (50)

import random

nums = [random.random() for _ in range(50)]

print("\nTablica przed sortowaniem:\n")

for num in nums:
    print(num)

sorted_nums = nums

for i in range(1, len(sorted_nums)):
    key = sorted_nums[i]
    j = i-1
    while (j >= 0 and key < sorted_nums[j]):
        sorted_nums[j+1] = sorted_nums[j]
        j -= 1
    sorted_nums[j+1] = key

# Sprawdzenie poprawnosci wykonanego sortowania
if (sorted(nums) != sorted_nums):
    sys.exit("Zastosowany algorytm sortujacy nie dziala poprawnie!")

print("\n\nTablica po sortowaniu:\n")

for num in sorted_nums:
    print(num)

print()
