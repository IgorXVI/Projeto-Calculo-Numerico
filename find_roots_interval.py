def find_roots_circle(polynomial):
    '''
    polynomial: polinômio unidimensional
    '''

    # aqui é feita uma cópia do array contendo os
    # coeficientes do polinômio
    cAbs = polynomial.c.copy()
    # aqui cada um dos coeficientes é convertido
    # para o seu valor em módulo
    cAbs = [abs(c) for c in cAbs]

    # aqui é feita uma cópia do array de coeficientes 
    # em módulo
    cA = cAbs.copy()
    # aqui é removido o primeiro elemento do array de 
    # coeficientes em módulo 
    cA.pop(0)
    # aqui o maior valor do array de coeficientes em
    # módulo sem o primeiro elemento é salvo na 
    # variável "A"
    A = max(cA)
    # aqui é feito o cálculo do "R" conforme 
    # visto em aula, cAbs[0] é o primeiro elemento
    # do array de coeficientes em módulo
    R = 1 + A/cAbs[0]

    # aqui é feita uma cópia do array de coeficientes 
    # em módulo
    cB = cAbs.copy()
    # aqui é removido o último elemento do array de 
    # coeficientes em módulo 
    cB.pop()
    # aqui o maior valor do array de coeficientes em
    # módulo sem o último elemento é salvo na 
    # variável "B"
    B = max(cB)
    # aqui é feito o cálculo do "r" conforme 
    # visto em aula, cAbs[-1] é o último elemento 
    # do array de coeficientes em módulo
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