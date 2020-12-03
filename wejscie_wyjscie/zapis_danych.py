#!/usr/bin/env python3

import sys

print("Podaj kod zamka szyfrowego: ")
code = input()

if not code.isnumeric():
    sys.exit("Kod nie jest poprawny! Prawidlowy kod powinien zawierac wylacznie cyfry.\n")

print("Kod zatwierdzony!\n")

remaining_attempts = 5

while (remaining_attempts):
    print("\nPodaj kod:")
    attempt = input()

    if (attempt == code):
        print("Zamek odblokowany!\n")
        break
    else:
        remaining_attempts -= 1
        
        if (remaining_attempts):
            print(f"Podano nieprawidlowy kod. Pozostale proby: {remaining_attempts}")
        else:
            print("Podano nieprawidlowy kod. Wykorzystano wszystkie proby! Zamek zostal permanentnie zablokowany.\n")

