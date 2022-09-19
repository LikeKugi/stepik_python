aTeam = int(input())
bTeam = int(input())
minDivider = aTeam
while minDivider % aTeam != 0 or minDivider % bTeam != 0:
    minDivider += 1
print(minDivider)
