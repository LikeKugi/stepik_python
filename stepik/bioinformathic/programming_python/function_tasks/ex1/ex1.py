def AddTeam(teams, team):
    teams[team] = [0, 0, 0, 0, 0]  # [ 0: games, 1: won, 2: pair, 3: loose, 4: scores ]


def WinAdd(teams, team_won, team_lose):
    teams[team_won][0] += 1
    teams[team_won][1] += 1
    teams[team_lose][0] += 1
    teams[team_lose][3] += 1


def PairAdd(teams, first, second):
    teams[first][0] += 1
    teams[first][2] += 1
    teams[second][0] += 1
    teams[second][2] += 1


results = {}
for _ in range(int(input())):
    f_team, f_score, s_team, s_score = input().split(';')
    if f_team not in results:
        AddTeam(results, f_team)
    if s_team not in results:
        AddTeam(results, s_team)
    if int(f_score) > int(s_score):
        WinAdd(results, f_team, s_team)
    elif int(f_score) < int(s_score):
        WinAdd(results, s_team, f_team)
    else:
        PairAdd(results,f_team,s_team)

for result in results:
    results[result][4] = results[result][1] * 3 + results[result][2]

for q, w in results.items():
    print((q+':'), *w, end='\n')