class MT5TradingActivityListTransformer:

    def __init__(self):
        pass
    
    def transform(self, list):
        for item in list:
            item.DEAL_Volume = "{0:.2f}".format(item.DEAL_Volume / 10000)
            item.DEAL_Profit = "{0:.2f}".format(round(item.DEAL_Profit, 2))

            if item.DEAL_Action == 0: 
                item.DEAL_Action = 'BUY'
            if item.DEAL_Action == 1: 
                item.DEAL_Action = 'SELL'

        return list