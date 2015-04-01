class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError
        self.numerator = numerator
        self.denominator = denominator
        self._simplify()

    def _gcd(self, a, b):
        common_factor = 1
        for i in range(min(abs(a), abs(b)), 1, -1):
            if a % i == 0 and b % i == 0:
                common_factor = i
                break
        if common_factor == 1:
            return a * b
        return common_factor

    def __add__(self, other):
        if self.denominator == other.denominator:
            return Fraction(self.numerator + other.numerator, self.denominator)
        else:
            return Fraction(self.numerator * other.denominator +
                            self.denominator * other.numerator,
                            self.denominator * other.denominator)

    def __sub__(self, other):
        if self.denominator == other.denominator:
            return Fraction(self.numerator - other.numerator, self.denominator)
        else:
            return Fraction(self.numerator * other.denominator -
                            self.denominator * other.numerator,
                            self.denominator * other.denominator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator,
                        self.denominator * other.denominator)

    def _simplify(self):
        gcd = self._gcd(self.numerator, self.denominator)
        if gcd != self.numerator * self.denominator:
            self.numerator = self.numerator // gcd
            self.denominator = self.denominator // gcd

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __str__(self):
        if self.numerator == 0:
            return str(0)
        elif self.denominator == 1:
            return str(self.numerator)
        else:
            return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()


# a = Fraction(2, 4)
# b = Fraction(1, 2)
# print(a == b)
# print(a + b)
# print(a - b)
# print(a * b)
