
from app.dto.UserListDTO import UserListDTO
from app.dto.UserRetrieveDTO import UserRetrieveDTO
from app.exceptions.UserNotFoundException import UserNotFoundException
from app.repositories.mt4.MT4TradingActivityRepository import MT4TradingActivityRepository 
from app.repositories.mt4.MT4UserRepository import MT4UserRepository
from app.services.PaginatorService import PaginatorService

class MT4UserService:
   
    def __init__(self,
                 paginatorService: PaginatorService, 
                 mt4UserRepository: MT4UserRepository,
                 mt4TradingActivityRepository: MT4TradingActivityRepository):
        self.paginatorService = paginatorService
        self.mt4TradingActivityRepository = mt4TradingActivityRepository
        self.mt4UserRepository = mt4UserRepository

    def getUserList(self, dto: UserListDTO):
        return self.paginatorService.paginate(
            self.mt4UserRepository.getListBuilder(dto.getLoggedUser()),
            dto.getPaginatorDTO()
        )

    def getUser(self, dto: UserRetrieveDTO):
        user = self.mt4UserRepository.retreive(dto.getUserId(), dto.getLoggedUser())
        if not user:
            raise UserNotFoundException("User not found")

        pnl = self.mt4TradingActivityRepository.getPnLByUser(user.LOGIN)

        user.BALANCE = "{0:.2f}".format(round(user.BALANCE, 2))
        if not pnl.LOGIN is None:
            user.PROFIT_LOSS = "{0:.2f}".format(round(pnl.PROFIT_LOSS, 2))
        else:
            user.PROFIT_LOSS = "{0:.2f}".format(0)

        return user