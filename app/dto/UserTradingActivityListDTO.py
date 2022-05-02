from app.dto.PaginatorDTO import PaginatorDTO
from masonite.request import Request

class UserTradingActivityListDTO:

    def __init__(self, 
                 request: Request):
        self.paginatorDTO = PaginatorDTO(request)
        self.userId = request.param("user")
        self.loggedUser = request.header('username')

    def getPaginatorDTO(self):
        return self.paginatorDTO

    def getUserId(self):
        return self.userId

    def getLoggedUser(self):
        return self.loggedUser