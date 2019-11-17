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
        "graus": {},
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

    for i in range(minGrau, maxGrau + 1):
        results["graus"]["grau%i" % i] = 0

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

        grauName = "grau%i" % p.o

        timeBstart = time.time()
        xB, itrB = methods.bisection(p, ERROR)
        timeBend = time.time()
        timeB = (timeBend - timeBstart)

        timeSstart = time.time()
        xS, itrS = methods.secant(p, ERROR)
        timeSend = time.time()
        timeS = (timeSend - timeSstart)

        timeNstart = time.time()
        xN, itrN = methods.newton(p, ERROR)
        timeNend = time.time()
        timeN = (timeNend - timeNstart)

        if xB == None:
            results["bissection"]["ignored"] += 1
            results["bissection"]["graus"][grauName]["ignored"] += 1
        
        if xN == None:
            results["newton"]["ignored"] += 1
            results["newton"]["graus"][grauName]["ignored"] += 1

        if xS == None:
            results["secant"]["ignored"] += 1
            results["secant"]["graus"][grauName]["ignored"] += 1


        if xB != None and xN != None and xS != None:
            results["calculadoPorTodos"] += 1

            results["graus"][grauName] += 1

            results["bissection"]["avgF(x)"] += (p.__call__(xB))/quantidade
            results["bissection"]["graus"][grauName]["avgF(x)"] += (p.__call__(xB))/quantidade

            results["bissection"]["iterations"] += itrB
            results["bissection"]["graus"][grauName]["iterations"] += itrB
            
            results["bissection"]["time"] += timeB
            results["bissection"]["graus"][grauName]["time"] += timeB


            results["newton"]["avgF(x)"] += (p.__call__(xN))/quantidade
            results["newton"]["graus"][grauName]["avgF(x)"] += (p.__call__(xN))/quantidade

            results["newton"]["iterations"] += itrN
            results["newton"]["graus"][grauName]["iterations"] += itrN

            results["newton"]["time"] += timeN
            results["newton"]["graus"][grauName]["time"] += timeN


            results["secant"]["avgF(x)"] += (p.__call__(xS))/quantidade
            results["secant"]["graus"][grauName]["avgF(x)"] += (p.__call__(xS))/quantidade

            results["secant"]["iterations"] += itrS
            results["secant"]["graus"][grauName]["iterations"] += itrS

            results["secant"]["time"] += timeS
            results["secant"]["graus"][grauName]["time"] += timeS
    

    for name in ["bissection", "newton", "secant"]:
        results[name]["iterations"] = results[name]["iterations"]/results["calculadoPorTodos"]
        results[name]["time"] = results[name]["time"]/results["calculadoPorTodos"]
        for i in range(minGrau, maxGrau + 1):
            results[name]["graus"]["grau%i" % i]["iterations"] = results[name]["graus"]["grau%i" % i]["iterations"]/results["graus"]["grau%i" % i]
            results[name]["graus"]["grau%i" % i]["time"] = results[name]["graus"]["grau%i" % i]["time"]/results["graus"]["grau%i" % i]

    return results

minGrau = int(input("Informe o grau minimo:"))
maxGrau = int(input("Informe o grau maximo:"))
quantidade = int(input("Informe a quantidade de polinomios:"))
mu = int(input("Informe o valor de mu:"))
sigma = int(input("Informe o valor de sigma:"))
erro = float(input("Informe o valor do erro:"))
results = gerar_resultados(minGrau, maxGrau, quantidade, mu, sigma, erro)

print(json.dumps(results, indent=4))

with open("results.json", 'w') as json_file:
    json.dump(results, json_file)

print("fim")