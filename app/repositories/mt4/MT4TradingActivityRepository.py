from app.models.mt4.MT4Trades import MT4Trades

class MT4TradingActivityRepository:
  
    def __init__(self):
        pass

    def getList(self, userIds):
        return MT4Trades.select().where_in('CMD', [0, 1]).where_in('LOGIN', userIds)

    def getListByUser(self, userId: int):
        return MT4Trades.select().where_in('CMD', [0, 1]).where('LOGIN', userId)

    def getPnLByUser(self, userId: int):
        return MT4Trades.sum('PROFIT as PROFIT_LOSS').where_in('CMD', [0, 1]).where('LOGIN', userId).first()