import numpy
import scipy
import random
import methods

def generate_random_polynomials(min_degree, max_degree, quantity, mu, sigma):
    random_polynomials = []

    for i in range(min_degree + 1, max_degree + 2):

        print("creating polynomials of degree: %i" % (i-1))

        for j in range(1, quantity + 1):
            buff = [] 

            for k in range(i):
                buff.append(random.gauss(mu, sigma))
            
            polynomial = numpy.poly1d(buff)

            random_polynomials.append(polynomial)

            completeness = float(j/quantity*100)
            if completeness in [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]:
                print("creation %i%% complete" % (int(completeness)))

                if(completeness == 100.0):
                    print("sample polynomial of degree %i:" % (i-1))
                    print(polynomial)
    
    print("total quantity of generated polynomials: %i" % (len(random_polynomials)))
    return random_polynomials

p = numpy.poly1d([1, 3, 0, -1])
x, itr = methods.bissecao(p, 0.000000001)
print(x, itr)



