from masoniteorm.models import Model

class MT5User(Model):

    __connection__ = "mysql-mt5"

    __table__ = "view_bb_mt5_users"

    __primary_key__ = "Login"
