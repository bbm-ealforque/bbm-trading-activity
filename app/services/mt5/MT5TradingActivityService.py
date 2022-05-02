
from app.dto.TradingActivityListDTO import TradingActivityListDTO
from app.dto.UserTradingActivityListDTO import UserTradingActivityListDTO
from app.exceptions.UserNotFoundException import UserNotFoundException
from app.repositories.mt5.MT5TradingActivityRepository import MT5TradingActivityRepository
from app.repositories.mt5.MT5UserRepository import MT5UserRepository
from app.services.PaginatorService import PaginatorService
from app.transformers.MT5TradingActivityListTransformer import MT5TradingActivityListTransformer

class MT5TradingActivityService:
   
    def __init__(self, 
               paginatorService: PaginatorService,
               mt5TradingActivityRepository: MT5TradingActivityRepository,
               mt5UserRepository: MT5UserRepository,
               mt5TradeListTransformer: MT5TradingActivityListTransformer):

        self.paginatorService = paginatorService
        self.mt5TradingActivityRepository = mt5TradingActivityRepository
        self.mt5UserRepository = mt5UserRepository
        self.mt5TradeListTransformer = mt5TradeListTransformer

    def getTradingActivityList(self, dto: TradingActivityListDTO):
        agentUsers = self.mt5UserRepository.getListForAgent(dto.getLoggedUser())

        result = self.paginatorService.paginate(
            self.mt5TradingActivityRepository.getList(agentUsers.pluck('Login')), 
            dto.getPaginatorDTO()
        )

        return self.mt5TradeListTransformer.transform(result)

    def getTradingActivityListForUser(self, dto: UserTradingActivityListDTO):
        user = self.mt5UserRepository.retreive(dto.getUserId(), dto.getLoggedUser())
        if not user:
            raise UserNotFoundException("User not found")

        result = self.paginatorService.paginate(
            self.mt5TradingActivityRepository.getListByUser(user.Login), 
            dto.getPaginatorDTO()
        )

        return self.mt5TradeListTransformer.transform(result)