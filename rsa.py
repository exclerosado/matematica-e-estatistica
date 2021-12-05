'''
Program: Testing the complexity of finding the two prime numbers of the RSA Algorithm
Author: Alef Matias
'''

from random import randint

red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
reset = '\033[0;0m'
print('*' * 45)
print(blue + 'SIMPLE TEST OF PRIME NUMBERS ON RSA ALGORITHM' + reset)
print('*' * 45)


# Checking if the number is prime
def prime_check(number):
    if number < 2:
        return False
    square_root = int(number ** (1 / 2))
    for divisor in range(2, square_root + 1):
        if number % divisor == 0:
            return False
    return True


# Generating a list of a prime numbers in a interval
def generate_primes_list(interval):
    primes_list = []
    for iteration in range(2, interval + 1):
        if prime_check(iteration):
            primes_list.append(iteration)
    return primes_list


# Getting 2 random prime numbers of a list and multiplying them
def multiplying(array):
    while True:
        first_number = int(array[randint(0, len(array) - 1)])
        second_number = int(array[randint(0, len(array) - 1)])
        if first_number != second_number:
            product_primes = int(first_number) * int(second_number)
        else:
            print(yellow + 'Equal prime numbers. Trying again...' + reset)
            continue
        print('Product of them: ' + yellow + '{}\n'.format(product_primes) + reset)
        return product_primes


# Accepting only integer numbers
while True:
    try:
        set_interval = int(input('\nEnter the max. limit interval of the prime numbers: '))
        break
    except:
        print(yellow + 'Characters or float numbers not accepted. Enter a interger number.\n' + reset)
        continue

print('Processing...')

result = multiplying(generate_primes_list(set_interval))
array_primes = generate_primes_list(set_interval)

print('List of valid prime numbers in the selected interval: ' + blue + '\n{}\n'.format(
    array_primes) + reset)


# Accepting only integer numbers and numbers that are in the list of prime numbers
while True:
    try:
        first_guess = int(input('Enter the first prime number guess: '))
        if first_guess not in array_primes:
            print(red + 'Out of the list or not a prime number!\n' + reset)
            continue
        second_guess = int(input('Enter the second prime number guess: '))
        if second_guess not in array_primes:
            print(red + 'Out of the list or not a prime number!\n' + reset)
            continue
        guess_result = first_guess * second_guess
    except:
        print(red + 'Only integer numbers are accepted! Try again...\n' + reset)
        continue
    print('Result of operation: ' + yellow + '{}'.format(guess_result) + reset)
    if guess_result == result:
        print(green + 'Ok' + reset)
        break
    else:
        print(red + 'Fail! Try again.\n' + reset)
