from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to

from app.models.mt4.MT4User import MT4User

class MT4Trades(Model):

    __table__ = "view_bb_mt4_trades"

    __selects__ = [
        "LOGIN", 
        "CMD",
        "VOLUME",
        "OPEN_PRICE",
        "OPEN_TIME",
        "CLOSE_PRICE",
        "CLOSE_TIME",
        "PROFIT",
    ]

    @belongs_to('LOGIN', 'LOGIN')
    def user(self):
        return MT4User
