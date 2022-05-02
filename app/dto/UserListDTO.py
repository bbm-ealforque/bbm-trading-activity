from app.dto.PaginatorDTO import PaginatorDTO
from masonite.request import Request

class UserListDTO:

    def __init__(self, 
                 request: Request):
        self.loggedUser = request.header('username')
        self.paginatorDTO = PaginatorDTO(request)

    def getPaginatorDTO(self):
        return self.paginatorDTO

    def getLoggedUser(self):
        return self.loggedUser