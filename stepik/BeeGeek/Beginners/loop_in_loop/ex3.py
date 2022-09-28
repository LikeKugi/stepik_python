"""
Решите уравнение в натуральных числах 28n + 30k + 31m = 365.
"""

n_max = 365//28
k_max = 365//30
m_max = 365//31

for n in range(n_max+1):
    for k in range(k_max+1):
        for m in range(m_max+1):
            if 28 * n + 30 * k + 31 * m == 365:
                print(n,k,m)