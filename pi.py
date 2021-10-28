'''
Descrição: Estimar o valor de Pi utitlizando o método de Monte Carlo
Autor: Alef Matias
'''

import random

def estimar_pi():
    n = 100000
    h = 0

    for i in range(1, n + 1):
        x = random.random()
        y = random.random()

        r = (x ** 2 + y ** 2) ** 0.5

        if r <= 1:
            h += 1
    p = h / n
    pi = p * 4

    return pi

print(estimar_pi())