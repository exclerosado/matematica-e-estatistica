'''
Descrição: Analisando a quantidade de vezes que o último dígito de um número primo aparece em um intervalo
Autor: Alef Matias
'''

def primos(n):
    raiz = int(n ** 0.5)
    for d in range(2, raiz + 1):
        if n % d == 0:
            return False
    return True

num = int(input('Intervalo desejado: '))

numerosprimos = []

for i in range(2, num):
    if primos(i):
        numerosprimos.append(i)

print(f'Primos de 1 a {num}: {numerosprimos}')
print(f'Entre 1 e {num} foram encontrados {len(numerosprimos)} números primos.\n')

ultimodigito = []

for i in range(len(numerosprimos)):
    ultimo = str(numerosprimos[i])[-1]
    ultimodigito.append(int(ultimo))

print('----------ANÁLISE----------\n')

for i in range(10):
    if ultimodigito.count(i) != 0:
        print(f'O número {i} apareceu {ultimodigito.count(i)} vez(es)!')