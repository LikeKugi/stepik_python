"""
sum([1/i! for i in range(1,int(input()+1))])
"""
from fractions import Fraction as FR
from math import factorial as FF

print(sum([FR(1, FF(i)) for i in range(1, int(input()) + 1)]))
