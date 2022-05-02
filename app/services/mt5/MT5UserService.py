
from app.dto.UserListDTO import UserListDTO
from app.dto.UserRetrieveDTO import UserRetrieveDTO
from app.exceptions.UserNotFoundException import UserNotFoundException
from app.repositories.mt5.MT5TradingActivityRepository import MT5TradingActivityRepository
from app.repositories.mt5.MT5UserRepository import MT5UserRepository 
from app.services.PaginatorService import PaginatorService

class MT5UserService:
   
    def __init__(self,
                 paginatorService: PaginatorService, 
                 mt5UserRepository: MT5UserRepository,
                 mt5TradingActivityRepository: MT5TradingActivityRepository):
        self.paginatorService = paginatorService
        self.mt5UserRepository = mt5UserRepository
        self.mt5TradingActivityRepository = mt5TradingActivityRepository

    def getUserList(self, dto: UserListDTO):
        return self.paginatorService.paginate(
            self.mt5UserRepository.getListBuilder(dto.getLoggedUser()),
            dto.getPaginatorDTO()
        )

    def getUser(self, dto: UserRetrieveDTO):
        user = self.mt5UserRepository.retreive(dto.getUserId(), dto.getLoggedUser())
        if not user:
            raise UserNotFoundException("User not found")

        pnl = self.mt5TradingActivityRepository.getPnLByUser(user.Login)

        user.Balance = "{0:.2f}".format(round(user.Balance, 2))
        if not pnl.DEAL_Login is None:
            user.Profit_Loss = "{0:.2f}".format(round(pnl.Profit_Loss, 2))
        else:
            user.Profit_Loss = "{0:.2f}".format(0)

        return user