import cmath


class ComplexNumber:

    def __init__(self, re=0.0, im=0.0):
        self.re = re
        self.im = im

    def __repr__(self):
        return f"({self.re}{'+' if self.im >= 0 else '-'}{abs(self.im)}j)"

    def __add__(self, other):
        if isinstance(other, (float, int)):
            other = ComplexNumber(other)
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __radd__(self, other):
        if isinstance(other, (float, int)):
            other = ComplexNumber(other)
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, (float, int)):
            other = ComplexNumber(other)
        return ComplexNumber(self.re - other.re, self.im - other.im)

    def __rsub__(self, other):
        if isinstance(other, (float, int)):
            other = ComplexNumber(other)
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            other = ComplexNumber(other)
        return ComplexNumber(self.re * other.re - self.im * other.im,
                             self.im * other.re + self.re * other.re)

    def __truediv__(self, other):
        if isinstance(other, (float, int)):
            other = ComplexNumber(other)
        divisor = (other.re ** 2 + other.im ** 2)
        return ComplexNumber((self.re * other.re) - (self.im * other.im) / divisor,
                             (self.im * other.re) + (self.re * other.im) / divisor)


if __name__ == "__main__":
    num1 = ComplexNumber(1, 2)
    num2 = ComplexNumber(3, 4)
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} * {num2} = {num1 * num2}")
    print(f"{num1} / {num2} = {num1 / num2}")





