'''
Implementação simples do conceito de Linear Feedback Shift Register (LFSR)
Autor: Alef Matias
'''

number, cont = '01100110', '01100110'
while True:
    last = number[-1]
    pen = number[-2]
    xor = int(pen) ^ int(last)
    new_number = str(xor) + number[:-1]
    number = new_number
    print(number, int(number, 2))
    if cont == number:
        break
