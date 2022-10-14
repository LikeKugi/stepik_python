"""
e^d + ln(d) + lg(d) + sqrt(d)

d.exp() == e^d
d.ln() == ln(d)
d.log10() == lg(d)
d.sqrt() == sqrt(d) == d**0.5
"""
from decimal import *

d = Decimal(input())

print(d.exp() + d.ln() + d.log10() + d.sqrt())