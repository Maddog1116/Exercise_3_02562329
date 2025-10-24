from numbers import Number


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other
    
    def __sub__(self, other):
        if isinstance(other, Polynomial):
            max_len = max(len(self.coefficients), len(other.coefficients))
            self_coeffs = list(self.coefficients) + [0] * (max_len - len(self.coefficients))
            other_coeffs = list(other.coefficients) + [0] * (max_len - len(other.coefficients))
            coefs = tuple(a - b for a, b in zip(self_coeffs, other_coeffs))
            return Polynomial(coefs)
        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] - other,) + self.coefficients[1:])
        else:
            return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, Number):
            neg_coeffs = (-c for c in self.coefficients)
            result_coeffs = list(neg_coeffs)
            result_coeffs[0] += other
            return Polynomial(tuple(result_coeffs))
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            result_len = len(self.coefficients) + len(other.coefficients) - 1
            result = [0] * result_len
            for i, a in enumerate(self.coefficients):
                for j, b in enumerate(other.coefficients):
                    result[i + j] += a * b
            return Polynomial(tuple(result))
        elif isinstance(other, Number):
            return Polynomial(tuple(a * other for a in self.coefficients))
        else:
            return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, Number):
            return self * other
        else:
            return NotImplemented
        
    def __pow__(self, power):
        if power == 0:
            return Polynomial((1,))

        result = Polynomial(self.coefficients)
        for _ in range(1, power):
            result *= self  

        return result
    
    def __call__(self, x):
        result = 0
        for i, coef in enumerate(self.coefficients):
            result += coef * (x ** i)
        return result
    
    def dx(self):
        if self.degree() == 0:
            return Polynomial((0,))
        d_coefs = tuple(i * c for i,c in enumerate(self.coefficients))[1:]
        return Polynomial(d_coefs)
    
def derivative(poly):
    return poly.dx()
