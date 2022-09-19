'''
Напишите программу, которая вычисляет процентное содержание
символов G (гуанин) и C (цитозин) в введенной строке
(программа не должна зависеть от регистра вводимых символов).
'''

genome = input()
count = 0
count = genome.upper().count('g'.upper()) + genome.upper().count('c'.upper())
print(count / len(genome) * 100)