import cmath


class WrongComplexNumberParameter(Exception):
    pass


class ComplexNumber:

    def __init__(self, re=0.0, im=0.0):
        if not isinstance(re, (float, int)) or not isinstance(im, (float, int)):
            raise WrongComplexNumberParameter("Wrong type of real or imag part of ComplexNumber. Please provide int or float.")
        self.re = re
        self.im = im

    @classmethod
    def str_format(cls, number_as_str):
        """
        Constructor from string -> provide number in 2+3j format
        """
        new_str = None
        sign = None
        signs = ['+', '-']
        for idx, char in enumerate(number_as_str):
            if char in signs:
                sign = number_as_str[idx]
                new_str = number_as_str.replace(sign, " ")
                break
        if new_str is None or sign is None:
            raise WrongComplexNumberParameter("Wrong format of string format constructor, please provide: 2+3j or 2.0+3.0j")
        else:
            re, im = new_str.split()
            im = im[:-1]
            re, im = float(re), float(im)
            im = im if sign == '+' else -im
            return cls(re, im)

    def __repr__(self):
        return f"({self.re}{'+' if self.im >= 0 else '-'}{abs(self.im)}j)"

    def __add__(self, other):
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return ComplexNumber(self.re - other.re, self.im - other.im)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        return ComplexNumber(self.re * other.re - self.im * other.im,
                             self.im * other.re + self.re * other.re)

    def __truediv__(self, other):
        divisor = (other.re ** 2 + other.im ** 2)
        return ComplexNumber((self.re * other.re) - (self.im * other.im) / divisor,
                             (self.im * other.re) + (self.re * other.im) / divisor)


if __name__ == "__main__":
    num1 = ComplexNumber(1, 3)
    num2 = ComplexNumber(3, 4)
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} * {num2} = {num1 * num2}")
    print(f"{num1} / {num2} = {num1 / num2}")





