import find_roots_interval

def bissecao(polynomial, E):
    a, b = find_roots_interval.budan_fourier(polynomial)

    x = 0.0
    itr = 0

    while abs((b - a)/2) > E:

        x = (a + b)/2

        if polynomial.__call__(a) * polynomial.__call__(x) < 0:
            b = x
        else:
            a = x

        itr += 1
    
    return x, itr

def newton(polynomial, E):
    a, b = find_roots_interval.budan_fourier(polynomial)

    pd1 = polynomial.deriv(1)
    pd2 = polynomial.deriv(2)

    x0 = None

    calcA = polynomial.__call__(a) * pd2.__call__(a)
    calcB = polynomial.__call__(b) * pd2.__call__(b)
    if calcA > 0:
        x0 = a
    elif calcB > 0:
        x0 = b
    else:
        return None, None

    fxp1 = lambda x: x - polynomial.__call__(x)/pd1.__call__(x)
    itr = 0

    x1 = fxp1(x0)
    while abs(x1 - x0) > E:
        x0 = x1
        x1 = fxp1(x0)
        itr += 1
    
    return x1, itr