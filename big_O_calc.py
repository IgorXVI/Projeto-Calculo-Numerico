from math import log2
from math import sqrt
from prettytable import PrettyTable

def secant(fun, x0, x1, E):
    m_n = x1
    while abs(fun(m_n)) > E:
        fx1 = fun(x1)
        fx0 = fun(x0)
        
        if fx1 - fx0 == 0:
            # se f(x1) - f(x0) for igual a 0 significa que o método não converge
            return None

        m_n = x1 - ( (x1 - x0) / ( fx1 - fx0 ) ) * fx1

        # aqui o valor de x1 é armazenado em um buffer 
        # o valor do último x da tabela é armazendo em x1 
        # o valor anterior de x1 que está no buffer é armazenado em x0
        buff = x1
        x1 = m_n
        x0 = buff

    # retorna a raíz da função
    return m_n

def big_O_calc(n_seg):
    res1 = n_seg
    res2 = secant(lambda x: x*log2(x)-n_seg, 2.2250738585072014e-308, n_seg, 0.00000001)
    res3 = sqrt(n_seg)
    res4 = log2(n_seg)

    return res1, res2, res3, res4

while True:
    n_segs_in = input("Informe a quantidade máxima de operações por segundo da máquina A e da máquina B: ")

    n_seg, n_seg_b = map(float, n_segs_in.split(","))

    res1, res2, res3, res4 = big_O_calc(n_seg)
    res1_b, res2_b, res3_b, res4_b = big_O_calc(n_seg_b)

    table = PrettyTable(["complexidade", "max entrada em 1s A", "max entrada em 1s B", "B/A"])
    table.add_row(["n", res1, res1_b, res1_b/res1])
    table.add_row(["n*log2(n)", res2, res2_b, res2_b/res2])
    table.add_row(["n^2", res3, res3_b, res3_b/res3])
    table.add_row(["2^n", res4, res4_b, res4_b/res4])

    print(table)