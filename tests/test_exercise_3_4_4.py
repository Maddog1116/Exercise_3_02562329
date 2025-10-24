try:
    from polynomials import Polynomial
except ImportError:
    pass
import pytest


@pytest.mark.parametrize(
    "f, x, val",
    (((0, 1), 8, 8),
     ((2, 0, 3), -3, 29),
     ((4, 2), -11, -18))
    )
def test_call(f, x, val):
    assert Polynomial(f)(x) == val

def __call__(self, x):
        result = 0
        for i, coef in enumerate(self.coefficients):
            result += coef * (x ** i)
        return result
