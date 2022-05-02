
from app.dto.TradingActivityListDTO import TradingActivityListDTO
from app.dto.UserTradingActivityListDTO import UserTradingActivityListDTO
from app.exceptions.UserNotFoundException import UserNotFoundException
from app.repositories.mt4.MT4TradingActivityRepository import MT4TradingActivityRepository
from app.repositories.mt4.MT4UserRepository import MT4UserRepository
from app.services.PaginatorService import PaginatorService
from app.transformers.MT4TradingActivityListTransformer import MT4TradingActivityListTransformer

class MT4TradingActivityService:
   
    def __init__(self, 
               paginatorService: PaginatorService,
               mt4TradingActivityRepository: MT4TradingActivityRepository,
               mt4UserRepository: MT4UserRepository,
               mt4TradeListTransformer: MT4TradingActivityListTransformer):

        self.paginatorService = paginatorService
        self.mt4TradingActivityRepository = mt4TradingActivityRepository
        self.mt4UserRepository = mt4UserRepository
        self.mt4TradeListTransformer = mt4TradeListTransformer

    def getTradingActivityList(self, dto: TradingActivityListDTO):
        agentUsers = self.mt4UserRepository.getListForAgent(dto.getLoggedUser())

        result = self.paginatorService.paginate(
            self.mt4TradingActivityRepository.getList(agentUsers.pluck('LOGIN')), 
            dto.getPaginatorDTO()
        )

        return self.mt4TradeListTransformer.transform(result)

    def getTradingActivityListForUser(self, dto: UserTradingActivityListDTO):
        user = self.mt4UserRepository.retreive(dto.getUserId(), dto.getLoggedUser())
        if not user:
            raise UserNotFoundException("User not found")

        result = self.paginatorService.paginate(
            self.mt4TradingActivityRepository.getListByUser(user.LOGIN), 
            dto.getPaginatorDTO()
        )

        return self.mt4TradeListTransformer.transform(result)