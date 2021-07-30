def tally(rows):
    match_score = {}
    for row in rows:
        team1,team2,Result = row.split(';')
        if team1 not in match_score:
            match_score[team1] = {'W': 0, 'L': 0, 'D': 0, 'P': 0, 'MP': 0}
        if team2 not in match_score:
            match_score[team2] = {'W': 0, 'L': 0, 'D': 0, 'P': 0, 'MP': 0}
        team_1 = match_score.get(team1)
        team_2 = match_score.get(team2)

        if Result == 'win':
            team_1["W"]+=1
            team_2["L"]+=1
            team_1["P"]+=3
            team_1["MP"]+=1
            team_2["MP"]+=1  

        elif Result == 'loss':
            team_2["W"]+=1
            team_1["L"]+=1
            team_2["P"]+=3
            team_1["MP"]+=1
            team_2["MP"]+=1

        elif Result == 'draw':
            team_1["D"]+=1
            team_2["D"]+=1
            team_1["P"]+=1
            team_2["P"]+=1
            team_2["MP"]+=1
            team_1["MP"]+=1        

    sort_score=sorted(list(match_score.items()),key=lambda x:x[0])
    sort_score.sort(key=lambda x: x[1]['P'], reverse=True)
    result_table = ["Team                           | MP |  W |  D |  L |  P"]

    for key, value in sort_score:
        result_table.append(f'{key:<31}| {value["MP"]:>2d} | {value["W"]:>2d} | {value["D"]:>2d} | {value["L"]:>2d} | {value["P"]:>2d}')
    return result_table