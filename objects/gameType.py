HEAD_TO_HEAD = 0
TEAM_VS = 1

def getGameType(gametype):
    if not isinstance(gametype, str):
        return None
    elif gametype == 'h2h':
        return HEAD_TO_HEAD
    elif gametype == 'teamvs':
        return TEAM_VS