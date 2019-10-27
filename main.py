import numpy
import scipy
import random
import methods
from matplotlib import pyplot
from timeit import time
import json

def generate_random_polynomials(quantity, mu, sigma, minGrau, maxGrau):
    
    '''
    quantity: quantidade de polinômios a serem gerados para cada um dos graus
    mu: mu da função gauss
    sigma: sigma da função gayss
    minGrau: grau mínimo
    maxGrau: grau máximo
    '''
    
    # array a ser retornado
    random_polynomials = []

    # loop que gera todos os polinomios
    for j in range(1, quantity + 1):
        # array de coeficientes
        buff = [] 

        # aqui os graus aleátorios são gerados, o loop abaixo tem um 
        # número de iteração igual ao número do grau
        for k in range(random.randint(minGrau + 1, maxGrau + 1)):
            # aqui um coeficiente aleatório é gerado e adicionado ao array 
            # de coeficientes
            buff.append(random.gauss(mu, sigma))
        
        # aqui a função poly1d gera um polinômio com base no array de
        # coeficientes
        polynomial = numpy.poly1d(buff)

        # polinômio é adicionado ao array que vai ser retornado
        random_polynomials.append(polynomial)

    # array é retornado
    return random_polynomials

def gerar_resultados(minGrau, maxGrau, quantidade, MU, SIGMA, ERROR):
    random_polinomials = generate_random_polynomials(quantidade, MU, SIGMA, minGrau, maxGrau)

    results = {
        "minGrau": minGrau,
        "maxGrau": maxGrau,
        "quantidade": quantidade,
        "mu": MU,
        "sigma": SIGMA,
        "error": ERROR,
        "calculadoPorTodos": 0,
        "bissection": {
            "iterations": 0,
            "time": 0,
            "avgF(x)": 0,
            "ignored": 0,
            "graus": {}
        },
        "newton": {
            "iterations": 0,
            "time": 0,
            "avgF(x)": 0,
            "ignored": 0,
            "graus": {}
        },
        "secant": {
            "iterations": 0,
            "time": 0,
            "avgF(x)": 0,
            "ignored": 0,
            "graus": {}
        }
    }

    for name in ["bissection", "newton", "secant"]:
        for i in range(minGrau, maxGrau + 1):
            results[name]["graus"]["grau%i" % i] = {
                "iterations": 0,
                "time": 0,
                "avgF(x)": 0,
                "ignored": 0
            }

    for p in random_polinomials:
        print(p)

        itrBTotal = 0
        itrNTotal = 0
        itrSTotal = 0

        timeB = 0
        timeN = 0
        timeS = 0

        timeBstart = time.time()
        xB, itrB = methods.bisection(p, ERROR)
        timeBend = time.time()

        grauName = "grau%i" % p.o

        xS = None
        if xB != None:
            itrBTotal += itrB
            timeB += (timeBend - timeBstart)

            timeSstart = time.time()
            xS, itrS = methods.secant(p, ERROR)
            timeSend = time.time()

            xN = None
            if xS != None:
                itrSTotal += itrS
                timeS += (timeSend - timeSstart)

                timeNstart = time.time()
                xN, itrN = methods.newton(p, ERROR)
                timeNend = time.time()

                if xN != None:
                    itrNTotal += itrN
                    timeN += (timeNend - timeNstart)

                    results["calculadoPorTodos"] += 1
            
                    results["bissection"]["avgF(x)"] += (p.__call__(xB))/quantidade
                    results["bissection"]["graus"][grauName]["avgF(x)"] += (p.__call__(xB))/quantidade

                    results["bissection"]["iterations"] += itrBTotal
                    results["bissection"]["graus"][grauName]["iterations"] += itrBTotal
                    
                    results["bissection"]["time"] += timeB
                    results["bissection"]["graus"][grauName]["time"] += timeB


                    results["newton"]["avgF(x)"] += (p.__call__(xN))/quantidade
                    results["newton"]["graus"][grauName]["avgF(x)"] += (p.__call__(xN))/quantidade

                    results["newton"]["iterations"] += itrNTotal
                    results["newton"]["graus"][grauName]["iterations"] += itrNTotal

                    results["newton"]["time"] += timeN
                    results["newton"]["graus"][grauName]["time"] += timeN


                    results["secant"]["avgF(x)"] += (p.__call__(xS))/quantidade
                    results["secant"]["graus"][grauName]["avgF(x)"] += (p.__call__(xS))/quantidade

                    results["secant"]["iterations"] += itrSTotal
                    results["secant"]["graus"][grauName]["iterations"] += itrSTotal

                    results["secant"]["time"] += timeS
                    results["secant"]["graus"][grauName]["time"] += timeS
                else:
                    results["newton"]["ignored"] += 1
                    results["newton"]["graus"][grauName]["ignored"] += 1

            else:
                results["secant"]["ignored"] += 1
                results["secant"]["graus"][grauName]["ignored"] += 1

        else:
            results["bissection"]["ignored"] += 1
            results["bissection"]["graus"][grauName]["ignored"] += 1

    return results

results = gerar_resultados(2, 8, 1000000, 1, 100, 0.01)

print(json.dumps(results, indent=4))

with open("results.json", 'w') as json_file:
    json.dump(results, json_file)

print("fim")