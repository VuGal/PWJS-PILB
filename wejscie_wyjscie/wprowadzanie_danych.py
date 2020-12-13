#!/usr/bin/env python3


print("Podaj imie, nazwisko i rok urodzenia (w jednej linii):")

data = input()
split_data = data.split(' ')

try:
    print("\nImie: " + split_data[0])
    print("Nazwisko: " + split_data[1])
    print("Data urodzenia: " + split_data[2] + "\n")
except:
    print("\nDane zostaly podane w nieprawidlowy sposob!")

