#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.


"""Order of 1 or O(1) solution"""
def function_demo():
    count=999
    total=0
    multiple3 = int(3*int(count/3)*(int(count/3)+1)/2)
    multiple5 =int(5*int(count/5)*(int(count/5)+1)/2)

    multiple15 = int(15*int(count/15)*(int(count/15)+1)/2)
    total=(multiple3+multiple5)-multiple15
    return total

print(function_demo())


"""O(n) solution"""

total_sum = 0
for i in range(1, 1000):
    if (i % 3 == 0 or i % 5 == 0):
        total_sum = total_sum + i
print(total_sum)
