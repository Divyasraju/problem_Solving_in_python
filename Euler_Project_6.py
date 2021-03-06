'''The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''

sum_of_hundred_squares=0
square_of_sum=0

for x in range(1,101):
    sum_of_hundred_squares += x ** 2

for y in range(1,101):
    square_of_sum += y


print(sum_of_hundred_squares)
print(square_of_sum)


print(square_of_sum ** 2 - sum_of_hundred_squares)




