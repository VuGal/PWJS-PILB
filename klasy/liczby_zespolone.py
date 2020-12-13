#!/usr/bin/env python3

import math


class Complex:


    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag


    def __add__(self, other):
        if isinstance(other, (float, int)):
            other = Complex(other)
        elif not ( hasattr(other, 'real') and hasattr(other, 'imag') ):
            raise TypeError('Liczba dodawana do liczby zespolonej powinna posiadac \
                             czesc rzeczywista i/lub urojona.')
        return Complex(self.real + other.real, self.imag + other.imag)


    def __radd__(self, other):
        return self.__add__(other)


    def __sub__(self, other):
        if isinstance(other, (float, int)):
            other = Complex(other)
        elif not ( hasattr(other, 'real') and hasattr(other, 'imag') ):
            raise TypeError('Liczba odejmowana od liczby zespolonej powinna posiadac \
                             czesc rzeczywista i/lub urojona.')
        return Complex(self.real - other.real, self.imag - other.imag)


    def __rsub__(self, other):
        if isinstance(other, (float, int)):
            other = Complex(other)
        return self.__sub__(self)


    def __mul__(self, other):
        if isinstance(other, (float, int)):
            other = Complex(other)
        elif not ( hasattr(other, 'real') and hasattr(other, 'imag') ):
            raise TypeError('Liczba mnozona z liczba zespolona powinna posiadac \
                             czesc rzeczywista i/lub urojona.')
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)


    def __rmul__(self, other):
        return self.__mul__(other)


    def __truediv__(self, other):
        if isinstance(other, (float, int)):
            other = Complex(other)
        elif not ( hasattr(other, 'real') and hasattr(other, 'imag') ):
            raise TypeError('Liczba, przez ktora jest dzielona liczba zespolona, \
                             powinna posiadac czesc rzeczywista i/lub urojona.')
        denom = other.real**2 + other.imag**2
        return Complex( 
            (self.real * other.real + self.imag * other.imag) / denom,
            (self.imag * other.real - self.real * other.imag) / denom
        )


    def __rtruediv__(self, other):
        if isinstance(other, (float, int)):
            other = Complex(other)
        return other / self


    def __floordiv__(self, other):
        raise NotImplementedError('Operacja dzielenia z zaokragleniem w dol nie jest wspierana.')


    def __rfloordiv__(self, other):
        raise NotImplementedError('Operacja dzielenia z zaokragleniem w dol nie jest wspierana.')


    def __pow__(self, n, z=None):
        raise NotImplementedError('Operacja podnoszenia do potegi nie jest wspierana.')


    def __rpow__(self, base):
        raise NotImplementedError('Operacja podnoszenia do potegi nie jest wspierana.')


    def __abs__(self):
        return sqrt(self.real**2 + self.imag**2)


    def __neg__(self):
        return Complex(-self.real, -self.imag)


    def __eq__(self, other):
        if isinstance(other, (float, int)):
            other = Complex(other)
        elif not ( hasattr(other, 'real') and hasattr(other, 'imag') ):
            raise TypeError('Liczba, z ktora porownywana jest liczba zespolona, powinna \
                             posiadac czesc rzeczywista i/lub urojona.')
        eps = 1e-14
        return ( (self.real - other.real < eps) and (self.imag - other.imag < eps) )


    def __ne__(self, other):
        if isinstance(other, (float, int)):
            other = Complex(other)
        elif not ( hasattr(other, 'real') and hasattr(other, 'imag') ):
            raise TypeError('Liczba, z ktora porownywana jest liczba zespolona, powinna \
                             posiadac czesc rzeczywista i/lub urojona.')
        return not self.__eq__(other)


    def __str__(self):
        return f'({self.real}, {self.imag}i)'


    def __repr__(self):
        return 'Complex' + str(self)


    def _illegal(self, op):
        print(f"Operacja '{op}' nie jest wspierana.")


    def __gt__(self, other):
        self._illegal('>')


    def __ge__(self, other):
        self._illegal('>=')


    def __lt__(self, other):
        self._illegal('<')


    def __le__(self, other):
        self._illegal('<=')


def main():

    print("\nTen program zawiera wylacznie definicje klasy Complex - patrz: kod zrodlowy.\n")


if __name__ == "__main__":

    main()

