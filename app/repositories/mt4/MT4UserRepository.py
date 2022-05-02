from app.models.mt4.MT4User import MT4User

class MT4UserRepository:
  
  def __init__(self):
    pass

  def getListBuilder(self, loginId):
    return MT4User.select('LOGIN', 'NAME', 'BALANCE').where('AGENT_ACCOUNT', loginId)

  def retreive(self, userId, loginId):
    return MT4User.select('LOGIN', 'NAME', 'BALANCE').where('LOGIN', userId).where('AGENT_ACCOUNT', loginId).first()

  def getListForAgent(self, loginId):
    return MT4User.select('LOGIN', 'NAME', 'BALANCE').where('AGENT_ACCOUNT', loginId).get()