# #Write a python program using function to find the sum of odd series and even series
# Odd series: 12/ 1! + 32/ 3! + 52/ 5!+……n
# Even series: 22/ 2! + 42/ 4! + 62/ 6!+……n

import math

def sum_odd_series(n):
    sum_odd = 0
    for k in range(1, n+1):
        i= 2*k-1
        sum_odd += (i**2)/math.factorial(i)
        return sum_odd
    
def sum_even_series(n):
    sum_even = 0
    for k in range(1, n+1):
        i = 2*k
        sum_even += (i**2)/math.factorial(i)
    return sum_even

n = 5

odd_series_sum = sum_odd_series(n)
even_series_sum = sum_even_series(n)

print(f"Sum of odd series up to {n} terms: {odd_series_sum}")
print(f"Sum of even series up to {n} terms: {even_series_sum}")