class User(object):
    userID = int()
    userName = str()
    country = str()

class Match(object):
    matchID = int()
    beatmapID = int()
    beatmapName = str()
    beatmapMD5 = str()
    scorev = int()
    
    
class Slot(object):
    user = None
    score = float()
