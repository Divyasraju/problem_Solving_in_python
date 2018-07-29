"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

def is_prime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
               break
            else:
                return True
    return False

def get_prime_factors(x):
   # This function takes a number and prints the factors
    prime_factors = []
    for i in range(1, x + 1):
        if (x % i == 0) and is_prime(i):
            prime_factors.append(i)
    return prime_factors

def max_prime_factor(num):
    max = -10000000000
    for item in get_prime_factors(num):
        if(item > max):
            max = item



print(max_prime_factor(600851475143))

