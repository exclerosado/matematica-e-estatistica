'''
Descrição: Imprimir a sequência Fibonacci usando lista
Autor: Alef Matias
'''

def fibonacci(n):
    a = 0
    b = 1
    lista = []

    for i in range (1, n + 1):
        lista.append(b)
        b = a + b
        a = b - a
        if a == 0:
            b = a + 1
    return lista

num = int(input('Quantos termos deseja exibir? '))

print(fibonacci(num))
