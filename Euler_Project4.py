'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''

max_val = 0
val1 = 0
val2 = 0
for a in range(100, 1000):
    for b in range(101, 1000):  # avoid duplicates
        prod = a * b
        if prod > max_val and str(prod) == (str(prod)[::-1]):
            val1 = a
            val2 = b
            max_val = prod


print(val1)
print(val2)
print(max_val)