def tally(rows):
    table = {}
    for row in rows:
        first_team,second_team,result = row.split(';')
        if first_team not in table:
            table[first_team] = {'W': 0, 'L': 0, 'D': 0, 'P': 0, 'MP': 0}
        if second_team not in table:
            table[second_team] = {'W': 0, 'L': 0, 'D': 0, 'P': 0, 'MP': 0}
        team1 = table.get(first_team)
        team2 = table.get(second_team)

        if result == 'win':
            team1["W"]+=1
            team2["L"]+=1
            team1["P"]+=3
            team1["MP"]+=1
            team2["MP"]+=1  

        elif result == 'loss':
            team2["W"]+=1
            team1["L"]+=1
            team2["P"]+=3
            team1["MP"]+=1
            team2["MP"]+=1

        elif result == 'draw':
            team1["D"]+=1
            team2["D"]+=1
            team1["P"]+=1
            team2["P"]+=1
            team2["MP"]+=1
            team1["MP"]+=1        

    sort_score=sorted(list(table.items()),key=lambda x:x[0])
    sort_score.sort(key=lambda x: x[1]['P'], reverse=True)
    result_table = ["Team                           | MP |  W |  D |  L |  P"]

    for key, value in sort_score:
        result_table.append(f'{key:<31}| {value["MP"]:>2} | {value["W"]:>2} | {value["D"]:>2} | {value["L"]:>2} | {value["P"]:>2}')
    return result_table
