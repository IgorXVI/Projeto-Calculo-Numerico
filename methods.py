import find_roots_interval

def bisection(p, E):
    a, r1, r2, b = find_roots_interval.find_roots_circle(p)

    itr = 0

    x = (a + b)/2.0
    while abs(p.__call__(x)) > E:
        if itr == 500:
            return None, None
        elif p.__call__(a) * p.__call__(x) < 0:
            b = x
        elif p.__call__(b) * p.__call__(x) < 0:
            a = x
            
        itr += 1
        x = (a + b)/2.0
    
    return x, itr

def newton(p, E):
    a, r1, r2, b = find_roots_interval.find_roots_circle(p)

    pd1 = p.deriv(1)
    pd2 = p.deriv(2)

    x0 = None
    calcA = p.__call__(a) * pd2.__call__(a)
    calcB = p.__call__(b) * pd2.__call__(b)
    if calcA > 0:
        x0 = a
    elif calcB > 0:
        x0 = b
    else:
        return None, None

    itr = 0
    x1 = x0 - p.__call__(x0)/pd1.__call__(x0)
    while abs(p.__call__(x1)) > E:
        if pd1.__call__(x0) == 0 or itr == 500:
            return None, None

        x0 = x1
        x1 = x0 - p.__call__(x0)/pd1.__call__(x0)
        itr += 1

    return x1, itr

def secant(p, E):
    a, r1, r2, b = find_roots_interval.find_roots_circle(p)

    itr = 0
    x0 = a
    x1 = b

    if p.__call__(x1) - p.__call__(x0) == 0:
        return None, None

    m_n = x1 - ( (x1 - x0) / (p.__call__(x1) - p.__call__(x0)) ) * p.__call__(x1)
    while abs(p.__call__(m_n)) > E:
        if itr == 500:
            return None, None

        buff = x1
        x1 = m_n
        x0 = buff

        if p.__call__(x1) - p.__call__(x0) == 0:
            return None, None

        m_n = x1 - ( (x1 - x0) / (p.__call__(x1) - p.__call__(x0)) ) * p.__call__(x1)
        itr += 1

    return m_n, itr