import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        c = Complex(0, 0)
        c. real = self.real + no.real
        c.imaginary = self.imaginary + no.imaginary
        return c

    def __sub__(self, no):
        c = Complex(0, 0)
        c. real = self.real - no.real
        c.imaginary = self.imaginary - no.imaginary
        return c

    def __mul__(self, no):
        c = Complex(0, 0)
        c.real = self.real * no.real - self.imaginary * no.imaginary
        c.imaginary = self.real * no.imaginary + self.imaginary * no.real
        return c

    def __truediv__(self, no):
        c = Complex(0,0)
        c.real = (self.real * no.real + self.imaginary * no.imaginary) \
                 / (no.real * no.real + no.imaginary * no.imaginary)
        c.imaginary = (- self.real * no.imaginary + self.imaginary * no.real) \
                / (no.real * no.real + no.imaginary * no.imaginary)
        return c

    def mod(self):
        c = Complex(0, 0)
        c.real = math.sqrt(self.real * self.real + self.imaginary * self.imaginary)
        c.imaginary = 0.0
        return c

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':

    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(x.mod())
    print(y.mod())
 #   print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')