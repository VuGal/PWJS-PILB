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
            raise TypeError('The number which is added to the complex number must have \
                             real and/or imaginary factor.')
        return Complex(self.real + other.real, self.imag + other.imag)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, (float, int)):
            other = Complex(other)
        elif not ( hasattr(other, 'real') and hasattr(other, 'imag') ):
            raise TypeError('The number which is subtracted from the complex number must have \
                             real and/or imaginary factor.')
        return Complex(self.real - other.real, self.imag - other.imag)

    def __rsub__(self, other):
        if isinstance(other, (float, int)):
            other = Complex(other)
        return self.__sub__(self)

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            other = Complex(other)
        elif not ( hasattr(other, 'real') and hasattr(other, 'imag') ):
            raise TypeError('The number which is multiplicated with the complex number must have \
                             real and/or imaginary factor.')
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, (float, int)):
            other = Complex(other)
        elif not ( hasattr(other, 'real') and hasattr(other, 'imag') ):
            raise TypeError('The number which the complex number is divided by must have \
                             real and/or imaginary factor.')
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
        raise NotImplementedError('Floor division is not supported in the Complex class.')

    def __rfloordiv__(self, other):
        raise NotImplementedError('Floor division is not supported in the Complex class.')

    def __pow__(self, n, z=None):
        raise NotImplementedError('Exponentation is not yet implemented in the Complex class.')

    def __rpow__(self, base):
        raise NotImplementedError('Exponentation is not yet implemented in the Complex class.')

    def __abs__(self):
        return sqrt(self.real**2 + self.imag**2)

    def __neg__(self):
        return Complex(-self.real, -self.imag)

    def __eq__(self, other):
        if isinstance(other, (float, int)):
            other = Complex(other)
        elif not ( hasattr(other, 'real') and hasattr(other, 'imag') ):
            raise TypeError('The number which the complex number is compared to must have \
                             real and/or imaginary factor.')
        eps = 1e-14
        return ( (self.real - other.real < eps) and (self.imag - other.imag < eps) )

    def __ne__(self, other):
        if isinstance(other, (float, int)):
            other = Complex(other)
        elif not ( hasattr(other, 'real') and hasattr(other, 'imag') ):
            raise TypeError('The number which the complex number is compared to must have \
                             real and/or imaginary factor.')
        return not self.__eq__(other)

    def __str__(self):
        return f'({self.real}, {self.imag}i)'

    def __repr__(self):
        return 'Complex' + str(self)

    def _illegal(self, op):
        print(f"Illegal operation '{op}' for Complex class.")

    def __gt__(self, other):
        self._illegal('>')

    def __ge__(self, other):
        self._illegal('>=')

    def __lt__(self, other):
        self._illegal('<')

    def __le__(self, other):
        self._illegal('<=')
