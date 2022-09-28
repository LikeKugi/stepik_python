"""
Имеется 100 рублей. Сколько быков, коров и телят можно купить на все эти деньги,
если плата за быка – 10 рублей, за корову – 5 рублей, за теленка – 0.5 рубля
и надо купить 100 голов скота?

10*bull + 5*cow + 0.5*calf = 100
"""

max_bull = 100 // 10
max_cow = 100 // 5
max_calf = 100 * 2

for bull in range(max_bull+1):
    for cow in range(max_cow+1):
        for calf in range(max_calf+1):
            if 10 * bull + 5 * cow + 0.5 * calf == 100 and bull + cow + calf == 100:
                print(bull,cow,calf)
