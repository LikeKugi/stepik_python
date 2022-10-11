"""
Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику, либо информатику, либо оба этих предмета.
У руководителя школы есть списки изучающих каждый предмет.

Напишите программу, позволяющую руководителю выяснить, сколько учеников изучает только один предмет.
"""

m = int(input())
n = int(input())
math_pupils = {input() for _ in range(m)}
cs_pupils = {input() for _ in range(n)}

print(len(math_pupils ^ cs_pupils) if math_pupils ^ cs_pupils else 'NO')