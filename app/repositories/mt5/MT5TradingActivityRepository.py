from app.models.mt5.MT5Trades import MT5Trades

class MT5TradingActivityRepository:
  
    def __init__(self):
        pass

    def getList(self, userIds):
        return MT5Trades.select().where_in('DEAL_Action', [0, 1]).where_in('DEAL_Login', userIds)

    def getListByUser(self, userId: int):
        return MT5Trades.select().where_in('DEAL_Action', [0, 1]).where('DEAL_Login', userId)
    
    def getPnLByUser(self, userId: int):
        return MT5Trades.sum('DEAL_Profit as Profit_Loss').where_in('DEAL_Action', [0, 1]).where('DEAL_Login', userId).first()