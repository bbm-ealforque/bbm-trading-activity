class MT4TradingActivityListTransformer:

    def __init__(self):
        pass
    
    def transform(self, list):
        for item in list:
            item.OPEN_PRICE = "{0:.2f}".format(round(item.OPEN_PRICE, 2))
            item.CLOSE_PRICE = "{0:.2f}".format(round(item.CLOSE_PRICE, 2))
            item.PROFIT = "{0:.2f}".format(round(item.PROFIT, 2))
            item.VOLUME = "{0:.2f}".format(item.VOLUME / 100)

            if item.CMD == 0: 
                item.CMD = 'BUY'
            if item.CMD == 1: 
                item.CMD = 'SELL'

        return list