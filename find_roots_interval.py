def find_roots_circle(polynomial):
    cAbs = polynomial.c.copy()
    cAbs = [abs(c) for c in cAbs]

    cA = cAbs.copy()
    cA.pop(0)
    A = max(cA)
    R = 1 + A/cAbs[0]

    cB = cAbs.copy()
    cB.pop()
    B = max(cB)
    r = 1/(1 + (B/cAbs[-1]))

    return -R, -r, r, R

def budan_fourier_x(polynomial, x):
    changes = 0

    initialResult = polynomial.__call__(x)
    lastSign = initialResult >= 0

    for i in range(1, polynomial.o + 1):

        derivative = polynomial.deriv(i)
        result = derivative.__call__(x)
        sign = result >= 0
    
        if lastSign != sign:
            changes += 1
        
        lastSign = sign

    return changes

def budan_fourier_N(polynomial, x1, x2):
    changes1 = budan_fourier_x(polynomial, x1)
    changes2 = budan_fourier_x(polynomial, x2)
    N = abs(changes1 - changes2)
    return N

def budan_fourier(polynomial):
    x11, x12, x21, x22 = find_roots_circle(polynomial)

    N1 = budan_fourier_N(polynomial, x11, x12)
    N2 = budan_fourier_N(polynomial, x21, x22)

    if(N1 < N2):
        return x21, x22
    
    return x11, x12