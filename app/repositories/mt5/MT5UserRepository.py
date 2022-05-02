from app.models.mt5.MT5User import MT5User

class MT5UserRepository:
  
    def __init__(self):
        pass

    def getListBuilder(self, loginId):
        return MT5User.select('Login', 'Name', 'Balance').where('Agent', loginId)

    def retreive(self, userId, loginId):
        return MT5User.select('Login', 'Name', 'Balance').where('Login', userId).where('Agent', loginId).first()

    def getListForAgent(self, loginId):
        return MT5User.select('Login', 'Name', 'Balance').where('Agent', loginId).get()