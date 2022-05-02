from masoniteorm.models import Model

class MT4User(Model):

    __table__ = "view_bb_mt4_users"

    __primary_key__ = "LOGIN"
