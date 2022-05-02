from app.dto.UserListDTO import UserListDTO
from app.dto.UserRetrieveDTO import UserRetrieveDTO
from http import HTTPStatus
from masonite.controllers import Controller
from masonite.response import Response
from masonite.request import Request

from app.services.mt5.MT5UserService import MT5UserService

class UserController(Controller):
    
    def __init__(self, 
                 request: Request, 
                 service: MT5UserService):
        self.request = request
        self.service = service

    def index(self, response: Response):
        dto = UserListDTO(self.request)
        result = self.service.getUserList(dto)
        
        return response.json(
            result.serialize(), 
            HTTPStatus.OK
        )

    def show(self, response: Response):
        dto = UserRetrieveDTO(self.request)
        result = self.service.getUser(dto)

        return response.json(
            result.serialize(), 
            HTTPStatus.OK
        )
