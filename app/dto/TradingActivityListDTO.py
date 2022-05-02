from app.dto.PaginatorDTO import PaginatorDTO
from masonite.request import Request

class TradingActivityListDTO:

    def __init__(self, 
                 request: Request):
        self.paginatorDTO = PaginatorDTO(request)
        self.loggedUser = request.header('username')

    def getPaginatorDTO(self):
        return self.paginatorDTO

    def getLoggedUser(self):
        return self.loggedUser