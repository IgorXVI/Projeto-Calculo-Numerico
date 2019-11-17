import find_roots_interval

def bisection(p, E):
    '''
    p é o polinômio
    E é o erro
    '''

    # aqui eu aramazeno os valores de -R e R na variáveis a e b
    a, r1, r2, b = find_roots_interval.find_roots_circle(p)

    itr = 0

    # aqui eu aplico o método de bisseção conforme visto em aula
    x = (a + b)/2.0
    # p.__call__(x) é equivalente à f(x)
    fx = p.__call__(x)
    fa = p.__call__(a)
    fb = p.__call__(b)
    while abs(fx) > E:
        if itr == 500:
            # se o número de iterações for igual à 500 
            # significa que o método não converge para o intervalo
            return None, None
        elif fa * fx < 0:
            b = x
        elif fb * fx < 0:
            a = x
            
        itr += 1
        x = (a + b)/2.0

        fx = p.__call__(x)
        fa = p.__call__(a)
        fb = p.__call__(b)
    
    # retorna a raíz da função e o número de iterações
    return x, itr

def newton(p, E):
    '''
    p é o polinômio
    E é o erro
    '''

    # aqui eu aramazeno os valores de -R e R na variáveis a e b
    a, r1, r2, b = find_roots_interval.find_roots_circle(p)

    # aqui eu aramazedo a derivada de primeira ordem do polinômio 
    # na variável pd1
    pd1 = p.deriv(1)
    # aqui eu armazeno a derivada de segunda ordem do polinômio 
    # na variável pd2
    pd2 = p.deriv(2)

    # calculo para escolher o x0, conforme visto em aula
    x0 = None
    # p.__call__(x) é equivalente à f(x) 
    # e pd2.__call__(x) é equivalente à f''(x) 
    calcA = p.__call__(a) * pd2.__call__(a)
    calcB = p.__call__(b) * pd2.__call__(b)
    if calcA > 0:
        x0 = a
    elif calcB > 0:
        x0 = b
    else:
        return None, None

    # calculo do método de newton conforme visto em aula
    itr = 0
    # pd1.__call__(x) é equivalente à f'(x)
    f1x0 = pd1.__call__(x0)
    x1 = x0 - p.__call__(x0)/f1x0
    while abs(p.__call__(x1)) > E:

        if f1x0 == 0 or itr == 500:
            # se o número de iterações for igual a 500
            # ou se o f(x0) for igual a 0
            # significa que o método não converge para o intervalo
            return None, None


        x0 = x1
        f1x0 = pd1.__call__(x0)
        x1 = x0 - p.__call__(x0)/f1x0
        itr += 1

    # retorna a raíz da função e o número de iterações
    return x1, itr

def secant(p, E):
    '''
    p é o polinômio
    E é o erro
    '''

    # aqui eu aramazeno os valores de -R e R na variáveis a e b
    a, r1, r2, b = find_roots_interval.find_roots_circle(p)

    itr = 0
    x0 = a
    x1 = b

    if p.__call__(x1) - p.__call__(x0) == 0:
        # se f(x1) - f(x0) for igual a 0 significa que o método não converge
        return None, None

    # aqui eu aplico o método das secantes conforme visto em aula 
    # com m_n sendo o último x da tabela
    fx1 = p.__call__(x1)
    fx0 = p.__call__(x0)
    m_n = x1 - ( (x1 - x0) / ( fx1 - fx0 ) ) * fx1
    while abs(p.__call__(m_n)) > E:
        if itr == 500:
            # se o número de iterações for igual à 500 
            # significa que o método não converge para o intervalo
            return None, None

        # aqui o valor de x1 é armazenado em um buffer 
        # o valor do último x da tabela é armazendao em x1 
        # o valor anterior de x1 que está no buffer é armazenado em x0
        buff = x1
        x1 = m_n
        x0 = buff

        fx1 = p.__call__(x1)
        fx0 = p.__call__(x0)
        
        if fx1 - fx0 == 0:
            # se f(x1) - f(x0) for igual a 0 significa que o método não converge
            return None, None

        m_n = x1 - ( (x1 - x0) / ( fx1 - fx0 ) ) * fx1
        itr += 1

    # retorna a raíz da função e o número de iterações
    return m_n, itr