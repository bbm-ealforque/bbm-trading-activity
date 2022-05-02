from masonite.providers import Provider

from app.repositories.mt4.MT4TradingActivityRepository import MT4TradingActivityRepository
from app.repositories.mt5.MT5TradingActivityRepository import MT5TradingActivityRepository
from app.repositories.mt5.MT5UserRepository import MT5UserRepository
from app.services.PaginatorService import PaginatorService
from app.repositories.mt4.MT4UserRepository import MT4UserRepository
from app.services.mt4.MT4TradingActivityService import MT4TradingActivityService
from app.services.mt4.MT4UserService import MT4UserService
from app.services.mt5.MT5TradingActivityService import MT5TradingActivityService
from app.services.mt5.MT5UserService import MT5UserService
from app.tasks.EstablishSSHTunnelTask import EstablishSSHTunnelTask
from app.transformers.MT4TradingActivityListTransformer import MT4TradingActivityListTransformer
from app.transformers.MT5TradingActivityListTransformer import MT5TradingActivityListTransformer

class AppProvider(Provider):
    def __init__(self, application):
        self.application = application

    def register(self):
        self.application.bind('PaginatorService', PaginatorService)

        self.application.bind('MT4TradingActivityRepository', MT4TradingActivityRepository)
        self.application.bind('MT5TradingActivityRepository', MT5TradingActivityRepository)
        self.application.bind('MT4UserRepository', MT4UserRepository)
        self.application.bind('MT5UserRepository', MT5UserRepository)

        self.application.bind('MT4TradingActivityService', MT4TradingActivityService)
        self.application.bind('MT5TradingActivityService', MT5TradingActivityService)
        self.application.bind('MT4UserService', MT4UserService)
        self.application.bind('MT5UserService', MT5UserService)

        self.application.bind('MT4TradingActivityListTransformer', MT4TradingActivityListTransformer)
        self.application.bind('MT5TradingActivityListTransformer', MT5TradingActivityListTransformer)

        # self.application.make('scheduler').add(EstablishSSHTunnelTask().every_minute())

    def boot(self):
        pass
