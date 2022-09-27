"""
factorize
"""

def factorize(n):
    if n == 1:
        return 1
    else:
        return n * factorize(n-1)

n = int(input())
print(factorize(n))