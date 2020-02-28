from objects import gameType
from datetime import date

class User(object):
    userID = int()
    userName = str()
    country = str()
    pp = str()
    playCount = int()
    level = int()
    accuracy = int()
    elo = int()

class Tournament(object):
    tourID = int()
    tourName = str()
    tourHost = User()
    tourTeamList = list()
    tourSetting = _tourSetting()
    tourCreateDate = date.today().isoformat()
    

class _tourSetting(object):
    scorev = 2
    gameType = gameType.TEAM_VS
    numRound = int()
    winCondition = int()

class Match(object):
    matchID = int()
    beatmapID = int()
    beatmapName = str()
    beatmapMD5 = str()
    scorev = int()
    
class Slot(object):
    user = None
    score = float()

class Team(object):
    teamName = str()
    teamLeader = User()
    teamCountry = str()
    teamAvatarURL = str()
    user1 = User()
    user2 = User()
    user3 = User()
    user4 = User()
    user5 = User()
    user6 = User()