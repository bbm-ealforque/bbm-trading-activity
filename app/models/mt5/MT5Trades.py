from masoniteorm.models import Model

class MT5Trades(Model):

    __connection__ = "mysql-mt5"

    __table__ = "view_bb_mt5_trades"

    __selects__ = [
        "DEAL_Login", 
        "DEAL_Action",
        "DEAL_Time",
        "DEAL_Volume",
        "DEAL_Price",
        "DEAL_Profit",
    ]
