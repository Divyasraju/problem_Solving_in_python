
import math




def nth_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number%2==0:
        return False
    counter=3
    while counter * counter <=number:
        if number%2==0:
            return False
    else:
        counter += 2
        return True

numPrimes = 1;
number = 1;

while numPrimes < 10001:
    number = number + 2
    if nth_prime(number):
        numPrimes+=1

print(nth_prime(3))
