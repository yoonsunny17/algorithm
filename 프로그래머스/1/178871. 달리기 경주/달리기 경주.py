def solution(players, callings):
    ranking = {name: rank for rank, name in enumerate(players)}
    
    for calling in callings:
        curr = ranking[calling]
        front = curr - 1
        
        players[curr], players[front] = players[front], players[curr]
        
        ranking[calling] = front
        ranking[players[curr]] = curr

    return players